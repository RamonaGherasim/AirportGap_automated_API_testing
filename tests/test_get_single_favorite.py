from requests_folder.get_single_favorite import get_single_favorite
from requests_folder.post_favorites import post_favorites
from helper_functions.assert_error_response_tokens import assert_error_response_unauthorized
from helper_functions.assert_not_found_error import assert_error_response_not_found
from helper_functions.assert_correct_fav_item import assert_correct_fav_item
from helper_functions.credentials import token


class TestGetSingleFavorite:
    # Negative testing - unauthenticated, with valid id
    def test_get_single_fav_unauthenticated_valid_id(self):
        # Create favorite with id HGU
        fav = post_favorites(token, "HGU")
        fav_id = fav.json()['data']['id']

        resp = get_single_favorite(fav_id)
        assert_error_response_unauthorized(resp)

    # Negative testing - unauthenticated, with invalid id
    def test_get_single_fav_unauthenticated_invalid_id(self):
        resp = get_single_favorite("1a")
        assert_error_response_unauthorized(resp)

    # Positive testing - valid id
    def test_get_single_fav_auth_valid_id(self):
        # Create favorite with id AEY
        fav = post_favorites(token, "AEY")
        fav_id = fav.json()['data']['id']

        # Get the favorite with the corresponding id for airport AEY
        resp = get_single_favorite(fav_id, token)
        assert_correct_fav_item(resp, fav_id)

    # Positive testing - valid id + decimal<5 with full stop/dot
    def test_get_single_fav_auth_decimal_id_dot(self):
        # Create favorite with id EGS
        fav = post_favorites(token, "EGS")
        fav_id = fav.json()['data']['id']

        # Get the favorite with the corresponding id for airport EGS
        resp = get_single_favorite(f"{fav_id}.1", token)
        assert_correct_fav_item(resp, fav_id)

    # Positive testing - valid id + decimal>5 with comma
    def test_get_single_fav_auth_decimal_id_comma(self):
        # Create favorite with id HZK
        fav = post_favorites(token, "HZK")
        fav_id = fav.json()['data']['id']

        # Get the favorite with the corresponding id for airport HZK
        resp = get_single_favorite(f"{fav_id},8", token)
        assert_correct_fav_item(resp, fav_id)

    # Positive testing - id starts with 0 + valid id
    def test_get_single_fav_auth_0_starting_id(self):
        # Create favorite with id IFJ
        fav = post_favorites(token, "IFJ")
        fav_id = fav.json()['data']['id']

        # Get the favorite with the corresponding id for airport IFJ
        resp = get_single_favorite(f"00{fav_id}", token)
        assert_correct_fav_item(resp, fav_id)

    # Negative testing - invalid param = alphanumeric value
    def test_get_single_fav_auth_alphanum_id(self):
        resp = get_single_favorite(f"abcd123", token)
        assert_error_response_not_found(resp)

    # Negative testing - invalid param = negative value
    def test_get_single_fav_auth_negative_id(self):
        resp = get_single_favorite("-7974", token)
        assert_error_response_not_found(resp)

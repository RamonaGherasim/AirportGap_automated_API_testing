from requests_folder.delete_single_favorite import delete_single_favorite
from requests_folder.post_favorites import post_favorites
from requests_folder.get_single_favorite import get_single_favorite
from helper_functions.credentials import token
from helper_functions.assert_not_found_error import assert_error_response_not_found
from helper_functions.assert_error_response_tokens import assert_error_response_unauthorized


class TestDeleteSingleFavorite:
    # Positive testing
    def test_delete_single_fav_authenticated_valid_id(self):
        # Create favorite with id YBR
        fav = post_favorites(token, "YBR")
        fav_id = fav.json()['data']['id']

        # Delete the favorite created item
        resp = delete_single_favorite(token, fav_id)
        assert resp.status_code == 204, f"Error: wrong status code. Expected 204, actual {resp.status_code}"

        # Check the favorite items list
        resp = get_single_favorite(fav_id, token)
        assert_error_response_not_found(resp)

    # Negative testing - authenticated, invalid id
    def test_delete_single_fav_authenticated_invalid_id(self):
        resp = delete_single_favorite(token, "abc456")
        assert_error_response_not_found(resp)

    # Negative testing - authenticated, missing id
    def test_delete_single_fav_authenticated_missing_id(self):
        resp = delete_single_favorite(token)
        assert resp.status_code == 404, f"Error: wrong status code. Expected 404, actual {resp.status_code}"

    # Negative testing - unauthenticated
    def test_delete_single_fav_unauthenticated(self):
        # Create favorite with id YBR
        fav = post_favorites(token, "YBR")
        fav_id = fav.json()['data']['id']

        # Try to delete the created favorite item
        resp = delete_single_favorite(fav_id=fav_id)
        assert_error_response_unauthorized(resp)




from requests_folder.get_favorites import get_favorites
from helper_functions.assert_error_response_tokens import assert_error_response_unauthorized
from requests_folder.post_favorites import post_favorites
from helper_functions.credentials import token


class TestGetFavorites:
    # Positive testing - valid token
    def test_get_favorites_valid_token(self):
        # Create some favorites
        post_favorites(token, "KIX")
        post_favorites(token, "UAK")

        # Get the created favorite airports
        resp = get_favorites(token)
        num_of_favorites = len(resp.json()['data'])
        assert resp.status_code == 200, f"Error: incorrect status code. Expected 200, actual {resp.status_code}"
        assert 'data' in resp.json(), "Error: No data response received"
        assert num_of_favorites >= 2

        for i in range(num_of_favorites):
            if resp.json()['data'][i]['attributes']['airport']['iata'] == "KIX": assert True
            assert resp.json()['data'][i]['type'] == 'favorite'

    # Negative testing - invalid token
    def test_get_favorites_invalid_token(self):
        resp = get_favorites("Tokentest123456789")
        assert_error_response_unauthorized(resp)

    # Negative testing - missing auth token
    def test_get_favorites_no_token(self):
        resp = get_favorites()
        assert_error_response_unauthorized(resp)


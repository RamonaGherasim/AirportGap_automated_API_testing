from requests_folder.delete_all_favorites import delete_all_favorites
from helper_functions.assert_error_response_tokens import assert_error_response_unauthorized
from requests_folder.get_favorites import get_favorites
from helper_functions.credentials import token


class TestDeleteAllFavorites:
    # Negative testing - unauthenticated
    def test_delete_all_fav_unauthenticated(self):
        resp = delete_all_favorites()
        assert_error_response_unauthorized(resp)

    # Positive testing
    def test_delete_all_fav_authenticated(self):
        resp = delete_all_favorites(token)
        assert resp.status_code == 204, f"Error: wrong status code. Expected 204, actual{resp.status_code}"

        favorites = get_favorites(token).json()['data']
        assert len(favorites) == 0

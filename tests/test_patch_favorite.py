from requests_folder.patch_favorite import patch_favorite
from requests_folder.post_favorites import post_favorites
from helper_functions.credentials import token
from helper_functions.assert_not_found_error import assert_error_response_not_found
from helper_functions.assert_error_response_tokens import assert_error_response_unauthorized


class TestPatchFavorite:
    # Positive testing
    def test_patch_fav_authenticated_valid_id(self):
        # Create favorite with id YBR
        fav = post_favorites(token, "YCL")
        fav_id = fav.json()['data']['id']

        # Patch the note for the created fave item
        note = "Patched note"
        resp = patch_favorite(note, token, fav_id)
        data = resp.json()['data']
        assert resp.status_code == 200, f"Error: wrong status code. Expected 200, actual {resp.status_code}"
        assert data['id'] == fav_id and data['attributes']['note'] == note

    # Negative testing - authenticated, invalid required id param
    def test_patched_fav_authenticated_invalid_id(self):
        resp = patch_favorite("Patched note part two", token, "asb509")
        assert_error_response_not_found(resp)

    # Negative testing - authenticated, missing required id param
    def test_patched_fav_authenticated_missing_id(self):
        resp = patch_favorite("Patched note part three", token)
        assert resp.status_code == 404, f"Error: wrong status code. Expected 404, actual {resp.status_code}"

    # Negative testing - unauthenticated, valid id param
    def test_patched_fav_unauthenticated_valid_id(self):
        # Create favorite with id YBR
        fav = post_favorites(token, "YND")
        fav_id = fav.json()['data']['id']

        # Try to patch the note for the created fave item
        note = "Patched note part four"
        resp = patch_favorite(note, fav_id=fav_id)
        assert_error_response_unauthorized(resp)

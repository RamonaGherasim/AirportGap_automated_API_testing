from requests_folder.post_favorites import post_favorites
from helper_functions.assert_error_response_tokens import assert_error_response_unauthorized
from helper_functions.credentials import token


class TestPostFavorites:
    # Negative testing - authenticated, missing required param
    def test_post_favorites_authenticated_no_params(self):
        resp = post_favorites(token)
        assert resp.status_code == 500, f"Error: wrong status code. Expected 500, actual {resp.status_code}"

    # Negative testing - unauthenticated, missing required param
    def test_post_favorites_unauthenticated_no_params(self):
        resp = post_favorites()
        assert_error_response_unauthorized(resp)

    # Negative testing - invalid authentication param, valid required param
    def test_post_favorites_invalid_token_valid_airport_id(self):
        resp = post_favorites("InvalidToken", airport_id="MAG")
        assert_error_response_unauthorized(resp)

    # Positive testing - authenticated, with required param, no optional param
    def test_post_favorites_authenticated_valid_id_no_note(self):
        airport_id = "LAE"
        resp = post_favorites(token, airport_id=airport_id)
        assert resp.status_code == 201, f"Error: wrong status code. Expected 201, actual {resp.status_code}"
        assert resp.json()['data']['type'] == 'favorite'
        assert resp.json()['data']['attributes']['airport']['iata'] == airport_id

    # Positive testing - authenticated, with required param, with optional param
    def test_post_favorites_authenticated_valid_id_with_note(self):
        airport_id = "POM"
        note = "This is Ramona's fave airport"
        resp = post_favorites(token, airport_id=airport_id, note=note)
        assert resp.status_code == 201, f"Error: wrong status code. Expected 201, actual {resp.status_code}"
        assert resp.json()['data']['type'] == 'favorite'
        assert resp.json()['data']['attributes']['airport']['iata'] == airport_id
        assert resp.json()['data']['attributes']['note'] == note

    # Negative testing - authenticated, missing required param, with optional param
    def test_post_favorites_authenticated_no_airport_id_with_note(self):
        resp = post_favorites(token, note="Note where no airport id")
        assert resp.status_code == 500, f"Error: wrong status code. Expected 500, actual {resp.status_code}"

    # Negative testing - authenticated, invalid required param
    def test_post_favorites_authenticated_invalid_airport_id(self):
        resp = post_favorites(token, airport_id="W1R")
        assert resp.status_code == 500, f"Error: wrong status code. Expected 500, actual {resp.status_code}"

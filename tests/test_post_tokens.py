from requests_folder.post_tokens import post_token
from helper_functions.assert_error_response_tokens import assert_error_response_unauthorized
from helper_functions.credentials import email, password


class TestPostTokens:
    # Positive testing - valid params
    def test_post_tokens_valid_params(self):
        resp = post_token(email, password)
        assert resp.status_code == 200, f"Error: incorrect status code. Expected 200, actual {resp.status_code}"
        assert len(resp.json()["token"]) > 0, "Error: empty token string returned"

    # Negative testing - missing params
    def test_post_tokens_no_params(self):
        resp = post_token()
        assert_error_response_unauthorized(resp)

    # Negative testing - missing password
    def test_post_tokens_valid_email_no_pass(self):
        resp = post_token(email)
        assert_error_response_unauthorized(resp)

    # Negative testing - missing email
    def test_post_tokens_no_email_valid_pass(self):
        resp = post_token(password=password)
        assert_error_response_unauthorized(resp)

    # Negative testing - incorrect email
    def test_post_tokens_incorrect_email(self):
        resp = post_token("test@airportgap.co.uk", password)
        assert_error_response_unauthorized(resp)

    # Negative testing - incorrect password
    def test_post_tokens_incorrect_pass(self):
        resp = post_token(email, "test_airportgappassword")
        assert_error_response_unauthorized(resp)

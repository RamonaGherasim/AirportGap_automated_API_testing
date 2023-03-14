from requests_folder.get_single_airport import get_single_airport
from helper_functions.assert_not_found_error import assert_error_response_not_found


class TestGetSingleAirport:
    # Positive testing
    def test_get_single_airport(self):
        resp = get_single_airport("KIX")
        assert resp.status_code == 200, f"Error: wrong status code. Expected 200, actual {resp.status_code}"
        assert len(resp.json()) == 1, f"Error: wrong number of results returned. Expected 1, actual {len(resp)}"

        airport_id = resp.json()['data']['id']
        assert airport_id == "KIX", "Error, airport id is different to the one requsted."

    # Negative testing - invalid id
    def test_get_single_airport_invalid_id(self):
        resp = get_single_airport(123)
        assert_error_response_not_found(resp)

    # Negative testing - incorrect id
    def test_get_single_airport_incorrect_id(self):
        resp = get_single_airport("kix")
        assert_error_response_not_found(resp)


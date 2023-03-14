from requests_folder.post_airports_distance import post_airports_distance
from helper_functions.assert_error_response_distance import assert_error_response


class TestPostAirportsDistance:
    # Positive testing, with different required params
    def test_post_airports_distance_valid_params(self):
        resp = post_airports_distance("KIX", "NRT")
        assert resp.status_code == 200, f"Error: incorrect status code. Expected 200, actual {resp.status_code}"
        assert resp.json()['data']['id'] == "KIX-NRT", f"Error: incorrect id returend. Expected 'KIX-NRT', actual {resp.json()['data']['id']}"
        assert resp.json()['data']['type'] == "airport_distance", "Error: returned JSON type is different to 'airport_distance"

        km = resp.json()['data']['attributes']['kilometers']
        miles = resp.json()['data']['attributes']['miles']
        naut_miles = resp.json()['data']['attributes']['nautical_miles']
        for i in [km, miles, naut_miles]:
            assert i > 0
        assert km > miles > naut_miles

    # Positive testing, with identical required params
    def test_post_airports_distance_identical_params(self):
        resp = post_airports_distance("KIX", "KIX")
        assert resp.status_code == 200, f"Error: incorrect status code. Expected 200, actual {resp.status_code}"
        assert resp.json()['data']['id'] == "KIX-KIX", f"Error: incorrect id returend. Expected 'KIX-NRT', actual {resp.json()['data']['id']}"
        assert resp.json()['data']['type'] == "airport_distance", "Error: returned JSON type is different to 'airport_distance"

        km = resp.json()['data']['attributes']['kilometers']
        miles = resp.json()['data']['attributes']['miles']
        naut_miles = resp.json()['data']['attributes']['nautical_miles']
        for i in [km, miles, naut_miles]:
            assert i == 0

    # Negative testing - no params
    def test_post_airports_distance_no_params(self):
        resp = post_airports_distance()
        assert_error_response(resp)

    # Negative testing - 'to' param missing
    def test_post_airports_distance_no_to_param(self):
        resp = post_airports_distance(from_a="KIX")
        assert_error_response(resp)

    # Negative testing - 'from' param missing
    def test_post_airports_distance_no_from_param(self):
        resp = post_airports_distance(to_a="KIX")
        assert_error_response(resp)

    # Negative testing - invalid 'to' param
    def test_post_airports_distance_invalid_to_param(self):
        resp = post_airports_distance("KIX", "1b5")
        assert_error_response(resp)

    # Negative testing - invalid 'from' param
    def test_post_airports_distance_invalid_from_param(self):
        resp = post_airports_distance("1b5", "NRT")
        assert_error_response(resp)

    # Negative testing - both params invalid
    def test_post_airports_distance_invalid_params(self):
        resp = post_airports_distance("G58", "V1!")
        assert_error_response(resp)

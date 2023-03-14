from requests_folder.get_airports import get_airports, get_airports_page_filter


class TestGetAirports:
    # Positive testing
    def test_get_airports(self):
        resp = get_airports()
        airports = resp.json()['data']
        assert resp.status_code == 200, f"Error, wrong status code. Expected 200, Actual {resp.status_code}"
        assert len(airports) == 30, f"Error, wrong number of results returned. Expected 30, actual {len(airports)}"

    # Boundary value analysis
    def test_get_airports_page_filter_0(self):
        resp = get_airports_page_filter(0)
        assert resp.status_code == 404, f"Error, wrong status code. Expected 404, Actual {resp.status_code}"

    # Boundary values analysis
    def test_get_airports_page_filter_1(self):
        resp = get_airports_page_filter(1)
        assert resp.status_code == 200, f"Error, wrong status code. Expected 200, Actual {resp.status_code}"

    # Boundary values analysis
    def test_get_airports_page_filter_203(self):
        resp = get_airports_page_filter(203)
        assert resp.status_code == 200, f"Error, wrong status code. Expected 200, Actual {resp.status_code}"

    # Boundary values analysis
    def test_get_airports_page_filter_204(self):
        resp = get_airports_page_filter(204)
        assert resp.status_code == 200, f"Error, wrong status code. Expected 200, Actual {resp.status_code}"
        assert len(resp.json()["data"]) == 0, f"Error, wrong number of results returned. Expected 0, actual {len(resp.json()['data'])}"

    # Negative testing - negative page number = -67
    def test_get_airport_page_filer_negative_value(self):
        resp = get_airports_page_filter(-67)
        assert resp.status_code == 404, f"Error, wrong status code. Expected 404, Actual {resp.status_code}"

    # Negative testing - decimal page number with full stop separator = 20.2
    def test_get_airport_page_filer_decimal_value_dot(self):
        resp = get_airports_page_filter(20.2)
        assert resp.status_code == 404, f"Error, wrong status code. Expected 404, Actual {resp.status_code}"

    # Negative testing - decimal page number with comma separator = 20,2
    def test_get_airport_page_filer_decimal_value_comma(self):
        resp = get_airports_page_filter("20,2")
        assert resp.status_code == 404, f"Error, wrong status code. Expected 404, Actual {resp.status_code}"

    # Negative testing - alphanumeric page param
    def test_get_airport_page_filer_alphanumeric(self):
        resp = get_airports_page_filter("2afd34")
        assert resp.status_code == 404, f"Error, wrong status code. Expected 404, Actual {resp.status_code}"

    def test_get_airports_page_filter_num_results(self):
        resp = get_airports_page_filter(30)
        airports = resp.json()['data']
        assert len(airports) == 30, f"Error, wrong number of results returned. Expected 30, actual {len(airports)}"

    def test_get_airports_page_filter_first_airport_id(self):
        first_page_first_airport_id = "GKA"
        resp_data = get_airports_page_filter(2).json()['data']
        second_page_first_airport_id = resp_data[0]['id']
        assert second_page_first_airport_id != first_page_first_airport_id, "Error, first airport id on page and on page two are the same!"
def assert_error_response_not_found(resp):
    assert resp.status_code == 404, f"Error: incorrect status code. Expected 404, actual {resp.status_code}"
    assert resp.json()['errors'], "No errors JSON returned."
    assert resp.json()['errors'][0]['status'] == str(resp.status_code), "Error, status code doesn't match with the one in JSON"
    assert resp.json()['errors'][0]['title'] == "Not Found", "Error: incorrect title returned in JSON"
    assert resp.json()['errors'][0]['detail'] == "The page you requested could not be found", "Error: incorrect detail section returned in JSON"
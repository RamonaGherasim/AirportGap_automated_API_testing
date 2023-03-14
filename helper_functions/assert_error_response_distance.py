def assert_error_response(resp):
    assert resp.status_code == 422, f"Error: incorrect status code. Expected 422, actual {resp.status_code}"
    assert resp.json()['errors'], "No errors JSON returned."
    assert resp.json()['errors'][0]['status'] == str(resp.status_code), "Error, status code doesn't match with the one in JSON"
    assert resp.json()['errors'][0]['title'] == "Unable to process request", "Error: incorrect title returned in JSON"
    assert resp.json()['errors'][0]['detail'] == "Please enter valid 'from' and 'to' airports.", "Error: incorrect detail section returned in JSON"
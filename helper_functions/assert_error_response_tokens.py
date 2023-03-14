def assert_error_response_unauthorized(resp):
    assert resp.status_code == 401, f"Error: incorrect status code. Expected 401, actual {resp.status_code}"
    assert resp.json()['errors'], "No errors JSON returned."
    assert resp.json()['errors'][0]['status'] == str(resp.status_code), "Error, status code doesn't match with the one in JSON"
    assert resp.json()['errors'][0]['title'] == "Unauthorized", "Error: incorrect title returned in JSON"
    assert resp.json()['errors'][0]['detail'] == "You are not authorized to perform the requested action.", "Error: incorrect detail section returned in JSON"
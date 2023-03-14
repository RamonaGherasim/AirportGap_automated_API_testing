def assert_correct_fav_item(resp, fav_id):
    assert resp.status_code == 200, f"Error: wrong status code. Expected 200, actual {resp.status_code}"
    assert len(resp.json()) == 1
    assert resp.json()['data']['id'] == fav_id
    assert resp.json()['data']['type'] == 'favorite'

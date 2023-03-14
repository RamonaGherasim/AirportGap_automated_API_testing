import requests


def get_single_favorite(fav_id, token=""):
    header_params = {'Authorization': token}
    return requests.get(f"https://airportgap.dev-tester.com/api/favorites/{fav_id}", headers=header_params)
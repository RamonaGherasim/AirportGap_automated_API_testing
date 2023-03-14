import requests


def get_favorites(token=""):
    header_params = {'Authorization': token}
    return requests.get("https://airportgap.dev-tester.com/api/favorites", headers=header_params)
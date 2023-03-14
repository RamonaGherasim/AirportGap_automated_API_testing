import requests


def delete_all_favorites(token=""):
    header_params = {'Authorization': token}
    return requests.delete("https://airportgap.dev-tester.com/api/favorites/clear_all", headers=header_params)
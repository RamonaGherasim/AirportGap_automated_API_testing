import requests


def delete_single_favorite(token="", fav_id=""):
    header_params = {'Authorization': token}
    if fav_id != "":
        return requests.delete(f"https://airportgap.dev-tester.com/api/favorites/{fav_id}", headers=header_params)
    else:
        return requests.delete(f"https://airportgap.dev-tester.com/api/favorites/{fav_id}", headers=header_params)
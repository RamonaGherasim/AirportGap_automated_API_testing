import requests


def patch_favorite(note, token="", fav_id=""):
    header_params = {'Authorization': token}
    if fav_id != "":
        return requests.patch(
            f"https://airportgap.dev-tester.com/api/favorites/{fav_id}?note={note}",
            headers=header_params)
    else:
        return requests.patch(
            f"https://airportgap.dev-tester.com/api/favorites/?note={note}",
            headers=header_params)

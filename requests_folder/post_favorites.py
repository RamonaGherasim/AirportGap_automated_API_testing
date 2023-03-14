import requests


def post_favorites(token="", airport_id="", note=""):
    header_params = {'Authorization': token}
    if airport_id == "" and note == "":
        return requests.post("https://airportgap.dev-tester.com/api/favorites", headers=header_params)
    elif airport_id != "" and note == "":
        return requests.post(f"https://airportgap.dev-tester.com/api/favorites?airport_id={airport_id}", headers=header_params)
    elif airport_id == "" and note != "":
        return requests.post(f"https://airportgap.dev-tester.com/api/favorites?note={note}", headers=header_params)
    else:
        return requests.post(f"https://airportgap.dev-tester.com/api/favorites?airport_id={airport_id}&note={note}", headers=header_params)

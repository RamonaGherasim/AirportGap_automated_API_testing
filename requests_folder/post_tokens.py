import requests


def post_token(email="", password=""):
    if email == "" and password == "":
        return requests.post(f"https://airportgap.dev-tester.com/api/tokens")
    elif email != "" and password == "":
        return requests.post(f"https://airportgap.dev-tester.com/api/tokens?email={email}")
    elif email == "" and password != "":
        return requests.post(f"https://airportgap.dev-tester.com/api/tokens?password={password}")
    else:
        return requests.post(f"https://airportgap.dev-tester.com/api/tokens?email={email}&password={password}")

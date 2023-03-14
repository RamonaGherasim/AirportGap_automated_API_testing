import requests


def post_airports_distance(from_a="", to_a=""):
    if from_a == "" and to_a == "":
        return requests.post(f"https://airportgap.dev-tester.com/api/airports/distance")
    elif from_a != "" and to_a == "":
        return requests.post(f"https://airportgap.dev-tester.com/api/airports/distance?from={from_a}")
    elif from_a == "" and to_a != "":
        return requests.post(f"https://airportgap.dev-tester.com/api/airports/distance?to={to_a}")
    else:
        return requests.post(f"https://airportgap.dev-tester.com/api/airports/distance?from={from_a}&to={to_a}")
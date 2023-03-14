import requests


def get_single_airport(airport_id):
    return requests.get(f"https://airportgap.dev-tester.com/api/airports/{airport_id}")

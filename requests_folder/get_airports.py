import requests


def get_airports():
    return requests.get("https://airportgap.dev-tester.com/api/airports")


def get_airports_page_filter(page_num):
    return requests.get(f"https://airportgap.dev-tester.com/api/airports?page={page_num}")
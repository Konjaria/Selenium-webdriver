# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
import requests
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import os


def main():
    print("Welcome to Saba's Club.We find the best flight deals and email you.")
    first_name = input("What is your first name? type here: ")
    last_name = input("What is your last name? type here: ")
    email = input("What is your email? type here: ")
    re_email = input("Type your email again: ")
    while email != re_email:
        re_email = input("Incorrect input.Type your email again: ")
    print("Congratulations! You're int the club!")
    api_endpoint = "https://api.sheety.co/[YOUR_USERNAME_GOES_HERE]/flightDeals/users"
    _body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }
    requests.post(url=api_endpoint,
                  json=_body)
    # ---------------- CONSTANT VARIABLES -----------------------
    sheety_api_endpoint = "https://api.sheety.co/[YOUR_USERNAME_GOES_HERE]/flightDeals/prices"
    # ---------------- IMPLEMENTATIONS --------------------------
    sheety_call = requests.get(url=sheety_api_endpoint)
    sheety_data = sheety_call.json()["prices"]
    data_management = DataManager()
    for city_data in sheety_data:
        header = {
            "apikey": os.environ.get("TEQUILA_KIWI_API_KEY")
        }
        body = {
            "term": city_data["city"],
            "locale": "en-us",
            "location_types": "airport",
            "limit": 1,
            "active_only": True,
            "sort": "name"
        }
        current_information = requests.get(url="https://api.tequila.kiwi.com/locations/query",
                                           headers=header,
                                           params=body)
        curr_data = current_information.json()
        curr_code = curr_data['locations'][0]['city']['code']

        search_obj = FlightSearch(from_code="TBS", to_code=curr_code)
        search_obj.search_flights()

        if city_data["iataCode"] == '':
            data_management.iata_updater(city_data["id"], curr_code)

        if int(city_data["lowestPrice"]) > search_obj.price:
            notifier = NotificationManager(from_code="TBS", to_code=curr_code)
            notifier.send_message()
            notifier.send_email(to=email)





if __name__ == "__main__":
    main()

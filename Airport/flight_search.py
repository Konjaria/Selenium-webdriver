from flight_data import FlightData
import requests
import os


class FlightSearch(FlightData):

    def __init__(self, from_code='TBS', to_code='PAR'):
        super().__init__(from_code, to_code)
        self.flyTo = None
        self.flyFrom = None
        self.cityFrom = None
        self.cityTo = None
        self.price = None


    def search_flights(self):
        search_api_header = {
            "apikey": os.environ.get("TEQUILA_KIWI_API_KEY")
        }

        search_api_body = {
            "fly_from": self._from_code_,
            "fly_to": self._to_code_,
            "date_from": self.tomorrow,
            "date_to": self.six_month_later,
            "curr": self._currency_,
            "sort": "price",
            "limit": 1
        }
        response = requests.get(url="https://api.tequila.kiwi.com/v2/search",
                                headers=search_api_header,
                                params=search_api_body)
        self.price = response.json()["data"][0]["price"]
        self.cityFrom = response.json()["data"][0]["cityFrom"]
        self.cityTo = response.json()["data"][0]["cityTo"]
        self.flyFrom = response.json()["data"][0]["flyFrom"]
        self.flyTo = response.json()["data"][0]["flyTo"]

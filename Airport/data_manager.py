import requests


class DataManager:
    def iata_updater(self, row_id, iata_code):
        url = "https://api.sheety.co/[YOUR_USERNAME]]/flightDeals/prices/" + str(row_id)
        body = {

            "price": {
                "iataCode": iata_code
            }
        }
        requests.put(url=url, json=body)

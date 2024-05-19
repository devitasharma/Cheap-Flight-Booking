from pprint import pprint
import requests

sheet_url = "https://api.sheety.co/78d11eefa08c1950bae7354cf64cefd0/ticketprice/sheet1"
class DataManager:
    def __int__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheet_url)
        response.raise_for_status()
        response_data = response.json()
        return response_data

    def update_destination_code(self):
        for i in self.destination_data["sheet1"]:
            print(i)
            parameter = {
                "sheet1": {
                    "iataCode": i["iataCode"]
                }
            }
            response = requests.put(url=f"{sheet_url}/{i["id"]}",
                                    json=parameter)
            print(response.text)




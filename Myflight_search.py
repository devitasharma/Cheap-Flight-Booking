import requests
from Myflightdata import FlightData
import pprint

TEQUILA_API_KEY = "XQHK4weILDW3AKwC9WTfz2CcyupKGcQN"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
code = []


class FlightSearch:
    def get_destination_code(self, city_name):
        for i in range(len(city_name)):
            location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
            header = {"apikey": TEQUILA_API_KEY}
            parameters = {
                "term": city_name[i],
                "location_types": "city"
            }
            repsonse = requests.get(url=location_endpoint, headers=header, params=parameters)
            repsonse.raise_for_status()
            result = repsonse.json()["locations"]
            code.append(result[0]["code"])
        return code

    def check_flight(self, origin_city, destination_code, from_time, to_time):
        header = {"apikey": TEQUILA_API_KEY}
        # nights_in_dst_from & to : kini der minimum & max rukna
        parameter = {
            "fly_from": origin_city,
            "fly_to": destination_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "CAD"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=parameter)
        response.raise_for_status()
        try:
            result_data = response.json()["data"][0]
        except IndexError:
            # print(f"No flight found for {destination_code}.")
            return None
        flightdata = FlightData(

            price = result_data["price"],
            origin_city = result_data["cityFrom"],
            destination_city = result_data["cityTo"],
            origin_airport  = result_data["flyFrom"],
            destination_airport = result_data["flyTo"],
            out_date = result_data["local_arrival"].split("T")[0],
            return_date = result_data["local_departure"].split("T")[0]
        )
        print(f"{flightdata.destination_city}:${flightdata.price}")
        return flightdata



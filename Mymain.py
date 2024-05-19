from pprint import pprint
from Mydata_manager import DataManager
from Myflight_search import FlightSearch
from datetime import datetime, timedelta
from MynotificationMenager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
codes_list = []
# todo getting whole google sheet data
sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_IATA = "PAR"

# todo retriving city name of code
# for i in range (len
#
# (sheet_data["sheet1"][0])):
#     if sheet_data["sheet1"][i]["iataCode"] == ORIGIN_CITY_IATA:
#         city_name = sheet_data["sheet1"][i]["city"]
#         print(city_name)

# todo if google sheet doesnot contain iata code then u can retrive iata code for each city from flight_search:
if sheet_data["sheet1"][0]["iataCode"] == "":
    city_names = [sheet_data["sheet1"][i]["city"] for i in range(len(sheet_data["sheet1"]))]
    print(city_names)
    codes_list = flight_search.get_destination_code(city_names)
    print(codes_list)
    for i in range(len(sheet_data["sheet1"])):
        sheet_data["sheet1"][i]["iataCode"] = codes_list[i]
    # pprint(sheet_data)
    data_manager.destination_data = sheet_data
    data_manager.update_destination_code()
# todo dates
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)
# todo flight check
for sheet in sheet_data["sheet1"]:
    flight = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        sheet["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    # todo sending messages
    if flight != None:
        if flight.price < sheet["lowestPrice"]:
            notification_manager.send_sms(
                message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport}"
                        f" to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to"
                        f" {flight.return_date}."
            )

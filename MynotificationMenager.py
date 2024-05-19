from twilio.rest import Client

API_KEY = "834188eae763c26e0658edbd8feb8dbf"
MY_LAT = 31.639770
MY_LONG = 74.838760
account_sid = "ACb1052496a183dbbea06529066f17eed2"
auth_token = "c97fdd383555a3d1781f461dc1271dc2"


class NotificationManager:

    # def __int__(self):
    #         self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=message,
                from_="+12052364403",
                to="+918283999274"

            )
            print(message.sid)

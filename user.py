import requests
from pprint import pprint

print("WELCOME TO DEVITA'S FLIGHT CLUB \nWE FIND THE BEST FLIGHT DEALS & EMAIL FOR YOU")
f_name = str(input("What's your First Name ? "))
l_name = str(input("What's your Last Name ? "))
email = str(input("Enter your Email : ")).lower()
confirm_email = str(input("Confirm your email : ")).lower()
while email != confirm_email:
    email = str(input("Enter your Email : ")).lower()
    if email.lower() == "quit" or email.lower() == "exit":
        exit()
    confirm_email = str(input("Confirm your email : ")).lower()
    if confirm_email.lower() == "quit" or confirm_email.lower() == "exit":
        exit()
print("You are in club!")

url = "https://api.sheety.co/78d11eefa08c1950bae7354cf64cefd0/ticketprice/newsheet"
headers = {
    "Content-Type": "application/json"
}
parameter = {
    "newsheet": {
        "FirstName": f_name,
        "LastName": l_name,
        "Email": email
    }
}
response = requests.post(url, headers=headers,json=parameter)
print(response.text)
response_get = requests.get(url)
data = response_get.json()
pprint(data)



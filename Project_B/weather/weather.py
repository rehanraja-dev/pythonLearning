import requests

API_KEY = "0e9740da8c8c4f2cbc4201142252110"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

city = input("Enter your city name: ")

params = {
    "key": API_KEY,
    "q": city,
    "aqi": "yes"
}

response = requests.get(BASE_URL, params)

status = response.status_code

if status == 200:
    data = response.json()
    print("Whether Data\n")
    print("City: ",data['location']['name'])
    print("Tempreture: ",data['current']['temp_c'],"°C")
else:
    print("something went wrong!!",status)
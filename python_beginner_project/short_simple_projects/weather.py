import requests
from pprint import pprint

API_Key = "2df254929b3631af9888b8e517d9e666"

city = input("enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city # url we are sending a response to
#base_url = "http://api.openweathermap.org/data/2.5/weather?q" + city + "&APPID=" + API_Key
weather_data = requests.get(base_url).json()

pprint(weather_data)
"""
2. Use web search to find some API to get weather data. Use that to get your region’s weather data every 30 minute.

Write a function named weather_data() and write your code inside this function. 
"""
import requests
import time

def weather_data():
    pi_address = 'https://api.openweathermap.org/data/2.5/weather?q=Dhaka&exclude=30&appid="collect api_id from openweathermap"&units=metric'
    url = pi_address
    json_data = requests.get(url).json()
    print(json_data)

weather_data()
time.sleep(1800)



import requests
import json
import csv
from api_keys import *

ip_list = ['122.35.203.161',
           '174.217.10.111',
           '187.121.176.91',
           '176.114.85.116',
           '174.59.204.133',
           '54.209.112.174',
           '109.185.143.49',
           '176.114.253.216',
           '210.171.87.76',
           '24.169.250.142']

with open('weather.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['IP', 'Country', 'City', 'Temperature', 'Weather'])

    for ip in ip_list:
        '''
        Part 1 - get API data for ip/country/city
        '''
        response = requests.get(f"https://api.ipbase.com/v2/info?ip={ip}&apikey={free_geo_ip}")
        data = json.loads(response.text)
        country = data['data']['location']['country']['name']
        lat = data['data']['location']['latitude']
        lon = data['data']['location']['longitude']
        city = data['data']['location']['city']['name']
        '''
        Part 2 - Get weather API data depending on country and city
        '''
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'lat': lat, 'lon': lon, 'appid': weather_api_key, 'units': 'metric'}
        weather_response = requests.get(url, params=params)
        weather_result = json.loads(weather_response.text)
        temp = weather_result['main']['temp']
        weather = weather_result['weather'][0]['main']
        writer.writerow([ip, country, city, temp, weather])
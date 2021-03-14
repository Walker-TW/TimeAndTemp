from globals import *
import time
import requests

resp = requests.get(WEATHER_FETCH_URL)

weatherJSON = resp.json()

weatherType = weatherJSON['weather'][0]['main']
tempreature = weatherJSON['main']['temp']
sunrise = weatherJSON['sys']['sunrise']
sunset = weatherJSON['sys']['sunset']
# final = weatherJSON['weather']

print(WEATHER_FETCH_URL)
print('weatherType ' + weatherType)
print('tempreature ', tempreature)
print('sunrise ' , time.ctime(int(sunrise)))
print('sunset ' , time.ctime(int(sunset)))

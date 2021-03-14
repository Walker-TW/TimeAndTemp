from globals import *
import requests

resp = requests.get(WEATHER_FETCH_URL)

verJSON = resp.json()

print(verJSON)

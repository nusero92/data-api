# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://weather.lewagon.com"


def search_city(query):
    '''Look for a given city. If multiple options are returned, have the user choose between them.
       Return one city (or None)
    '''
    response = requests.get(f"https://weather.lewagon.com/geo/1.0/direct?q={query}&limit=5" ).json()
    if not response:
        return None
    citys=response[0]
    return {'name': citys['name'],
            'lat':citys['lat'],
            'lon':citys['lon'],
            'country': citys['country'],
            'state': citys['state'] }

def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''

    response = requests.get(f"https://weather.lewagon.com/data/2.5/forecast", params={"lat":lat,"lon":lon}).json()
    forecast=response["list"][::8]
    return forecast

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    # TODO: Display weather forecast for a given city
    question=input("Multiple matches found, which city did you mean?")




if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)

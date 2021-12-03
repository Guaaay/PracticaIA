import configparser
import values
from requests.auth import HTTPBasicAuth
import requests

config = configparser.ConfigParser()  # https://docs.python.org/3/library/configparser.html
config.read(values.API_KEY_FILE)


def api_key() -> str:
    return config['Credentials']['APIKey']


def get_geocoding_data(station_name):
    params_query = {
        'address': station_name + ' metro station',
        'key': api_key()}
    response = requests.get(values.GEOCODING_URL, params=params_query)

    if len(response.json()['results']) < 1:  # If it yielded no results, try with a different request
        params_query['address'] = station_name + ' station'
        response = requests.get(values.GEOCODING_URL, params=params_query)

    return response.json()

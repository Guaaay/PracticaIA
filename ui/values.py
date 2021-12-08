from os.path import expanduser
#PATHS
API_KEY_FILE = expanduser('~/.key/gmapsapigeocoding')
STATION_JSONS = 'resources/restapi/station_geolocation_jsons/'

#REST API
GEOCODING_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

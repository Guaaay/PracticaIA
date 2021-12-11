import database
import restapi
import os.path
import cte
import values
import json


def load_geolocation_data() -> None:
    """
    Updates the json files containing data of every station via API requests where necessary
    :return: None
    """
    raw_json = {}
    for station in database.lines_stations.keys():
        print('Checking station: ' + station)
        file_name = values.STATION_JSONS + station + '.json'

        # Load if json exists locally, otherwise send an API request
        if os.path.isfile(file_name):
            raw_json = json.load(open(file_name))  # Load saved json
            if len(raw_json['results']) < 1:  # No data in json
                send_api_request(station, file_name)
        else:
            send_api_request(station, file_name)

        geometry = raw_json['results'][0]['geometry']['location']
        latitude = geometry['lat']
        longitude = geometry['lng']
        print('latitude: ' + str(latitude))
        print('longitude: ' + str(longitude))


def send_api_request(station, file_name) -> None:
    """
    Requests data about the specified station, to be saved in the specified file
    :param station: name of the station
    :param file_name: name of the file to store it
    :return: None
    """
    print('\tSent an api request for ' + station)
    raw_json = restapi.get_geocoding_data(station)  # API request for data
    outfile = open(file_name, 'w')
    json.dump(raw_json, outfile)  # Store for next uses


def load_stations_geolocation() -> None:
    """
    Updates geolocation for each station
    :return: None
    """
    for station in lines_stations.keys():
        file_name = values.STATION_JSONS + station + '.json'

        # Load if json exists locally, otherwise send an API request
        if not os.path.isfile(file_name):
            geolocationdata.load_geolocation_data()

        raw_json = json.load(open(file_name))  # Load saved json
        if len(raw_json['results']) > 0:  # No data in json
            geometry = raw_json['results'][0]['geometry']['location']
            latitude = geometry['lat']
            longitude = geometry['lng']
            stations_geolocation[station] = (latitude, longitude)
        else:
            print('Failed to load data for station: ' + station)


stations_geolocation: dict[str, tuple[float, float]] = {}
load_stations_geolocation()



def get_distance(origin: str, destination: str) -> float:
    """
        Distance in Km from station "origin" to station "destination".
        :param origin: Name of origin station
        :param destination: Name of destination station
        :return: distance between stations or -1 if the stations are invalid (p.e. dont exist)
        """
    if origin == destination:
        return 0
    coords_origin = stations_geolocation[origin]
    coords_destination = stations_geolocation[destination]
    return geopy.distance.distance(coords_origin, coords_destination).km
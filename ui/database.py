"""
This file provides access to methods to manage data about the Metro of Kiev.
The current data corresponds to:
    -Time between 2 stations
    -Stations connected to one specified
    -Line corresponding to one station
    -Stations corresponding to one line
"""
import pandas as pd
import values
import json
import os.path
from pathlib import Path


lines_stations: dict[str, int] = {
    "Akademmistechko": 1,
    "Zhytomyrska": 1,
    "Sviatoshyn": 1,
    "Nyvky": 1,
    "Beresteiska": 1,
    "Shuliavska": 1,
    "Politekhnichnyi Instytut": 1,
    "Vokzalna": 1,
    "Universytet": 1,
    "Teatralna": 1,
    "Khreshchatyk": 1,
    "Arsenalna": 1,
    "Dnipro": 1,
    "Hidropark": 1,
    "Livoberezhna": 1,
    "Darnytsia": 1,
    "Chernihivska": 1,
    "Lisova": 1,
    "Heroiv Dnipra": 2,
    "Minska": 2,
    "Obolon": 2,
    "Pochaina": 2,
    "Tarasa Shevchenka": 2,
    "Kontraktova Ploshcha": 2,
    "Poshtova Ploshcha": 2,
    "Maidan Nezalezhnosti": 2,
    "Ploshcha Lva Tolstoho": 2,
    "Olimpiiska": 2,
    "Palats Ukrayina": 2,
    "Lybidska": 2,
    "Demiivska": 2,
    "Holosiivska": 2,
    "Vasylkivska": 2,
    "Vystavkovyi Tsentr": 2,
    "Ipodrom": 2,
    "Teremky": 2,
    "Syrets": 3,
    "Dorohozhychi": 3,
    "Lukianivska": 3,
    "Zoloti Vorota": 3,
    "Palats Sportu": 3,
    "Klovska": 3,
    "Pecherska": 3,
    "Druzhby Narodiv": 3,
    "Vydubychi": 3,
    "Slavutych": 3,
    "Osokorky": 3,
    "Pozniaky": 3,
    "Kharkivska": 3,
    "Vyrlytsia": 3,
    "Boryspilska": 3,
    "Chervony Khutir": 3
}

lines_stations_number: dict[str, int] = {
    "Akademmistechko": 110,
    "Zhytomyrska": 111,
    "Sviatoshyn": 110,
    "Nyvky": 113,
    "Beresteiska": 114,
    "Shuliavska": 115,
    "Politekhnichnyi Instytut": 116,
    "Vokzalna": 117,
    "Universytet": 118,
    "Teatralna": 119,
    "Khreshchatyk": 120,
    "Arsenalna": 121,
    "Dnipro": 122,
    "Hidropark": 123,
    "Livoberezhna": 124,
    "Darnytsia": 125,
    "Chernihivska": 126,
    "Lisova": 127,
    "Heroiv Dnipra": 210,
    "Minska": 211,
    "Obolon": 212,
    "Pochaina": 213,
    "Tarasa Shevchenka": 214,
    "Kontraktova Ploshcha": 215,
    "Poshtova Ploshcha": 216,
    "Maidan Nezalezhnosti": 217,
    "Ploshcha Lva Tolstoho": 218,
    "Olimpiiska": 219,
    "Palats Ukrayina": 220,
    "Lybidska": 221,
    "Demiivska": 222,
    "Holosiivska": 223,
    "Vasylkivska": 224,
    "Vystavkovyi Tsentr": 225,
    "Ipodrom": 226,
    "Teremky": 227,
    "Syrets": 310,
    "Dorohozhychi": 311,
    "Lukianivska": 312,
    "Zoloti Vorota": 314,
    "Palats Sportu": 315,
    "Klovska": 316,
    "Pecherska": 317,
    "Druzhby Narodiv": 318,
    "Vydubychi": 319,
    "Slavutych": 321,
    "Osokorky": 322,
    "Pozniaky": 323,
    "Kharkivska": 324,
    "Vyrlytsia": 325,
    "Boryspilska": 326,
    "Chervony Khutir": 327
}

lines_number_station = {value : key for (key, value) in lines_stations_number.items()}

stations_connections: dict[str, str] = {
    "Teatralna": "Zoloti Vorota",
    "Khreshchatyk": "Maidan Nezalezhnosti",
    "Maidan Nezalezhnosti": "Khreshchatyk",
    "Ploshcha Lva Tolstoho": "Palats Sportu",
    "Zoloti Vorota": "Teatralna",
    "Palats Sportu": "Ploshcha Lva Tolstoho"
}

adjacent_stations: dict[str, tuple[str]] = {
    # 1st before, 2nd after, 3rd connection
    # Line 1
    "Akademmistechko": ["Zhytomyrska"],
    "Zhytomyrska": ["Akademmistechko", "Sviatoshyn"],
    "Sviatoshyn": ["Zhytomyrska", "Nyvky"],
    "Nyvky": ["Sviatoshyn", "Beresteiska"],
    "Beresteiska": ["Nyvky", "Shuliavska"],
    "Shuliavska": ["Beresteiska", "Politekhnichnyi Instytut"],
    "Politekhnichnyi Instytut": ["Shuliavska", "Vokzalna"],
    "Vokzalna": ["Politekhnichnyi Instytut", "Universytet"],
    "Universytet": ["Vokzalna", "Teatralna"],
    "Teatralna": ["Universytet", "Khreshchatyk", "Zoloti Vorota"],
    "Khreshchatyk": ["Teatralna", "Arsenalna", "Maidan Nezalezhnosti"],
    "Arsenalna": ["Khreshchatyk", "Dnipro"],
    "Dnipro": ["Arsenalna", "Hidropark"],
    "Hidropark": ["Dnipro", "Livoberezhna"],
    "Livoberezhna": ["Hidropark", "Darnytsia"],
    "Darnytsia": ["Livoberezhna", "Chernihivska"],
    "Chernihivska": ["Darnytsia", "Lisova"],
    "Lisova": ["Chernihivska"],
    # Line 2
    "Heroiv Dnipra": ["Minska"],
    "Minska": ["Heroiv Dnipra", "Obolon"],
    "Obolon": ["Minska", "Pochaina"],
    "Pochaina": ["Obolon", "Tarasa Shevchenka"],
    "Tarasa Shevchenka": ["Pochaina", "Kontraktova Ploshcha"],
    "Kontraktova Ploshcha": ["Tarasa Shevchenka", "Politekhnichnyi Instytut"],
    "Poshtova Ploshcha": ["Kontraktova Ploshcha", "Maidan Nezalezhnosti"],
    "Maidan Nezalezhnosti": ["Poshtova Ploshcha", "Ploshcha Lva Tolstoho", "Khreshchatyk"],
    "Ploshcha Lva Tolstoho": ["Maidan Nezalezhnosti", "Olimpiiska", "Palats Sportu"],
    "Olimpiiska": ["Ploshcha Lva Tolstoho", "Palats Ukrayina"],
    "Palats Ukrayina": ["Olimpiiska", "Lybidska"],
    "Lybidska": ["Palats Ukrayina", "Demiivska"],
    "Demiivska": ["Lybidska", "Holosiivska"],
    "Holosiivska": ["Demiivska", "Vasylkivska"],
    "Vasylkivska": ["Holosiivska", "Vystavkovyi Tsentr"],
    "Vystavkovyi Tsentr": ["Vasylkivska", "Ipodrom"],
    "Ipodrom": ["Teremky", "Vystavkovyi Tsentr"],
    "Teremky": ["Ipodrom"],
    # Line 3
    "Syrets": ["Dorohozhychi"],
    "Dorohozhychi": ["Akademmistechko", "Lukianivska"],
    "Lukianivska": ["Dorohozhychi", "Zoloti Vorota"],
    "Zoloti Vorota": ["Lukianivska", "Palats Sportu", "Teatralna"],
    "Palats Sportu": ["Zoloti Vorota", "Klovska", "Ploshcha Lva Tolstoho"],
    "Klovska": ["Palats Sportu", "Pecherska"],
    "Pecherska": ["Klovska", "Druzhby Narodiv"],
    "Druzhby Narodiv": ["Pecherska", "Vydubychi"],
    "Vydubychi": ["Druzhby Narodiv", "Slavutych"],
    "Slavutych": ["Vydubychi", "Osokorky"],
    "Osokorky": ["Slavutych", "Pozniaky"],
    "Pozniaky": ["Osokorky", "Kharkivska"],
    "Kharkivska": ["Pozniaky", "Vyrlytsia"],
    "Vyrlytsia": ["Kharkivska", "Boryspilska"],
    "Boryspilska": ["Vyrlytsia", "Chervony Khutir"],
    "Chervony Khutir": ["Boryspilska"]
}


'''def load_stations_geolocation() -> None:
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
            print('Failed to load data for station: ' + station)'''


'''stations_geolocation: dict[str, tuple[float, float]] = {}
load_stations_geolocation()'''

times_1 = pd.read_csv(Path('../resources/data/tiempos_1.csv'), index_col='Sviatoshynsko-Brovarska Line M1')
times_2 = pd.read_csv(Path('../resources/data/tiempos_2.csv'), index_col='Obolonsko–Teremkivska Line M2')
times_3 = pd.read_csv(Path('../resources/data/tiempos_3.csv'), index_col='Syretsko-Pecherska Line M3')


def get_time(origin: str, destination: str) -> float:
    """
    Time from station "origin" to station "destination", for stations that aren't immediately next in the line, it takes
    into account the time the train spends stopped when un/loading passengers.
    :param origin: Name of origin station
    :param destination: Name of destination station
    :return: time between stations or -1 if the stations are invalid (not in the same line or dont exist)
    """
    if origin == destination:
        return 0
    if lines_stations.get(origin) == lines_stations.get(destination):
        if lines_stations.get(origin) == 1:
            return float(times_1[destination][origin])
        elif lines_stations.get(origin) == 2:
            return float(times_2[destination][origin])
        elif lines_stations.get(origin) == 3:
            return float(times_3[destination][origin])
    elif stations_connections.get(origin) is not None \
            and stations_connections.get(origin).__contains__(destination):
        return 2.0  # TODO valor random de 2 min para los transbordos
    else:
        return -1.0


'''def get_distance(origin: str, destination: str) -> float:
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
    return geopy.distance.distance(coords_origin, coords_destination).km'''

def get_adjacent_stations(station: str) -> tuple[str]:
    """
    Stations directly connected to the one given
    :param station: Station with neighbor stations
    :return: tuple of adjacent stations, or None if no station exists
    """
    return adjacent_stations.get(station)


def get_line(station: str) -> int:
    """
    Line of the station specified
    :param station: name of station of metro Kiev
    :return: the line number that it belongs to
    """
    return lines_stations[station]


def get_stations(line: int) -> list[str]:
    """
    Stations of the line specified
    :param line: Number of the line to check for stations
    :return: a list of all the stations (in order) of the line specified
    """
    stations = []

    for i in lines_stations.items():
        if i[1] == line:
            stations.append(i[0])

    return stations

##TODO Sparkles:
##Get geolocation of each station using google maps API:
##https://developers.google.com/maps/documentation/geocoding/overview
##Name of station + "subway" yields the coordinates of the station

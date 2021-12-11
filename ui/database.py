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
from cte import *

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
        return 5.0  # TODO valor random de 2 min para los transbordos
    else:
        return -1.0



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

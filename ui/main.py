import database

#print(database.get_time('Syrets', 'Vydubychi'))
import ui.geolocationdata as geolocationdata

#geolocationdata.load_geolocation_data()

print('Distance from Teatralna to Lukianivska')
print(geolocationdata.get_distance('Teatralna','Lukianivska'))
print(geolocationdata.get_distance('Teatralna','Lukianivska')/100*60)

# for station1 in database.lines_stations:
#     for station2 in database.lines_stations:
#         ##print("Distance from " + station1 + " to " + station2 + ": ")
#         print(int(geolocationdata.get_distance(station1, station2)))
import json
import requests
import time

# Les liens vers les données JSON des stations
status_url = "https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json"
info_url = "https://montpellier-fr-smoove.klervi.net/gbfs/en/station_information.json"

period=int(input("Période(min):"))
period=period*60
duration=int(input("duration(sec):"))


# Récupère les données JSON des stations
response = requests.get(status_url)
status_data = response.json()

response = requests.get(info_url)
info_data = response.json()



# Stocke les données dans des fichiers différents
with open("status_data.txt", "w") as outfile:
    json.dump(status_data, outfile)

with open("info_data.txt", "w") as outfile:
    json.dump(info_data, outfile)



# Calcule le taux d'occupation des stations
total_stations = len(status_data)
occupied_stations = 0
for station in status_data:
    bikes_available = station["num_bikes_available"]
    station_id = station["station_id"]
    capacity = info_data[station_id]["capacity"]
    if bikes_available < capacity:
        occupied_stations += 1
occupancy_rate = occupied_stations / total_stations

# Affiche le taux d'occupation
print("Taux d'occupation des stations: {:.2f}%".format(occupancy_rate * 100))


time.sleep(duration)
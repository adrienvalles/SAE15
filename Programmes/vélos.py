import requests
import json
import time




# URL de l'API JSON

# Récupérer les données à partir de l'URL
response = requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json")
response2 = requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_information.json")


period=int(input("Période(min):"))
period=period*60
duration=int(input("duration(sec):"))

data = json.loads(response.text)
with open("data.txt", "w") as file:
    # Écrire les données dans le fichier
    file.write(json.dumps(data))

# Initialisation des variables pour le calcul du taux d'occupation
    total_bike_stands = 0
    available_bike_stands = 0

# Boucle pour parcourir toutes les stations et calculer le taux d'occupation
    for station in data:
        total_bike_stands += station("capacity")
        available_bike_stands += station("num_bikes_available")

occupancy_rate = (total_bike_stands - available_bike_stands) / total_bike_stands

# Écriture des données dans un fichier texte
with open("data.txt", "w") as text_file:
    text_file.write("Taux d'occupation des places de vélos : {:.2f}%\n".format(occupancy_rate * 100))
    text_file.write("Données :\n")
    json.dump(json_data, text_file, indent=4)
    
time.sleep(duration)
    
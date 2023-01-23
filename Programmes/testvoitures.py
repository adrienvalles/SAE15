import requests
from lxml import etree
import time

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE',
          'FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL',
          'FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250',
          'FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']

Toville=0 #Le nombre total des parkings de toute la ville
FrVille=0 #Le nombre total des parkings libres de toute la ville
Nom=input("Nom du fichier:")# indiquer le nom du fichier
period=int(input("Période(min):"))
period=period*60
duration=int(input("duration(sec):"))
t=60
for p in range(t):
    for x in parkings: #la liste "parkings" contient les noms des fichiers de chaque zone. On fait un boucle pour récupérer des données de chaque zone. #Récupérer les données et les mettre dans un nouveau fichier
        data=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{x}.xml")
        f1=open(f"{x}.txt","w",encoding='utf8')
        f1.write(data.text)
        f1.close()
        #trier des données et choisir le nombre des places libre et des places total.
        tree=etree.parse(f"{x}.txt")
        a=0
        b=0
        for user in tree.xpath("Total"):
            total=int(user.text)
            a=a+total
        for user in tree.xpath("Free"):
            libre=int(user.text)
            b=b+libre
        # ajouter des nombre dans le valeur du "nombre total". C'est pour obtenir la somme de tous les parkings et tous les parkings libres
        Toville=Toville+a
        FrVille=FrVille+b
    PVoiture=FrVille/Toville # la valeur : Parkings libres/ Parkings total
    PVoiture=1-PVoiture # pour obtenir le taux d'occupation des voitures
    temps=time.time()
    temps=time.ctime(temps)
    f2=open(f"{Nom}.txt","a",encoding='utf8')
    f2.write(f"{temps} Le Taux d'occupation des parkings de la ville de Montpellier est de: {round(PVoiture*100, 2)}%")
    f2.write('\n')
    f2.close()
    time.sleep(duration)
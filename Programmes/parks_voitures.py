import requests
from lxml import etree
import time



parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE',
          'FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL',
          'FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250',
          'FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']



Toville=0 #Le nombre total des parkings voituresde toute la ville
FrVille=0 #Le nombre total des parkings voitures libres de toute la ville
Nom=input("Nom du fichier:")# indiquer le nom du fichier
periode=int(input("Période(min):"))
periode=periode*60  # cela indique la durée de l'acquisition du programme en minutes . Par exemple si je tape période= 2 , la durée sera de 120min c'est à dire 2 heures car ici on multiplie par 60
duree=int(input("durée(sec):"))
t=60  # t c'est le nombre de fois que le programme va se répeter .

for p in range(t):
    for i in parkings: #la liste "parkings" contient les noms des fichiers de chaque zone. On fait un boucle pour récupérer des données de chaque zone. #Récupérer les données et les mettre dans un nouveau fichier
        data=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{i}.xml")
        f1=open(f"{i}.txt","w",encoding='utf8') #Cette fonction va ouvrir un fcihier texte conteant les inforùations de tous les parkings de Montpellier
        f1.write(data.text)
        f1.close()
        #trier ces données et choisir le nombre des places libres et des places totales.
        tree=tree.parse(f"{i}.txt")
        a=0
        b=0
        for user in tree.xpath("Total"):
            total=int(user.text)
            a=a+total
        for user in tree.xpath("Free"):
            libre=int(user.text)
            b=b+libre
        # ajouter des nombrse dans la valeur du "nombre total". C'est pour obtenir la somme de tous les parkings et celle de tous les parkings libres
        Toville=Toville+a
        FrVille=FrVille+b
    PVoiture=FrVille/Toville # la valeur : Parkings libres/ Parkings total
    PVoiture=1-PVoiture # pour obtenir le taux d'occupation des voitures
    temps=time.time()
    temps=time.ctime(temps)
    #fonction qui va permettre d'afficher la date a côté de chaque données

    # Ici ça va permettre d'ouvrir un fichier avec le champ "nom" que l'on souhaite donné et que l'on a spéciffié au début avec la fonction f2.write qui va permttre d'écrire dans
    # ce fichier qui stockera les données avec la date et le taux d'occupation 
    f2=open(f"{Nom}.txt","a",encoding='utf8')
    f2.write(f"{temps} Le Taux d'occupation des parkings de la ville de Montpellier est de: {round(PVoiture*100, 2)}%")
    f2.write('\n')
    f2.close()
    time.sleep(duree) #fonction qui suspend l'éxecution en fonction du nombre de secondes que j'ai attribué à ma fonction "duree"
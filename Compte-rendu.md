# Etude de l'utilisation des parkings de la ville de Montpellier
 


> A noter: J'ai finalement réalisé cette SAE seul, puisque Raid Neghouche a été absent à plusieurs séance c'est donc pour cela que j'ai préféré travailler seul pour pas me pénaliser


Nous voulons nous intéresser sur:
- Le taux d’occupation des parkings voiture.
- Le taux d’occupation des parkings vélos.
- Le bon fonctionnement du relais voiture / vélo.
- La relation entre l'usage des parkings voiture et l'usage des parkings velo
 
Pour ce faire, j'ai utilisé les données extraites du site ***open data de Montpellier*** qui m'ont permis d'analyser les données .


### Préparation du mini projet ###
---

Avant de pouvoir réaliser le mini projet, j'ai eu une séance TP afin de me préparer au mieux au traitement des données du site opendata. Pour pouvoiur récupérer ces données je me suis appuyer sur les premières questions du TP qui m'a beaucoup aidé, en demandant de tester le programme.

En effet ce programme va grâce à la fonction requets, envoyer une demande http vers le site en question afin d'extraire les données pour les affciher dans un fichier texte conteant toutes les information s pour tous les parkings voiture de la Ville de Montpellier



PAR=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
'FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']
 
for i in PAR:
    x=requests.get(f'https://data.montpellier3m.fr/sites/default/files/ressources/{i}.xml')
    print(x.text)
 



***Ceci est un programme  qui permet le suivi de l’occupation de tous les parkings de Montpellier et en affichant à la fin le pourcentage de places libres  et de places occupées de toute la ville.***


````

import requests
from lxml import etree
PAR=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
'FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']
 
y=0
w=0
p=0
for i in PAR:
    x=requests.get(f'https://data.montpellier3m.fr/sites/default/files/ressources/{i}.xml')
    f1=open(f'{i}.txt',"w", encoding='utf8')
    f1.write(x.text)
    f1.close()
    tree = etree.parse(f"{i}.txt")   #retirer les donnees
    for user in tree.xpath("Name"):    #extrait les données de name
        print('Nom du parking :',user.text)
    for user1 in tree.xpath("Total"):  
        print('Places totales :',user1.text)
    for user2 in tree.xpath("Free"):
        print('Nombre de places libres :',user2.text)
        x=int((user1.text))-int((user2.text))
        print('Nombres de places occupées:' ,x)
    y=int((user1.text))+ y
    w=int((user2.text))+w
    p=int((x))+ p
#print('Nombres de places occupées dans toute la ville:' ,x)
print('Nombre de Places totales de toute la ville:' ,y)
print('Nombres de places libres de toute la ville:' ,w)
print('Nombre de place occupées dans toute la ville:' ,p)
pour=int((w))*100/int(y)
opour=int((p))*100/int(y)
print('Pourcentage de places libres de toute la ville' ,round(pour,2) ,'%')
print('Pourcentage de places occupées de toute la ville' ,round(opour,2) ,'%')
````


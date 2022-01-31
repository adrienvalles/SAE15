import requests #librairie HTTP
import time
from lxml import etree

parkings=["FR_MTP_ANTI","FR_MTP_COME","FR_MTP_CORU","FR_MTP_EURO","FR_MTP_FOCH","FR_MTP_GAMB","FR_MTP_GARE","FR_MTP_TRIA","FR_MTP_ARCT","FR_MTP_PITO",
"FR_MTP_CIRC","FR_MTP_SABI","FR_MTP_GARC","FR_MTP_MOSS","FR_STJ_SJLC","FR_MTP_MEDC","FR_MTP_OCCI","FR_CAS_VICA","FR_MTP_GA109",
"FR_MTP_GA250","FR_CAS_CDGA","FR_MTP_ARCE"]
#Parkings de Montpellier

url="https://data.montpellier3m.fr/dataset/disponibilite-des-places-dans-les-parkings-de-montpellier-mediterranee-metropole"
#lien du site open data montpellier

num=2 #

for j in range(num):
    for i in parkings:
        response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/"+i+".xml")
        #Récuperer tout les liens de chaque parking de montpellier
        f1=open(i,"w", encoding='utf8')
        f1.write(response.text)
        f1.close()
        f2=open("resultats.text","a",encoding='utf8')
        tree = etree.parse(i)
        for user in tree.xpath("Date_time"):
            time=user.text
            f2.write('\n')
            f2.write('Date:')
            f2.write(user.text)
            f2.write('\n')
        
        for user in tree.xpath("Name"):
            print('Nom du parking :',user.text)
            f2.write('Parking :')
            f2.write(user.text)
            f2.write('\n')
            #Afficher le nom du parking
            
        for user in tree.xpath("Total"):
            f2.write('Nombre total de places:')
            f2.write(user.text)
            f2.write('\n')
            total=int(user.text)
            #Afficher le nombre de total de places du parking
            
        for user in tree.xpath("Free"):
            f2.write('Nombre de places libres :')
            f2.write(user.text)
            f2.write('\n')
            free=int(user.text)
            pourcentage=round((free*100)/total,2)
            f2.write('Le pourcentage de places libres est de :')
            f2.write(str(pourcentage))
            f2.write("%")
            f2.write('\n')
            f2.write('\n')
            #Afficher le nombre de places libres dans un parking
    f2.write('\n')
    f2.write('\n')
    f2.write('\n')
    f2.write(' Programme en pause')
    f2.write('\n')
    f2.write('\n')
    f2.write('\n')
        
    velomag=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")
    f3=open("velomag.text", "w", encoding="utf8")
    f3.write(velomag.text)
    f3.close()
    f4=open("velomag_result.text","a",encoding='utf8')
    tree=etree.parse("velomag.text")
    for si in tree.xpath("/vcs/sl/si"):
        if si.get("id")=="002":
            f4.write('Nom de la station :')
            f4.write(si.get("na"))
            f4.write('\n')
            f4.write('Nombre de places occupées :')
            f4.write(si.get("av"))
            f4.write('\n')
            f4.write('Nombre de places libres :')
            f4.write(si.get("fr"))
            f4.write('\n')
            f4.write('Nombre de places totales :')
            f4.write(si.get("to"))
            f4.write('\n')
            f4.write('\n')
            f4.write('\n')
            f4.write('Programme en pause')
            f4.write('\n')
            f4.write('\n')
            f4.write('\n')
            f4.close()
            print("velos")
            f2.close()
    time.sleep(3600)

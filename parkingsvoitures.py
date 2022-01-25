import requests
from lxml import etree

parkings=["FR_MTP_ANTI","FR_MTP_COME","FR_MTP_CORU","FR_MTP_EURO","FR_MTP_FOCH","FR_MTP_GAMB","FR_MTP_GARE","FR_MTP_TRIA","FR_MTP_ARCT","FR_MTP_PITO",
"FR_MTP_CIRC","FR_MTP_SABI","FR_MTP_GARC","FR_MTP_MOSS","FR_STJ_SJLC","FR_MTP_MEDC","FR_MTP_OCCI","FR_CAS_VICA","FR_MTP_GA109",
"FR_MTP_GA250","FR_CAS_CDGA","FR_MTP_ARCE"]

url="https://data.montpellier3m.fr/dataset/disponibilite-des-places-dans-les-parkings-de-montpellier-mediterranee-metropole"


for i in parkings:
    response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/"+i+".xml")
    print(response.text)
    f1=open("FR_MTP_COME.txt","w", encoding='utf8')
    f1.write(response.text)
    f1.close()
    tree = etree.parse("FR_MTP_COME.txt")
    for user in tree.xpath("Name"):
        print('Nom du parking :',user.text)
    for user in tree.xpath("Free"):
        print('Nombre de places libres :',user.text) 
    
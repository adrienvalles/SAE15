from math import sqrt

def pourcentage(a,b):
    '''
    :param a: partie de b
    :param b: total
    :return: Pourcentage de a par rapport à b
    '''
    return a/(b/100)



def moyenne(liste):
    '''
    :param liste: liste contenant des valeurs  entières ou réelles
    :return: La moyenne des valeurs contenus dans la liste
    '''
    total = 0
    for element in liste:
        total += element
    return total/len(liste)


def ecart_type(liste, moyenne):
    '''
    :param liste: Liste de valeurs
    :param moyenne: Valeur moyenne de la liste de valeurs
    :return: Retourne l'écart-type
    '''
    variance = 0
    for element in liste:
        variance += (element - moyenne)**2
    variance /= len(liste)
    return sqrt(variance)

def covariance(liste_x, liste_y, moyenne_x, moyenne_y):
    '''
    :param liste_x: liste de valeurs
    :param liste_y: liste de valeurs
    :param moyenne_x: valeur moyenne de la liste liste_x
    :param moyenne_y: valeur moyenne de la liste liste_y
    :return: Retourne la covariance entre liste_x et liste_y
    '''
    resultat = 0
    taille = len(liste_x)
    for i in range(taille):
        resultat += (liste_x[i] - moyenne_x) * (liste_y[i] - moyenne_y)
    resultat /= taille
    return resultat

def coefficient_correlation(liste_x, liste_y, moyenne_x, moyenne_y):
    '''
    :param liste_x: liste de valeurs
    :param liste_y: liste de valeurs
    :param moyenne_x: valeur moyenne de la liste liste_x
    :param moyenne_y: valeur moyenne de la liste liste_y
    :return: Retourne la covariance entre liste_x et liste_y
    '''
    ecart_type_x = ecart_type(liste_x, moyenne_x)
    ecart_type_y = ecart_type(liste_y, moyenne_y)
    if ecart_type_x == 0: ecart_type_x = 1/1000000000
    if ecart_type_y == 0: ecart_type_y = 1/1000000000
    return covariance(liste_x, liste_y, moyenne_x, moyenne_y) * 1/(ecart_type_x * ecart_type_y)

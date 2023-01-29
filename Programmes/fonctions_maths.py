from statistics import *
from math import *

def moyenne(liste):
    return (1/len(liste)) * sum(liste)

def ecart_type(liste):
    moy = moyenne(liste)
    N = len(liste)
    var = 0
    for nb in liste:
        var += (nb - moy)**2
    return sqrt((1/N) * var)



occup=[58.79, 61.46, 62.78, 64.82, 65.41, 65.28, 63.93, 62.43, 60.17, 57.59, 55.68, 51.70, 49.91, 48.12, 46.09, 43.29 ,39.94]

print(moyenne(occup))
print(ecart_type(occup))
print(pvariance(occup))

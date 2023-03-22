# -*- coding: utf-8 -*-
"""
@author:
"""

def somme(L):
    s = 0 # on initialise une variable à 0
    for l in L: #on parcourt les éléments de la liste
        s = s + l # on ajoute à s les éléments de L
    return s

def moyenne(L):
    return somme(L) / len(L) # on renvoie la somme sur le nombre d'éléments

def variance(L):
    m = moyenne(L) #on récupère la moyenne de L
    s = 0 #on initialise une variable à 0
    for x in L: #on parcourt les valeurs de L
        s += (x - m)**2
    return s / len(L)


import math
def ecart_type(L):
    return math.sqrt(variance(L))

L = [1, 2, 3, 4, 5]
print("Somme de L = ", somme(L))
print("Moyenne de L = ", moyenne(L))
print("Variance de L = ", variance(L))
print("Ecart-type de L = ", ecart_type(L))

    
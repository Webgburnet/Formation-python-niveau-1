# -*- coding: utf-8 -*-
"""
@author:
"""

def somme_n_premiers_entiers(n):
    som = 0 # on initialise un variable à 0
    for i in range(1, n + 1):#i prend les valeurs de 1 à n
        som = som + i
    return som

n = 5
print(somme_n_premiers_entiers(n))
print(n * (n + 1) / 2)

def factorielle(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

x = 5
print(factorielle(x))

def coeff_binom(k, n):
    return factorielle(n) / (factorielle(k) * factorielle(n - k))

k = 2
print(coeff_binom(k, n))
# -*- coding: utf-8 -*-
"""
@author:
"""
import math
def est_pair(x):
    return x%2 == 0 #x est pair si le reste de sa division par 2 est nul

def est_premier(x):
    i = 2
    while i <= math.sqrt(x):#on essaye de diviser x par tous les entiers inférieurs à racine de x
        if x % i == 0: # si le reste de la division est nul, x n'est pas premier
            return False
        i += 1
    return True

def affiche_n_premiers_premiers(n):
    k = 0 # nombre de nombres premiers trouvés
    i = 2 # nombre à tester
    while k < n:
        if est_premier(i):
            print(i)
            k += 1
        i += 1
    return
        
    
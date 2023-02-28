# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
L=[]

#Exo4.1
def est_pair(x):
    return x%2==0

pair1 = est_pair(5)
pair2 = est_pair(6)

#Exo4.2
def est_premier(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

prems2=est_premier(5)
prems1=est_premier(6)

#Exo4.3
def affiche(L):
    i=0
    n=2
    while i<50:
        if est_premier(n):
            L=L+[n]
            i+=1
        n+=1
    return L

L= affiche(L)
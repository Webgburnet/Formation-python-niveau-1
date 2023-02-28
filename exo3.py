# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

L = [1,2,3,4]

#Exo3.1
def somme(L):
    s=0
    for l in L:
        s=l+s
    return s

s=somme(L)

#Exo3.2
def moyenne(L):
    return 1/len(L)*somme(L)

m=moyenne(L)

#Exo3.3
def variance(L):
    i=0
    for l in L:
        i=i+(l-m)**2
    return 1/len(L)*i

v=variance(L)

#Exo 3.4
def ecart_type(L):
    return math.sqrt(v)

e=ecart_type(L)
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Exo2.1
def somme_n_premiers_entiers(n):
    Sn=0
    for i in range (n+1):
        Sn=Sn+i
    return Sn

Sn=somme_n_premiers_entiers(5)

#Exo2.2
def factorielle_n(n):
    i=0
    fact=1
    while i<n:
        i+=1
        fact=fact*i
    return fact

fn=factorielle_n(5)
#Exo2.3
def coef_binomial(n,k):
    if(n<0):
        return "n<0"
    elif(k>n):
        return "k>n"
    else:
        return factorielle_n(n)/(factorielle_n(k)*factorielle_n(n-k))

cn=coef_binomial(5,4)
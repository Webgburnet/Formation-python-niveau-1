# -*- coding: utf-8 -*-
"""
@author: 
"""
#code complet sans utiliser de variables globales
#définition des fonctions
def passage_feu_vert(fv, fo, fr):
    fv, fo, fr = True, False, False
    return fv, fo, fr


def passage_feu_orange(fv, fo, fr):
    fv, fo, fr = False, True, False
    return fv, fo, fr


def passage_feu_rouge(fv, fo, fr):
    fv, fo, fr = False, False, True
    return fv, fo, fr


def passage_pieton_vert(pv, pr):
    pv, pr = True, False
    return pv, pr


def passage_pieton_rouge(pv, pr):
    pv, pr = False, True
    return pv, pr


def changement_feux(fv, fo, fr, pv, pr):
    if fv:#si le feu est vert, on passe à l'orange
        fv, fo, fr = passage_feu_orange(fv, fo, fr)
    elif fo:#sinon si le feu est orange, on passe au rouge
        fv, fo, fr = passage_feu_rouge(fv, fo, fr)
        pv, pr = passage_pieton_vert(pv, pr)#on met le pieton au vert
    else: # pour faire passer le piéton au rouge avant le feu vert
        if pv:#si le piéton est vert on passe au piéton rouge
            pv, pr = passage_pieton_rouge(pv, pr)
        else:#sinon on passe au feu vert
            fv, fo, fr = passage_feu_vert(fv, fo, fr)
    return fv, fo, fr, pv, pr

#initialisation des variables
feu_vert, feu_orange, feu_rouge = True, False, False
pieton_vert, pieton_rouge = False, True

#On appelle ensuite la fonction changement_feux avec la console. 
#Le \ permet de continuer une instruction trop longue sur la ligne suivante.

feu_vert, feu_orange, feu_rouge, pieton_vert, pieton_rouge = \
changement_feux(feu_vert, feu_orange, feu_rouge, pieton_vert, pieton_rouge) \
# le feu passe au orange
feu_vert, feu_orange, feu_rouge, pieton_vert, pieton_rouge = \
changement_feux(feu_vert, feu_orange, feu_rouge, pieton_vert, pieton_rouge) \
# le feu passe au rouge et le piéton au vert
# on peut continuer indéfiniment 
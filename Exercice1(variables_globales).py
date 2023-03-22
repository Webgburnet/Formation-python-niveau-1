# -*- coding: utf-8 -*-
"""
@author:
"""
#code complet sans utiliser de variables globales

#initialisation des variables globales
feu_vert, feu_orange, feu_rouge = True, False, False
pieton_vert, pieton_rouge = False, True

#définition des fonctions
def passage_feu_vert():
    global feu_vert, feu_orange, feu_rouge #on déclare que les variables sont globales
    feu_vert, feu_orange, feu_rouge = True, False, False
    return #on ne renvoie rien car les variables ont été modifiées directement en global


def passage_feu_orange():
    global feu_vert, feu_orange, feu_rouge
    feu_vert, feu_orange, feu_rouge = False, True, False
    return


def passage_feu_rouge():
    global feu_vert, feu_orange, feu_rouge
    feu_vert, feu_orange, feu_rouge = False, False, True
    return 


def passage_pieton_vert():
    global pieton_vert, pieton_rouge
    pieton_vert, pieton_rouge = True, False
    return 


def passage_pieton_rouge():
    global pieton_vert, pieton_rouge
    pieton_vert, pieton_rouge = False, True
    return 


def changement_feux():
    global feu_vert, feu_orange, feu_rouge, pieton_vert, pieton_rouge
    if feu_vert:#si le feu est vert, on passe à l'orange
        passage_feu_orange()
    elif feu_orange:#sinon si le feu est orange, on passe au rouge
        passage_feu_rouge()
        passage_pieton_vert()#on met le pieton au vert
    else: # pour faire passer le piéton au rouge avant le feu vert
        if pieton_vert:#si le piéton est vert on passe au piéton rouge
            passage_pieton_rouge()
        else:#sinon on passe au feu vert
            passage_feu_vert()
    return 



#On appelle ensuite la fonction changement_feux avec la console. 
changement_feux()
# le feu passe au orange
changement_feux()
# le feu passe au rouge et le piéton au vert
# on peut continuer indéfiniment 
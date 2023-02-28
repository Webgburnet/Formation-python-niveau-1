# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

feu_vert = False
feu_orange = False
feu_rouge = False
pieton_rouge = False
pieton_vert = False

#Exo 1.1
# def exo1_1 () :
#     if (feu_vert or feu_orange) :
#         pieton_vert = False
#         pieton_rouge = True
    
# #Exo 1.2
# def exo1_2 () :
#     if (feu_rouge) :
#         pieton_vert = False
#         pieton_rouge = True
#     else :
#         pieton_vert = True
#         pieton_rouge = False
        
# #Exo 1.3
# def exo1_3 () :
#     while (pieton_vert) :
#         feu_vert = False
#         feu_orange = False
#         feu_rouge=True

#Exo 1.4
def passage_feu_vert(fv,fo,fr) :
    fv = True
    fo = False
    fr = False
    return fv,fo,fr

# feu_vert, feu_orange, feu_rouge = passage_feu_vert(feu_vert, feu_orange, feu_rouge)

#Exo 1.5
def passage_feu_orange(fv,fo,fr) :
    fv = False
    fo = True
    fr = False
    return fv,fo,fr

# feu_vert, feu_orange, feu_rouge = passage_feu_orange(feu_vert, feu_orange, feu_rouge)

def passage_feu_rouge(fv,fo,fr) :
    fv = False
    fo = False
    fr = True
    return fv,fo,fr

# feu_vert, feu_orange, feu_rouge = passage_feu_rouge(feu_vert, feu_orange, feu_rouge)

def passage_pieton_vert(pv,pr) :
    pv = True
    pr = False
    return pv,pr

# pieton_vert, pieton_rouge = passage_pieton_vert(pieton_vert, pieton_rouge)

def passage_pieton_rouge(pv,pr) :
    pv = False
    pr = True
    return pv,pr

# pieton_vert, pieton_rouge = passage_pieton_rouge(pieton_vert, pieton_rouge)

def changement_feux(fv,fo,fr,pv,pr):
    if (fv):
        print("feu vert")
        fv,fo,fr = passage_feu_orange(fv,fo,fr)
        pv,pr = passage_pieton_rouge(pv,pr)
        print("feu orange + pieton rouge")
    elif(fo):
        print("feu orange")
        fv,fo,fr = passage_feu_rouge(fv,fo,fr)
        pv,pr = passage_pieton_vert(pv,pr)
        print("feu rouge + pieton vert")
    else :
        print("feu rouge")
        fv,fo,fr = passage_feu_vert(fv,fo,fr)
        pv,pr = passage_pieton_rouge(pv,pr)
        print("feu vert + pieton rouge")
    return fv,fo,fr,pv,pr

feu_vert, feu_orange, feu_rouge, pieton_vert, pieton_rouge = changement_feux(feu_vert, feu_orange, feu_rouge, pieton_vert, pieton_rouge)
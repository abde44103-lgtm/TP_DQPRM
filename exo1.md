# DQPRM /

## Exercices de mise en pratique en Python

#### Albertine Dubois - albertine.dubois@cea.fr, Ludovic Ferrer - Ludovic.Ferrer@ico.unicancer.fr & Marion Savanier - marion.savanier@cea.fr

Version 2026

## Exercice 1 - Calcul automatique de l'IMC d'un individu

Ecrire une fonction qui calcule l'indice de masse corporelle (IMC) d'un(e) patient(e) donné(e)

* La fonction nécessitera 2 paramètres en entrée, le poids (en $kg$) et la taille (en $m$), et renverra la valeur de l'IMC en sortie
* Suivant la valeur d'IMC, la fonction devra également fournir une interprétation du résultat (maigreur, IMC normal, surpoids, obésité, obésité massive)
* Tester la fonction avec différents couples de valeurs poids/taille

**Rappel :**

<img width=400 src='./data/imc.gif'>

---
def indice_de_masse_corporelle(...,...):
    imc = ... # Indiquer la formule pour calculer l'IMC.
    print("IMC = {:0.1f}".format(imc))
    if imc <= 18.5:
        print("Valeur d'IMC indiquant une maigreur")
    elif ... < imc <= ... :
        print("Valeur d'IMC normal")
    elif ... < imc <= ... :
        print("Valeur d'IMC indiquant un surpoids")
    elif ... < imc <= ... :
        print("Valeur d'IMC indiquant un obésité")
    else :
        print("Valeur d'IMC indiquant une obésité massive")
    return ...

imc = indice_de_masse_corporelle(...,...)
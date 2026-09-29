## Exercice 1 - Calcul automatique de l'IMC d'un individu

Ecrire une fonction qui calcule l'indice de masse corporelle (IMC) d'un(e) patient(e) donné(e)

* La fonction nécessitera 2 paramètres en entrée, le poids (en $kg$) et la taille (en $m$), et renverra la valeur de l'IMC en sortie
* Suivant la valeur d'IMC, la fonction devra également fournir une interprétation du résultat (maigreur, IMC normal, surpoids, obésité, obésité massive)
* Tester la fonction avec différents couples de valeurs poids/taille

**Rappel :**

<img width=400 src='./data/imc.gif'>

---
def indice_de_masse_corporelle(taille, masse):
    imc = masse / (taille**2)  # Formule de l'IMC : masse (kg) / taille (m)²
    print("IMC = {:0.1f}".format(imc))
    
    if imc <= 18.5:
        print("Valeur d'IMC indiquant une maigreur")
    elif 18.5 < imc <= 25:
        print("Valeur d'IMC normal")
    elif 25 < imc <= 30:
        print("Valeur d'IMC indiquant un surpoids")
    elif 30 < imc <= 40:
        print("Valeur d'IMC indiquant une obésité")
    else:
        print("Valeur d'IMC indiquant une obésité massive")
        
    return imc

# Exemple d'appel pour une personne de 1,75 m et 70 kg :
imc = indice_de_masse_corporelle(1.75, 70)
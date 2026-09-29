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
        print("Valeur d'IMC indiquant une obésité sévère")
        
    return imc

# Exemple d'appel pour une personne de 1,75 m et 70 kg :
imc = indice_de_masse_corporelle(1.75, 70)


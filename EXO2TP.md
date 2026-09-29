## Exercice 2 - Suivi glycémie
-----------

**Question 1.** Lire avec la bibliothèque Pandas le fichier `glycemie.csv` contenu dans le dossier `data` (attention au séparateur décimal : . ou , ?)

**Question 2.** Tracer sur un même graphique, dont vous fixerez les dimensions, les courbes de la variation au cours du temps de la glycémie de ce patient pour chacun des points de mesure renseigné par colonne

**Question 3.** Indiquer le nom des axes et la légende


## RÉPONSES

**Question 1 :**

import pandas as pd

df = pd.read_csv("data/glycemie.csv", sep=";", decimal=",")
df
# Question 2 : Tracé des courbes sur un même graphique avec dimensions fixées
plt.figure(figsize=(10, 6))

# Récupération du temps (première colonne) et tracé de chaque colonne de mesure
temps = df.iloc[:, 0]

for colonne in df.columns[1:]:
    plt.plot(temps, df[colonne])


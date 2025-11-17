# ----------------------------------------------------------------------------------
# Exercice 2  Effectue ces calculs
# 5 + 3
# 10 - 2 * 3
# (10 - 2) * 3

""" a = 5
b = 3
c = 10
d = 2

print(a + b)
print(c - d * b)
print((c - d) * b) """


# ----------------------------------------------------------------------------------
# Exercice 3 Exercices sur les Messages et Commentaires

""" a = 5               # premier nombre
b = 10                  # deuxieme
resultat = a + b        # calcul de la somme

print("le resultat de l'addition est :", resultat) """


# ----------------------------------------------------------------------------------
# Exercice 4 : Écris un programme qui présente une personne avec :

# Un commentaire en tête décrivant le programme
# Des commentaires expliquant chaque étape
# Un message de fin

# Logiciel servant à décrire une personne selon ses attributs

""" # ajout des criteres
couleur_yeux = "yeux pairs"
couleur_cheveux = "cheveux brun"
grandeur_cm = 168
age = 41

# assemblage des attributs

print("Je vous présente Marc qui a", age,"ans et mesure", grandeur_cm,"cm.  Il a les", couleur_cheveux,"et les",couleur_yeux)
print(f"Je vous présente Marc qui a { age } ans et mesure { grandeur_cm } cm.  Il a les {couleur_cheveux} et les {couleur_yeux}.")
print("Bienvenue a toi Marc !!!") """


# ----------------------------------------------------------------------------------
# Exercice 5 : Messages utilisateur Crée un programme qui :

# Demande le nom de l'utilisateur
# Demande son âge
# Affiche un message personnalisé

""" name = input("Quel est votre nom ? ")
age = input("Quel age avez-vous ?")
print("Bienvenue à bord", name,",", age, "ce n'est pas trop vieux pour débuter !!!") """


# ----------------------------------------------------------------------------------
# Exercice 6 : Reconnaissance des types Pour chaque valeur, indique son type :

""" nbr = 42
logiciel = "Python"
pi = 3.14
verite = True
adresse = '123'

print("variable nbr :", type(nbr))
print("variable logiciel :", type(logiciel))
print("variable pi :", type(pi))
print("variable verite :", type(verite))
print("variable adresse :", type(adresse)) """


# ----------------------------------------------------------------------------------
# Exercice 7 : Conversions de types, Complete le code suivant :

""" # Conversion en entier

nombre_texte = "100"
nombre_entier = int(nombre_texte)

# Conversion en texte

age = 25
age_texte = str(age)

# Conversion en float

prix = "15.99"
prix_decimal = float(prix)

print("nombre_texte :",nombre_entier,type(nombre_texte))
print("age_texte :",age_texte,type(age_texte))
print("prix_decimal :",prix_decimal,type(prix_decimal)) """


# ----------------------------------------------------------------------------------
# Exercice 8 : Opérations et types Devine le résultat de ces opérations, puis teste-les :

""" 5 + 3.0                         # 8.0               !!!
"Bonjour" + " " + "Monde"       # Bonjour Monde     !!!
"10" + "5"                      # 10 , 15           FAUX = 105 car str
int("10") + int("5")            # 15                !!!

print(5+3.0,type(5),type(3.0))
print("Bonjour" + " " + "Monde",type("Bonjour"),type("Monde"))
print("10" + "5",type("10"),type("5"))
print(int("10") + int("5")) """

# --------------------------Exercices Combinés--------------------------------------
# Exercice 9 : Calculateur simple


# CALCULATRICE SIMPLE
# Programme : Effectue des opérations basiques
# Auteur : MAD
# Date : 2025-11-10


""" # Demander deux nombres à l'utilisateur

nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))

# Afficher les résultats des opérations

print("Addition :",int(nombre1),"+",int(nombre2),"=", nombre1 + nombre2)
print("Soustraction :",int(nombre1),"+",int(nombre2),"=", nombre1 - nombre2)
print("Multiplication :",int(nombre1),"+",int(nombre2),"=", nombre1 * nombre2) """


# ----------------------------------------------------------------------------------
# Exercice 10 : Profil utilisateur Crée un programme complet qui :

# Utilise des commentaires pour expliquer chaque section
# Demande différentes informations (nom, âge, ville, profession)
# Affiche un profil complet avec des messages formatés
# Gère correctement les types de données

nom = str(input("Veuillez enter votre nom svp : "))
prenom = str(input("Veuillez entre votre prénom svp : "))

# age = (input("Quelle âge avez-vous ? "))

while True:
    age = input("Quelle age avez-vous : ")
    try:      
        integer_value = int(age)                    # Attempt to convert the input string to an integer
        print("Passons à la question suivante:")    # If conversion is successful, break the loop
        break 
    except ValueError:                              # If a ValueError occurs (meaning the input is not a valid integer),
        print("Veuillez entrer un chiffre")         # print an error message and the loop continues

region = str(input("Quelle est votre région administrative ? "))
ville = str(input("Et votre ville maintenant ? "))
emploi = str(input("Quelle est votre profession ? "))

print("==== Résultat d'entrevue ====")
print("=============================")
print("")
print(prenom.capitalize(), nom.capitalize())
print(age,"ans")
print(ville.capitalize(),"," ,region.capitalize())
print(emploi.capitalize())
print("")
print("=============================")
print("====== FIN ======")
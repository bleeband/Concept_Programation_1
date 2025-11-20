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



# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


# Solutions Complètes
# Exercices sur les Interpréteurs
# Solution Exercice 1 :

# # Dans l'interpréteur Python :
# print("Bonjour le monde!")

# # Différence :
# # - Interpréteur : exécution immédiate ligne par ligne
# # - Fichier .py : code sauvegardé et exécuté en entier
# Solution Exercice 2 :

# # Dans l'interpréteur :
# 5 + 3          # → 8
# 10 - 2 * 3     # → 4 (priorité opérations)
# (10 - 2) * 3   # → 24 (parenthèses changent la priorité)
# Exercices sur les Messages et Commentaires
# Solution Exercice 3 :

# # Déclaration des variables
# a = 5          # Premier nombre
# b = 10         # Deuxième nombre

# # Calcul de la somme
# resultat = a + b

# # Affichage du résultat
# print("Le résultat de l'addition est :", resultat)
# Solution Exercice 4 :

# """
# PRÉSENTATION PERSONNELLE
# Programme : Affiche une présentation complète
# Auteur : Débutant Python
# """

# # Déclaration des informations personnelles
# nom = "Alice"
# age = 25
# ville = "Paris"
# profession = "Développeuse"

# # Affichage de la présentation
# print("=== PRÉSENTATION ===")
# print("Nom :", nom)
# print("Âge :", age, "ans")
# print("Ville :", ville)
# print("Profession :", profession)

# # Message de fin
# print("=== FIN DE LA PRÉSENTATION ===")
# Solution Exercice 5 :

# # Programme d'interaction avec l'utilisateur

# # Demander les informations
# nom = input("Quel est votre nom ? ")
# age = input("Quel est votre âge ? ")

# # Afficher le message personnalisé
# print("Bonjour", nom + "!", "Vous avez", age, "ans.")
# print("Ravi de vous rencontrer !")
# Exercices sur les Types
# Solution Exercice 6 :

# type(42)        # → <class 'int'> (entier)
# type("Python")  # → <class 'str'> (chaîne de caractères)
# type(3.14)      # → <class 'float'> (nombre décimal)
# type(True)      # → <class 'bool'> (booléen)
# type('123')     # → <class 'str'> (chaîne, pas un nombre)
# Solution Exercice 7 :

# # Conversion en entier
# nombre_texte = "100"
# nombre_entier = int(nombre_texte)  # Convertit "100" en 100

# # Conversion en texte
# age = 25
# age_texte = str(age)  # Convertit 25 en "25"

# # Conversion en float
# prix = "15.99"
# prix_decimal = float(prix)  # Convertit "15.99" en 15.99

# # Vérification
# print(nombre_entier, type(nombre_entier))  # 100 <class 'int'>
# print(age_texte, type(age_texte))          # 25 <class 'str'>
# print(prix_decimal, type(prix_decimal))    # 15.99 <class 'float'>
# Solution Exercice 8 :

# 5 + 3.0                    # → 8.0 (int + float = float)
# "Bonjour" + " " + "Monde"  # → "Bonjour Monde" (concaténation)
# "10" + "5"                 # → "105" (concaténation de strings)
# int("10") + int("5")       # → 15 (addition d'entiers)
# Exercices Combinés
# Solution Exercice 9 :

# """
# CALCULATRICE SIMPLE
# Programme : Effectue des opérations basiques
# Auteur : [Ton nom]
# Date : [Date]
# """

# # Demander deux nombres à l'utilisateur
# nombre1 = float(input("Entrez le premier nombre : "))
# nombre2 = float(input("Entrez le deuxième nombre : "))

# # Afficher les résultats des opérations
# print("Addition :", nombre1 + nombre2)
# print("Soustraction :", nombre1 - nombre2)
# print("Multiplication :", nombre1 * nombre2)

# # Gestion de la division par zéro
# if nombre2 != 0:
#     print("Division :", nombre1 / nombre2)
# else:
#     print("Division : Impossible de diviser par zéro")
# Solution Exercice 10 :

# """
# PROFIL UTILISATEUR COMPLET
# Programme : Crée et affiche un profil personnel détaillé
# Auteur : Apprenant Python
# Version : 1.0
# """

# print("=== CRÉATION DE VOTRE PROFIL ===")

# # SECTION 1 : COLLECTE DES INFORMATIONS
# print("\nVeuillez répondre aux questions suivantes :")

# # Informations personnelles
# nom = input("Quel est votre nom complet ? ")
# age = int(input("Quel est votre âge ? "))  # Conversion en entier
# ville = input("Où habitez-vous ? ")
# profession = input("Quelle est votre profession ? ")

# # Informations supplémentaires
# taille = float(input("Quelle est votre taille en mètres (ex: 1.75) ? "))
# est_etudiant = input("Êtes-vous étudiant ? (oui/non) ").lower() == "oui"

# # SECTION 2 : TRAITEMENT DES DONNÉES
# # Calcul de l'année de naissance (approximative)
# annee_naissance = 2024 - age

# # SECTION 3 : AFFICHAGE DU PROFIL
# print("\n" + "="*40)
# print("VOTRE PROFIL COMPLET")
# print("="*40)

# print(f"Nom : {nom}")
# print(f"Âge : {age} ans (né vers {annee_naissance})")
# print(f"Ville : {ville}")
# print(f"Profession : {profession}")
# print(f"Taille : {taille} m")

# # Affichage conditionnel
# if est_etudiant:
#     print("Statut : Étudiant")
# else:
#     print("Statut : Professionnel")

# print("\nMerci d'avoir créé votre profil !")

# # SECTION 4 : RÉSUMÉ TECHNIQUE (pour l'apprentissage)
# print("\n" + "-"*20)
# print("INFORMATIONS TECHNIQUES :")
# print(f"Type de 'nom' : {type(nom)}")
# print(f"Type de 'age' : {type(age)}")
# print(f"Type de 'taille' : {type(taille)}")
# print(f"Type de 'est_etudiant' : {type(est_etudiant)}")
# Conseils Supplémentaires
# Pour tester dans l'interpréteur :

# # Tape directement ces commandes :
# >>> x = 10
# >>> type(x)
# <class 'int'>

# >>> message = "Hello"
# >>> type(message)
# <class 'str'>
# Erreurs courantes à éviter :

# # MAUVAIS :
# resultat = "5" + 3  # Erreur! On ne peut additionner string et int

# # BON :
# resultat = int("5") + 3  # → 8
# # ou
# resultat = "5" + str(3)  # → "53"
# Vérification des types :

# # Pour vérifier un type :
# nombre = 42
# if type(nombre) == int:
#     print("C'est un entier!")

# # Méthode plus pythonique :
# if isinstance(nombre, int):
#     print("C'est un entier!")
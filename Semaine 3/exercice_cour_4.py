# 17 Novembre 2025

# Exercices Python - Structures Conditionnelles (Version Révisée)

# Exercice 1 : Instructions if, elif et else

""" ## Exercice 1.1 : Validation d'âge

# Écrivez un programme qui prend un âge et affiche :

# - "Mineur" si l'âge est inférieur à 18 ans
# - "Majeur" si l'âge est entre 18 et 64 ans
# - "Senior" si l'âge est 65 ans ou plus

age = int((input("Enter votre age")))

if age and age < 18:
    adult = "Mineur"
elif age >= 18 and age <= 64:
    adult = "Majeur" 
else:
    adult = "Senior"

print(adult) """


""" # ----------------------------------------------------------------------------------
### Exercice 1.2 : Calcul de note

#Créez un programme qui convertit une note sur 100 en lettre :

# - A : 90-100
# - B : 80-89
# - C : 70-79
# - D : 60-69
# - E : 0-59

note = int((input("Enter votre note ")))

if note <= 59:
    print("Votre note est E")
elif note >=60 and note < 69:
    print("Votre note est D")
elif note >=70 and note < 79:
    print("Votre note est C")
elif note >=80 and note < 89:
    print("Votre note est B")
else:
    print("Votre note est A")

print(note) """


""" # ----------------------------------------------------------------------------------
### Exercice 1.3 : Saison de l'année

# Écrivez un programme qui prend un numéro de mois (1-12) et affiche la saison correspondante.

mois = int(input("Quel mois sommes nous"))

if mois <= 3:
    print("La saison est l'hiver")
elif mois > 3 and mois < 7:
    print("La saison est le printemps")
elif mois > 6 and mois < 10:
    print("La saison est l'été'")
else:
    print("Nous somme à l'automne")
     

# if mois in [12, 1, 2]:
#     print("Hiver")
# elif mois in [3, 4, 5]:
#     print("Printemps")
# elif mois in [6, 7, 8]:
#     print("Été")
# elif mois in [9, 10, 11]:
#     print("Automne")
# else:
#     print("Mois invalide") """



# ----------------------------------------------------------------------------------
## Exercice 2 : Opérateurs logiques avec NOT

""" ### Exercice 2.1 : Accès autorisé

# Créez un programme qui vérifie si l'accès est autorisé :

# - L'utilisateur doit avoir un badge valide
# - ET ne pas être banni
# - ET avoir payé son abonnement

badge = True
ban = False
solde = False

if not badge == False and not ban == True and not solde == True:
    print("L'utilisateur est admis")
else:
    print("L'utilisateur ne rencontre pas les pré-requis") 
    

# acces_autorise = badge and not ban and solde

# if acces_autorise:
#     print("Accès autorisé")
# else:
#     print("Accès refusé")"""


""" # ----------------------------------------------------------------------------------
### Exercice 2.2 : Conditions météorologiques

# Écrivez un programme qui détermine si on peut sortir :

# - Il ne doit pas pleuvoir
# - ET la température doit être entre 15°C et 30°C
# - ET il ne doit pas y avoir d'alerte météo

pluie = False
alert = False
temp = int(input(range(15, 30)))

if not pluie == True:
    print("il n'y a pas de pluie")
if not alert == True:
    print("il n'y a pas d'alert")
elif alert == True:
    print("Alerte en cour")
    print("Restons à l'interieur")
if temp >=15 and temp <=30:
    print("Nous pouvons sortir")
else:
    print("Restons à l'interieur")

# peut_sortir = not pluie and 15 <= temp <= 30 and not alert

# if peut_sortir:
#     print("Conditions idéales pour sortir")
# else:
#     print("Mieux vaut rester à l'intérieur") """


""" # ----------------------------------------------------------------------------------
### Exercice 2.3 : Validation de données

# Créez un programme qui vérifie si des données sont valides :

# - L'email ne doit pas être vide
# - ET l'âge doit être entre 0 et 120
# - ET le nom ne doit pas contenir de chiffres

email = input("Veuillez entrer votre adresse email : ")
age = input("Veuillez entrer votre age : ")
nom = input("Veuillez enter votre nom : ")

email_ver = email != ""
age_ver = 0 <= int(age) <=120
nom_ver = not any(char.isdigit() for char in nom)

if email_ver == True and age_ver == True and nom_ver == True:
    print(email) 
    print(age)
    print(nom)
    print("bienvenue a bord !!!")
else:
    print("Désolé, vous n'etes pas admis")

# email_valide = email != ""
# age_valide = 0 <= int(age) <= 120
# nom_valide = not any(char.isdigit() for char in nom)

# donnees_valides = email_valide and age_valide and nom_valide

# if donnees_valides:
#     print("Données valides")
# else:
#     print("Données invalides") """


# ----------------------------------------------------------------------------------
## Exercice 3 : Opérateur match


""" ### Exercice 3.1 : Directions

# Écrivez un programme qui utilise match pour afficher la direction correspondante :

# - "n" : "Nord"
# - "s" : "Sud"
# - "e" : "Est"
# - "w" : "Ouest"
# - Autre : "Direction invalide"

dir = (input(("Entrer la premiere lettre de votre direction (n,s,e,o) : ")))

while dir != "q":

    match dir:
        case "n":
            print("Nord")
        case "s":
            print("Sud")
        case "e":
            print("Est")
        case "o":
            print("Ouest")
        case "_":
            print("ouff vous êtes perdu!!!")
    dir = (input(("Alors, vous allez ou? (n,s,e,o ou q) : "))) """


""" # ----------------------------------------------------------------------------------
### Exercice 3.2 : Statut de commande

# Créez un programme qui traite des statuts de commande avec match :

# - "en_attente" : "Votre commande est en attente"
# - "expediee" : "Votre commande a été expédiée"
# - "livree" : "Votre commande a été livrée"
# - "annulee" : "Votre commande a été annulée"

statut = (input(("Entrer le code du statut : ")))

while statut != "q":

    match statut:
        case 1:
            print("en_attente" "\n" "Votre commande est en attente")
        case 2:
            print("expediee" "\n" "Votre commande a été expédiée")
        case 3:
            print("livree" "\n" "Votre commande a été livrée")
        case 4:
            print("annulee" "\n" "Votre commande a été annulée")
        case _:
            print("Veuillez communiquer avec l'admin")
    
    statut = (input(("Alors, quel est le code ? (q) : "))) """
            

""" # ----------------------------------------------------------------------------------
### Exercice 3.3 : Types de véhicules

# Écrivez un programme qui affiche le type de véhicule :

# - "voiture" : "Véhicule terrestre à 4 roues"
# - "moto" : "Véhicule terrestre à 2 roues"
# - "bateau" : "Véhicule maritime"
# - "avion" : "Véhicule aérien"

ty_veh = (input(("Entrer le vehicule a traduire : ")))

while ty_veh != "q":

    match ty_veh:
        case "car":
            print(f"{ty_veh} : voiture \nVehicule terrestre à 4 roues")
        case "moto":
            print(f"{ty_veh} : moto \nVehicule terrestre à 2 roues")
        case "boat":
            print(f"{ty_veh} : bateau \nVehicule maritime")
        case "plane":
            print(f"{ty_veh} : avion \nVehicule aerien")
        case "quad":
            print(f"{ty_veh} : v.t.t \nVehicule tout-terrain")
        case _:
            print(f"{ty_veh} : Ceci n'est pas un vehicule connu")
    
    ty_veh = (input(("Alors, vehicule a traduire ? (q) : "))) """


# ----------------------------------------------------------------------------------
## Exercice 4 : Opérateur ternaire

""" ### Exercice 4.1 : Positif ou négatif

# Utilisez l'opérateur ternaire pour déterminer si un nombre est positif ou négatif.


nombre = int((input(("Entrer un nombre : "))))

signe = "Positif" if nombre > 0 else "Negatif" if nombre < 0 else "zero"
print(signe) """



""" # ----------------------------------------------------------------------------------
### Exercice 4.2 : Majorité légale

# Créez un programme qui affiche "majeur" ou "mineur" selon l'âge avec l'opérateur ternaire.


age = int((input(("Entrer votre age : "))))

valeur = "Mineur" if age < 18 else "Majeur"
print(valeur) """


""" # ----------------------------------------------------------------------------------
### Exercice 4.3 : Remise automatique

# Écrivez un programme qui applique une remise de 20% si le prix est supérieur à 100$, sinon garde le prix original avec l'opérateur ternaire.

prix_ori = float((input(("Entrer le prix indique : "))))
rabais = 1 if prix_ori <= 100 else 0.2
prix_final = prix_ori - (prix_ori * rabais)

print(f"Votre total est de ${prix_final:,.2f}") """


# ----------------------------------------------------------------------------------
## Exercice 5 : Combinaisons

""" ### Exercice 5.1 : Système d'authentification

# Créez un programme qui vérifie :

# - Nom d'utilisateur non vide
# - Mot de passe d'au moins 6 caractères
# - L'utilisateur n'est pas bloqué

user = str(input(("Entrer votre username : ")))

if len(user) <= 0:
    print("votre usager doit contenir un minimum de caractere")
else:
    passw = str(input(("Entrer votre password : ")))
    if len(passw) <= 5:
        print("entrer un minimum de 6 caractere")
    else:
        print("vous etes admis") """


""" # ----------------------------------------------------------------------------------
### Exercice 5.2 : Calculateur de catégorie sportive

# Écrivez un programme qui détermine la catégorie sportive selon l'âge :

age = int((input(("Entrer votre age : "))))

if 6 <= age <= 7:
    categorie = "Poussin"
elif 8 <= age <= 9:
    categorie = "Benjamin"
elif 10 <= age <= 11:
    categorie = "Minime"
elif 12 <= age <= 15:
    categorie = "Cadet"
elif 16 <= age <= 17:
    categorie = "Junior"
elif 18 <= age <= 39:
    categorie = "Senior"
elif age >= 40:
    categorie = "Veteran"
else:
    categorie = "Trop jeune"

print(f"Tu as {age} ans, dans la categorie : {categorie}")
 """



# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

# Solutions
# Solution Exercice 1
# 1.1 : Validation d'âge
# age = 25

# if age < 18:
#     print("Mineur")
# elif age <= 64:
#     print("Majeur")
# else:
#     print("Senior")
# 1.2 : Calcul de note
# note = 85

# if note >= 90:
#     print("A")
# elif note >= 80:
#     print("B")
# elif note >= 70:
#     print("C")
# elif note >= 60:
#     print("D")
# else:
#     print("E")
# 1.3 : Saison de l'année
# mois = 7

# if mois in [12, 1, 2]:
#     print("Hiver")
# elif mois in [3, 4, 5]:
#     print("Printemps")
# elif mois in [6, 7, 8]:
#     print("Été")
# elif mois in [9, 10, 11]:
#     print("Automne")
# else:
#     print("Mois invalide")
# Solution Exercice 2
# 2.1 : Accès autorisé
# badge_valide = True
# utilisateur_banni = False
# abonnement_paye = True

# acces_autorise = badge_valide and not utilisateur_banni and abonnement_paye

# if acces_autorise:
#     print("Accès autorisé")
# else:
#     print("Accès refusé")
# 2.2 : Conditions météorologiques
# il_pleut = False
# temperature = 22
# alerte_meteo = False

# peut_sortir = not il_pleut and 15 <= temperature <= 30 and not alerte_meteo

# if peut_sortir:
#     print("Conditions idéales pour sortir")
# else:
#     print("Mieux vaut rester à l'intérieur")
# 2.3 : Validation de données
# email = "user@example.com"
# age = 25
# nom = "Dupont"

# email_valide = email != ""
# age_valide = 0 <= age <= 120
# nom_valide = not any(char.isdigit() for char in nom)

# donnees_valides = email_valide and age_valide and nom_valide

# if donnees_valides:
#     print("Données valides")
# else:
#     print("Données invalides")
# Solution Exercice 3
# 3.1 : Directions
# direction = "n"

# match direction:
#     case "n":
#         print("Nord")
#     case "s":
#         print("Sud")
#     case "e":
#         print("Est")
#     case "w":
#         print("Ouest")
#     case _:
#         print("Direction invalide")
# 3.2 : Statut de commande
# statut = "expediee"

# match statut:
#     case "en_attente":
#         print("Votre commande est en attente")
#     case "expediee":
#         print("Votre commande a été expédiée")
#     case "livree":
#         print("Votre commande a été livrée")
#     case "annulee":
#         print("Votre commande a été annulée")
#     case _:
#         print("Statut inconnu")
# 3.3 : Types de véhicules
# vehicule = "moto"

# match vehicule:
#     case "voiture":
#         print("Véhicule terrestre à 4 roues")
#     case "moto":
#         print("Véhicule terrestre à 2 roues")
#     case "bateau":
#         print("Véhicule maritime")
#     case "avion":
#         print("Véhicule aérien")
#     case _:
#         print("Type de véhicule non reconnu")
# Solution Exercice 4
# 4.1 : Positif ou négatif
# nombre = -5

# resultat = "positif" if nombre >= 0 else "négatif"
# print(f"Le nombre {nombre} est {resultat}")
# 4.2 : Majorité légale
# age = 20

# statut = "majeur" if age >= 18 else "mineur"
# print(f"À {age} ans, vous êtes {statut}")
# 4.3 : Remise automatique
# prix_original = 120

# prix_final = prix_original * 0.8 if prix_original > 100 else prix_original
# print(f"Prix final : {prix_final}$")


# Solution Exercice 5
# 5.1 : Système d'authentification

# username = "john_doe"
# password = "secret123"
# user_blocked = False

# username_ok = username != ""
# password_ok = len(password) >= 6
# not_blocked = not user_blocked

# authentification_reussie = username_ok and password_ok and not_blocked

# if authentification_reussie:
#     print("Authentification réussie")
# else:
#     print("Échec de l'authentification")
#     if not username_ok:
#         print("- Le nom d'utilisateur ne peut pas être vide")
#     if not password_ok:
#         print("- Le mot de passe doit avoir au moins 6 caractères")
#     if user_blocked:
#         print("- L'utilisateur est bloqué")`


# 5.2 : Calculateur de catégorie sportive
# age = 14

# if 6 <= age <= 7:
#     categorie = "Poussin"
# elif 8 <= age <= 9:
#     categorie = "Benjamin"
# elif 10 <= age <= 11:
#     categorie = "Minime"
# elif 12 <= age <= 15:
#     categorie = "Cadet"
# elif 16 <= age <= 17:
#     categorie = "Junior"
# elif 18 <= age <= 39:
#     categorie = "Senior"
# elif age >= 40:
#     categorie = "Vétéran"
# else:
#     categorie = "Trop jeune"

# # Utilisation de l'opérateur ternaire pour le message
# message = "Bienvenue en compétition !" if categorie != "Trop jeune" else "Revenez quand vous serez plus âgé"

# print(f"À {age} ans, catégorie : {categorie}")
# print(message)

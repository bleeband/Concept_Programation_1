# 19 Novembre 2025

# Exercices Python - Boucles et Itérations

# ----------------------------------------------------------------------------------
# Exercice 1 : Les itérables et la boucle for

""" # Exercice 1.1 : Parcours de liste
# Écrivez un programme qui parcourt une liste de fruits et affiche chaque fruit avec sa position.

liste = list((184, 186, 187, 189))

for index, item in enumerate(liste):
    print(f"Position {index}: {item}") """


""" # ----------------------------------------------------------------------------------
# Exercice 1.2 : Somme des éléments
# Créez un programme qui calcule la somme de tous les éléments d'une liste de nombres.

liste = list((1, 2, 3, 4))

print(sum(liste)) """


""" # ----------------------------------------------------------------------------------
# Exercice 1.3 : Comptage de caractères
# Écrivez un programme qui compte combien de fois la lettre 'a' apparaît dans une chaîne de caractères.

chaine = "allo banane et patate"

print(chaine.count("a")) """


# ----------------------------------------------------------------------------------
# Exercice 2 : Le type range()

""" # Exercice 2.1 : Nombres pairs
# Utilisez range() pour afficher tous les nombres pairs entre 0 et 20.

x = range(0, 21, 2)
print(x)
print(list(x)) """


""" # ----------------------------------------------------------------------------------
# Exercice 2.2 : Table de multiplication
# Créez un programme qui affiche la table de multiplication d'un nombre donné de 1 à 10.

x = int(input("entrer votre chiffre :"))
multi = x

# for multi in range(1, 11):
#     print(f"\n--- Table de multiplication de {multi} ---")

for i in range(1, 11):
    table = x * i
    print(f"{multi} x {i} = {table}") """


""" # ----------------------------------------------------------------------------------
# Exercice 2.3 : Compte à rebours
# Écrivez un programme qui affiche un compte à rebours de 10 à 1.

# x = range(10, 0, -1)
# print(list(x))

for x in range(10, -1, -1):
    print(x) """


# ----------------------------------------------------------------------------------
# Exercice 3 : La fonction enumerate()

""" # Exercice 3.1 : Liste numérotée
# Utilisez enumerate() pour afficher une liste de villes avec leur numéro.

x = ["pomme", "banane", "patate"]
y = enumerate(x)

print(list(y)) """

""" # ----------------------------------------------------------------------------------
# Exercice 3.2 : Recherche d'élément
# Créez un programme qui trouve la position d'un élément spécifique dans une liste.

y = ["pomme", "banane", "patate"]
print(y)
x = (input("entrer votre fruit :"))
z = y.index(x)
print(z) """


""" # ----------------------------------------------------------------------------------
# Exercice 3.3 : Modification sélective
# Écrivez un programme qui double la valeur des éléments aux positions paires d'une liste.

ma_liste = [0, 1, 2, 3, 4, 5, 6]

for i in range(0, len(ma_liste), 2):
    ma_liste[i] = ma_liste[i] * 2
print(ma_liste) """


# ----------------------------------------------------------------------------------
# Exercice 4 : La boucle while

""" # Exercice 4.1 : Saisie contrôlée
# Créez un programme qui demande un nombre entre 1 et 10 jusqu'à ce que l'utilisateur donne une valeur valide.

while True:
    try:
        nbr = int(input("Entrez votre nombre : "))
        if 0 <= nbr <= 10:
            print(f"{nbr} est nombre valide")
            break # Sort de la boucle si l'âge est valide
        else:
            print("veuillez reessayer")
    except ValueError:
        print("Veuillez saisir un nombre valide.") """


""" # ----------------------------------------------------------------------------------
# Exercice 4.2 : Devinette de nombre
# Écrivez un programme où l'ordinateur choisit un nombre et l'utilisateur doit le deviner.

import random

x = (random.randrange(0, 10))
y = int(input("choisir un chiffre en 0 et 10"))

while y != x:
    try:
        print("Raté, réessayez.")
        y = int(input("Choisir un chiffre entre 0 et 10 : "))
    except ValueError:
        print("Veuillez saisir un nombre valide.")

print("Félicitations !") """


""" # ----------------------------------------------------------------------------------
# Exercice 4.3 : Calcul de factorielle
# Créez un programme qui calcule la factorielle d'un nombre en utilisant while.

starting_number = int(input("entrer un nombre ? "))
number = starting_number
total = 1

while number > 1:
    total *= number  # multiplie le total par le nombre (5, puis 4, puis 3...)
    number -= 1  # réduit le nombre de un

print('{}! est égal à {}'.format(starting_number, total)) """

# ----------------------------------------------------------------------------------
# Exercice 5 : Instructions break, continue et pass

# Exercice 5.1 : Recherche avec break
# Écrivez un programme qui cherche un nombre dans une liste et s'arrête dès qu'il le trouve.

""" liste = [1,2,3,4,5]

for x in liste:
    print(x)
    if x > 3:
        break """


# ----------------------------------------------------------------------------------
# Exercice 5.2 : Filtrage avec continue
# Créez un programme qui affiche seulement les nombres positifs d'une liste en utilisant continue.

""" for x in range(0, 11):
    if x % 2 == 1:
        continue
    print(f"la valeur de x est {x}") """

""" # ----------------------------------------------------------------------------------
# Exercice 5.3 : Structure avec pass
# Écrivez un programme qui utilise pass comme placeholder pour une condition à implémenter plus tard.

nombres = [1, 2, 3, 4, 5]

for nombre in nombres:
    if nombre % 2 == 0:
        # À implémenter : traitement des nombres pairs
        #print(f"nombre pairs sont {nombre}")
        pass
    else:
        print(f"nombre impair sont {nombre}") """

# ----------------------------------------------------------------------------------
# Exercice 6 : Combinaisons

# Exercice 6.1 : Statistiques d'une liste
# Créez un programme qui calcule le minimum, maximum et moyenne d'une liste de nombres.

""" note = [68, 78, 65, 81, 72]

print(note)
print(sum(note) / len(note))
print(min(note))
print(max(note))
print()

if note:
    minimum = note[0]
    maximum = note[0]
    somme = 0

    for nombre in note:
        if nombre < minimum:
            minimum = nombre
        if nombre > maximum:
            maximum = nombre
        somme += nombre

    moyenne = somme / len(note)

    print(f"Minimum : {minimum}")
    print(f"Maximum : {maximum}")
    print(f"Moyenne : {moyenne:.2f}")
else:
    print("La liste est vide") """



# ----------------------------------------------------------------------------------
# Exercice 6.2 : Palindrome
# Écrivez un programme qui vérifie si un mot est un palindrome.

""" def palindrome(texte):
  # 1. Nettoyer le texte : retirer les espaces et mettre en minuscules
  texte_nettoye = "".join(texte.split()).lower()

  # 2. Inverser le texte nettoyé
  texte_inverse = texte_nettoye[::-1]

  # 3. Comparer les deux chaînes
  return texte_nettoye == texte_inverse

# Exemple d'utilisation
print(palindrome("la mariee ira mal"))
print(palindrome("Bonjour"))
print(palindrome("1 2 3 2 1")) """

# ----------------------------------------------------------------------------------
# Exercice 6.3 : Jeu de devinette amélioré
# Créez un jeu de devinette avec limite d'essais et indices.

""" atrouver = 50
essais_max = 5
essais = 0

while essais < essais_max:
    essai = int(input("entrer un nombre :"))
    essais += 1

    if essai == atrouver:
        print(f"Bravo ! Trouvé en {essais} essai(s)")
        break
    elif essai < atrouver:
        print("Trop petit")
    else:
        print("Trop grand")

    if abs(essai - atrouver) <= 5:
        print("Vous êtes très proche !")

    print(f"Il vous reste {essais_max - essais} essai(s)")
else:
    print(f"Perdu ! Le nombre était {atrouver}") """




# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


# Solutions
# Solution Exercice 1
# 1.1 : Parcours de liste
# fruits = ["pomme", "banane", "orange", "kiwi"]

# for fruit in fruits:
#     print(fruit)
# 1.2 : Somme des éléments
# nombres = [5, 12, 8, 3, 15]
# somme = 0

# for nombre in nombres:
#     somme += nombre

# print(f"La somme est : {somme}")
# 1.3 : Comptage de caractères
# texte = "programmation python avancee"
# compteur = 0

# for lettre in texte:
#     if lettre == 'a':
#         compteur += 1

# print(f"La lettre 'a' apparaît {compteur} fois")
# Solution Exercice 2
# 2.1 : Nombres pairs
# for i in range(0, 21, 2):
#     print(i)
# 2.2 : Table de multiplication
# nombre = 7

# for i in range(1, 11):
#     resultat = nombre * i
#     print(f"{nombre} x {i} = {resultat}")
# 2.3 : Compte à rebours
# for i in range(10, 0, -1):
#     print(i)
# print("Décollage !")
# Solution Exercice 3
# 3.1 : Liste numérotée
# villes = ["Paris", "Lyon", "Marseille", "Toulouse"]

# for index, ville in enumerate(villes):
#     print(f"{index + 1}. {ville}")
# 3.2 : Recherche d'élément
# nombres = [10, 25, 30, 45, 50]
# recherche = 30

# for index, nombre in enumerate(nombres):
#     if nombre == recherche:
#         print(f"Trouvé à la position {index}")
#         break
# 3.3 : Modification sélective
# nombres = [1, 2, 3, 4, 5, 6]
# resultat = []

# for index, nombre in enumerate(nombres):
#     if index % 2 == 0:  # positions paires
#         resultat.append(nombre * 2)
#     else:
#         resultat.append(nombre)

# print(resultat)
# Solution Exercice 4
# 4.1 : Saisie contrôlée
# nombre = 0

# while nombre < 1 or nombre > 10:
#     nombre = 5  # Simulation d'une saisie
#     if 1 <= nombre <= 10:
#         print(f"Nombre valide : {nombre}")
#     else:
#         print("Erreur : entrez un nombre entre 1 et 10")
#         nombre = 0  # Pour continuer la boucle
# 4.2 : Devinette de nombre
# atrouver = 42
# essai = 0
# trouve = False

# while not trouve:
#     essai = 25  # Simulation d'une saisie
#     if essai == atrouver:
#         print("Bravo ! Vous avez trouvé le nombre secret.")
#         trouve = True
#     elif essai < atrouver:
#         print("Trop petit, essayez encore.")
#     else:
#         print("Trop grand, essayez encore.")
# 4.3 : Calcul de factorielle
# nombre = 5
# factorial = 1
# compteur = 1

# while compteur <= nombre:
#     factorial *= compteur
#     compteur += 1

# print(f"La factorielle de {nombre} est {factorial}")
# Solution Exercice 5
# 5.1 : Recherche avec break
# nombres = [15, 8, 23, 42, 7, 19]
# recherche = 42

# for nombre in nombres:
#     print(f"Vérification de {nombre}")
#     if nombre == recherche:
#         print("Nombre trouvé !")
#         break
# else:
#     print("Nombre non trouvé")
# 5.2 : Filtrage avec continue
# nombres = [5, -2, 10, -8, 3, -1, 7]

# for nombre in nombres:
#     if nombre < 0:
#         continue
#     print(f"Nombre positif : {nombre}")
# 5.3 : Structure avec pass
# nombres = [1, 2, 3, 4, 5]

# for nombre in nombres:
#     if nombre % 2 == 0:
#         # À implémenter : traitement des nombres pairs
#         pass
#     else:
#         print(f"Nombre impair : {nombre}")
# Solution Exercice 6
# 6.1 : Statistiques d'une liste
# nombres = [12, 45, 8, 32, 19, 67, 23]

# if nombres:
#     minimum = nombres[0]
#     maximum = nombres[0]
#     somme = 0

#     for nombre in nombres:
#         if nombre < minimum:
#             minimum = nombre
#         if nombre > maximum:
#             maximum = nombre
#         somme += nombre

#     moyenne = somme / len(nombres)

#     print(f"Minimum : {minimum}")
#     print(f"Maximum : {maximum}")
#     print(f"Moyenne : {moyenne:.2f}")
# else:
#     print("La liste est vide")


# 6.2 : Palindrome

# mot = "radar"
# est_palindrome = True

# for i in range(len(mot) // 2):
#     if mot[i] != mot[len(mot) - 1 - i]:
#         est_palindrome = False
#         break

# if est_palindrome:
#     print(f"'{mot}' est un palindrome")
# else:
#     print(f"'{mot}' n'est pas un palindrome")


# 6.3 : Jeu de devinette amélioré
# atrouver = 50
# essais_max = 5
# essais = 0

# while essais < essais_max:
#     essai = 30  # Simulation d'une saisie
#     essais += 1

#     if essai == atrouver:
#         print(f"Bravo ! Trouvé en {essais} essai(s)")
#         break
#     elif essai < atrouver:
#         print("Trop petit")
#     else:
#         print("Trop grand")

#     if abs(essai - atrouver) <= 5:
#         print("Vous êtes très proche !")

#     print(f"Il vous reste {essais_max - essais} essai(s)")
# else:
#     print(f"Perdu ! Le nombre était {atrouver}")
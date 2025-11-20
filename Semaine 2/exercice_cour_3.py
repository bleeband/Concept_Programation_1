""" # ----------------------------------------------------------------------------------
# Exercice 1 : Calculs avec précédence
# Calcule mentalement le résultat de ces expressions, puis vérifie avec Python :

# Expression 1 = 16
resultat1 = 10 + 3 * 2


# Expression 2 = 26
resultat2 = (10 + 3) * 2

# Expression 3 = 13
resultat3 = 15 - 4 / 2

# Expression 4 = 5.5
resultat4 = (15 - 4) / 2

# Expression 5 = 16
resultat5 = 2 ** 3 * 2

# Expression 6 = 64
resultat6 = 2 ** (3 * 2)

print(resultat1,resultat2,resultat3,resultat4,resultat5,resultat6) """


""" # ----------------------------------------------------------------------------------
# Exercice 2 : Associativité des opérateurs
# Trouve le résultat de ces expressions en tenant compte de l'associativité :

# Expression 1 (associativité gauche-droite) = 8
resultat1 = 15 - 4 - 3

# Expression 2 (associativité droite-gauche) = 512
resultat2 = 2 ** 3 ** 2

# Expression 3 = 2.5
resultat3 = 20 / 4 / 2

# Expression 4 = false
resultat4 = not True or False

print(resultat1,resultat2,resultat3,resultat4) """


""" # ----------------------------------------------------------------------------------
# Exercice 3 : Expressions complexes
# Évalue ces expressions complexes :

# Expression 1 = 17
a = 5
b = 3
c = 2
resultat1 = a + b * c ** 2

# Expression 2 = 32
resultat2 = (a + b) * c ** 2

# Expression 3 = 8
# // = RÉSULTAT ENTIER
resultat3 = a * b // c + 1

# Expression 4 = 8
# % = MODULO
resultat4 = a % b + c * 3 

print(resultat1,resultat2,resultat3,resultat4) """


""" # ----------------------------------------------------------------------------------
# Exercices sur la Conversion Simple et Cast

# Exercice 4 : Conversions de base
# Complète le code suivant avec les conversions appropriées :

# Conversion de string vers entier
texte_nombre = "123"
nombre_entier = int(texte_nombre)
print(nombre_entier)

# Conversion de string vers float
texte_decimal = "45.67"
nombre_decimal = float(texte_decimal)
print(nombre_decimal)

# Conversion de float vers entier
prix = 99.99
prix_entier = int(prix)
print(prix_entier)

# Conversion de booléen vers entier
vrai = True
faux = False
vrai_entier = int(vrai)
faux_entier = int(faux)

print(vrai_entier)
print(faux_entier) """


""" # ----------------------------------------------------------------------------------
# Exercice 5 : Conversions avec input
# Écris un programme qui demande deux nombres à l'utilisateur et effectue différentes conversions :

# Demander deux nombres
nombre1 = input("Entrez le premier nombre : ")
nombre2 = input("Entrez le deuxième nombre : ")

# Convertir en entiers et calculer la somme
somme = int(nombre1) + int(nombre2)
print(somme)

# Convertir en floats et calculer la moyenne
moyenne = float(somme / 2)
print(moyenne)

# Convertir en strings et créer un message
message = 'valeur de a', int(nombre1), 'valeur de b', int(nombre2)
print(message) """


""" # ----------------------------------------------------------------------------------
# Exercice 6 : Gestion des erreurs de conversion
# Écris un programme qui gère les erreurs de conversion :

# Essayer de convertir différentes valeurs
valeurs = ["123", "45.67", "abc", "789", "12.34.56"]

for valeur in valeurs:
    try:
        # Essayer de convertir en float
        resultat = [float(x) for x in valeurs]
        print(f"Conversion réussie: {valeur} -> {resultat}")
    except ValueError:
        print(f"Erreur: impossible de convertir '{valeur}' en nombre") """


""" # Exercices sur les Types Mutables et Immuables
# ----------------------------------------------------------------------------------
# Exercice 7 : Identification des types
# Pour chaque variable, indique si son type est mutable ou immuable :

# Liste de variables

a = 10                              #int    immuable
b = "hello"                         #str    immuable
c = [1, 2, 3]                       #list   mutable
d = (4, 5, 6)                       #turple immuable
e = {"nom": "Alice", "age": 25}     #dict   mutable
f = 3.14                            #float  immuable
g = True                            #bool   immuable
h = {1, 2, 3}                       #dict   mutable """


""" # ----------------------------------------------------------------------------------
# Exercice 8 : Manipulation des types mutables
# Observe le comportement des types mutables :

# Liste (mutable)
liste1 = [1, 2, 3]
liste2 = liste1
liste2.append(4)

print("Liste1 après modification de liste2:", liste1)

# Dictionnaire (mutable)
dict1 = {"a": 1, "b": 2}
dict2 = dict1
dict2["c"] = 3

print("Dict1 après modification de dict2:", dict1) """


""" # ----------------------------------------------------------------------------------
# Exercice 9 : Comportement des types immuables
# Observe le comportement des types immuables :

# String (immuable)
texte1 = "hello"
texte2 = texte1
texte2 = texte2 + " world"

print("Texte1 après opération sur texte2:", texte1)
print("Texte2 après opération sur texte2:", texte2)

# Tuple (immuable)
tuple1 = (1, 2, 3)
tuple2 = tuple1
#tuple2[0] = 4  # Cette ligne générera une erreur

print("Tuple1 après opération sur tuple2:", tuple1) """


""" # ----------------------------------------------------------------------------------
# Exercice 10 : Copie de types mutables
# Écris un programme qui montre la différence entre copie superficielle et référence :

# Liste originale
originale = [1, 2, [3, 4]]

# Référence
reference = originale

# Copie superficielle
copie_superficielle = reference.copy()

# Modification
copie_superficielle[1] = 100
copie_superficielle[2][0] = 300

print("Originale après modifications:", originale)
print("Référence après modifications:", reference)
print("Copie superficielle après modifications:", copie_superficielle) """


""" # ----------------------------------------------------------------------------------
# Exercices sur les Opérateurs de Comparaison et d'Identité

# Exercice 11 : Opérateurs de comparaison
# Prédit le résultat de ces comparaisons :

# Comparaisons numériques
a = 10
b = 5
c = 10

resultat1 = a > b       #true
resultat2 = a == c      #true
resultat3 = a != b      #true
resultat4 = a <= c      #true
resultat5 = b >= a      #false

# Comparaisons de strings
texte1 = "abc"
texte2 = "abd"
texte3 = "abc"

resultat6 = texte1 == texte3    #true
resultat7 = texte1 < texte2     #true
resultat8 = texte1 != texte2    #true

print(resultat1,resultat2,resultat3,resultat4,resultat5,resultat6,resultat7,resultat8) """

""" # ----------------------------------------------------------------------------------
# Exercice 12 : Opérateurs d'identité
# Comprends la différence entre == et is :

# Cas 1 : Même valeur, même objet
a = 100
b = 100
resultat1 = a == b
resultat2 = a is b
print(resultat1)
print(resultat2)

# Cas 2 : Même valeur, objets différents
c = [1, 2, 3]
d = [1, 2, 3]
resultat3 = c == d
resultat4 = c is d

print(resultat3)
print(resultat4)


# Cas 3 : Petits entiers (interning)
e = 5
f = 5
resultat5 = e is f

print(resultat5)


# Cas 4 : Gros entiers
g = 1000
h = 1000
resultat6 = g is h

print(resultat6) """


""" # ----------------------------------------------------------------------------------
# Exercice 13 : Expressions booléennes complexes
# Évalue ces expressions complexes :

x = 10
y = 5
z = 10

# Expression 1  =  true
resultat1 = x > y and x == z

# Expression 2  =  true
resultat2 = x < y or x == z

# Expression 3  =  true
resultat3 = not (x == y)

# Expression 4  =  true
resultat4 = x > y and x != z or y < z

# Expression 5  = ( T and F ) or True  REP : false  CORRECTION--  TRUE
resultat5 = (x > y and x != z) or y < z

print(resultat1)
print(resultat2)
print(resultat3)
print(resultat4)
print(resultat5) """


""" # ----------------------------------------------------------------------------------
# Exercice 14 : Programme de validation
# Écris un programme qui valide des conditions complexes :

# Données d'un utilisateur
sexe = "Mr"
nom = "Dufour"
age = 25
salaire = 44000
experience = 3
diplome = True

# Conditions pour un prêt
condition1 = age >= 18 and salaire >= 40000
condition2 = experience >= 2 or diplome
condition3 = salaire >= 50000 or (diplome and experience >= 1)

# Validation finale
pret_approuve = condition1 and condition2 and condition3

print(" ")
print(f"Condition 1 respecté : {condition1}")
print(f"Condition 2 respecté : {condition2}")
print(f"Condition 3 respecté : {condition3}")
print(f"Prêt approuvé : {pret_approuve}")
print(" ")

if pret_approuve:
    print(f"Félicitation {sexe} {nom}, votre prêt est approuvé")
else:
    print(f"Désolé {sexe} {nom}, votre prêt est refusé") """



# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


# Solutions Complètes
# Solutions Exercice 1 : Calculs avec précédence
# # Expression 1
# resultat1 = 10 + 3 * 2  # 10 + 6 = 16

# # Expression 2
# resultat2 = (10 + 3) * 2  # 13 * 2 = 26

# # Expression 3
# resultat3 = 15 - 4 / 2  # 15 - 2 = 13

# # Expression 4
# resultat4 = (15 - 4) / 2  # 11 / 2 = 5.5

# # Expression 5
# resultat5 = 2 ** 3 * 2  # 8 * 2 = 16

# # Expression 6
# resultat6 = 2 ** (3 * 2)  # 2 ** 6 = 64

# print("Exercice 1 résultats:")
# print(f"10 + 3 * 2 = {resultat1}")
# print(f"(10 + 3) * 2 = {resultat2}")
# print(f"15 - 4 / 2 = {resultat3}")
# print(f"(15 - 4) / 2 = {resultat4}")
# print(f"2 ** 3 * 2 = {resultat5}")
# print(f"2 ** (3 * 2) = {resultat6}")
# Solutions Exercice 2 : Associativité des opérateurs
# # Expression 1 (associativité gauche-droite)
# resultat1 = 15 - 4 - 3  # (15-4)-3 = 11-3 = 8

# # Expression 2 (associativité droite-gauche)
# resultat2 = 2 ** 3 ** 2  # 2**(3**2) = 2**9 = 512

# # Expression 3
# resultat3 = 20 / 4 / 2  # (20/4)/2 = 5/2 = 2.5

# # Expression 4
# resultat4 = not True or False  # (not True) or False = False or False = False

# print("\nExercice 2 résultats:")
# print(f"15 - 4 - 3 = {resultat1}")
# print(f"2 ** 3 ** 2 = {resultat2}")
# print(f"20 / 4 / 2 = {resultat3}")
# print(f"not True or False = {resultat4}")
# Solutions Exercice 3 : Expressions complexes
# # Expression 1
# a = 5
# b = 3
# c = 2
# resultat1 = a + b * c ** 2  # 5 + 3*(2**2) = 5 + 3*4 = 5 + 12 = 17

# # Expression 2
# resultat2 = (a + b) * c ** 2  # (5+3)*2**2 = 8*4 = 32

# # Expression 3
# resultat3 = a * b // c + 1  # (5*3)//2 + 1 = 15//2 + 1 = 7 + 1 = 8

# # Expression 4
# resultat4 = a % b + c * 3  # 5%3 + 2*3 = 2 + 6 = 8

# print("\nExercice 3 résultats:")
# print(f"a + b * c ** 2 = {resultat1}")
# print(f"(a + b) * c ** 2 = {resultat2}")
# print(f"a * b // c + 1 = {resultat3}")
# print(f"a % b + c * 3 = {resultat4}")
# Solutions Exercice 4 : Conversions de base
# # Conversion de string vers entier
# texte_nombre = "123"
# nombre_entier = int(texte_nombre)

# # Conversion de string vers float
# texte_decimal = "45.67"
# nombre_decimal = float(texte_decimal)

# # Conversion de float vers entier
# prix = 99.99
# prix_entier = int(prix)  # 99 (troncature)

# # Conversion de booléen vers entier
# vrai = True
# faux = False
# vrai_entier = int(vrai)  # 1
# faux_entier = int(faux)  # 0

# print("\nExercice 4 résultats:")
# print(f"int('123') = {nombre_entier}")
# print(f"float('45.67') = {nombre_decimal}")
# print(f"int(99.99) = {prix_entier}")
# print(f"int(True) = {vrai_entier}")
# print(f"int(False) = {faux_entier}")
# Solutions Exercice 5 : Conversions avec input
# # Demander deux nombres
# nombre1 = input("Entrez le premier nombre : ")
# nombre2 = input("Entrez le deuxième nombre : ")

# # Convertir en entiers et calculer la somme
# somme = int(nombre1) + int(nombre2)

# # Convertir en floats et calculer la moyenne
# moyenne = (float(nombre1) + float(nombre2)) / 2

# # Convertir en strings et créer un message
# message = "Nombres: " + nombre1 + " et " + nombre2

# print("\nExercice 5 résultats:")
# print(f"Somme: {somme}")
# print(f"Moyenne: {moyenne}")
# print(f"Message: {message}")
# Solutions Exercice 6 : Gestion des erreurs de conversion
# # Essayer de convertir différentes valeurs
# valeurs = ["123", "45.67", "abc", "789", "12.34.56"]

# print("\nExercice 6 résultats:")
# for valeur in valeurs:
#     try:
#         # Essayer de convertir en float
#         resultat = float(valeur)
#         print(f"Conversion réussie: {valeur} -> {resultat}")
#     except ValueError:
#         print(f"Erreur: impossible de convertir '{valeur}' en nombre")
# Solutions Exercice 7 : Identification des types
# # Liste de variables
# a = 10          # int - immuable
# b = "hello"     # str - immuable
# c = [1, 2, 3]   # list - mutable
# d = (4, 5, 6)   # tuple - immuable
# e = {"nom": "Alice", "age": 25}  # dict - mutable
# f = 3.14        # float - immuable
# g = True        # bool - immuable
# h = {1, 2, 3}   # set - mutable

# print("\nExercice 7 résultats:")
# print(f"int (10): immuable")
# print(f"str ('hello'): immuable")
# print(f"list ([1,2,3]): mutable")
# print(f"tuple ((4,5,6)): immuable")
# print(f"dict ({{'nom': 'Alice'}}): mutable")
# print(f"float (3.14): immuable")
# print(f"bool (True): immuable")
# print(f"set ({{1,2,3}}): mutable")
# Solutions Exercice 8 : Manipulation des types mutables
# # Liste (mutable)
# liste1 = [1, 2, 3]
# liste2 = liste1
# liste2.append(4)

# print("\nExercice 8 résultats:")
# print("Liste1 après modification de liste2:", liste1)  # [1, 2, 3, 4]

# # Dictionnaire (mutable)
# dict1 = {"a": 1, "b": 2}
# dict2 = dict1
# dict2["c"] = 3

# print("Dict1 après modification de dict2:", dict1)  # {'a': 1, 'b': 2, 'c': 3}
# Solutions Exercice 9 : Comportement des types immuables
# # String (immuable)
# texte1 = "hello"
# texte2 = texte1
# texte2 = texte2 + " world"

# print("\nExercice 9 résultats:")
# print("Texte1 après opération sur texte2:", texte1)  # "hello"

# # Tuple (immuable)
# tuple1 = (1, 2, 3)
# tuple2 = tuple1
# # tuple2[0] = 4  # Cette ligne générera une erreur

# print("Tuple1 inchangé:", tuple1)  # (1, 2, 3)
# Solutions Exercice 10 : Copie de types mutables
# import copy

# # Liste originale
# originale = [1, 2, [3, 4]]

# # Référence
# reference = originale

# # Copie superficielle
# copie_superficielle = originale.copy()

# # Modification
# copie_superficielle[0] = 100
# copie_superficielle[2][0] = 300

# print("\nExercice 10 résultats:")
# print("Originale après modifications:", originale)  # [1, 2, [300, 4]]
# print("Référence après modifications:", reference)  # [1, 2, [300, 4]]
# print("Copie superficielle après modifications:", copie_superficielle)  # [100, 2, [300, 4]]
# Solutions Exercice 11 : Opérateurs de comparaison
# # Comparaisons numériques
# a = 10
# b = 5
# c = 10

# resultat1 = a > b    # True
# resultat2 = a == c   # True
# resultat3 = a != b   # True
# resultat4 = a <= c   # True
# resultat5 = b >= a   # False

# # Comparaisons de strings
# texte1 = "abc"
# texte2 = "abd"
# texte3 = "abc"

# resultat6 = texte1 == texte3  # True
# resultat7 = texte1 < texte2   # True ('abc' < 'abd')
# resultat8 = texte1 != texte2  # True

# print("\nExercice 11 résultats:")
# print(f"10 > 5: {resultat1}")
# print(f"10 == 10: {resultat2}")
# print(f"10 != 5: {resultat3}")
# print(f"10 <= 10: {resultat4}")
# print(f"5 >= 10: {resultat5}")
# print(f"'abc' == 'abc': {resultat6}")
# print(f"'abc' < 'abd': {resultat7}")
# print(f"'abc' != 'abd': {resultat8}")
# Solutions Exercice 12 : Opérateurs d'identité
# # Cas 1 : Même valeur, même objet
# a = 100
# b = 100
# resultat1 = a == b  # True
# resultat2 = a is b  # True (interning des petits entiers)

# # Cas 2 : Même valeur, objets différents
# c = [1, 2, 3]
# d = [1, 2, 3]
# resultat3 = c == d  # True
# resultat4 = c is d  # False

# # Cas 3 : Petits entiers (interning)
# e = 5
# f = 5
# resultat5 = e is f  # True

# # Cas 4 : Gros entiers
# g = 1000
# h = 1000
# resultat6 = g is h  # False (dépend de l'implémentation)

# print("\nExercice 12 résultats:")
# print(f"100 == 100: {resultat1}")
# print(f"100 is 100: {resultat2}")
# print(f"[1,2,3] == [1,2,3]: {resultat3}")
# print(f"[1,2,3] is [1,2,3]: {resultat4}")
# print(f"5 is 5: {resultat5}")
# print(f"1000 is 1000: {resultat6}")
# Solutions Exercice 13 : Expressions booléennes complexes
# x = 10
# y = 5
# z = 10

# # Expression 1
# resultat1 = x > y and x == z  # True and True = True

# # Expression 2
# resultat2 = x < y or x == z   # False or True = True

# # Expression 3
# resultat3 = not (x == y)      # not False = True

# # Expression 4
# resultat4 = x > y and x != z or y < z  # True and False or True = False or True = True

# # Expression 5
# resultat5 = (x > y and x != z) or y < z  # (True and False) or True = False or True = True

# print("\nExercice 13 résultats:")
# print(f"x > y and x == z: {resultat1}")
# print(f"x < y or x == z: {resultat2}")
# print(f"not (x == y): {resultat3}")
# print(f"x > y and x != z or y < z: {resultat4}")
# print(f"(x > y and x != z) or y < z: {resultat5}")
# Solutions Exercice 14 : Programme de validation
# # Données d'un utilisateur
# age = 25
# salaire = 45000
# experience = 3
# diplome = True

# # Conditions pour un prêt
# condition1 = age >= 18 and salaire >= 40000  # True and True = True
# condition2 = experience >= 2 or diplome     # True or True = True
# condition3 = salaire >= 50000 or (diplome and experience >= 1)  # False or (True and True) = False or True = True

# # Validation finale
# pret_approuve = condition1 and condition2 and condition3  # True and True and True = True

# print("\nExercice 14 résultats:")
# print(f"Condition 1 (âge >= 18 et salaire >= 40000): {condition1}")
# print(f"Condition 2 (expérience >= 2 ou diplôme): {condition2}")
# print(f"Condition 3 (salaire >= 50000 ou (diplôme et expérience >= 1)): {condition3}")
# print(f"Prêt approuvé: {pret_approuve}")
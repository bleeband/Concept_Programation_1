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

# Exercices Python Avancés pour Débutants
# Exercices sur les Opérateurs, Précédence et Associativité


""" # ----------------------------------------------------------------------------------
# Exercice 1 : Décomposition d'expressions complexes
# Écris les étapes intermédiaires de calcul pour ces expressions :

# Expression 1
resultat1 = 3 + 4 * 2 ** 3 // 2 - 1
    # Étape 1: 3 // 2 = 1
    # Étape 2: 2 ** 1 = 2
    # Étape 3: 4 * 2 = 8
    # Étape 4: 3 + 8 = 11
    # Étape 5: 11 - 1 = 10
      

# Expression 2
a, b, c = 5, 3, 2
resultat2 = a % b + c * (a // b) ** c
    # Étape 1: 5 // 3 = 1
    # Étape 2: 1 ** 2 = 1
    # Étape 3: 2 * 1 = 2
    # Étape 4: 5 % 3 = 2
    # Étape 5: 2 + 2 = 4
    
# Expression 3
x, y, z = 8, 3, 2
resultat3 = (x > y and y < z) or (x == y * z)
    # Étape 1: 8 > 3 = True
    # Étape 2: 3 < 2 = False
    # Étape 3: 3 * 2 = 6
    # Étape 4: 8 == 6 = False
    # Étape 5: True and False = False """


""" # ----------------------------------------------------------------------------------
# Exercice 2 : Réécriture avec parenthèses
# Réécris ces expressions en ajoutant toutes les parenthèses implicites :

# Expression originale
    # expr1 = a + b * c - d / e % f
    # expr1 = a + (b * c) - ((d / e) % f)

# Expression originale
    # expr2 = not x or y and z
    # expr2 = not (x or y and z)

# Expression originale
    # expr3 = p ** q ** r * s
    # expr3 = ((p ** q) ** r) * s """


""" # ----------------------------------------------------------------------------------
# Exercice 3 : Correction d'expressions
# Trouve et corrige les erreurs dans ces expressions :

# Code avec erreurs
# resultat1 = 15 / 2 * 3  # L'étudiant veut (15/2)*3
# resultat2 = 2 ** 3 ** 2  # L'étudiant veut (2**3)**2
# resultat3 = 10 - 5 + 3   # L'étudiant veut 10 - (5 + 3)
resultat1 = (15 / 2) * 3  # L'étudiant veut (15/2)*3
resultat2 = (2 ** 3) ** 2  # L'étudiant veut (2**3)**2
resultat3 = 10 - (5 + 3)   # L'étudiant veut 10 - (5 + 3)

print()
print(resultat1, resultat2, resultat3) """


""" # ----------------------------------------------------------------------------------
# Exercices sur la Conversion Simple et Cast

# Exercice 4 : Conversions imbriquées
# Trouve le résultat final de ces conversions :

# Conversions chainées
valeur1 = int(float("12.75"))       # 12
valeur2 = str(int(8.999))           # "8"
valeur3 = bool(int("0"))            # False
valeur4 = float(str(3 + 4.5))       # 7.5

# Conversions complexes
texte = "15.5 euros"                # 
prix = float(texte.split()[0])      #
quantite = 3                        #
total = prix * quantite             #

resultat = str(int(total)) + " " + texte.split()[1]

print()
print(valeur1, valeur2, valeur3, valeur4)
print(resultat) """



# ----------------------------------------------------------------------------------
# Exercice 5 : Programme de conversion universelle
# Crée un programme qui détecte automatiquement le type d'entrée et le convertit :

def detecter_et_convertir(valeur):
    # À compléter : doit détecter si c'est un int, float, bool ou string
    # et retourner la valeur convertie dans tous les types possibles

    for x in range(len(test_values)):

        print("Valeur originale :", test_values[x])
        y = test_values[x]
        print(type(test_values[x]))
    pass


# Tests
test_values = ["123", "45.67", "True", "hello", "0"]


print()
detecter_et_convertir(test_values)



""" # ----------------------------------------------------------------------------------
# Exercice 6 : Gestion des arrondis et troncatures
# Écris un programme qui montre les différences entre différentes méthodes de conversion :

# Valeurs à convertir
valeurs = [12.3, 12.7, -12.3, -12.7, "12.3", "12.7"]

for valeur in valeurs:
    # Conversions avec int(), round(), et math.floor()
    pass """


""" # ----------------------------------------------------------------------------------
# Exercices sur les Types Mutables et Immuables

# Exercice 7 : Effets de bord complexes
# Prédit le résultat de ce code :

def modifier_data(data1, data2):
    data1[0] = 100
    data2 = "modifié"
    return data2

# Données initiales
liste_originale = [1, 2, 3]
texte_original = "original"

# Appel de fonction
resultat = modifier_data(liste_originale, texte_original)

print("Liste après appel:", liste_originale)
print("Texte après appel:", texte_original)
print("Résultat fonction:", resultat) """


""" # ----------------------------------------------------------------------------------
# Exercice 8 : Copies profondes vs superficielles
# Analyse ce code et explique les résultats :

import copy

# Structure complexe
donnees_complexes = [
    [1, 2, 3],
    {"a": 10, "b": [4, 5]},
    (6, 7, [8, 9])
]

# Différentes copies
ref = donnees_complexes
copie_simple = donnees_complexes.copy()
copie_profonde = copy.deepcopy(donnees_complexes)

# Modifications
ref[0][0] = 100
ref[1]["b"][0] = 400
# ref[2][2][0] = 800  # Pourquoi cette ligne génère une erreur ?

print("Original:", donnees_complexes[0][0], donnees_complexes[1]["b"][0])
print("Copie simple:", copie_simple[0][0], copie_simple[1]["b"][0])
print("Copie profonde:", copie_profonde[0][0], copie_profonde[1]["b"][0]) """


""" # ----------------------------------------------------------------------------------
# Exercice 9 : Performance des types
# Compare l'efficacité mémoire des différents types :

import sys

# Création de différentes structures
entier = 1000000
chaine = "A" * 1000
liste = ["A"] * 1000
tuple_data = ("A",) * 1000

# Compare la taille mémoire
print(f"Int: {sys.getsizeof(entier)} octets")
print(f"String: {sys.getsizeof(chaine)} octets")
print(f"Liste: {sys.getsizeof(liste)} octets")
print(f"Tuple: {sys.getsizeof(tuple_data)} octets") """


""" # ----------------------------------------------------------------------------------
# Exercices sur les Opérateurs de Comparaison et d'Identité

# Exercice 10 : Tables de vérité complexes
# Complète la table de vérité pour ces expressions :

# Pour a = True, b = False, c = True
expression1 = not a or b and c
expression2 = (not a) or (b and c)
expression3 = not (a or b) and c
expression4 = a != b == c """


""" # ----------------------------------------------------------------------------------
Exercice 11 : Comparaisons chainées
Évalue ces comparaisons chainées :

# Comparaisons multiples
a, b, c, d = 5, 10, 5, 20

resultat1 = a < b < c < d
resultat2 = a == c != b < d
resultat3 = a <= c == 5 != b """


""" # ----------------------------------------------------------------------------------
# Exercice 12 : Programme de validation d'identité
# Crée un système qui vérifie l'identité des objets :

def verifier_identite(obj1, obj2, nom1, nom2):
    # Doit retourner un rapport complet
    egalite = obj1 == obj2
    identite = obj1 is obj2
    type_identique = type(obj1) == type(obj2)

    return {
        "égalité": egalite,
        "identité": identite,
        "même_type": type_identique
    }

# Tests avec différents cas
cas_test = [
    (100, 100, "a", "b"),
    (1000, 1000, "c", "d"),
    ([1,2], [1,2], "liste1", "liste2"),
    ("hello", "hello", "str1", "str2")
] """


""" # ----------------------------------------------------------------------------------
# Exercice 13 : Expressions de priorité mixte
# Évalue ces expressions mélangeant différents types d'opérateurs :

# Données de test
x, y, z = 10, 5, 10
a, b = True, False

# Expressions complexes
expr1 = x > y and y < z or a and not b
expr2 = (x == z) != (y == z) and a or b
expr3 = not (x > y) or (y < z and a) == b """
#### **Exercices de Programmation Fonctionnelle **

#**Objectif :** Comprendre et pratiquer les concepts de la programmation fonctionnelle : pureté des fonctions, `map()`, `filter()`, `zip()`, `reduce()`, et expressions lambda.

## **Partie 1 : Fonctions Pures vs Non Pures**

### **Exercice 1.1 : Identifier la Pureté**
# Pour chaque fonction ci-dessous, déterminez si elle est **pure** ou **non pure** et expliquez pourquoi.

# Fonction A
def ajouter_pure(a, b):
    return a + b
# PURE

# Fonction B
total = 0
def ajouter_impure(a):
    global total
    total += a
    return total
# NON PURE

# Fonction C
def formater_message(nom):
    return f"Bonjour, {nom} !"
# PURE

# Fonction D
import random
def lancer_de():
    return random.randint(1, 6)
# PURE

# Fonction E
liste_resultats = []
def traiter_liste(lst):
    resultat = []
    for x in lst:
        resultat.append(x * 2)
    liste_resultats.extend(resultat)
    return resultat
# NON PURE

### **Exercice 1.2 : Transformer en Fonction Pure**
# Transformez cette fonction non pure en une fonction pure :

# Version non pure
compteur = 0

def incrementer_impur():
    global compteur
    compteur += 1
    return compteur

# Votre version pure ici :
def incrementer_pur(valeur_actuelle):
    return valeur_actuelle + 1

# Test
print(incrementer_pur(5))  # Devrait retourner 6
print(incrementer_pur(10)) # Devrait retourner 11


## **Partie 2 : Expressions Lambda**

### **Exercice 2.1 : Convertir en Lambda**
# Convertissez ces fonctions normales en expressions lambda :

# 1. Fonction qui double un nombre
def doubler(x):
    return x * 2

# Version lambda :
doubler_lambda = lambda x: x * 2

# 2. Fonction qui vérifie si un nombre est pair
def est_pair(x):
    return x % 2 == 0

# Version lambda :
est_pair_lambda = lambda x: x % 2 == 0

# 3. Fonction qui concatène deux chaînes avec un espace
def concatener(a, b):
    return a + " " + b

# Version lambda :
concatener_lambda = lambda a, b: a + " " + b

## **Exercice 2.2 : Utilisation avec Tri**
# Utilisez une expression lambda pour trier cette liste de tuples par le deuxième élément :

etudiants = [("Alice", 85), ("Bob", 72), ("Charlie", 93), ("Diana", 68)]

# Trier par note (du plus bas au plus haut) avec lambda
etudiants_tries = sorted(etudiants, key=lambda e: e[1])

print(etudiants_tries)


# **Partie 3 : La fonction `map()`**
## **Exercice 3.1 : Application Simple**

# Utilisez `map()` pour appliquer différentes transformations à une liste de nombres :

nombres = [1, 2, 3, 4, 5]

# 1. Calculer les carrés
carres = map(lambda x: x ** 2, nombres)
print(list(carres))

# 2. Convertir en chaîne avec préfixe "Nombre: "
chaines = map(lambda x: f"Nombre: {x}", nombres)
print(list(chaines))


## **Exercice 3.2 : Map avec Fonction Personnalisée**
# Créez une fonction pure `celsius_vers_fahrenheit()` et utilisez-la avec `map()` :

temperatures_c = [0, 20, 37, 100]

def celsius_vers_fahrenheit(c):
    return (c * 9 / 5) + 32

# Utiliser map() avec votre fonction
temperatures_f = list(map(celsius_vers_fahrenheit, temperatures_c))
print(list(temperatures_f))


# **Partie 4 : La fonction `filter()`**
## **Exercice 4.1 : Filtrage Basique**

# Utilisez `filter()` pour sélectionner des éléments selon des critères :

nombres = range(1, 21)

# 1. Nombres pairs
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(list(pairs))

# 2. Nombres divisibles par 3
div_par_3 = list(filter(lambda x: x % 3 == 0, nombres))
print(list(div_par_3))

# 3. Nombres > 10
grands = list(filter(lambda x: x > 10, nombres))
print(list(grands))


## **Exercice 4.2 : Filtrage Complexe**

# Filtrez cette liste de mots selon deux critères :

mots = ["", "java", "functional", "programming", "lambda", "map", "filter", "reduce"]

# 1. Mots de plus de 5 caractères
longs_mots = list(filter(lambda x: len(x) > 5,mots))
print(list(longs_mots))

# 2. Mots qui contiennent la lettre 'a'
avec_a = list(filter(lambda x: "a" in x ,mots))
print(list(avec_a))


# **Partie 5 : La fonction `zip()`**
## **Exercice 5.1 : Combinaison de Listes**
# Utilisez `zip()` pour combiner plusieurs listes :

noms = ["Alice", "Bob", "Charlie"]
notes = [85, 72, 93]
matieres = ["Math", "", "Physique"]

# 1. Créer des tuples (nom, note)
combinaison1 = tuple(zip(noms, notes))
print(list(combinaison1))

# 2. Créer des tuples (nom, note, matière)
combinaison2 = tuple(zip(noms, notes, matieres))
print(list(combinaison2))

# 3. Créer un dictionnaire nom -> note
dictionnaire = dict(zip(noms, notes))
print(dictionnaire)


## **Exercice 5.2 : Dézipper et Transposer**
# Utilisez `zip()` avec l'opérateur `*` pour "dézipper" :

# Liste de coordonnées (x, y)
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Dézipper en deux listes : xs et ys
xs, ys = list(zip(*points))

print("Xs:", xs)
print("Ys:", ys)

# Vérification : re-zip doit redonner les points originaux
points_reconstruits = list(zip(xs, ys))
print(points_reconstruits)


## **Partie 6 : La fonction `reduce()`**
# _Note : `reduce()` se trouve dans le module `functools`_

### **Exercice 6.1 : Opérations de Réduction**
# Utilisez `reduce()` pour effectuer différentes opérations de réduction :

from functools import reduce

nombres = [1, 2, 3, 4, 5]

# 1. Somme des nombres
somme = reduce(lambda x, y: x + y, nombres)
print("Somme:", somme)  # 15

# 2. Produit des nombres (factorielle de 5)
produit = reduce(lambda x, y: x * y, nombres)
print("Produit:", produit)  # 120

# 3. Plus grand nombre
maximum = reduce(lambda x, y: x if x > y else y, nombres)
print("Maximum:", maximum)  # 5

# 4. Concaténation de chaînes
mots = ["Programmation", " ", "Fonctionnelle", " ", ""]
phrase = reduce(lambda x, y: x + y, mots)
print("Phrase:", phrase)  # "Programmation Fonctionnelle "


### **Exercice 6.2 : Réduction Complexe**
# Créez une fonction de réduction personnalisée :

from functools import reduce

# Liste de transactions (nom, montant)
transactions = [
    ("dépôt", 100),
    ("retrait", 30),
    ("dépôt", 50),
    ("retrait", 20),
    ("frais", 5)
]

def calculer_solde(solde_actuel, transaction):
    operation, montant = transaction

    if operation == "dépôt":
        return solde_actuel + montant
    elif operation in ("retrait", "frais"):
        return solde_actuel - montant
    else:
        return solde_actuel

# Utiliser reduce() avec un solde initial de 0
solde_final = reduce(calculer_solde, transactions, 0)
print("Solde final:", solde_final)  # 95


## **Partie 7 : Combinaison des Concepts**

### **Exercice 7.1 : Pipeline Fonctionnel**
# Créez un pipeline qui traite une liste de données en utilisant plusieurs fonctions fonctionnelles :

from functools import reduce

donnees = [12, 7, 14, 9, 21, 18, 5, 16]

# Pipeline:
# 1. Filtrer pour garder seulement les nombres > 10
# 2. Multiplier chaque nombre par 2
# 3. Calculer la moyenne des résultats

etape1 = filter(lambda x: x > 10, donnees)  # Nombres > 10
etape2 = map(lambda x: x * 2, etape1)     # Multiplier par 2
resultats = list(etape2)

# Calcul de la moyenne avec reduce
if resultats:
    somme_totale = reduce(lambda x, y: x + y, resultats)
    moyenne = somme_totale / len(resultats)

    print("Résultats:", resultats)
    print("Moyenne:", moyenne)


### **Exercice 7.2 : Traitement de Données Réelles**

# Traitez ces données d'étudiants avec une approche fonctionnelle :

etudiants = [
    {"nom": "Alice", "notes": [85, 90, 78]},
    {"nom": "Bob", "notes": [72, 68, 74]},
    {"nom": "Charlie", "notes": [93, 95, 91]},
    {"nom": "Diana", "notes": [68, 72, 65]}
]

# Objectif: Calculer la moyenne de chaque étudiant, puis la moyenne de la classe

# 1. Calculer la moyenne de chaque étudiant (map)
moyennes_individuelles = list(map(lambda etudiant: sum(etudiant["notes"]) / len(etudiant["notes"]),etudiants))
print("Moyennes individuelles:", moyennes_individuelles)

# 2. Calculer la moyenne de la classe (reduce)
if moyennes_individuelles:
    somme = reduce(lambda x, y: x + y, moyennes_individuelles)
    moyenne_classe = somme / len(moyennes_individuelles)
    print("Moyenne de classe:", moyenne_classe)


## **Partie 8 : Défi Final**
### **Exercice 8.1 : Analyse de Textes**

# Écrivez un programme fonctionnel qui analyse une liste de phrases :

phrases = [
    "La programmation fonctionnelle est intéressante.",
    " supporte plusieurs paradigmes.",
    "Les fonctions pures n'ont pas d'effets de bord.",
    "map, filter et reduce sont des fonctions d'ordre supérieur."
]

# Objectif: Trouver le mot le plus fréquent (hors mots communs)

mots_communs = {"la", "le", "les", "est", "sont", "de", "des", "et", "d'"}

# 1. Diviser chaque phrase en mots
mots_par_phrase = map(
    lambda p: p.lower().split(),
    phrases
)
# 2 & 3. Aplatir + filtrer les mots communs
tous_les_mots = reduce(
    lambda acc, mots: acc + list(
        filter(
            lambda m: m not in mots_communs,
            map(lambda m: m.strip(".,'"), mots)
        )
    ),
    mots_par_phrase,
    []
)
# 4. Compter les occurrences
frequences = reduce(
    lambda acc, mot: {**acc, mot: acc.get(mot, 0) + 1},
    tous_les_mots,
    {}
)
# 5. Trouver le mot le plus fréquent
mot_plus_frequent = reduce(
    lambda a, b: a if frequences[a] >= frequences[b] else b,
    frequences
)

print("Mot le plus fréquent:", mot_plus_frequent)
print("Occurrences:", frequences[mot_plus_frequent])

# ---------------------------------------------------------------------------------------------

## **Solutions Guide (Indications)**

### **Pour l'Exercice 1.1 :**

# - **Fonction A** : Pure (mêmes entrées → mêmes sorties, pas d'effets de bord)
# - **Fonction B** : Non pure (modifie une variable globale)
# - **Fonction C** : Pure (déterministe, pas d'effets de bord)
# - **Fonction D** : Non pure (utilise random, résultat imprévisible)
# - **Fonction E** : Non pure (modifie `liste_resultats`)

# ### **Pour l'Exercice 3.1 :**

# # 1. Calculer les carrés
# carres = map(lambda x: x ** 2, nombres)

# # 2. Convertir en chaîne
# chaines = map(lambda x: f"Nombre: {x}", nombres)

# ### **Pour l'Exercice 5.1 :**

# # 1. Créer des tuples (nom, note)
# combinaison1 = zip(noms, notes)

# # 3. Créer un dictionnaire
# dictionnaire = dict(zip(noms, notes))

# ### **Pour l'Exercice 6.1 :**

# # 1. Somme des nombres
# somme = reduce(lambda x, y: x + y, nombres)

# # 3. Plus grand nombre
# maximum = reduce(lambda x, y: x if x > y else y, nombres)
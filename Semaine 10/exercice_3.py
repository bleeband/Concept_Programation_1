# ### **Partie 1 : Compréhensions de listes**

# **Exercice 1 : Transformations basiques**

# 1. Créez une liste `nombres` contenant les entiers de 1 à 10. Ensuite, utilisez une compréhension de liste pour créer une nouvelle liste où chaque nombre est multiplié par 3.
nombre = [x for x in range(11)]
triples = [x * 3 for x in nombre]
print(nombre)
print(triples)
# 2. À partir d'une liste `mots = ["python", "est", "puissant"]`, créez une nouvelle liste contenant la longueur de chaque mot.
mots = ["python", "est", "puissant"]
longueur_mots = [len(mot) for mot in mots]
print(mots)
print(longueur_mots)

# **Exercice 2 : Filtrage simple**

# 1. À partir de la liste `nombres` de 1 à 15, créez une liste ne contenant que les nombres divisibles par 3.
nombres = [x for x in range(1, 16)]
divisible_par_3 = [x for x in nombres if x % 3 == 0]
print(nombres)
print(divisible_par_3)

# 2. À partir d'une liste `temperatures = [23, 17, 30, 15, 28, 10, 5]`, créez une liste contenant seulement les températures supérieures à 20.
temperatures = [23, 17, 30, 15, 28, 10, 5]
temp_sup_20 = [temp for temp in temperatures if temp > 20]
print(temperatures)
print(temp_sup_20)

# **Exercice 3 : Conditions complexes**

# 1. À partir de la liste `nombres` de 1 à 10, créez une liste de chaînes de caractères qui indique "Pair" pour les nombres pairs et "Impair" pour les impairs.
liste_nombres = [x for x in range(1, 11)]
pair_ou_impair = ["Pair" if x % 2 == 0 else "Impair" for x in liste_nombres]
print(liste_nombres)
print(pair_ou_impair)

# 2. À partir de `notes = [12, 8, 17, 5, 14, 20, 9]`, créez une liste de booléens où `True` indique une note supérieure ou égale à la moyenne (10) et `False` l'inverse.
notes = [12, 8, 17, 5, 14, 20, 9]
au_dessus_moyenne = [note >= 10 for note in notes]
print(notes)
print(au_dessus_moyenne)

# **Exercice 4 : Boucles imbriquées**

# 1. Créez une liste de tuples `(x, y)` pour tous les `x` dans `[1, 2, 3]` et tous les `y` dans `['a', 'b']`.
tuples_xy = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(tuples_xy)

# 2. Aplatissez une liste de listes `matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]` en une liste simple.
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
liste_aplatie = [element for sous_liste in matrice for element in sous_liste]
print(matrice)
print(liste_aplatie)

# **Exercice 5 : Mise en pratique**

# 1. Étant donné une phrase `phrase = "Le Python est un langage de programmation"`, créez une liste des mots de la phrase qui contiennent la lettre 'o', en minuscules.
phrase = "Le Python est un langage de programmation"
mots_avec_o = [mot.lower() for mot in phrase.split() if 'o' in mot.lower()]
print(phrase)
print(mots_avec_o)

# 2. À partir de deux listes `liste1 = [1, 2, 3]` et `liste2 = [4, 5, 6]`, créez une liste des sommes des paires `(1+4, 2+5, 3+6)` en utilisant `zip` dans une compréhension.
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
somme_paires = [a + b for a, b in zip(liste1, liste2)]
print(liste1)
print(liste2)
print(somme_paires)


# ### **Partie 2 : Compréhensions de dictionnaires**

# **Exercice 1 : Création basique**

# 1. Créez un dictionnaire où les clés sont les nombres de 1 à 5 et les valeurs sont leurs carrés.
dict_carres = {x: x**2 for x in range(1, 6)}
print(dict_carres)

# 2. À partir de `noms = ["Alice", "Bob", "Charlie"]`, créez un dictionnaire ayant ces noms comme clés et la longueur de chaque nom comme valeur.
noms = ["Alice", "Bob", "Charlie"]
dict_longueurs = {nom: len(nom) for nom in noms}
print(noms)
print(dict_longueurs)

# **Exercice 2 : Transformations et filtrage**

# 1. À partir du dictionnaire `inventaire = {"pommes": 5, "bananes": 8, "oranges": 3}`, créez un nouveau dictionnaire contenant seulement les fruits dont la quantité est supérieure à 4.
dict_inventaire = {"pommes": 5, "bananes": 8, "oranges": 3}
fruits_plus_de_4 = {fruit: quantite for fruit, quantite in dict_inventaire.items() if quantite > 4}
print(dict_inventaire)
print(fruits_plus_de_4)

# 2. À partir d'une liste de tuples `coordonnees = [("x", 10), ("y", 20), ("z", 30)]`, créez un dictionnaire.
tuples_coordonnees = [("x", 10), ("y", 20), ("z", 30)]
dict_coordonnees = {cle: valeur for cle, valeur in tuples_coordonnees}
print(tuples_coordonnees)
print(dict_coordonnees)

# **Exercice 3 : Inversion et manipulation**

# 1. Inverser le dictionnaire `d = {"a": 1, "b": 2, "c": 3}` pour obtenir `{1: "a", 2: "b", 3: "c"}`.
d = {"a": 1, "b": 2, "c": 3}
dict_inverse = {valeur: cle for cle, valeur in d.items()}
print(d)
print(dict_inverse)

# 2. À partir de deux listes `cles = ["id", "nom", "age"]` et `valeurs = [101, "Alice", 25]`, créez un dictionnaire en les associant.
cles = ["id", "nom", "age"]
valeurs = [101, "Alice", 25]
dict_associe = {cle: valeur for cle, valeur in zip(cles, valeurs)}
print(cles)
print(valeurs)
print(dict_associe)

# **Exercice 4 : Conditions avec `if-else`**

# 1. À partir de `notes = {"Alice": 15, "Bob": 8, "Charlie": 12, "David": 17}`, créez un nouveau dictionnaire avec les mêmes clés, mais où la valeur est "Admis" si la note >= 10, sinon "Recalé".
notes = {"Alice": 15, "Bob": 8, "Charlie": 12, "David": 17}
resultats = {eleve: ("Admis" if note >= 10 else "Recalé") for eleve, note in notes.items()}
print(notes)
print(resultats)

# ### **Partie 3 : Compréhensions d'ensembles (sets)**

# **Exercice 1 : Création et dédoublonnage**

# 1. À partir d'une liste `donnees = [1, 2, 2, 3, 4, 4, 4, 5]`, créez un ensemble contenant les carrés de ces nombres. Observez l'effet de dédoublonnage.
donnees = [1, 2, 2, 3, 4, 4, 4, 5]
carres_ensembles = {x**2 for x in donnees}
print(donnees)
print(carres_ensembles)

# 2. À partir d'une chaîne `phrase = "hello world"`, créez un ensemble des lettres consonnes qu'elle contient (ignorez les espaces).
phrase = "hello world"
consonnes = {char for char in phrase if char.isalpha() and char.lower() not in 'aeiou'}
print(phrase)
print(consonnes)

# **Exercice 2 : Filtrage**

# 1. À partir d'une liste `nombres = [12, 7, 15, 3, 20, 8, 10]`, créez un ensemble contenant seulement les nombres divisibles par 2 **et** par 3.
nombres = [12, 7, 15, 3, 20, 8, 10]
divisibles_par_2_et_3 = {x for x in nombres if x % 2 == 0 and x % 3 == 0}
print(nombres)
print(divisibles_par_2_et_3)

# 2. À partir d'une liste de mots `mots = ["python", "java", "python", "c++", "java"]`, créez un ensemble des mots qui ont plus de 4 lettres.
mots = ["python", "java", "python", "c++", "java"]
mots_plus_de_4_lettres = {mot for mot in mots if len(mot) > 4}
print(mots)
print(mots_plus_de_4_lettres)

# **Exercice 3 : Opérations avancées**

# 1. Générez un ensemble des paires `(x, y)` où `x` et `y` sont tous deux dans l'ensemble `{1, 2, 3}` et `x` != `y`.
ensembles = {(x, y) for x in {1, 2, 3} for y in {1, 2, 3} if x != y}
print(ensembles)

# 2. À partir d'une liste de phrases `["le chat dort", "le chien court", "le chat mange"]`, créez un ensemble de tous les mots uniques présents.
phrases = ["le chat dort", "le chien court", "le chat mange"]
mots_uniques = {mot for phrase in phrases for mot in phrase.split()}
print(phrases)
print(mots_uniques)


# ### **Partie 4 : Exercices de synthèse**

# **Exercice 1 : Analyse de texte**
# À partir de la chaîne suivante :
# `texte = "Les compréhensions de liste en Python offrent une syntaxe concise pour créer des listes."`
texte = "Les compréhensions de liste en Python offrent une syntaxe concise pour créer des listes."
print(texte)

# 1. Créez une liste des mots (sans ponctuation, en minuscules).
liste_mots = [mot.strip('.,') .lower() for mot in texte.split()]
print(liste_mots)

# 2. À partir de cette liste, créez un dictionnaire où chaque mot est une clé et sa valeur est le nombre de voyelles qu'il contient.
dict_voyelles = {mot: sum(1 for char in mot if char in 'aeiou') for mot in liste_mots}
print(dict_voyelles)

# 3. Créez un ensemble des mots qui ont plus de 3 consonnes.
ensembles = {mot for mot in liste_mots if sum(1 for char in mot if char.isalpha() and char not in 'aeiou') > 3} 
print(ensembles)

# **Exercice 2 : Traitement de données**
# Vous avez une liste de dictionnaires représentant des étudiants :

etudiants = [
    {"nom": "Alice", "notes": [14, 12, 16]},
    {"nom": "Bob", "notes": [8, 10, 7]},
    {"nom": "Charlie", "notes": [18, 15, 17]}
]

# 1. Créez une liste des noms des étudiants.
liste_noms = [etud["nom"] for etud in etudiants]
print(liste_noms)

# 2. Créez un dictionnaire `{nom: moyenne}` contenant la moyenne de chaque étudiant.
dict_moyennes = {etud["nom"]: sum(etud["notes"])/len(etud["notes"]) for etud in etudiants}
print(dict_moyennes)

# 3. Créez un ensemble des notes uniques supérieures à 15 présentes dans toutes les listes.
ensembles = {note for etud in etudiants for note in etud["notes"] if note > 15}
print(ensembles)

# **Exercice 3 : Combinaison de structures**

# 1. En une seule ligne de code, générez une liste de dictionnaires. Chaque dictionnaire représente un carré et a les clés `"côté"` (un entier de 1 à 5) et `"aire"` (le carré de `"côté"`).
liste_carres = [{"côté": x, "aire": x**2} for x in range(1, 6)]
print(liste_carres)

# 2. À partir de la liste générée, créez un ensemble des aires qui sont des multiples de 4.
aires_multiples_de_4 = {carre["aire"] for carre in liste_carres if carre["aire"] % 4 == 0}
print(aires_multiples_de_4)

# ----------------------------------------------------------------------

# ### **Corrections suggérées (à ne consulter qu'après avoir essayé)**

# **Partie 1 - Exercice 1.1**

# nombres = list(range(1, 11))
# triples = [n * 3 for n in nombres]

# **Partie 2 - Exercice 1.1**

# carres_dict = {x: x**2 for x in range(1, 6)}

# **Partie 3 - Exercice 1.1**

# donnees = [1, 2, 2, 3, 4, 4, 4, 5]
# carres_uniq = {x**2 for x in donnees}

# **Partie 4 - Exercice 2.2**

# moyennes = {etud["nom"]: sum(etud["notes"])/len(etud["notes"]) for etud in etudiants}

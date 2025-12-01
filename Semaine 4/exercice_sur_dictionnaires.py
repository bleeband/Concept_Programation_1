import copy
# # Exercices sur les Dictionnaires en Python

# ## Exercice 1 : Déclaration et Création

# ### 1.1 : Déclaration basique (À compléter)


# Créez un dictionnaire représentant une personne avec:
# - nom: "Dupont"
# - age: 25
# - ville: "Paris"

""" personne = {
    "nom": "Dupont",
    "age": 25,
    "ville": "Paris"
}

print(personne) """


# ----------------------------------------------------------------------------------

### 1.2 : Depuis une liste de tuples (À compléter)


""" # Créez un dictionnaire à partir de cette liste de tuples
donnees = [("nom", "Alice"), ("age", 30), ("metier", "ingenieure")]
personne = dict(donnees)

print(personne) """


# ----------------------------------------------------------------------------------

# ### 1.3 : Avec dict() (Erreurs à corriger)

# Ce code devrait créer un dictionnaire mais contient des erreurs

""" etudiant = dict(
    nom = "Martin",
    prenom = "Pierre",
    notes = [15, 18, 12]
)

print(etudiant) """


# ----------------------------------------------------------------------------------

# ## Exercice 2 : Accès aux Éléments
# ### 2.1 : Accès simple (À compléter)

""" livre = {
    "titre": "1984",
    "auteur": "George Orwell",
    "annee": 1949,
    "pages": 328
}

# Accédez au titre et à l'année
titre = livre["titre"]
annee = livre["annee"]

print(f"'{titre}' publié en {annee}") """

# ----------------------------------------------------------------------------------
### 2.2 : Accès sécurisé (Erreurs à corriger)

""" # Ce code génère une erreur, corrigez-le
config = {"host": "localhost", "port": 8080}

print(f"Host: {config['host']}")
print(f"Database: {config.get('database', "non specifie")}")
print(f"Port: {config.get('port')}") """


# ----------------------------------------------------------------------------------
### 2.3 : Valeurs par défaut (À compléter)

""" utilisateur = {"nom": "Alice", "age": 25}

# Utilisez get() avec valeur par défaut
ville = utilisateur.get("ville", "Montreal")
profession = utilisateur.get("profession", "chauffeur")

print(f"Ville: {ville}")
print(f"Profession: {profession}") """


# ----------------------------------------------------------------------------------
## Exercice 3 : Modifications

### 3.1 : Ajout et modification (À compléter)

""" inventaire = {"pommes": 10, "bananes": 5}

# Ajoutez "oranges" avec 8 unités
inventaire.update({"oranges": 8})
# Modifiez les bananes à 7 unités
inventaire.update({"bananes": 7 })
# Ajoutez 3 aux pommes existantes
inventaire["pommes"] += 3

# inventaire["oranges"] = 8
# inventaire["bananes"] = 7
# inventaire["pommes"] += 3

print(inventaire) """

### 3.2 : update() (Erreurs à corriger)

""" # Ce code ne fait pas ce qui est attendu, corrigez-le
base = {"a": 1, "b": 2}
nouveau = {"b": 3, "c": 4}

base.update(nouveau)

print(base)  # Devrait être {"a": 1, "b": 3, "c": 4} """

### 3.3 : setdefault() (À compléter)

""" # Utilisez setdefault() pour initialiser des valeurs si absentes
stats = {"visites": 100}

# Si 'telechargements' n'existe pas, initialisez à 0
stats.setdefault("telechargements", 0)

# Si 'visites' existe, ne changez pas
stats.setdefault("visites", 200)


print(stats) """


## Exercice 4 : Suppression

### 4.1 : Suppression basique (À compléter)

""" donnees = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# Supprimez la clé 'c' avec del
del donnees["c"]
# Supprimez 'd' avec pop() et récupérez la valeur
valeur_d = donnees.pop("d")
# Supprimez et retournez un élément arbitraire
element = donnees.popitem()

print(f"Donnees: {donnees}")
print(f"Valeur de d: {valeur_d}")
print(f"Element supprimé: {element}") """


### 4.2 : Nettoyage conditionnel (Erreurs à corriger)


""" # Ce code devrait supprimer toutes les valeurs None mais contient des erreurs
produits = {
    "livre": 15,
    "stylo": None,
    "cahier": 8,
    "gomme": None,
    "regle": 12
}

cle_remove = [cle for cle, valeur in produits.items() if valeur is None]
for cle in cle_remove:
        del produits[cle]

print(produits) """


### 4.3 : pop() avec défaut (À compléter)

""" config = {"theme": "sombre", "langue": "fr"}

# Supprimez 'theme' avec valeur par défaut "clair"
ancien_theme = config.pop("theme", "clair")
# Essayez de supprimer 'volume' avec défaut 50
volume = config.pop("volume", 50)

print(f"Ancien theme: {ancien_theme}")
print(f"Volume: {volume}") """


## Exercice 5 : Copies

### 5.1 : Copie superficielle (À compléter)

""" original = {"a": 1, "b": [2, 3], "c": {"d": 4}}

# Créez une copie superficielle
copie = original.copy()

# Modifiez la copie
copie["a"] = 10
copie["b"].append(4)  # une copie de l'objets de "b"

print(f"Original: {original}")
print(f"Copie: {copie}") """


### 5.2 : Deepcopy (Erreurs à corriger)

""" # Ce code ne crée pas une vraie copie indépendante, corrigez-le
import copy

niveau1 = {"donnees": [1, 2, 3], "config": {"resolu": False}}
niveau2 = copy.deepcopy(niveau1)

niveau2["donnees"].append(4)
niveau2["config"]["resolu"] = True

print(f"Niveau 1: {niveau1}")
print(f"Niveau 2: {niveau2}") """


### 5.3 : Comparaison de copies (À compléter)

""" d1 = {"a": 1, "b": 2}
d2 = d1.copy()  # Créez une copie de d1
d3 = d1

print(f"d1 == d2: {d1 == d2}")
print(f"d1 is d2: {d1 is d2}")
print(f"d1 is d3: {d1 is d3}") """


## Exercice 6 : Parcours

### 6.1 : Parcours des clés (À compléter)

""" employe = {"nom": "Alice", "age": 30, "poste": "Developpeur", "salaire": 50000}

# Parcourez et affichez toutes les clés
for cle in employe:
    print(f"- {cle}")
# Vérifiez si "experience" est une clé
if "experience" in employe:
    print("Experience trouvée")
else:
    print("Experience non trouvée") """


### 6.2 : Parcours des valeurs (Erreurs à corriger)

""" # Ce code devrait calculer la somme des valeurs mais contient des erreurs
notes = {"math": 15, "francais": 12, "histoire": 18, "sport": 16}

total = 0
for note in notes.values():
    total += note

print(f"Somme: {total}")
print(f"Moyenne: {total / len(notes)}") """


# ### 6.3 : Parcours des items (À compléter)

""" inventaire = {"pommes": 10, "bananes": 5, "oranges": 8, "kiwis": 3}

# Affichez chaque produit avec sa quantité
for cle, items in inventaire.items():
        print(f"{cle} : {items}")

# Trouvez le produit avec la plus grande quantité
max_produit = max(inventaire, key=inventaire.get)
max_quantite = inventaire[max_produit]

print(f"Produit le plus stocké: {max_produit} ({max_quantite} unités)") """


## Exercice 7 : Méthodes Utiles

### 7.1 : keys(), values(), items() (À compléter)

""" config = {"host": "localhost", "port": 8080, "debug": True}

# Obtenez la liste des clés
cles = list(config.keys())

# Obtenez la liste des valeurs
valeurs = list(config.values())

# Obtenez la liste des items (clé, valeur)
items = list(config.items())

print(f"Clés: {cles}")
print(f"Valeurs: {valeurs}")
print(f"Items: {items}")
 """

### 7.2 : fromkeys() (Erreurs à corriger)

""" # Ce code devrait créer un dictionnaire avec des valeurs par défaut
cles = ["nom", "age", "ville"]
valeur_par_defaut = "inconnu"

resultat = dict.fromkeys(cles, valeur_par_defaut)

print(resultat) """


# ### 7.3 : Comprehension de dictionnaire (À compléter)


""" nombres = [1, 2, 3, 4, 5]

# Créez un dict {nombre: carre} avec compréhension
carre = {}
for i in nombres:
    carre[i] = i **2

# carres = {n: n**2 for n in nombres}

# print(carres)
print(carre) """


#-------------------------------------------------------------
#-------------------------------------------------------------
#-------------------------------------------------------------
#-------------------------------------------------------------


# Solutions des Exercices
# Solution Exercice 1
# 1.1 : Déclaration basique

# personne = {"nom": "Dupont", "age": 25, "ville": "Paris"}
# print(personne)

# 1.2 : Depuis une liste de tuples
# donnees = [("nom", "Alice"), ("age", 30), ("metier", "ingenieure")]
# personne = dict(donnees)
# print(personne)

# 1.3 : Avec dict() - Corrigé
# etudiant = dict(
#     nom="Martin",
#     prenom="Pierre",
#     notes=[15, 18, 12]
# )
# print(etudiant)

# Solution Exercice 2
# 2.1 : Accès simple

# livre = {
#     "titre": "1984",
#     "auteur": "George Orwell",
#     "annee": 1949,
#     "pages": 328
# }

# titre = livre["titre"]
# annee = livre["annee"]

# print(f"'{titre}' publié en {annee}")

# 2.2 : Accès sécurisé - Corrigé
# config = {"host": "localhost", "port": 8080}

# print(f"Host: {config['host']}")
# print(f"Database: {config.get('database', 'Non spécifié')}")
# print(f"Port: {config.get('port')}")

# 2.3 : Valeurs par défaut
# utilisateur = {"nom": "Alice", "age": 25}

# ville = utilisateur.get("ville", "Non spécifiée")
# profession = utilisateur.get("profession", "Sans emploi")

# print(f"Ville: {ville}")
# print(f"Profession: {profession}")

# Solution Exercice 3
# 3.1 : Ajout et modification

# inventaire = {"pommes": 10, "bananes": 5}

# inventaire["oranges"] = 8
# inventaire["bananes"] = 7
# inventaire["pommes"] += 3

# print(inventaire)

# 3.2 : update() - Corrigé
# base = {"a": 1, "b": 2}
# nouveau = {"b": 3, "c": 4}

# base.update(nouveau)

# print(base)

# 3.3 : setdefault()
# stats = {"visites": 100}

# stats.setdefault("telechargements", 0)
# stats.setdefault("visites", 200)

# print(stats)

# Solution Exercice 4
# 4.1 : Suppression basique

# donnees = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# del donnees["c"]
# valeur_d = donnees.pop("d")
# element = donnees.popitem()

# print(f"Donnees: {donnees}")
# print(f"Valeur de d: {valeur_d}")
# print(f"Element supprimé: {element}")

# 4.2 : Nettoyage conditionnel - Corrigé
# produits = {
#     "livre": 15,
#     "stylo": None,
#     "cahier": 8,
#     "gomme": None,
#     "regle": 12
# }

# cles_a_supprimer = [cle for cle, valeur in produits.items() if valeur is None]
# for cle in cles_a_supprimer:
#     del produits[cle]

# print(produits)

# 4.3 : pop() avec défaut
# config = {"theme": "sombre", "langue": "fr"}

# ancien_theme = config.pop("theme", "clair")
# volume = config.pop("volume", 50)

# print(f"Ancien theme: {ancien_theme}")
# print(f"Volume: {volume}")

# Solution Exercice 5
# 5.1 : Copie superficielle

# original = {"a": 1, "b": [2, 3], "c": {"d": 4}}

# copie = original.copy()

# copie["a"] = 10
# copie["b"].append(4)

# print(f"Original: {original}")
# print(f"Copie: {copie}")

# 5.2 : Deepcopy - Corrigé
# import copy

# niveau1 = {"donnees": [1, 2, 3], "config": {"resolu": False}}
# niveau2 = copy.deepcopy(niveau1)

# niveau2["donnees"].append(4)
# niveau2["config"]["resolu"] = True

# print(f"Niveau 1: {niveau1}")
# print(f"Niveau 2: {niveau2}")

# 5.3 : Comparaison de copies
# d1 = {"a": 1, "b": 2}
# d2 = d1.copy()
# d3 = d1

# print(f"d1 == d2: {d1 == d2}")
# print(f"d1 is d2: {d1 is d2}")
# print(f"d1 is d3: {d1 is d3}")

# Solution Exercice 6
# 6.1 : Parcours des clés

# employe = {"nom": "Alice", "age": 30, "poste": "Developpeur", "salaire": 50000}

# for cle in employe:
#     print(f"- {cle}")

# if "experience" in employe:
#     print("Experience trouvée")
# else:
#     print("Experience non trouvée")

# 6.2 : Parcours des valeurs - Corrigé
# notes = {"math": 15, "francais": 12, "histoire": 18, "sport": 16}

# total = 0
# for note in notes.values():
#     total += note

# print(f"Moyenne: {total / len(notes)}")

# 6.3 : Parcours des items
# inventaire = {"pommes": 10, "bananes": 5, "oranges": 8, "kiwis": 3}

# for produit, quantite in inventaire.items():
#     print(f"{produit}: {quantite} unités")

# max_produit = max(inventaire, key=inventaire.get)
# max_quantite = inventaire[max_produit]

# print(f"Produit le plus stocké: {max_produit} ({max_quantite} unités)")

# Solution Exercice 7
# 7.1 : keys(), values(), items()

# config = {"host": "localhost", "port": 8080, "debug": True}

# cles = list(config.keys())
# valeurs = list(config.values())
# items = list(config.items())

# print(f"Clés: {cles}")
# print(f"Valeurs: {valeurs}")
# print(f"Items: {items}")

# 7.2 : fromkeys() - Corrigé
# cles = ["nom", "age", "ville"]
# valeur_par_defaut = "inconnu"

# resultat = dict.fromkeys(cles, valeur_par_defaut)

# print(resultat)

# 7.3 : Comprehension de dictionnaire
# nombres = [1, 2, 3, 4, 5]

# carres = {n: n**2 for n in nombres}

# print(carres)
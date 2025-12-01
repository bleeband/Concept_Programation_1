# Examen : Découverte des Types en Python
# Durée : 2h00
# Niveau : Débutant
# Objectif : Évaluer la compréhension des types de base et leur manipulation

#-----------------------------------------------------------------------------------------

# Exercice 1 : Développement - Gestion de Bibliothèque Simple
# Contexte
# Vous devez créer un système simple pour gérer des livres dans une bibliothèque en utilisant seulement des variables et des structures de données de base.

# À réaliser :

#-----------------------------------------------------------------------------------------

# # EXERCICE 1 - SYSTÈME BIBLIOTHÈQUE
# # Créez le système en utilisant uniquement des listes, dictionnaires et variables

# # 1. Créez une liste de livres (chaque livre est un dictionnaire)
# # Structure d'un livre: titre, auteur, année, statut ("disponible" ou "emprunté")

biblio = [
    {"titre": "1984","auteur": "George Orwell","Année" : 1949,"statut": "disponible"},
    {"titre": "Python pour les nuls","auteur": "John Doe","Année": 2020,"statut": "disponible"},
    {"titre": "Le Seigneur des Anneaux","auteur": "J.R.R. Tolkien","Année": 1954,"statut": "disponible"},
    {"titre": "La Moufette qui pet", "auteur": "Richard Petit","Année": 2019, "statut": "emprunté"},
    {"titre": "Le lutin cretin", "auteur": "Richard Petit","Année": 2020, "statut": "emprunté"}
]

#-----------------------------------------------------------------------------------------
# # 2. Affichez tous les livres disponibles
# print("=== LIVRES DISPONIBLES ===")

print("------------------------------------------")
print("==== Voici le contenu de ma biblio ====\n")
for livre in list(biblio):
    print("•", livre["titre"], "de", livre["auteur"])
print()

# Parcourez la liste et affichez seulement les livres disponibles

print("------------------------------------------")
print("==== Voici le contenu disponible ====\n")
for livre in biblio:
    if livre["statut"].lower() == "disponible":
        print("•", livre["titre"], "de", livre["auteur"], "est", livre["statut"])
print()

""" for livre in biblio:
    if livre["statut"] == "disponible":
        print(f"- {livre['titre']} par {livre['auteur']} est {livre['statut']}") """
#-----------------------------------------------------------------------------------------
# # 3. Empruntez un livre (changez son statut)

# Trouvez le livre et changez son statut en "emprunté"

livre_a_emprunter = "1984"

print(f'\n=== EMPRUNT DU LIVRE "{livre_a_emprunter}" ===')

for livre in biblio:
    if livre["titre"] == livre_a_emprunter:
        livre["statut"] = "emprunté"
        break

print("------------------------------------------")
print("==== Voici le contenu emprunté ====\n")
for livre in biblio:
    if livre["statut"].lower() == "emprunté":
        print("•", livre["titre"], "de", livre["auteur"], "est", livre["statut"])
print()

""" livre_a_emprunter = "1984"
for livre in biblio:
    if livre["titre"] == livre_a_emprunter and livre["statut"] == "disponible":
        livre['statut'] == "emprunté"
        print("•", livre["titre"], "de", livre["auteur"], "est", livre["statut"]) """

#-----------------------------------------------------------------------------------------
# # 4. Retournez un livre

livre_a_retourner = "Le lutin cretin"

print(f"\n=== RETOUR DE '{livre_a_retourner}' ===")

# Trouvez le livre et changez son statut en "disponible"

for livre in biblio:
    if livre["titre"] == livre_a_retourner:
        livre["statut"] = "disponible"
        break

print("------------------------------------------")
print("==== Voici le contenu disponible ====\n")
for livre in biblio:
    if livre["statut"].lower() == "disponible":
        print("•", livre["titre"], "de", livre["auteur"], "est", livre["statut"])
print()


#-----------------------------------------------------------------------------------------
# # 5. Calculez des statistiques

print("------------------------------------------")
print("\n=== STATISTIQUES ===")
total_livres = len(biblio)

livres_dispo = [livre for livre in biblio if livre["statut"] == "disponible"]
nb_dispo = len(livres_dispo)
livres_disponibles = nb_dispo

pourcentage_disponibles = (livres_disponibles / total_livres) * 100

print(f"Total livres: {total_livres}")
print(f"Livres disponibles: {livres_disponibles}")
print(f"Pourcentage disponibles: {pourcentage_disponibles:.1f}%\n")


#-----------------------------------------------------------------------------------------
# # 6. Recherche par auteur`

auteur_recherche = "George Orwell"

print("------------------------------------------")
print(f"=== RECHERCHE PAR AUTEUR '{auteur_recherche}' ===\n")
for livre in biblio:
    if livre["auteur"].lower() == auteur_recherche.lower():
        print("•", livre["titre"], "de", livre["auteur"])
print()

#-----------------------------------------------------------------------------------------

# EXERCICE 2 - CORRECTION D'ERREURS
# Corrigez toutes les erreurs dans ce code


# Données de l'inventaire
produits = ["pommes", "bananes", "oranges", "kiwis"]
stocks = [15, 8, 12, 5]
prix = [1.2, 0.8, 1.5, 2.0]


# 1. Affichage de l'inventaire
print("------------------------------------------")
print("=== INVENTAIRE ===")
for i in range(len(produits)):
    print(f"{produits[i]} - Stock: {stocks[i]} - Prix: {prix[i]}$")


# 2. Calcul du stock total
stock_total = sum(stocks)
print("------------------------------------------")
print(f"\nStock total: {stock_total}")


# 3. Produit le plus cher
index_plus_cher = prix.index(max(prix))
produit_plus_cher = produits[index_plus_cher]
print("------------------------------------------")
print(f"Produit le plus cher: {produit_plus_cher}")


# 4. Produits en rupture de stock
ruptures = []
for i in range(len(stocks)):
    if stocks[i] == 0:
        ruptures.append(produits[i])
print("------------------------------------------")
print(f"Produits en rupture: {ruptures}")


# 5. Ajout d'un nouveau produit
nouveau_produit = "mangues"
nouveau_stock = 10
nouveau_prix = 1.8

produits.append(nouveau_produit)
stocks.append(nouveau_stock)
prix.append(nouveau_prix)

print("------------------------------------------")
print(f"\nAprès ajout de {nouveau_produit}:")
print(f"Produits: {produits}")
print(f"Stocks: {stocks}")
print(f"Prix: {prix}")

# 6. Vérification des types
print("------------------------------------------")
print(f"\nTypes des données:")
print(f"Type de produits: {type(produits)}")
print(f"Type de stocks:, {type(stocks)}")
print(f"Type de prix: {type(prix)}")
print("------------------------------------------\n")


#-----------------------------------------------------------------------------------------

# # EXERCICE 3 - SYSTÈME DE NOTES
# # Complétez les parties manquantes


# 1. Données des étudiants et leurs notes
# Utilisez un dictionnaire où la clé est le nom et la valeur est une liste de notes

etudiants_notes = [
    {"nom" : "Alice", "notes": [15, 18, 12]},
    {"nom" : "Bob", "notes": [8, 14, 16]},
    {"nom" : "Charlie", "notes": [20, 19, 18]},
    {"nom" : "David", "notes": [10, 11, 9]}
]

# 2. Affichage des notes de chaque étudiant
print("------------------------------------------")
print("=== NOTES DES ÉTUDIANTS ===")
# Parcourez le dictionnaire et affichez nom + notes
for etudiant in list(etudiants_notes):
    print("•", etudiant["nom"], "resultat : ", etudiant["notes"])
print()

# 3. Calcul des moyennes individuelles
print("------------------------------------------")
print("\n=== MOYENNES INDIVIDUELLES ===")

moyennes = {}  # Dictionnaire pour stocker les moyennes
for etudiant in etudiants_notes:
    liste_notes = etudiant["notes"]
    moyenne = sum(liste_notes) / len(liste_notes)
    print(f"Moyenne de {etudiant['nom']} : {moyenne:.2f}\n")

for etudiant in etudiants_notes:
    etudiant["moyenne"] = round(sum(etudiant["notes"]) / len(etudiant["notes"]), 2)
# print(etudiants_notes)

""" for etudiant, notes in etudiants_notes.item():
    moyenne = sum(notes) / len(notes)
    moyenne[etudiant] = moyenne
    print(f"{etudiant}: {moyenne:.1f}/20") """

# 4. Trouver le meilleur étudiant
print("------------------------------------------")
print("\n=== CLASSEMENT ===")
meilleur_etudiant = None
meilleure_moyenne = 0

# Trouvez l'étudiant avec la meilleure moyenne
for etudiant in etudiants_notes:
    moyenne_actuelle = sum(etudiant["notes"]) / len(etudiant["notes"])
    if moyenne_actuelle > meilleure_moyenne:
        meilleure_moyenne = moyenne_actuelle
        meilleur_etudiant = etudiant["nom"]

print(f"Meilleur étudiant: {meilleur_etudiant} avec {meilleure_moyenne:.2f}/20")


# 5. Statistiques de la classe
print("------------------------------------------")
print("\n=== STATISTIQUES CLASSE ===")

toutes_notes = []

for etudiant in etudiants_notes:
    toutes_notes.extend(etudiant["notes"])
if len(toutes_notes) > 0:
    moyenne_generale = sum(toutes_notes) / len(toutes_notes)
else:
    print("Aucune note disponible.")

toutes_les_notes = [n for etudiant in etudiants_notes for n in etudiant["notes"]]
la_meilleure_note = max(toutes_les_notes)
meilleure_note = max(toutes_notes)
pire_note = min(toutes_notes)

print("------------------------------------------")
print(f"La meilleure note de la classe est : {la_meilleure_note}")

print("------------------------------------------")
print(f"Moyenne générale: {moyenne_generale:.2f}/20")
print(f"Meilleure note: {meilleure_note}/20")
print(f"Pire note: {pire_note}/20")


# 6. Distribution des notes

print("\n------------------------------------------")
print("=== DISTRIBUTION DES NOTES ===")
notes_tranches = {
    "16-20": 0,
    "14-15": 0,
    "12-13": 0,
    "10-11": 0,
    "0-9": 0
}

for etudiant in etudiants_notes:
    for note in etudiant["notes"]:
        if note >= 16:
            notes_tranches["16-20"] += 1
        elif note >= 14:
            notes_tranches["14-15"] += 1
        elif note >= 12:
            notes_tranches["12-13"] += 1
        elif note >= 10:
            notes_tranches["10-11"] += 1
        else:
            notes_tranches["0-9"] += 1
print("------------------------------------------")
print(f"Répartition des notes : {notes_tranches}")


# # 7. Ajout d'un nouvel étudiant
print("\n------------------------------------------")
print("=== AJOUT NOUVEL ÉTUDIANT ===")
nouvel_etudiant = "Eve"
nouvelles_notes = [17, 16, 15]
nouveau_profil = {
    "nom": nouvel_etudiant, 
    "notes": nouvelles_notes
}

etudiants_notes[etudiant] 
etudiants_notes.append(nouveau_profil)
print("------------------------------------------")
print(f"Après ajout de {nouvel_etudiant}:")
print("\n------------------------------------------")
print(etudiants_notes)
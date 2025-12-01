
# # EXERCICE COUR 7

# Exercices sur les Chaînes de Caractères

# Exercice 1 : Formatage avec f-strings

# 1.1 : Présentation personnelle
# Créez une présentation personnelle utilisant f-string avec variables.

""" nom = "dufour"
prenom = "marc-andre"
age = "41"
ville = "charlemagne"

print(f"Bonjour, mon nom est {prenom.title()} {nom.title()}, j'ai présentement {age} ans et je demeure à {ville.title()}") """

# ----------------------------------------------------------------------------------

# 1.2 : Calcul de prix
# Affichez un calcul de prix TTC avec formatage monétaire.

""" prix_av_txs = float(input("Veuillez enter le montant :"))
tps = 0.05
tvq = 0.09975
plus_tps = prix_av_txs * tps
plus_tvq = prix_av_txs * tvq
prix_ttc = prix_av_txs + plus_tps + plus_tvq
print(f"Le prix total est de {prix_ttc:.2f} $") """

# ----------------------------------------------------------------------------------

# 1.3 : Table de multiplication
# Générez une table de multiplication formatée.

""" x = int(input("entrer votre chiffre :"))
multi = x

for i in range(1, 11):
    table = x * i
    print(f"{multi} x {i} = {table}") """

# ----------------------------------------------------------------------------------

# Exercice 2 : Indexing et Slicing

""" # 2.1 : Extraction d'information
# Extrayez différentes parties d'une chaîne en utilisant les indexes.

phrase = "Bonjour Mme la professeur, quel est le programme aujourd'hui"

print(phrase.split(" ", 4))
print(phrase[0: 12])
print(phrase[-22:]) """

# ----------------------------------------------------------------------------------

# 2.2 : Inversion de chaîne
# Inversez une chaîne en utilisant le slicing.

""" chaine = "python"
inverse = chaine[::-1]
print(f"Original: {chaine}")
print(f"Inversé: {inverse}") """


# ----------------------------------------------------------------------------------

# 2.3 : Extraction sélective
# Extrayez des motifs spécifiques d'une chaîne.

""" test = "[DB] resultat 1 - fait [DB]"
test2 = "[DB] resultat 2 - fait [DB]"
test3 = "[DB] resultat 3 - fait [DB]"

print(test.removeprefix("[DB]").removesuffix("[DB]"))
print(test2.removeprefix("[DB]").removesuffix("[DB]"))
print(test3.removeprefix("[DB]").removesuffix("[DB]")) """

# ----------------------------------------------------------------------------------

# Exercice 3 : Fonctions de Base

# 3.1 : Analyse de texte
# Utilisez len(), capitalize(), title(), upper(), lower() sur un texte.

""" texte = "simple texte d'exemple : 1 "

print(f" le texte compte --> {len(texte)} mots")
print(f" fonction capitalize --> {texte.capitalize()}")
print(f" fonction lower --> {texte.lower()}")
print(f" fonction upper --> {texte.upper()}")
print(f" fonction title --> {texte.title()}") """


# ----------------------------------------------------------------------------------

# 3.2 : Normalisation de données
# Normalisez des noms et adresses email.

""" personne_1 = "marc-andre dufour"
courrie_1 = "BLeeBand@Gmail.com"

nom_normalise = personne_1.strip().title()
email_normalise = courrie_1.strip().lower()

print(f"Nom original: '{personne_1}'")
print(f"Nom normalisé: '{nom_normalise}'")
print(f"Email original: '{courrie_1}'")
print(f"Email normalisé: '{email_normalise}'") """

# ----------------------------------------------------------------------------------

# 3.3 : Formatage de titre
# Créez un système de formatage de titres.

""" titre1 = "la moufette qui pet"

titre_aff = titre1.title()
print(f"Titre original : {titre1}")
print(f"Titre à afficher : {titre_aff.replace("", "~ ",1)}") """


# ----------------------------------------------------------------------------------

# Exercice 4 : Recherche et Vérification

# 4.1 : Analyse de fréquences
# Utilisez count(), find(), index() pour analyser un texte.

""" phrase = "Le python est un langage de programmation pythonique"

print(f"Phrase: '{phrase}'")
print(f"Longueur: {len(phrase)} caractères")
print(f"Occurrences de 'python': {phrase.count('python')}")
print(f"Position de 'langage': {phrase.find('langage')}")
print(f"Index de 'programmation': {phrase.index('programmation')}")

# Différence entre find et index
try:
    print(f"Find 'java': {phrase.find('java')}")  # Retourne -1
    print(f"Index 'java': {phrase.index('java')}")  # Lève une exception
except ValueError as e:
    print(f"Erreur avec index: {e}") """


# ----------------------------------------------------------------------------------

# 4.2 : Validation de données
# Utilisez startswith(), endswith() pour valider des formats.

""" fichiers = ["document.pdf", "image.png", "script.py", "data.txt", "archive.zip"]

print("Fichiers Python:")
for fichier in fichiers:
    if fichier.endswith(".py"):
        print(f"  ✓ {fichier}")

print("\nFichiers commençant par 'd':")
for fichier in fichiers:
    if fichier.startswith("d"):
        print(f"  ✓ {fichier}")

# Validation email
email = "user@domain.com"
est_email_valide = email.endswith(".com") and "@" in email
print(f"\nEmail valide: {est_email_valide}") """

# ----------------------------------------------------------------------------------

# 4.3 : Recherche avancée
# Combinez plusieurs méthodes de recherche.

""" texte = "Python 3.9 est sorti en 2020. Python 3.10 est sorti en 2021."

motif = "Python"
position = texte.find(motif)
occurrences = texte.count(motif)

print(f"Motif recherché: '{motif}'")
print(f"Première occurrence: position {position}")
print(f"Nombre d'occurrences: {occurrences}")

# Trouver toutes les occurrences
index = 0
positions = []
while index < len(texte):
    index = texte.find(motif, index)
    if index == -1:
        break
    positions.append(index)
    index += len(motif)

print(f"Positions: {positions}") """

# ----------------------------------------------------------------------------------

# Exercice 5 : Transformation et Découpage

# 5.1 : Nettoyage de texte
# Utilisez split(), splitlines() pour analyser un texte structuré.

# csv_data = "Alice;25;Paris;Developpeur\nBob;30;Lyon;Designer\nCharlie;35;Marseille;Manager"

# print("Données CSV:")
# lignes = csv_data.splitlines()
# for ligne in lignes:
#     colonnes = ligne.split(";")
#     print(f"  Nom: {colonnes[0]}, Age: {colonnes[1]}, Ville: {colonnes[2]}, Métier: {colonnes[3]}")

# # Texte multiligne
# texte_multiligne = """Première ligne
# Deuxième ligne
# Troisième ligne"""
# print()
# print(texte_multiligne)

# lignes = texte_multiligne.splitlines()
# print(f"\nNombre de lignes: {len(lignes)}")
# for i, ligne in enumerate(lignes, 1):
#     print(f"Ligne {i}: {ligne}")

# ----------------------------------------------------------------------------------

# 5.2 : Reconstruction
# Utilisez join() pour reconstruire des chaînes.

""" mots = ["Python", "est", "un", "langage", "puissant"]
phrase = " ".join(mots)
print(f"Liste: {mots}")
print(f"Phrase: {phrase}")

# Application pratique
chemin = ["usr", "local", "bin", "python"]
chemin_complet = "/".join(chemin)
print(f"\nChemin: {chemin_complet}")

tags = ["python", "programmation", "développement"]
hashtags = " ".join(["#" + tag for tag in tags])
print(f"Hashtags: {hashtags}") """

# ----------------------------------------------------------------------------------

# 5.3 : Correction automatique
# Utilisez replace() pour corriger des erreurs.

""" texte_avec_erreurs = "J'aime la programation en Pythn. C'est trés intérressant."

corrections = {
    "programation": "programmation",
    "Pythn": "Python",
    "trés": "très",
    "intérressant": "intéressant"
}

texte_corrige = texte_avec_erreurs
for erreur, correction in corrections.items():
    texte_corrige = texte_corrige.replace(erreur, correction)

print(f"Original: {texte_avec_erreurs}")
print(f"Corrigé: {texte_corrige}")

# Remplacement multiple
template = "Bonjour {nom}, votre commande {id} est prête."
commande = template.replace("{nom}", "Alice").replace("{id}", "CMD123")
print(f"\nTemplate: {template}")
print(f"Rempli: {commande}") """

# ----------------------------------------------------------------------------------

# Exercice 6 : Nettoyage avec removeprefix/removesuffix

# 6.1 : Nettoyage d'URL
# Nettoyez des URLs et chemins de fichier.

""" urls = [
    "https://www.example.com",
    "http://blog.example.com/",
    "ftp://files.example.com",
    "www.example.com/path"
]

print("URLs nettoyées:")
for url in urls:
    nettoyee = url.removeprefix("https://").removeprefix("http://").removeprefix("ftp://")
    nettoyee = nettoyee.removesuffix("/")
    print(f"  {url} -> {nettoyee}")

# Chemins de fichiers
chemins = ["/home/user/file.txt", "C:\\Windows\\System32\\file.exe", "./local/file.md"]

print("\nChemins relatifs:")
for chemin in chemins:
    relatif = chemin.removeprefix("/home/user/").removeprefix("C:\\Windows\\System32\\").removeprefix("./")
    print(f"  {chemin} -> {relatif}") """

# ----------------------------------------------------------------------------------

# 6.2 : Formatage de numéros
# Nettoyez des numéros de téléphone et codes.

""" telephones = ["+33123456789", "0033123456789", "0123456789"]

print("Numéros normalisés:")
for tel in telephones:
    nettoye = tel.removeprefix("+33").removeprefix("0033")
    if nettoye.startswith("0"):
        nettoye = nettoye[1:]
    print(f"  {tel} -> {nettoye}")

# Codes produits
codes = ["PROD-12345", "ITEM-67890", "PROD-", "-TEST"]

print("\nCodes nettoyés:")
for code in codes:
    nettoye = code.removeprefix("PROD-").removeprefix("ITEM-").removesuffix("-TEST")
    print(f"  {code} -> '{nettoye}'") """

# ----------------------------------------------------------------------------------

# 6.3 : Normalisation d'identifiants
# Normalisez des identifiants système.

""" identifiants = [
    "user_12345",
    "admin_001",
    "guest_99999",
    "user_",
    "_temp"
]

print("IDs normalisés:")
for id in identifiants:
    # Supprimer les préfixes et suffixes communs
    nettoye = id.removeprefix("user_").removeprefix("admin_").removeprefix("guest_")
    nettoye = nettoye.removesuffix("_temp")

    # Garder seulement les chiffres
    if nettoye and nettoye.isdigit():
        print(f"  {id} -> ID{nettoye}")
    else:
        print(f"  {id} -> INVALIDE") """


# ----------------------------------------------------------------------------------

# Exercice 7 : Projets Complets

# 7.1 : Système de génération d'email
# Créez un générateur d'emails professionnels.

""" # Données des employés
employes = [
    {"prenom": "jean", "nom": "dupont", "departement": "IT"},
    {"prenom": "marie", "nom": "martin", "departement": "RH"},
    {"prenom": "pierre", "nom": "durand", "departement": "VENTES"}
]

print("Emails professionnels générés:")
for emp in employes:
    prenom = emp["prenom"].lower().strip()
    nom = emp["nom"].lower().strip()
    dept = emp["departement"].lower().strip()

    # Générer l'email
    email = f"{prenom}.{nom}@company.com"

    # Formatage du nom complet
    nom_complet = f"{prenom.title()} {nom.upper()}"

    print(f"  {nom_complet} ({dept.upper()}) -> {email}") """





# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
#   
# Solutions des Exercices


# Solution Exercice 1
# 1.1 : Présentation personnelle
# nom = "Alice"
# age = 25
# metier = "développeuse"
# ville = "Paris"

# presentation = f"Bonjour, je m'appelle {nom}, j'ai {age} ans. Je suis {metier} et je vis à {ville}."
# print(presentation)


# 1.2 : Calcul de prix
# prix_ht = 150
# taux_tva = 0.2
# tva = prix_ht * taux_tva
# prix_ttc = prix_ht + tva

# facture = f"""
# DÉTAIL DE LA FACTURE
# Prix HT: {prix_ht}$
# TVA ({taux_tva*100}%): {tva}$
# Total TTC: {prix_ttc}$
# """
# print(facture)


# 1.3 : Table de multiplication
# nombre = 7

# for i in range(1, 6):
#     resultat = nombre * i
#     ligne = f"{nombre} × {i:2d} = {resultat:2d}"
#     print(ligne)


# Solution Exercice 2

# 2.1 : Extraction d'information
# texte = "Python-3.9.1-installer.exe"

# print(f"Texte complet: {texte}")
# print(f"Premier caractère: {texte[0]}")
# print(f"5 premiers caractères: {texte[:5]}")
# print(f"5 derniers caractères: {texte[-5:]}")
# print(f"Du 7ème au 12ème: {texte[7:12]}")
# print(f"Un caractère sur deux: {texte[::2]}")

# 2.2 : Inversion de chaîne

# mot = "python"
# inverse = mot[::-1]
# print(f"Original: {mot}")
# print(f"Inversé: {inverse}")

# # Application pratique
# palindrome = "radar"
# est_palindrome = palindrome == palindrome[::-1]
# print(f"'{palindrome}' est un palindrome: {est_palindrome}")

# 2.3 : Extraction sélective
# url = "https://www.example.com/page/article.html"

# protocole = url[:5]  # https
# domaine = url[8:21]  # www.example.com
# extension = url[-4:]  # .html
# nom_fichier = url[22:-5]  # page/article

# print(f"Protocole: {protocole}")
# print(f"Domaine: {domaine}")
# print(f"Nom fichier: {nom_fichier}")
# print(f"Extension: {extension}")

# Solution Exercice 3
# 3.1 : Analyse de texte

# texte = "  python programming is FUN!  "

# print(f"Original: '{texte}'")
# print(f"Longueur: {len(texte)}")
# print(f"Capitalize: '{texte.capitalize()}'")
# print(f"Title: '{texte.title()}'")
# print(f"Upper: '{texte.upper()}'")
# print(f"Lower: '{texte.lower()}'")
# print(f"Strip: '{texte.strip()}'")

# 3.2 : Normalisation de données
# nom_entree = "  jean-marie dupont  "
# email_entree = "  CONTACT@EXAMPLE.COM  "

# nom_normalise = nom_entree.strip().title()
# email_normalise = email_entree.strip().lower()

# print(f"Nom original: '{nom_entree}'")
# print(f"Nom normalisé: '{nom_normalise}'")
# print(f"Email original: '{email_entree}'")
# print(f"Email normalisé: '{email_normalise}'")

# 3.3 : Formatage de titre
# titre_article = "introduction à la programmation python"

# titre_formate = titre_article.title()
# slug = titre_article.replace(" ", "-").lower()

# print(f"Titre: {titre_formate}")
# print(f"Slug: {slug}")
# print(f"En-tête: {titre_formate.upper()}")


# Solution Exercice 4
# 4.1 : Analyse de fréquences

# phrase = "Le python est un langage de programmation pythonique"

# print(f"Phrase: '{phrase}'")
# print(f"Longueur: {len(phrase)} caractères")
# print(f"Occurrences de 'python': {phrase.count('python')}")
# print(f"Position de 'langage': {phrase.find('langage')}")
# print(f"Index de 'programmation': {phrase.index('programmation')}")

# # Différence entre find et index
# try:
#     print(f"Find 'java': {phrase.find('java')}")  # Retourne -1
#     print(f"Index 'java': {phrase.index('java')}")  # Lève une exception
# except ValueError as e:
#     print(f"Erreur avec index: {e}")

# 4.2 : Validation de données
# fichiers = ["document.pdf", "image.png", "script.py", "data.txt", "archive.zip"]

# print("Fichiers Python:")
# for fichier in fichiers:
#     if fichier.endswith(".py"):
#         print(f"  ✓ {fichier}")

# print("\nFichiers commençant par 'd':")
# for fichier in fichiers:
#     if fichier.startswith("d"):
#         print(f"  ✓ {fichier}")

# # Validation email
# email = "user@domain.com"
# est_email_valide = email.endswith(".com") and "@" in email
# print(f"\nEmail valide: {est_email_valide}")

# 4.3 : Recherche avancée
# texte = "Python 3.9 est sorti en 2020. Python 3.10 est sorti en 2021."

# motif = "Python"
# position = texte.find(motif)
# occurrences = texte.count(motif)

# print(f"Motif recherché: '{motif}'")
# print(f"Première occurrence: position {position}")
# print(f"Nombre d'occurrences: {occurrences}")

# # Trouver toutes les occurrences
# index = 0
# positions = []
# while index < len(texte):
#     index = texte.find(motif, index)
#     if index == -1:
#         break
#     positions.append(index)
#     index += len(motif)

# print(f"Positions: {positions}")


# Solution Exercice 5
# 5.1 : Nettoyage de texte

# csv_data = "Alice;25;Paris;Developpeur\nBob;30;Lyon;Designer\nCharlie;35;Marseille;Manager"

# print("Données CSV:")
# lignes = csv_data.splitlines()
# for ligne in lignes:
#     colonnes = ligne.split(";")
#     print(f"  Nom: {colonnes[0]}, Age: {colonnes[1]}, Ville: {colonnes[2]}, Métier: {colonnes[3]}")

# # Texte multiligne
# texte_multiligne = """Première ligne
# Deuxième ligne
# Troisième ligne"""

# lignes = texte_multiligne.splitlines()
# print(f"\nNombre de lignes: {len(lignes)}")
# for i, ligne in enumerate(lignes, 1):
#     print(f"Ligne {i}: {ligne}")

# 5.2 : Reconstruction
# mots = ["Python", "est", "un", "langage", "puissant"]
# phrase = " ".join(mots)
# print(f"Liste: {mots}")
# print(f"Phrase: {phrase}")

# # Application pratique
# chemin = ["usr", "local", "bin", "python"]
# chemin_complet = "/".join(chemin)
# print(f"\nChemin: {chemin_complet}")

# tags = ["python", "programmation", "développement"]
# hashtags = " ".join(["#" + tag for tag in tags])
# print(f"Hashtags: {hashtags}")

# 5.3 : Correction automatique
# texte_avec_erreurs = "J'aime la programation en Pythn. C'est trés intérressant."

# corrections = {
#     "programation": "programmation",
#     "Pythn": "Python",
#     "trés": "très",
#     "intérressant": "intéressant"
# }

# texte_corrige = texte_avec_erreurs
# for erreur, correction in corrections.items():
#     texte_corrige = texte_corrige.replace(erreur, correction)

# print(f"Original: {texte_avec_erreurs}")
# print(f"Corrigé: {texte_corrige}")

# # Remplacement multiple
# template = "Bonjour {nom}, votre commande {id} est prête."
# commande = template.replace("{nom}", "Alice").replace("{id}", "CMD123")
# print(f"\nTemplate: {template}")
# print(f"Rempli: {commande}")

# Solution Exercice 6
# 6.1 : Nettoyage d'URL

# urls = [
#     "https://www.example.com",
#     "http://blog.example.com/",
#     "ftp://files.example.com",
#     "www.example.com/path"
# ]

# print("URLs nettoyées:")
# for url in urls:
#     nettoyee = url.removeprefix("https://").removeprefix("http://").removeprefix("ftp://")
#     nettoyee = nettoyee.removesuffix("/")
#     print(f"  {url} -> {nettoyee}")

# # Chemins de fichiers
# chemins = ["/home/user/file.txt", "C:\\Windows\\System32\\file.exe", "./local/file.md"]

# print("\nChemins relatifs:")
# for chemin in chemins:
#     relatif = chemin.removeprefix("/home/user/").removeprefix("C:\\Windows\\System32\\").removeprefix("./")
#     print(f"  {chemin} -> {relatif}")

# 6.2 : Formatage de numéros
# telephones = ["+33123456789", "0033123456789", "0123456789"]

# print("Numéros normalisés:")
# for tel in telephones:
#     nettoye = tel.removeprefix("+33").removeprefix("0033")
#     if nettoye.startswith("0"):
#         nettoye = nettoye[1:]
#     print(f"  {tel} -> {nettoye}")

# # Codes produits
# codes = ["PROD-12345", "ITEM-67890", "PROD-", "-TEST"]

# print("\nCodes nettoyés:")
# for code in codes:
#     nettoye = code.removeprefix("PROD-").removeprefix("ITEM-").removesuffix("-TEST")
#     print(f"  {code} -> '{nettoye}'")

# 6.3 : Normalisation d'identifiants
# identifiants = [
#     "user_12345",
#     "admin_001",
#     "guest_99999",
#     "user_",
#     "_temp"
# ]

# print("IDs normalisés:")
# for id in identifiants:
#     # Supprimer les préfixes et suffixes communs
#     nettoye = id.removeprefix("user_").removeprefix("admin_").removeprefix("guest_")
#     nettoye = nettoye.removesuffix("_temp")

#     # Garder seulement les chiffres
#     if nettoye and nettoye.isdigit():
#         print(f"  {id} -> ID{nettoye}")
#     else:
#         print(f"  {id} -> INVALIDE")

# Solution Exercice 7
# 7.1 : Système de génération d'email

# # Données des employés
# employes = [
#     {"prenom": "jean", "nom": "dupont", "departement": "IT"},
#     {"prenom": "marie", "nom": "martin", "departement": "RH"},
#     {"prenom": "pierre", "nom": "durand", "departement": "VENTES"}
# ]

# print("Emails professionnels générés:")
# for emp in employes:
#     prenom = emp["prenom"].lower().strip()
#     nom = emp["nom"].lower().strip()
#     dept = emp["departement"].lower().strip()

#     # Générer l'email
#     email = f"{prenom}.{nom}@company.com"

#     # Formatage du nom complet
#     nom_complet = f"{prenom.title()} {nom.upper()}"

#     print(f"  {nom_complet} ({dept.upper()}) -> {email}")
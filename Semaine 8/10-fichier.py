#  **  OUVERTURE EN W (WRITE) - créé ou écrase un fichier

# with open("mon-fichier.txt", "w") as fichier:
#     fichier.write("Bonjour tout le monde !\n")
#     fichier.write("Bienvenue dans le monde des fichiers")

# print("fichier écrit avec succès !")

ligne = [
    "Alice : 25 ans\n",
    "pierre : 32 ans\n",
    "fred : 25 ans\n",
    "albert : 28 ans\n",
    "boris : 31 ans\n",
]

# with open("personne.txt", "w") as f:
#     f.writelines(ligne)

# MODE a pour append - ajouter au fichier

# with open("journal.txt", "a") as g:
#     g.write("*** Nouvelle entrée ***\n")
#     g.write("Date: 18-12-2025\n")
#     g.write("Date: 18-12-2025\n")
#     g.write("\n")


# ***  LECTURE D'UN FICHIER ***
# MODE r pour read - lecture seule

# with open("mon-fichier.txt", "r") as f:
#     contenu = f.read()
#     print("Contenu complet :")
#     print(contenu)

# with open("mon-fichier.txt", "r") as f:
#     print("Lecture ligne par ligne :")
#     for ligne in f:
#         print(f" ligne : {ligne.strip()} ")

# with open("mon-fichier.txt", "r") as f:
#     ligne = f.readlines()
#     print(f"le nombre de ligne est : {len(ligne)}")
#     for i, ligne in enumerate(ligne, 1):
#         print(f"ligne {i} : {ligne.strip()}")


# Présentation du TP 1 - Cour concept de programation 1
# Réalisé par Marc-André Dufour

biblio = [
    {"titre": "Harry Potter", "auteur": "JK Rowling", "statut": "disponible"},
    {"titre": "1984", "auteur": "George Orwell", "statut": "emprunté"},
    {"titre": "La Moufette qui pet", "auteur": "Richard Petit", "statut": "emprunté"},
    {"titre": "Le lutin cretin", "auteur": "Richard Petit", "statut": "emprunté"},
    {"titre": "2020 l'odysee de l'espace", "auteur": "Jules Vernes", "statut": "disponible"},
    {"titre": "Le code civil du quebec", "auteur": "Badoin, Renaud", "statut": "disponible"}
]

print()
print("MENU  -->",  "1.  Afficher la bibliothèque", "2.  Rechercher un titre de livre", "3.  Vérifier le statut")
print()

choix = int(input("Veuillez faire un choix parmi le menu : "))
choix_menu = choix

if choix == 1:
# AFFICHER LA BIBLIOTHEQUE
    for livre in list(biblio):
            print("•", livre["titre"], "de", livre["auteur"])
print()

if choix == 2:
# RECHERCHE PAR TITRE
    rech_titre = input("Quelle titre recherchez-vous : ").lower()

    for livre in list(biblio):
        if rech_titre in livre["titre"].lower():
            print(f"{livre["titre"]} - {livre["auteur"]}")
print()

if choix == 3:
# AFFICHER LA DISPONIBILITE DES LIVRES

    for livre in biblio:
        if livre["statut"].lower() == "disponible":
            print("•", livre["titre"], "de", livre["auteur"])
            
print()

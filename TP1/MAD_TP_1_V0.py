# Présentation du TP 1 - Cour concept de programation 1
# Réalisé par Marc-André Dufour

hp = "Harry Potter"
biblio = [
    {"titre": f"{hp} 1 : L'École des soriers", "auteur": "JK Rowling", "statut": "disponible", "note": "4", "client": ""},
    {"titre": f"{hp} 2 : La chambre des secrets", "auteur": "JK Rowling", "statut": "disponible", "note": "4", "client": ""},
    {"titre": f"{hp} 3 : Le Prisonnier d'Azkaban", "auteur": "JK Rowling", "statut": "emprunté", "note": "3", "client": ""},
    {"titre": f"{hp} 4 : La coupe de feu", "auteur": "JK Rowling", "statut": "disponible", "note": "5", "client": ""},
    {"titre": f"{hp} 5 : L'ordre du Phénix", "auteur": "JK Rowling", "statut": "disponible", "note": "4", "client": ""},
    {"titre": f"{hp} 6 : Le prince de sang-mêlé", "auteur": "JK Rowling", "statut": "disponible", "note": "3", "client": ""},
    {"titre": f"{hp} et Les reliques de la mort", "auteur": "JK Rowling", "statut": "disponible", "note": "4", "client": ""},
    {"titre": "1984", "auteur": "George Orwell", "statut": "emprunté", "note": "2", "client": ""},
    {"titre": "La Moufette qui pet", "auteur": "Richard Petit", "statut": "emprunté", "note": "3", "client": ""},
    {"titre": "Le lutin cretin", "auteur": "Richard Petit", "statut": "emprunté", "note": "3", "client": ""},
    {"titre": "2020 l'odysee de l'espace", "auteur": "Jules Vernes", "statut": "disponible", "note": "4", "client": ""},
    {"titre": "Le code civil du quebec", "auteur": "Badoin, Renaud", "statut": "disponible", "note": "1", "client": ""},
]

choix_inv = "Choix invalide, veuillez recommencer"
menu1 = "MENU  -->  1.  Afficher la bibliothèque  2.  Rechercher un titre de livre   3.  Vérifier le statut   Q.  Quitter"
menu2 = "STATUT -->  1. Disponible  2. Emprunté  R.  Retour au menu principal"

# IDENTIFICATION DE L'USAGER
print("-----------------------------------------------")
client_iden = input("Bonjour ! Veuillez entrer votre nom : ")
client = client_iden
print()

print("--------------------------------------------------------------")
print(f"==== Bienvenue dans ma bibliothèque personnelle {client} ====")
print()
print(menu1)
print()

while True:
    choix = input("Veuillez faire un choix parmi le menu : ")

    if choix == "1":
    # AFFICHER LA BIBLIOTHEQUE
        print("---------------------------------------")
        print("==== Voici le contenu de ma biblio ====")
        for livre in list(biblio):
                print("•", livre["titre"], "de", livre["auteur"])
        print()

    elif choix == "2":
    # RECHERCHE PAR TITRE
        print("---------------------------------")
        print("Effectuer une recherche par titre")
        rech_titre = input(f"{client}, quelle titre recherchez-vous : ").lower()
        print()
        print(f"Voici le résultat de la recherche contenent: {rech_titre}")
        for livre in list(biblio):
            if rech_titre in livre["titre"].lower():
                print("•", livre["titre"], "de", livre["auteur"])
        print()

    elif choix == "3":
    # AFFICHER LA DISPONIBILITE DES LIVRES
        print("--------------------------------")
        print("Vérifitacion de la disponibilité")
        print()
        print(menu2)
        while True:

            choix_statut = input("Veuillez faire votre choix : ")
            if choix_statut == "1":
                for livre in biblio:
                    if livre["statut"].lower() == "disponible":
                        print("•", livre["titre"], "de", livre["auteur"])
            elif choix_statut == "2":
                for livre in biblio:
                    if livre["statut"].lower() == "emprunté":
                        print("•", livre["titre"], "de", livre["auteur"])            
            elif choix_statut.lower == "r" or "R":
                print()
                print("Retour au menu principal")
                print(menu1)
                break
            else:
                print()
                print(choix_inv + client)

    elif choix.lower == "q" or "Q":
        print()
        print(f"Merci {client}, à la prochaine ! Au plaisir de vous revoir")
        print("-----------------------------------------------------------")
        break

    else:
        print()
        print(choix_inv + client)




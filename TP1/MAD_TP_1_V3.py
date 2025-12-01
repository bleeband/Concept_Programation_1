# Présentation du TP 1 - Cour concept de programation 1
# Réalisé par Marc-André Dufour

# DECLARATION DES VARIABLES
hp = "Harry Potter"
choix_inv = "Choix invalide, veuillez recommencer"
choix_menu = "\nVeuillez faire un choix parmi le menu : "
short = "--------------------------------------------"
long = "----------------------------------------------------------------------------------------------------------"
menu1 = f"   MENU      -->  1.  Afficher la bibliothèque  2.  Rechercher un titre de livre   3.  Vérifier le statut\nPRINCIPAL    -->  4.  Gestion des livres   5.  Statistique  6.  Gestion de la bibliothèque  Q.  Quitter"
menu2 = "RECHERCHE -->  1. Par titre  2. Par auteur  R.  Retour au menu principal"
menu3 = "STATUT -->  1. Disponible  2. Emprunté  R.  Retour au menu principal"
menu4 = "GESTION LIVRE -->  1.  Emprunt  2.  Retour  R.  Retour au menu principal"
menu5 = "STATISTIQUE -->  1.  Rapport blibliothèque  2.  Top 3  3.  Statistiques générales   R.  Retour au menu principal"
menu6 = "GESTION BIBLIO -->  1.  Ajout d'un livre  2.  Retrait d'un livre  R.  Retour au menu principal"

biblio = [
    {"titre": f"{hp} 1 : L'École des soriers", "auteur": "JK Rowling", "statut": "disponible", "note": "4", "client": ""},
    {"titre": f"{hp} 2 : La chambre des secrets", "auteur": "JK Rowling", "statut": "disponible", "note": "4", "client": ""},
    {"titre": f"{hp} 3 : Le Prisonnier d'Azkaban", "auteur": "JK Rowling", "statut": "emprunté", "note": "3", "client": "test"},
    {"titre": f"{hp} 4 : La coupe de feu", "auteur": "JK Rowling", "statut": "disponible", "note": "5", "client": ""},
    {"titre": f"{hp} 5 : L'ordre du Phénix", "auteur": "JK Rowling", "statut": "disponible", "note": "4", "client": ""},
    {"titre": f"{hp} 6 : Le prince de sang-mêlé", "auteur": "JK Rowling", "statut": "disponible", "note": "3", "client": ""},
    {"titre": f"{hp} et Les reliques de la mort", "auteur": "JK Rowling", "statut": "disponible", "note": "4", "client": ""},
    {"titre": "1984", "auteur": "George Orwell", "statut": "emprunté", "note": "2", "client": "Marc"},
    {"titre": "La Moufette qui pet", "auteur": "Richard Petit", "statut": "emprunté", "note": "3", "client": "123"},
    {"titre": "Le lutin cretin", "auteur": "Richard Petit", "statut": "emprunté", "note": "3", "client": "123"},
    {"titre": "2020 l'odysee de l'espace", "auteur": "Jules Vernes", "statut": "disponible", "note": "4", "client": ""},
    {"titre": "Le code civil du quebec", "auteur": "Badoin, Renaud", "statut": "disponible", "note": "1", "client": ""},
]

# IDENTIFICATION DE L'USAGER
print(f"\n{long}")
client_iden = input("Bonjour ! pour débuter, veuillez vous identifier : ")
client = client_iden
print(f"\n{long}\nBienvenue dans ma bibliothèque personnelle, {client.upper()} !")

# MESSAGE LORSQUE LE CLIENT QUITTE
quitter = f"\n{long}\nMerci {client.upper()}, à la prochaine ! Au plaisir de vous revoir bientôt !!!"

while True:
    print(f"{long}")
    print(f"\n{menu1}")
    choix = input(choix_menu)

    # AFFICHER LA BIBLIOTHEQUE
    if choix == "1":
        print(f"{short}\nVoici le contenu de ma biblio :\n")
        for livre in list(biblio):
                print("•", livre["titre"], "écrit par", livre["auteur"])

    # RECHERCHE PERSONNALISÉ DANS LA BIBLIOTHEQUE
    elif choix == "2":
        while True:
            print(f"{long}")
            print(f"\n{menu2}")
            choix_recherche = input(choix_menu)

            # RECHERCHE PAR TITRE
            if choix_recherche == "1":
                print(f"\n{short}\nEffectuer une recherche par titre")
                rech_titre = input(f"\n{client.upper()}, quelle titre recherchez-vous : ").lower()
                print(f"\nVoici le résultat de la recherche contenent : {rech_titre.upper()}\n")
                for livre in list(biblio):
                    if rech_titre in livre["titre"].lower():
                        print("•", livre["titre"], "écrit par", livre["auteur"])           

            # RECHERCHE PAR NOM D'AUTEUR
            elif choix_recherche == "2":
                print(f"\n{short}\nEffectuer une recherche par nom d'auteur")
                rech_auteur = input(f"\n{client.upper()}, quelle auteur recherchez-vous : ").lower()
                print(f"{short}\nVoici le résultat de la recherche contenent: {rech_auteur.upper()} \n")
                for livre in list(biblio):
                    if rech_auteur in livre["auteur"].lower():
                        print("•", livre["titre"], "écrit par", livre["auteur"],)      

            elif choix_recherche.lower == "r" or "R":
                print(f"\nRetour au menu principal")
                break

            else:
                print(f"\n{choix_inv} + {client.upper()}")
                print(f"\n{menu2}\n")

    # AFFICHER LA DISPONIBILITE DES LIVRES
    elif choix == "3":
        while True:
            print(f"{long}")    
            print(f"\n{menu3}")
            choix_statut = input(choix_menu)

            if choix_statut == "1":
                livres_dispo = [livre for livre in biblio if livre["statut"] == "disponible"]
                nb_dispo = len(livres_dispo)
                livres_disponibles = nb_dispo
                print(f"\n{short}\n===> LIVRE DISPONIBLE <===")
                print(f"Nombre de livres disponible présentement : {livres_disponibles}\n")
                for livre in biblio:
                    if livre["statut"].lower() == "disponible":
                        print("•", livre["titre"], "écrit par", livre["auteur"])
                break

            elif choix_statut == "2":
                livres_empr = [livre for livre in biblio if livre["statut"] == "emprunté"]
                nb_empr = len(livres_empr)
                livres_emprunté = nb_empr
                print(f"\n{short}\n===> LIVRE EMPRUNTÉ <===")
                print(f"Nombre de livres emprunté présentement : {livres_emprunté}\n")
                for livre in biblio:
                    if livre["statut"].lower() == "emprunté":
                        print("•", livre["titre"], "écrit par", livre["auteur"],)
                break

            elif choix_statut.lower() == "r" or "R":
                print(f"\nRetour au menu principal")
                break   

            else:
                print(f"\n{choix_inv} + {client.upper()}")
                print(f"\n{menu3}\n")
    
    # GESTION DES EMPRUNT ET RETOUR
    elif choix == "4":
        while True:
            print(f"{long}")    
            print(f"\n{menu4}")
            choix_gestL = input(choix_menu)

            # VERIFIER DE LA LIMITE DE 2 LIVRES MAX
            if choix_gestL == "1":

                # COMPTER LES EMPRUNTS DU CLIENT ET CREER UNE LISTE
                nb_emprunts = 0
                liste_emprunt = []
                for livre in list(biblio):
                    # On regarde si le livre est emprunté par CE client précis et on fait une liste
                    if livre["client"].lower() == client.lower():
                        nb_emprunts += 1
                        liste_emprunt.append(livre["titre"])

                # LIMITE ATTEINTE
                if nb_emprunts >= 2:
                    print(f"{long}\n\nDésolé {client.upper()}, vous avez atteint la limite de {nb_emprunts} livres en votre possession.\n")
                    for titre_a_rendre in liste_emprunt:
                        print(f"• {titre_a_rendre.title()}")
                    print("\nVeuillez retourner un livre avant de pouvoir refaire un emprunt.")
                
                else:
                    # AFFICHAGE DES LIVRES DIPONIBLES
                    print(f"\n{long}\n")
                    for livre in biblio:
                        if livre["statut"].lower() == "disponible":
                            print("•", livre["titre"], "écrit par", livre["auteur"],)
                    print(f"\n{long}\n")

                    # GESTION DE L'EMPRUNT
                    livre_a_emprunter = input(f"{client.upper()}, quelle titre voulez-vous emprunter : ").lower()
                    print(f"\nEMPRUNT DU LIVRE {livre_a_emprunter}\n")

                    livre_trouve = False
                    
                    for livre in biblio:
                        if livre["titre"].lower() == livre_a_emprunter.lower():
                            livre_trouve = True
                            if livre["statut"] == "disponible":
                                livre["statut"] = "emprunté"
                                livre["client"] = client
                                print(f"{short}\n{client.upper()}, vous avez emprunté {livre['titre'].upper()}\n")
                            
                            elif livre["statut"] == "emprunté":
                                print(f"{short}\nLe livre {livre['titre'].upper()} n'est pas disponible pour le moment.")
                            break 

                if not livre_trouve:
                    print(f"{short}\nLe livre {livre['titre'].upper()} n'est pas disponible dans ma bibliothèque.")

            elif choix_gestL == "2":

                # AFFICHAGE DES LIVRES EMPRUNTÉ PAR LE CLIENT
                print(f"\n{short}\n")
                livre_emprunter = False
                for livre in biblio:
                    if livre["client"].lower() == client.lower():
                        print("•", livre["titre"])
                        livre_emprunter = True

                if not livre_emprunter:
                        print("Vous n'avez aucun livre à retourner.")
                
                else:  
                    # GESTION DU RETOUR
                    print(f"\n{short}\n") 
                    livre_a_retourner = input(f"{client.upper()}, quelle titre voulez-vous retourner : ").lower()
                    print(f"\nRETOUR DU LIVRE {livre_a_retourner.title()}\n")
                    livre_trouve = False

                    for livre in biblio:
                        if livre["titre"].lower() == livre_a_retourner.lower():
                            livre_trouve = True
                            if livre["statut"] == "emprunté":
                                nouvelle_note = input(f"Veuillez noter votre livre sur une note de 1 à 5 étoiles : ")
                                if nouvelle_note.isdigit():
                                    livre["note"] = int(nouvelle_note)
                                else:
                                    livre["note"] = 0
                                livre["statut"] = "disponible"
                                livre["client"] = ""
                                print(f"{short}\n{client.upper()}, vous avez retourné et noté {livre['titre'].upper()}")
                                
                            elif livre["statut"] == "disponible":
                                print(f"{short}\nLe livre {livre['titre'].upper()} est déjà dans la bibliothèque.\n")
                            break 
    
                    if not livre_trouve:
                        print(f"{short}\nLe livre {livre_a_retourner.upper()} n'est pas disponible dans ma bibliothèque.\n")

            elif choix_gestL.lower() == "r" or "R":
                print(f"\nRetour au menu principal")
                break

            else:
                print(f"\n{choix_inv} + {client.upper()}")
                print(f"\n{menu4}\n")

    # STATISTIQUE ET RAPPORT
    elif choix == "5":
        while True:
            print(f"{long}")    
            print(f"\n{menu5}")
            choix_stats = input(choix_menu)
            
            if choix_stats == "1":
                print(f"{short}\nRapport de la bibliothèque\n")
                for numero, livre in enumerate(biblio, 1):
                    print(f"{numero}. {livre['titre'].title()} écrit par {livre['auteur'].title()} | STATUT : {livre['statut']} | NOTE : {livre['note']} | CLIENT : {livre['client']}")
            
            elif choix_stats == "2":
                print(f"{short}\nTOP 3 des livres les mieux notés\n")
                decroissant = ("note")
                biblio.sort(key=lambda x: x['note'], reverse=decroissant)
                for numero, livre in enumerate(biblio[:3], 1):
                    print(f"{numero}. {livre['titre'].title()} écrit par {livre['auteur'].title()} | NOTE : {livre['note']}/5")
            
            elif choix_stats == "3":
                print(f"{short}\nStatistique générales\n")
                nb_total = len(biblio)
                nb_empruntes = 0
                nb_disponibles = 0
                somme_notes = 0
                for livre in biblio:
                    if livre["statut"] == "emprunté":
                        nb_empruntes += 1
                    else:
                        nb_disponibles += 1
                    somme_notes += int(livre["note"])
                    if nb_total > 0:
                        moyenne = somme_notes / nb_total
                    else:
                        moyenne = 0

                print(f"1. Nombre total de livres : {nb_total}")
                print(f"2. Livres disponibles     : {nb_disponibles}")
                print(f"3. Livres empruntés       : {nb_empruntes}")
                print(f"4. Note moyenne globale   : {moyenne:.1f}/5")

            elif choix_stats.lower == "r" or "R":
                print(f"\nRetour au menu principal")
                
                break

            else:
                print(f"\n{choix_inv} + {client.upper()}")
                print(f"\n{menu5}\n")

    # AJOUTER UN LIVRE DANS LA BIBLIOTHEQUE
    #{"titre": "  ", "auteur": "  ", "statut": "  ", "note": "  ", "client": "  "}
    elif choix == "6":
        while True:
            print(f"{long}") 
            print(f"\n{menu6}")
            choix_gestB = input(choix_menu)

            if choix_gestB == "1":
                print(f"{short}\nAjouter un livre\n")
                ajout_titre = input(f"\n{client.upper()}, quelle titre voulez-vous ajouter à la biliothèque : ").lower()
                ajout_auteur = input(f"\net identifier qui est l'auteur(autrice) : ").lower()
                nouveau_livre = {
                    "titre": ajout_titre, 
                    "auteur": ajout_auteur,
                    "statut": "disponible",
                    "note": 0,
                    "client": ""
                }
                biblio.append(nouveau_livre)
                print(f"\n{short}\nVotre nouveau livre {ajout_titre.title()} a été ajouté à la bibliothèque.\n{short}\n")
                for livre in list(biblio):
                    print("•", livre["titre"], "écrit par", livre["auteur"]," | ", "STATUT :", livre["statut"]," | ", "NOTE : ", livre["note"]," | ", "CLIENT : ", livre["client"])

            elif choix_gestB == "2":
                while True:
                    print(f"{short}\nRetirer un livre\n")
                    retrait_titre = input(f"\n{client.upper()}, quelle titre voulez-vous retirer de la biliothèque : ").lower()
                    index_trouve = None
                    for index, livre in enumerate(biblio):
                        if livre["titre"].lower() == retrait_titre:
                            index_trouve = index
                            break
                    if index_trouve is not None:
                        livre_retire = biblio.pop(index_trouve)
                        print(f"Le livre suivant : {livre_retire['titre'].upper()}, a été retiré de votre bibliothèque.")
                        break
                    else:
                        suggestion = None
                        for livre in biblio:
                            if retrait_titre in livre["titre"].lower():
                                suggestion = livre["titre"].lower()
                                break                        
                        if suggestion:
                            print(f"Le titre que vous recherchez est introuvable. Voulez-vous dire {suggestion.upper()} ?")
                        else:
                            print(f"Erreur : Le livre '{retrait_titre.upper()}' n'a pas été trouvé ni aucun titre ressemblant.")
            
            elif choix_gestB == "0":
                    print(f"{long}\nEffectuer un classement par : titre, auteur, statut, note ou client\n")
                    choix_tri = input(f"{client.upper()}, comment voulez-vous classer la bibliothèque ? ").lower()
                    cle_dispo = ["titre", "auteur", "statut", "note", "client"]

                    if choix_tri in cle_dispo:
                        decroissant = (choix_tri == "note")
                        biblio.sort(key=lambda x: x[choix_tri], reverse=decroissant)
                        print(f"{short}\nClassement par {choix_tri.upper()}\n")
                        for livre in biblio:
                                print("•", livre["titre"], "écrit par", livre["auteur"]," | ", "STATUT :", livre["statut"]," | ", "NOTE : ", livre["note"]," | ", "CLIENT : ", livre["client"])
                    else:
                        print(choix_inv)

            elif choix_gestB.lower == "r" or "R":
                print(f"\nRetour au menu principal")
                break

            else:
                print(f"\n{choix_inv} + {client.upper()}")
                print(f"\n{menu6}\n")


    # QUITTER
    elif choix.lower == "q" or "Q":
        print(quitter)
        exit()
        break

    else:
        print(f"\n{choix_inv} + {client.upper()}")
        print(f"\n{menu1}\n")





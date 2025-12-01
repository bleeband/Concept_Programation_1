# Présentation du TP 1 - Cour concept de programation 1
# Réalisé par Marc-André Dufour

# DECLARATION DES VARIABLES
hp = "Harry Potter"
resume_session = []
short = "-----------------------------------------------------"     
long = "-------------------------------------------------------------------------------------------------------------------" # J'ai apprit maintenant à utiliser => long = "-" * 50

# MENU
menu1 = f"   MENU      -->  1.  Afficher la bibliothèque  2.  Rechercher un titre de livre   3.  Vérifier le statut\nPRINCIPAL    -->  4.  Gestion des livres   5.  Statistique  6.  Gestion de la bibliothèque  Q.  Quitter"
menu2 = "RECHERCHE -->  1. Par titre  2. Par auteur  3.  Mix titre et/ou auteur  4.  Combinée titre et auteur  R.  Retour au menu principal"
menu3 = "STATUT -->  1. Disponible  2. Emprunté  R.  Retour au menu principal"
menu4 = "GESTION LIVRE -->  1.  Emprunt  2.  Retour  R.  Retour au menu principal"
menu5 = "STATISTIQUE -->  1.  Rapport blibliothèque  2.  Top 3  3.  Livre coup de coeur  4.  Liste ordonnée  5.  Statistiques générales   R.  Retour au menu principal"
menu6 = "GESTION BIBLIO -->  1.  Ajout d'un livre  2.  Retrait d'un livre  R.  Retour au menu principal"

# BIBLIOTHEQUE (format DICT)      *** TP PARTIE 1 - STOCKAGE ***
biblio = [
    {"titre": f"{hp} 1 : L'École des soriers", "auteur": "JK Rowling", "statut": "disponible", "note": "5", "client": "", "nbemprunt" : 8},
    {"titre": f"{hp} 2 : La chambre des secrets", "auteur": "JK Rowling", "statut": "disponible", "note": "4", "client": "", "nbemprunt" : 6},
    {"titre": f"{hp} 3 : Le Prisonnier d'Azkaban", "auteur": "JK Rowling", "statut": "emprunté", "note": "3", "client": "Mathis", "nbemprunt" : 2},
    {"titre": f"{hp} 4 : La coupe de feu", "auteur": "JK Rowling", "statut": "disponible", "note": "3", "client": "", "nbemprunt" : 2},
    {"titre": f"{hp} 5 : L'ordre du Phénix", "auteur": "JK Rowling", "statut": "disponible", "note": "4", "client": "", "nbemprunt" : 4},
    {"titre": f"{hp} 6 : Le prince de sang-mêlé", "auteur": "JK Rowling", "statut": "disponible", "note": "3", "client": "", "nbemprunt" : 3},
    {"titre": f"{hp} et Les reliques de la mort", "auteur": "JK Rowling", "statut": "disponible", "note": "4", "client": "", "nbemprunt" : 5},
    {"titre": "1984", "auteur": "George Orwell", "statut": "emprunté", "note": "5", "client": "Marc", "nbemprunt" : 11},
    {"titre": "La Moufette qui pet", "auteur": "Richard Petit", "statut": "emprunté", "note": "3", "client": "123", "nbemprunt" : 5},
    {"titre": "Le lutin cretin", "auteur": "Richard Petit", "statut": "emprunté", "note": "3", "client": "123", "nbemprunt" : 2},
    {"titre": "2020 l'odysee de l'espace", "auteur": "Jules Vernes", "statut": "disponible", "note": "0", "client": "", "nbemprunt" : 0},
    {"titre": "Le code civil du quebec", "auteur": "Badoin, Renaud", "statut": "disponible", "note": "1", "client": "", "nbemprunt" : 1},
    {"titre": "test", "auteur": "test", "statut": "disponible", "note": "0", "client": "", "nbemprunt" : 0}
]

# IDENTIFICATION DE L'USAGER
print(f"\n{long}\nLOGICIEL DE GESTION BIBLIOTHÈQUE\n{long}\n")
client_iden = input("Bonjour ! pour débuter, veuillez vous identifier : ")
client = client_iden
print(f"\n{long}\nBienvenue dans la MAD o thèque personnelle, {client.upper()} !")

# MESSAGE
quitter = (f"\n{long}\n\nMerci {client.upper()}, à la prochaine ! Au plaisir de vous revoir bientôt !!!\n{long}")
choix_inv = "Choix invalide, veuillez recommencer"
choix_menu = "\nVeuillez faire un choix parmi le menu : "

# *************** DEBUT APPLICATION ***************
while True:
    print(f"{long}")
    print(f"\n{menu1}")
    choix = input(choix_menu)

    # AFFICHER LA BIBLIOTHEQUE      *** TP PARTIE 1 - LISTE***
    if choix == "1":
        print(f"{short}\nVoici le contenu de ma biblio :\n")
        for livre in list(biblio):
            print("•", livre["titre"], "écrit par", livre["auteur"])
        print()

    # RECHERCHE PERSONNALISÉ DANS LA BIBLIOTHEQUE      *** TP PARTIE 2 *** DEFI 2 ***
    elif choix == "2":
        while True:
            print(f"{long}")
            print(f"\n{menu2}")
            choix_recherche = input(choix_menu)
            resul_recher = False

            # RECHERCHE PAR TITRE      *** TP PARTIE 2 - RECHERCHE PAR TITRE ***
            if choix_recherche == "1":
                print(f"\n{short}\nEffectuer une recherche par titre")
                rech_titre = input(f"\n{client.upper()}, quelle titre recherchez-vous : ").lower()
                print(f"\nVoici le résultat de la recherche contenent ==> {rech_titre.upper()}\n")
                for livre in biblio:
                    if rech_titre in livre["titre"].lower():
                        print("•", livre["titre"], "écrit par", livre["auteur"])
                        resul_recher = True

            # RECHERCHE PAR NOM D'AUTEUR      *** TP PARTIE 2 - RECHERCHE PAR AUTEUR ***
            elif choix_recherche == "2":
                print(f"\n{short}\nEffectuer une recherche par nom d'auteur")
                rech_auteur = input(f"\n{client.upper()}, quelle auteur recherchez-vous : ").lower()
                print(f"{short}\nVoici le résultat de la recherche contenent ==> {rech_auteur.upper()} \n")
                for livre in biblio:
                    if rech_auteur in livre["auteur"].lower():
                        print("•", livre["titre"], "écrit par", livre["auteur"],)
                        resul_recher = True

            # RECHERCHE PAR TITRE ET/OU NOM D'AUTEUR
            elif choix_recherche == "3":
                print(f"\n{short}\nEffectuer une recherche par titre et/ou nom d'auteur")
                rech_mix = input(f"\n{client.upper()}, quelle titre OU auteur recherchez-vous : ").lower()                 # UTILISER "or" pour sorcier et Orwell
                print(f"{short}\nVoici le résultat de la recherche mix (et/ou) contenent ==> {rech_mix.upper()}\n")
                for livre in biblio:
                    if (rech_mix in livre["titre"].lower()) or (rech_mix in livre["auteur"].lower()):
                        print("•", livre["titre"], "écrit par", livre["auteur"],)
                        resul_recher = True
            
            # RECHERCHE PAR TITRE ET NOM D'AUTEUR       ***  DEFI 2 - RECHERCHRE COMBINÉE***
            elif choix_recherche == "4":
                print(f"\n{short}\nEffectuer une recherche par titre et nom d'auteur")
                rech_titre = input(f"\n{client.upper()}, quelle titre recherchez-vous : ").lower()
                rech_auteur = input(f"\n{client.upper()}, quelle est le nom de l'auteur : ").lower()
                print(f"{short}\nVoici le résultat de la recherche mix et/ou contenent ==> {rech_titre.upper()} écrit par {rech_auteur.upper()}\n")
                for livre in biblio:
                    if (rech_titre in livre["titre"].lower()) and (rech_auteur in livre["auteur"].lower()):
                        print("•", livre["titre"], "écrit par", livre["auteur"],)
                        resul_recher = True

            if not resul_recher:
                print(f"\nAucune correspondance trouvée dans la bibliothèque.\n")

            elif choix_recherche.lower() == "r" or "R":
                print(f"\nRetour au menu principal")
                break

            else:
                print(f"\n{choix_inv} + {client.upper()}")
                print(f"\n{menu2}\n")

    # AFFICHER LA DISPONIBILITE DES LIVRES      *** TP PARTIE 1 ***
    elif choix == "3":
        while True:
            print(f"{long}")    
            print(f"\n{menu3}")
            choix_statut = input(choix_menu)
            
            # DISPONIBLE      *** TP PARTIE 1 - STATUT DISPONIBLE ***      *** TP PARTIE 2 - LIVRES EMPRUNTÉS ***
            if choix_statut == "1":
                livres_dispo = [livre for livre in biblio if livre["statut"] == "disponible"]

                nb_dispo = len(livres_dispo)      #*** TP PARTIE 2 - COMPTAGE DES LIVRES ***
                livres_disponibles = nb_dispo
                print(f"\n{short}\nNombre de livres disponible présentement : {livres_disponibles}\n")

                for livre in biblio:
                    if livre["statut"].lower() == "disponible":
                        print("•", livre["titre"], "écrit par", livre["auteur"])
                print()
                break

            # EMPRUNTÉ
            elif choix_statut == "2":
                livres_empr = [livre for livre in biblio if livre["statut"] == "emprunté"]

                nb_empr = len(livres_empr)      #*** TP PARTIE 2 - COMPTAGE DES LIVRES ***
                livres_emprunté = nb_empr
                print(f"\n{short}\nNombre de livres emprunté présentement : {livres_emprunté}\n")

                for livre in biblio:
                    if livre["statut"].lower() == "emprunté":
                        print("•", livre["titre"], "écrit par", livre["auteur"],)
                print()
                break

            elif choix_statut.lower() == "r":
                print(f"\nRetour au menu principal")
                break   

            else:
                print(f"\n{choix_inv} + {client.upper()}")
                print(f"\n{menu3}\n")
    
    # GESTION DES EMPRUNT ET RETOUR      *** TP PARTIE 3  ***
    # (utilisateur "123" a 2 livres empruntés)
    elif choix == "4":
        while True:
            print(f"{long}")    
            print(f"\n{menu4}")
            choix_gestL = input(choix_menu)
            livre_trouve = False

            # VERIFIER DE LA LIMITE DE 2 LIVRES MAX      *** TP PARTIE 3 - VERIFIER LIMITES ***
            if choix_gestL == "1":

                # COMPTER LES EMPRUNTS DU CLIENT ET CREER UNE LISTE
                nb_emprunts = 0
                liste_emprunt = []
                # VERIFIER SI CLIENT A DEJA UN LIVRE ET ON LISTE
                for livre in list(biblio):
                    if livre["client"].lower() == client.lower():
                        nb_emprunts += 1
                        liste_emprunt.append(livre["titre"])

                # VERIFIER LIMITE ATTEINTE      *** TP PARTIE 3 - VERIFIER LIMITES ***
                if nb_emprunts >= 2:
                    print(f"{long}\n\nDésolé {client.upper()}, vous avez atteint la limite de {nb_emprunts} livres en votre possession.\n")
                    for titre_a_rendre in liste_emprunt:
                        print(f"• {titre_a_rendre.title()}")
                    print("\nVeuillez retourner un livre avant de pouvoir refaire un emprunt.")
                
                else:
                    # AFFICHAGE DES LIVRES DIPONIBLES
                    print(f"\n{long}\n")
                    print(f"Liste des livres disponible à l'emprunt\n")                    
                    for livre in biblio:
                        if livre["statut"].lower() == "disponible":
                            print("•", livre["titre"], "écrit par", livre["auteur"],)
                    print(f"\n{long}\n")

                # GESTION DE L'EMPRUNT      *** TP PARTIE 3 - EMPRUNTER UN LIVRE ***
                livre_a_emprunter = input(f"{client.upper()}, quelle titre voulez-vous emprunter : ").lower()
                print(f"\n{short}\nVerification de la disponibilité de {livre_a_emprunter}....\n")

                for livre in biblio:        #      *** TP PARTIE 3 - VERIFICATION DE DISPONIBILITÉ EMPRUNT ***
                    if livre["titre"].lower() == livre_a_emprunter.lower():
                        livre_trouve = True
                        if livre["statut"] == "disponible":
                            livre["statut"] = "emprunté"
                            livre["client"] = client
                            resume_session.append(f"Emprunt du livre : {livre['titre'].title()}")      # *** DEFI 3 - SAUVEGARDE DONNÉES ***
                            print(f"\n{client.upper()}, vous avez emprunté {livre['titre'].upper()}\n")
                        
                        elif livre["statut"] == "emprunté":
                            print(f"{short}\nLe livre {livre['titre'].upper()} n'est pas disponible pour le moment.")
                        break 

                if not livre_trouve:
                    print(f"{short}\nLe livre {livre['titre'].upper()} n'est pas disponible dans ma bibliothèque.")

            elif choix_gestL == "2":

                # AFFICHAGE DES LIVRES EMPRUNTÉ PAR LE CLIENT
                print(f"\n{short}\n")
                print(f"Liste de vos livres à retourner\n")
                livre_emprunter = False
                
                for livre in biblio:
                    if livre["client"].lower() == client.lower():
                        print("•", livre["titre"])
                        livre_emprunter = True

                if not livre_emprunter:
                        print("Vous n'avez aucun livre à retourner.")
                
                else:  
                    # GESTION DU RETOUR      *** TP PARTIE 3 - RETOURNER UN LIVRE ***
                    print(f"\n{short}\n") 
                    livre_a_retourner = input(f"{client.upper()}, quelle titre voulez-vous retourner : ").lower()
                    print(f"\nRETOUR DU LIVRE {livre_a_retourner.title()}\n")
                    livre_trouve = False

                    for livre in biblio:        #      *** TP PARTIE 3 - VERIFICATION DE DISPONIBILITÉ RETOUR ***
                        if livre["titre"].lower() == livre_a_retourner.lower():
                            livre_trouve = True
                            if livre["statut"] == "emprunté":
                                nouvelle_note = input(f"Veuillez noter votre livre sur une note de 1 à 5 ★ : ")
                                if nouvelle_note.isdigit():
                                    livre["note"] = int(nouvelle_note)
                                else:
                                    livre["note"] = 0
                                livre["statut"] = "disponible"
                                livre["client"] = ""
                                resume_session.append(f"Retour du livre : {livre['titre'].title()} que vous avez noté {nouvelle_note} ★")      # *** DEFI 3 - SAUVEGARDE DONNÉES ***
                                print(f"\n{short}\n{client.upper()}, vous avez retourné et noté {livre['titre'].upper()}")
                                
                            elif livre["statut"] == "disponible":
                                print(f"{short}\nLe livre {livre['titre'].upper()} est déjà dans la bibliothèque.\n")
                            break 
    
                    if not livre_trouve:
                        print(f"{short}\nLe livre {livre_a_retourner.upper()} n'est pas disponible dans ma bibliothèque.\n")

            elif choix_gestL.lower() == "r":
                print(f"\nRetour au menu principal")
                break

            else:
                print(f"\n{choix_inv} + {client.upper()}")
                print(f"\n{menu4}\n")

    # STATISTIQUE ET RAPPORT      *** TP PARTIE 4 ***
    elif choix == "5":
        while True:
            print(f"{long}")    
            print(f"\n{menu5}")
            choix_stats = input(choix_menu)
            
                # AFFICHAGE LISTE NUMEROTÉE      *** TP PARTIE 4 - LISTE NUMÉROTÉE ***
            if choix_stats == "1":
                print(f"{short}\nRapport de la bibliothèque\n")
                for numero, livre in enumerate(biblio, 1):
                    print(f"{numero}. {livre['titre'].title()} écrit par {livre['auteur'].title()} | STATUT : {livre['statut']} | NOTE : {livre['note']} | CLIENT : {livre['client']} | SORTIE : {livre['nbemprunt']}")
                print()
                
                # AFFICHAGE DES 3 LIVRES LES PLUS EMPRUNTÉ      *** TP PARTIE 4 - TOP 3 ***
            elif choix_stats == "2":
                print(f"{short}\nTOP 3 des livres les plus emprunté\n")
                biblio.sort(key=lambda x: int(x['nbemprunt']), reverse=True)
                for numero, livre in enumerate(biblio[:3], 1):
                    print(f"{numero}. {livre['titre'].title()} écrit par {livre['auteur'].title()} | NOTE : {livre['note']} | SORTIE : {livre['nbemprunt']}")
                print()

                # AFFICHAGE COUP DE COEUR   *** DEFI 1 - liste 4★ et 5★ ***
            elif choix_stats == "3":    
                print(f"{short}\nLivres COUP DE CŒUR 4 et 5 ★\n")
                livres_top = [livre for livre in biblio if int(livre["note"]) >= 4]
                livres_top.sort(key=lambda x: int(x["note"]), reverse=True)

                if not livres_top:
                    print(f"Aucun livre n'a encore reçu de note de 4 ou 5.")
                else:
                    for livre in livres_top:
                        note_actuelle = int(livre["note"])
                        etoiles = "★ " * note_actuelle
                        nb_sorties = livre.get("nbemprunt", 0)                         
                        print(f"• NOTE : {etoiles} | {livre['titre'].title()} ecrit par ({livre['auteur'].title()}) | SORTIE : {livre['nbemprunt']} fois")
                # print(f"{short}\nLivres COUP DE CŒUR 4 et 5 ★\n")
                # meilleur_livre = 0
                # for livre in biblio:
                #     note_actuelle = int(livre["note"])
                #     if note_actuelle >= 4:
                #         meilleur_livre += 1
                #         etoiles = "★ " * note_actuelle
                #         print(f"• NOTE : {etoiles} | {livre['titre'].title()} ecrit par ({livre['auteur'].title()}) | SORTIE : {livre['nbemprunt']} fois")
                # print()
                # if meilleur_livre == 0:
                #     print("Aucun livre n'a encore reçu de note de 4 ou 5.")

                # CLASSEMENT ORDONNÉE
            elif choix_stats == "4":
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

                # SECTION CALCUL   *** TP PARTIE 4 *** DEFI 1 ***
            elif choix_stats == "5":
                print(f"{short}\nStatistique générales\n")
                nb_total = len(biblio)
                nb_empruntes = 0
                nb_disponibles = 0
                nb_total_pret = 0
                somme_notes = 0

                # CALCUL DES STATS      *** TP PARTIE 4 - STATISTIQUES GENERALES ***
                for livre in biblio:
                    if livre["statut"] == "emprunté":
                        nb_empruntes += 1
                    else:
                        nb_disponibles += 1
                    somme_notes += int(livre["note"])
                    nb_total_pret += int(livre["nbemprunt"])

                if nb_total > 0:
                    moyenne = somme_notes / nb_total        #   *** DEFI 1 - NOTE MOYENNE ***
                else:
                    moyenne = 0

                print(f"1. Nombre total de livres : {nb_total}")
                print(f"2. Livres disponibles     : {nb_disponibles}")
                print(f"3. Livres empruntés       : {nb_empruntes}")
                print(f"4. Nombre total de prèt   : {nb_total_pret}")                
                print(f"5. Note moyenne globale   : {moyenne:.1f}★/5\n")       #   *** DEFI 1 - NOTE MOYENNE ***
                
            elif choix_stats.lower() == "r":
                print(f"\nRetour au menu principal")
                break

            else:
                print(f"\n{choix_inv} + {client.upper()}")
                print(f"\n{menu5}\n")

    # AJOUTER UN LIVRE DANS LA BIBLIOTHEQUE
    #{"titre": "  ", "auteur": "  ", "statut": "  ", "note": "  ", "client": "  ", "nbemprunt": " "}
    elif choix == "6":
        while True:
            print(f"{long}") 
            print(f"\n{menu6}")
            choix_gestB = input(choix_menu)

            if choix_gestB == "1":
                print(f"{short}\nAjouter un livre")
                ajout_titre = input(f"\n{client.upper()}, quelle titre voulez-vous ajouter à la biliothèque : ").lower()
                ajout_auteur = input(f"\net veuillez identifier qui est l'auteur(autrice) : ").lower()
                nouveau_livre = {
                    "titre": ajout_titre, 
                    "auteur": ajout_auteur,
                    "statut": "disponible",
                    "note": 0,
                    "client": "",
                    "nbemprunt": 0,
                }

                biblio.append(nouveau_livre)
                resume_session.append(f"Ajout du livre : {livre['titre'].title()} ecrit par {livre['auteur'].title()}")
                print(f"\n{short}\nVotre nouveau livre {ajout_titre.title()} ecrit par {livre['auteur'].title()} a été ajouté à la bibliothèque.\n{short}\n")

                for livre in list(biblio):
                    print("•", livre["titre"], "écrit par", livre["auteur"]," | ", "STATUT :", livre["statut"]," | ", "NOTE : ", livre["note"]," | ", "CLIENT : ", livre["client"," | ", "SORTIE : ", livre["nbemprunt"]])

            elif choix_gestB == "2":
                while True:
                    print(f"{short}\nRetirer un livre")
                    retrait_titre = input(f"\n{client.upper()}, quelle titre voulez-vous retirer de la biliothèque : ").lower()
                    index_trouve = None
                    for index, livre in enumerate(biblio):
                        if livre["titre"].lower() == retrait_titre:
                            index_trouve = index
                            break

                    if index_trouve is not None:
                        livre_retire = biblio.pop(index_trouve)
                        resume_session.append(f"Retrait du livre : {livre['titre'].title()} ecrit par {livre['auteur'].title()}")
                        print(f"Le livre suivant : {livre_retire['titre'].upper()} ecrit par {livre['auteur'].title()}, a été retiré de votre bibliothèque.")
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
                            print(f"\nLa recherche de {retrait_titre.upper()} ne semble pas appartenir à la bibliothèque ni aucune de ses ressemblance.")

            elif choix_gestB.lower() == "r":
                print(f"\nRetour au menu principal")
                break

            else:
                print(f"\n{choix_inv} + {client.upper()}")
                print(f"\n{menu6}\n")

    # QUITTER       *** DEFI 3 - Exporter un resumé
    elif choix.lower() == "q":

        if len(resume_session) == 0:
            print(f"{short}\n\nAucune donnée n'a été enregistrée durant cette session.")
        
        else:
            print(f"{short}\n\nRÉSUMÉ DE LA SESSION DE {client.upper()} :\n\n")
            
            for d, donnee in enumerate(resume_session, 1):
                print(f"{d}. {donnee}")
            
            print(f"\nNombre total d'actions effectuées : {len(resume_session)}")

        print(quitter)
        break
    
    # LOOP
    else:
        print(f"\n{choix_inv} + {client.upper()}")
        print(f"\n{menu1}\n")





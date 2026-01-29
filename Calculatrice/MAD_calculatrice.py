

# Objectif : Créer une calculatrice simple en Python avec une gestion robuste des erreurs à l'aide des exceptions.

# Énoncé de l'exercice
# Vous devez créer une calculatrice interactive qui permet à l'utilisateur d'effectuer des opérations mathématiques de base : addition, soustraction, multiplication et division.

# La calculatrice doit :

# Afficher un menu des opérations disponibles  OK
# Demander à l'utilisateur de choisir une opération     OK
# Demander deux nombres à l'utilisateur     OK
# Afficher le résultat de l'opération       OK
# Gérer proprement les erreurs à l'aide d'exceptions        OK
# Spécifications détaillées :
    # Opérations disponibles :

    # Addition (+)      OK
    # Soustraction (-)      OK
    # Multiplication (*)     OK
    # Division (/)      OK

# Gestion des exceptions :

    # Si l'utilisateur entre un choix d'opération invalide, afficher un message d'erreur      OK
    # Si l'utilisateur entre une valeur non numérique, afficher un message d'erreur         OK
    # Si l'utilisateur tente une division par zéro, afficher un message d'erreur        OK

# Fonctionnement :

    # La calculatrice continue de fonctionner jusqu'à ce que l'utilisateur décide de quitter
    # Après chaque calcul, proposer à l'utilisateur de continuer ou de quitter

# Structure suggérée:  voici un squelette de code pour aider vos étudiants à démarrer :

def calculatrice():
    
    print("\n=== CALCULATRICE SIMPLE ===")

    while True:
            print("\nOpérations disponibles :")
            print("1. Addition (+)")
            print("2. Soustraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Modulo (%)")
            print("6. Puissance (**)")            
            print("Q. Quitter")

            try:
                choix_menu = input("Veuillez faire votre choix : ").lower()

                if choix_menu == "q":
                    print("Merci ! Au revoir !")
                    break

                choix_menu = int(choix_menu)

                if choix_menu not in [1, 2, 3, 4, 5, 6]:
                    raise ValueError("Veuillez faire un choix parmi le menu")
                
                try:
                    nbr_un = float(input("Entrez votre premier nombre : "))
                    nbr_deux = float(input("Entrez votre deuxième nombre : "))
                except ValueError:
                    raise ValueError("Veuillez entrer un nombre valide")

                if choix_menu == 1:
                    resultat = nbr_un + nbr_deux
                    operateur = "+"

                elif choix_menu == 2:
                    resultat = nbr_un - nbr_deux
                    operateur = "-"

                elif choix_menu == 3:
                    resultat = nbr_un * nbr_deux
                    operateur = "*"

                elif choix_menu == 4:
                    if nbr_deux == 0:
                        raise ZeroDivisionError("Attention : division par zéro interdite")
                    resultat = nbr_un / nbr_deux  # peut lever ZeroDivisionError
                    operateur = "/"

                elif choix_menu == 5:
                    resultat = nbr_un % nbr_deux
                    operateur = "%"

                elif choix_menu == 6:
                    resultat = nbr_un ** nbr_deux
                    operateur = "**"

                print(f"Résultat : {nbr_un} {operateur} {nbr_deux} = {resultat}")

            except ValueError as ve:
                print(f"Erreur : {ve}")

            except ZeroDivisionError as zde:
                print(f"Erreur : {zde}")

            except Exception as e:
                print(f"Erreur inattendue : {e}")

            continuer = input("\nOn continu ? (o/n) : ").lower()
            if continuer != "o":
                print("Merci ! Au revoir !")
                break

calculatrice()


# calculatrice()
# Questions pour vous guider
# Quelle exception est levée lorsque vous essayez de convertir en nombre une chaîne qui ne contient pas de nombre valide ?
    # int() -> ValueError

# Quelle exception est levée lorsque vous essayez de diviser par zéro ?
    # ZeroDivisionError

# Comment pouvez-vous gérer plusieurs types d'exceptions dans un même bloc try?
    # en creant des except

# Quelle est la différence entre except ValueError et except Exception ?
    # except ValueError : capture uniquement les erreurs de conversion ou de valeur incorrecte (par exemple "abc" → int).
    # except Exception : capture toutes les erreurs héritées de Exception, donc beaucoup plus général.

# Exemple d'exécution attendue
# === CALCULATRICE SIMPLE ===

# Opérations disponibles :
# 1. Addition (+)
# 2. Soustraction (-)
# 3. Multiplication (*)
# 4. Division (/)
# 5. Quitter
# Votre choix (1-5) : 1
# Entrez le premier nombre : 10
# Entrez le deuxième nombre : 5
# Résultat : 10 + 5 = 15

# Opérations disponibles :
# 1. Addition (+)
# 2. Soustraction (-)
# 3. Multiplication (*)
# 4. Division (/)
# 5. Quitter
# Votre choix (1-5) : 4
# Entrez le premier nombre : 10
# Entrez le deuxième nombre : 0
# Erreur : Division par zéro impossible!

# Opérations disponibles :
# 1. Addition (+)
# 2. Soustraction (-)
# 3. Multiplication (*)
# 4. Division (/)
# 5. Quitter
# Votre choix (1-5) : 6
# Erreur : Choix invalide. Veuillez entrer un nombre entre 1 et 5.

# Opérations disponibles :
# 1. Addition (+)
# 2. Soustraction (-)
# 3. Multiplication (*)
# 4. Division (/)
# 5. Quitter
# Votre choix (1-5) : 2
# Entrez le premier nombre : abc
# Erreur : Veuillez entrer un nombre valide.
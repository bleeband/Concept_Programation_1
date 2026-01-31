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

# --------------------------------------------------------------------------------------------------
under = "\033[4m"
red = "\033[31m"
end = "\033[0m"
question = "\033[30m"
rep = "\033[36m"

def calculatrice():
    
    print(f"\n=== {under}CALCULATRICE SIMPLE{end} ===")

    while True:
            print(f"\n{under}Opérations disponibles{end} :\n")
            print("     1. Addition (+)")
            print("     2. Soustraction (-)")
            print("     3. Multiplication (*)")
            print("     4. Division (/)")
            print("     5. Modulo (%)")
            print("     6. Puissance (**)")            
            print("     Q. Quitter")

            try:
                choix_menu = input("\nVeuillez faire votre choix : ").lower()

                if choix_menu == "q":
                    print("Merci ! Au revoir !")
                    break

                choix_menu = int(choix_menu)

                if choix_menu not in [1, 2, 3, 4, 5, 6]:
                    raise ValueError(f"{red}Veuillez faire un choix parmi le menu{end}")
                
                try:
                    nbr_un = float(input("Entrez votre premier nombre : "))
                    nbr_deux = float(input("Entrez votre deuxième nombre : "))
                except ValueError:
                    raise ValueError(f"{red}Veuillez entrer un nombre valide{end}")
                
                operateur = str ; resultat = int
                
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
                        raise ZeroDivisionError("{red}Attention : division par zéro interdite{end}")
                    resultat = nbr_un / nbr_deux
                    operateur = "/"

                elif choix_menu == 5:
                    resultat = nbr_un % nbr_deux
                    operateur = "%"

                elif choix_menu == 6:
                    resultat = nbr_un ** nbr_deux
                    operateur = "**"

                print(f"Résultat : {int(nbr_un)} {operateur} {int(nbr_deux)} = {resultat:.2f}")

            except ValueError as ve:
                print(f"{red}Erreur : {ve}{end}")

            except ZeroDivisionError as zde:
                print(f"{red}Erreur : {zde}{end}")

            except Exception as e:
                print(f"{red}Erreur inattendue : {e}{end}")

            continuer = input("\nVoulez-vous continuer ? \033[1m(o/n){end} : ").lower()
            if continuer != "o":
                print("\nMerci ! Au revoir !\n")
                break

calculatrice()

print(
"""
\033[30mQuelle exception est levée lorsque vous essayez de convertir en nombre une chaîne qui ne contient pas de nombre valide ?{end}
    
    \033[36m- int() -> ValueError{end}

\033[30mQuelle exception est levée lorsque vous essayez de diviser par zéro ?{end}
    
    \033[36m- ZeroDivisionError{end}

\033[30mComment pouvez-vous gérer plusieurs types d'exceptions dans un même bloc try ?{end}
    
    \033[36m- en creant des except{end}

\033[30mQuelle est la différence entre except ValueError et except Exception ?{end}
    
    \033[36m- except ValueError : capture uniquement les erreurs de conversion ou de valeur incorrecte (par exemple "abc" → int).{end}
    
    \033[36m- except Exception : capture toutes les erreurs héritées de Exception, donc beaucoup plus général.{end} """)
def calculatrice():
    print("\n=== CALCULATRICE SIMPLE ===")

    # Dictionnaire des opérations
    operations = {
        1: ("+", lambda x, y: x + y),
        2: ("-", lambda x, y: x - y),
        3: ("*", lambda x, y: x * y),
        4: ("/", lambda x, y: x / y),
        5: ("%", lambda x, y: x % y),
        6: ("**", lambda x, y: x ** y)
    }

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

            if choix_menu not in operations:
                raise ValueError("Veuillez faire un choix parmi le menu")

            nbr_un = float(input("Entrez votre premier nombre : "))
            nbr_deux = float(input("Entrez votre deuxième nombre : "))

            operateur, fonction = operations[choix_menu]

            resultat = fonction(nbr_un, nbr_deux)

            print(f"Résultat : {nbr_un} {operateur} {nbr_deux} = {resultat}")

        except ValueError as ve:
            print(f"Erreur : {ve}")

        except ZeroDivisionError:
            print("Erreur : division ou modulo par zéro interdit")

        except Exception as e:
            print(f"Erreur inattendue : {e}")

        continuer = input("\nOn continue ? (o/n) : ").lower()
        if continuer != "o":
            print("Merci ! Au revoir !")
            break


calculatrice()
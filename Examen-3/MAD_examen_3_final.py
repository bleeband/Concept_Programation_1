under = "\033[4m"
red = "\033[31m"
end = "\033[0m"

def format_nombre(n):
    """Affichage joli : si c'est un entier, pas de décimales"""
    return str(int(n)) if n == int(n) else f"{n:.2f}"

def operations_multiples(memories):
    """Gère les calculs avec plus de 2 nombres"""
    print(f"\n=== OPERATION MULTIPLE ===")
    operation = input("Veuillez sélectionner votre opération (+ - * /) : ")
    if operation not in ["+", "-", "*", "/"]:
        print(f"{red}Veuillez entrer un opérateur valide{end}")
        return None

    while True:
        try:
            nombre_nbr = int(input("Combien de nombres voulez-vous dans votre opération ? "))
            if nombre_nbr < 2:
                raise ValueError("Veuillez choisir au moins deux nombres")
            break
        except ValueError as ve:
            print(f"{red}Erreur : {ve}{end}")

    nombre = []
    for nb in range(nombre_nbr):
        while True:
            val = input(f"Entrez le nombre {nb+1} ou une mémoire (M1-M5) : ")
            val_upper = val.upper()
            if val_upper in memories and memories[val_upper] is not None:
                nombre.append(memories[val_upper])
                break
            else:
                try:
                    nombre.append(float(val))
                    break
                except ValueError:
                    print(f"{red}Erreur : entrez un nombre valide ou une mémoire existante{end}")

    resultat = nombre[0]
    for nb in nombre[1:]:
        if operation == "+": resultat += nb
        elif operation == "-": resultat -= nb
        elif operation == "*": resultat *= nb
        elif operation == "/":
            if nb == 0:
                print(f"{red}Division par zéro interdite{end}")
                return None
            resultat /= nb

    calcul_multi = f" {operation} ".join(format_nombre(n) for n in nombre)
    print(f"\nCalcul : {calcul_multi} = {format_nombre(resultat)}")
    return resultat

def gestion_memoire(memories, dernier_resultat):
    while True:
        print(f"\n{under}GESTION DE LA MÉMOIRE{end}\n")
        print("a. Stocker le dernier résultat")
        print("b. Afficher/Utiliser une mémoire")
        print("c. Afficher toutes les mémoires")
        print("d. Effacer une mémoire")
        print("e. Retour")

        choix_gestion = input("Votre choix : ").lower()

        if choix_gestion == "a":
            if dernier_resultat is None:
                print("Aucun résultat à stocker")
            else:
                mem = input("Dans quelle mémoire (M1-M5) ? ").upper()
                if mem in memories:
                    memories[mem] = dernier_resultat
                    print(f"{format_nombre(dernier_resultat)} stocké dans {mem}")
                else:
                    print("Mémoire invalide")

        elif choix_gestion == "b":
            print("\nMémoires disponibles :")
            for m, val in memories.items():
                print(f"{m}: {format_nombre(val) if val is not None else 'vide'}")
            mem = input("Quelle mémoire voulez-vous utiliser ? (juste pour info) ").upper()
            if mem in memories and memories[mem] is not None:
                print(f"Valeur de {mem} : {format_nombre(memories[mem])}")
            else:
                print(f"{red}Mémoire invalide ou vide{end}")

        elif choix_gestion == "c":
            print(f"\n{under}Mémoires actuelles{end}\n")
            for m, val in memories.items():
                print(f"{m}: {format_nombre(val) if val is not None else 'vide'}")

        elif choix_gestion == "d":
            mem = input("Quelle mémoire effacer (M1-M5 ou TOUTES) ? ").upper()
            if mem == "TOUTES":
                for m in memories:
                    memories[m] = None
                print("Toutes les mémoires effacées")
            elif mem in memories:
                memories[mem] = None
                print(f"{mem} effacée")
            else:
                print("Mémoire invalide")

        elif choix_gestion == "e":
            break
        else:
            print(f"{red}Choix invalide{end}")

def calculatrice():
    memories = {"M1": None, "M2": None, "M3": None, "M4": None, "M5": None}
    dernier_resultat = None

    print(f"\n=== {under}CALCULATRICE SIMPLE{end} ===")

    while True:
        print(f"\n{under}Opérations disponibles{end}\n")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulo (%)")
        print("6. Puissance (**)")
        print("7. Opérations multiples")
        print("8. Gestion de la mémoire")
        print("Q. Quitter")

        choix_menu = input("\nVotre choix : ").lower()
        if choix_menu == "q":
            print("Merci ! Au revoir !")
            break

        try:
            choix_menu = int(choix_menu)
        except ValueError:
            print(f"{red}Veuillez entrer un chiffre du menu ou Q pour quitter{end}")
            continue

        if choix_menu == 7:
            resultat = operations_multiples(memories)
            if resultat is not None:
                dernier_resultat = resultat
            continue

        if choix_menu == 8:
            gestion_memoire(memories, dernier_resultat)
            continue

        if choix_menu not in [1,2,3,4,5,6]:
            print(f"{red}Choix invalide du menu{end}")
            continue

        # Saisie des nombres (acceptant mémoires)
        nombres = []
        for i in range(2):
            while True:
                val = input(f"Entrez le nombre {i+1} ou une mémoire (M1-M5) : ")
                val_upper = val.upper()
                if val_upper in memories and memories[val_upper] is not None:
                    nombres.append(memories[val_upper])
                    break
                else:
                    try:
                        nombres.append(float(val))
                        break
                    except ValueError:
                        print(f"{red}Entrée invalide{end}")

        nbr_un, nbr_deux = nombres

        # Calcul selon le choix
        if choix_menu == 1: resultat = nbr_un + nbr_deux; operateur = "+"
        elif choix_menu == 2: resultat = nbr_un - nbr_deux; operateur = "-"
        elif choix_menu == 3: resultat = nbr_un * nbr_deux; operateur = "*"
        elif choix_menu == 4:
            if nbr_deux == 0:
                print(f"{red}Division par zéro interdite{end}")
                continue
            resultat = nbr_un / nbr_deux
            operateur = "/"
        elif choix_menu == 5: resultat = nbr_un % nbr_deux; operateur = "%"
        elif choix_menu == 6: resultat = nbr_un ** nbr_deux; operateur = "**"

        print(f"Résultat : {format_nombre(nbr_un)} {operateur} {format_nombre(nbr_deux)} = {format_nombre(resultat)}")
        dernier_resultat = resultat

        continuer = input(f"\nVoulez-vous continuer ? {red}(o/n){end} : ").lower()
        if continuer != "o":
            print("\nMerci ! Au revoir !\n")
            break

calculatrice()

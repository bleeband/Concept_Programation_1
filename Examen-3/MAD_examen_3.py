under = "\033[4m"
red = "\033[31m"
end = "\033[0m"

def operations_multiples(memories):    # Gère les calculs avec plus de 2 nombres

    print(f"\n=== OPERATION MULTIPLE")
    operation = input(f"\nVeuillez selectioner votre operation ( + - * / ) : ")

    if operation not in ["+", "-", "*", "/"]:
        print(f"{red}Veuillez entrer un opérateur valide{end}")
        return None
    
    try:
        nombre_nbr = int(input(f"\nCombien de nombre voulez-vous dans votre opération ? "))
        if nombre_nbr < 2:
            raise ValueError(f"{red}Veuillez choisir au moins deux nombres{end}")
        
    except ValueError as ve:
        print(f"{red}Erreur : {ve}{end}")
        return None
        
    # Pour gérer plusieurs nombres
    nombre = []
    for nb in range(nombre_nbr):
        while True:
            val = input(f"Entrer le nombre {nb+1} : ")
            if val.upper() in memories:
                if memories[val.upper()] is not None:
                    nombre.append(memories[val.upper()])
                    break
                else:
                    print(f"{val.upper()} est vide")
            else:
                try:
                    nombre.append(float(val))
                    break
                except ValueError as ve:
                    print(f"{red}Erreur : {ve}{end}")
                    return None

    resultat = nombre[0]

    for nb in nombre[1:]:
        if operation == "+":
            resultat += nb
        if operation == "-":
            resultat -= nb
        if operation == "*":
            resultat *= nb
        if operation == "/":
            if nb == 0:
                print(f"{red}Attention : division par zéro interdite{end}")
                return None
            resultat /= nb

    # Pour afficher le calcul
    calcul_multi = f" {operation} ".join(str(nbr) for nbr in nombre)
    print(f"\nCalcul : {calcul_multi} = {resultat}")

    return resultat
        
def gestion_memoire(memories, dernier_resultat):

    while True:
        print(f"\n{under}GESTION DE LA MÉMOIRE{end} :\n")
        print("     a. Stocker le dernier résultat")
        print("     b. Utiliser une mémoire dans un calcul")
        print("     c. Afficher toutes les mémoires")
        print("     d. Effacer une mémoire")
        print("     e. Retour")

        choix_gestion = input("\nVeuillez faire votre choix : ").lower()

        if choix_gestion == "a":
            if dernier_resultat is None:
                print("Aucun résultat à stocker")
            else:
                mem = input("Dans quelle mémoire (M1-M5) ? ").upper()
                if mem in memories:
                    memories[mem] = dernier_resultat
                    print(f"{dernier_resultat} stocké dans {mem}")
                else:
                    print("Mémoire invalide")

        elif choix_gestion == "b":
            for m, val in memories.items():
                print(f"{m} : {val if val is not None else 'vide'}")

        elif choix_gestion == "c": 
            print(f"\n{under}Mémoires actuelles : {end} :\n") 
            for m, val in memories.items(): 
                print(f"{m}: {val if val is not None else 'vide'}")

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

def calculatrice():
    memories = {"M1": None, "M2": None, "M3": None, "M4": None, "M5": None}  # Dictionnaire pour stocker les valeurs
    dernier_resultat = None
    
    print(f"\n=== {under}CALCULATRICE SIMPLE{end} ===")

    while True:
            print(f"\n{under}Opérations disponibles{end} :\n")
            print("     1. Addition (+)")
            print("     2. Soustraction (-)")
            print("     3. Multiplication (*)")
            print("     4. Division (/)")
            print("     5. Modulo (%)")
            print("     6. Puissance (**)")
            print("     7. Opérations multiples (+deNbr)")
            print("     8. Gestion de la mémoire")
            print("     Q. Quitter")

            try:
                operateur = str ; resultat = int

                choix_menu = input("\nVeuillez faire votre choix : ").lower()

                if choix_menu == "q":
                    print("Merci ! Au revoir !")
                    break

                choix_menu = int(choix_menu)
                
                if choix_menu == 7:
                    resultat = operations_multiples(memories)
                    if resultat is not None:
                        dernier_resultat = resultat
                    continue

                if choix_menu == 8:
                    gestion_memoire(memories, dernier_resultat)
                    continue

                if choix_menu not in [1, 2, 3, 4, 5, 6]:
                    raise ValueError(f"{red}Veuillez faire un choix parmi le menu{end}")
                
                try:
                    nbr_un = float(input("Entrez votre premier nombre : "))
                    nbr_deux = float(input("Entrez votre deuxième nombre : "))

                except ValueError:
                    raise ValueError(f"{red}Veuillez entrer un nombre valide{end}")
                
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
                        print(f"{red}Attention : division par zéro interdite{end}")
                        continue
                    resultat = nbr_un / nbr_deux
                    operateur = "/"

                elif choix_menu == 5:
                    resultat = nbr_un % nbr_deux
                    operateur = "%"

                elif choix_menu == 6:
                    resultat = nbr_un ** nbr_deux
                    operateur = "**"

                print(f"Résultat : {int(nbr_un)} {operateur} {int(nbr_deux)} = {resultat:.2f}")
                dernier_resultat = resultat


            except ValueError as ve:
                print(f"{red}Erreur : {ve}{end}")

            except ZeroDivisionError as zde:
                print(f"{red}Erreur : {zde}{end}")

            except Exception as e:
                print(f"{red}Erreur inattendue : {e}{end}")

            continuer = input(f"\nVoulez-vous continuer ? {red}(o/n){end} : ").lower()
            if continuer != "o":
                print("\nMerci ! Au revoir !\n")
                break

calculatrice()

def calcularice():
    """
    Fonction principale de la calculatrice améliorée
    """
    print("=== CALCULATRICE AMÉLIORÉE ===")

    # Variables pour la mémoire
    memories = {"M1": None, "M2": None, "M3": None, "M4": None, "M5": None}
    current_memory = "M1"
    dernier_resultat = None

    def afficher_memories():
        """Affiche toutes les mémoires"""
        print("\n=== MÉMOIRES ===")
        for key, value in memories.items():
            if value is None:
                print(f"{key}: vide")
            else:
                print(f"{key}: {value}")

    def utiliser_memoire():
        """Propose d'utiliser une mémoire et retourne la valeur"""
        afficher_memories()
        while True:
            choix = input("\nQuelle mémoire utiliser ? (M1-M5 ou 'a' pour annuler) : ").upper()
            if choix == 'A':
                return None
            if choix in memories:
                if memories[choix] is not None:
                    print(f"Utilisation de {choix} = {memories[choix]}")
                    return memories[choix]
                else:
                    print(f"La mémoire {choix} est vide!")
            else:
                print("Choix invalide. Entrez M1, M2, M3, M4, M5 ou 'a'")

    def operations_multiples():
        """Gère les opérations avec plusieurs nombres"""
        nonlocal dernier_resultat

        print("\n" + "="*40)
        print("OPÉRATIONS MULTIPLES")
        print("="*40)

        # Choix de l'opération
        while True:
            operation = input("\nOpération (+, -, *, /) : ").strip()
            if operation in ['+', '-', '*', '/']:
                break
            print("Erreur : Opération doit être +, -, * ou /")

        # Nombre d'opérandes
        while True:
            try:
                nb_nombres = int(input("Combien de nombres ? (minimum 2) : "))
                if nb_nombres >= 2:
                    break
                print("Erreur : Il faut au moins 2 nombres")
            except ValueError:
                print("Erreur : Entrez un nombre entier")

        # Saisie des nombres
        nombres = []
        for i in range(nb_nombres):
            while True:
                try:
                    # Proposition d'utiliser une mémoire
                    use_mem = input(f"\nPour le nombre {i+1}, utiliser une mémoire ? (o/n) : ").lower()
                    if use_mem == 'o':
                        mem_val = utiliser_memoire()
                        if mem_val is not None:
                            nombres.append(mem_val)
                            break
                        else:
                            continue

                    # Saisie normale
                    prompt = f"Entrez le nombre {i+1} : "
                    valeur = float(input(prompt))
                    nombres.append(valeur)
                    break

                except ValueError:
                    print("Erreur : Entrez un nombre valide")

        # Vérification pour la division
        if operation == '/' and 0 in nombres[1:]:
            print("Erreur : Division par zéro impossible")
            return None

        # Calcul
        if operation == '+':
            resultat = sum(nombres)
            operateur = " + "
        elif operation == '-':
            resultat = nombres[0]
            for n in nombres[1:]:
                resultat -= n
            operateur = " - "
        elif operation == '*':
            resultat = 1
            for n in nombres:
                resultat *= n
            operateur = " × "
        elif operation == '/':
            resultat = nombres[0]
            for n in nombres[1:]:
                resultat /= n
            operateur = " ÷ "

        # Affichage
        expression = operateur.join(str(n) for n in nombres)
        print(f"\n{'='*40}")
        print(f"RÉSULTAT : {expression} = {resultat}")
        print('='*40)

        dernier_resultat = resultat
        return resultat

    def gestion_memoire():
        """Gère le sous-menu de la mémoire"""
        nonlocal current_memory, dernier_resultat

        while True:
            print("\n" + "="*40)
            print(f"GESTION DE LA MÉMOIRE (Active: {current_memory})")
            print("="*40)
            print("a. Stocker le dernier résultat")
            print("b. Afficher toutes les mémoires")
            print("c. Effacer une mémoire")
            print("d. Effacer toutes les mémoires")
            print("e. Changer la mémoire active")
            print("f. Retour au menu principal")

            choix = input("\nVotre choix (a-f) : ").lower()

            if choix == 'a':  # Stocker résultat
                if dernier_resultat is None:
                    print("Aucun résultat à stocker ! Faites un calcul d'abord.")
                else:
                    memories[current_memory] = dernier_resultat
                    print(f"Résultat {dernier_resultat} stocké dans {current_memory}")

            elif choix == 'b':  # Afficher mémoires
                afficher_memories()

            elif choix == 'c':  # Effacer une mémoire
                afficher_memories()
                mem = input("\nQuelle mémoire effacer ? (M1-M5) : ").upper()
                if mem in memories:
                    memories[mem] = None
                    print(f"Mémoire {mem} effacée")
                else:
                    print("Mémoire invalide")

            elif choix == 'd':  # Effacer toutes
                confirmation = input("Êtes-vous sûr ? (o/n) : ").lower()
                if confirmation == 'o':
                    for key in memories:
                        memories[key] = None
                    print("Toutes les mémoires effacées")

            elif choix == 'e':  # Changer mémoire active
                afficher_memories()
                while True:
                    new_mem = input("\nNouvelle mémoire active (M1-M5) : ").upper()
                    if new_mem in memories:
                        current_memory = new_mem
                        print(f"Mémoire active changée à {current_memory}")
                        break
                    else:
                        print("Mémoire invalide. Choisissez M1 à M5")

            elif choix == 'f':  # Retour
                break

            else:
                print("Choix invalide. Entrez a, b, c, d, e ou f")

    def demander_nombre(prompt, allow_memory=True):
        """Demande un nombre avec option d'utiliser une mémoire"""
        while True:
            if allow_memory:
                use_mem = input(f"\n{prompt} - Utiliser une mémoire ? (o/n) : ").lower()
                if use_mem == 'o':
                    mem_val = utiliser_memoire()
                    if mem_val is not None:
                        return mem_val

            try:
                valeur = float(input(prompt + " : "))
                return valeur
            except ValueError:
                print("Erreur : Entrez un nombre valide")

    # Boucle principale
    while True:
        print("\n" + "="*40)
        print("MENU PRINCIPAL")
        print("="*40)
        print("1. Addition (+) [2 nombres]")
        print("2. Soustraction (-) [2 nombres]")
        print("3. Multiplication (*) [2 nombres]")
        print("4. Division (/) [2 nombres]")
        print("5. Opérations multiples (+, -, *, /)")
        print("6. Gestion de la mémoire")
        print("7. Quitter")

        try:
            choix = input("\nVotre choix (1-7) : ")

            if choix == '7':
                print("\nMerci d'avoir utilisé la calculatrice améliorée. Au revoir !")
                break

            # Opérations avec 2 nombres
            if choix in ['1', '2', '3', '4']:
                print(f"\n=== OPÉRATION À 2 NOMBRES ===")

                # Premier nombre
                num1 = demander_nombre("Entrez le premier nombre")

                # Deuxième nombre
                num2 = demander_nombre("Entrez le deuxième nombre")

                # Calcul
                if choix == '1':  # Addition
                    resultat = num1 + num2
                    operateur = "+"
                elif choix == '2':  # Soustraction
                    resultat = num1 - num2
                    operateur = "-"
                elif choix == '3':  # Multiplication
                    resultat = num1 * num2
                    operateur = "×"
                elif choix == '4':  # Division
                    if num2 == 0:
                        raise ZeroDivisionError("Division par zéro impossible !")
                    resultat = num1 / num2
                    operateur = "÷"

                # Affichage et stockage
                print(f"\n{'='*40}")
                print(f"RÉSULTAT : {num1} {operateur} {num2} = {resultat}")
                print('='*40)

                dernier_resultat = resultat

            # Opérations multiples
            elif choix == '5':
                resultat = operations_multiples()
                if resultat is not None:
                    dernier_resultat = resultat

            # Gestion mémoire
            elif choix == '6':
                gestion_memoire()

            else:
                print("Erreur : Choix invalide. Entrez un nombre de 1 à 7")

        except ZeroDivisionError as zde:
            print(f"\n❌ ERREUR : {zde}")

        except ValueError as ve:
            print(f"\n❌ ERREUR : {ve}")

        except Exception as e:
            print(f"\n❌ ERREUR INATTENDUE : {e}")


# Lancement de la calculatrice
if __name__ == "__main__":
    calcularice()
# TP2 - MATRICE - MARC-ANDRE DUFOUR - A REMETTRE POUR LE 16 FEVRIER 2026

"""
Le programme part d'une case et regarde tout autour.
S'il voit une case plus petite, il y va et répète la même chose.
À chaque étape, il garde le meilleur chemin trouvé jusqu'ici. 
Si on a déjà calculé un chemin pour une case, on se souvient pour pas refaire le travail.
À la fin, on garde juste le chemin le plus long qu'on a trouvé.
"""

import random

under = "\033[4m"
red = "\033[31m"
yellow = "\033[33m"
blue = "\033[34m"
nc= "\033[0m"

max_size = 7
max_val = 99
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # → ["haut", "bas", "gauche", "droite"]


def user_input():
    """
    On demande à la personne combien de lignes, de colonnes et la valeur max pour remplir la matrice.
    On s'assure que les valeurs entrées respecte les conditions sinon on recommence.
    Retourne les trois nombres : lignes, colonnes et valeur max.
    """
    while True:
        try:
            ligne = int(input(f"\nVeuillez entrer le nombre de lignes de votre matrice : "))
            if ligne <= 0 or ligne > max_size:
                raise ValueError(f"La valeur doit être entre 1 et {max_size}")

            colonne = int(input("Veuillez entrer le nombre de colonnes : "))
            if colonne <= 0 or colonne > max_size:
                raise ValueError(f"La valeur doit être entre 1 et {max_size}")

            val_max = int(input("Veuillez entrer la valeur maximale : "))
            if val_max <= 0 or val_max > max_val:
                raise ValueError(f"Valeur maximale autorisée : {max_val}")

            return ligne, colonne, val_max

        except ValueError as ve:
            if "invalid literal" in str(ve):
                print(f"{red}Erreur : vous devez entrer un nombre entier valide {nc}")
            else:
                print(f"{red}Erreur : {ve}{nc}")

        except Exception as e:
            print(f"{red}Erreur inattendue : {e}{nc}")

def mat_generator(lignes, colonnes, max_val):
    """
    On crée une matrice de la taille que l'utilisateur a donnée.
    Chaque case a un nombre au hasard entre 1 et la valeur max.
    On retourne cette matrice dans une liste.
    """
    return [[random.randint(1, max_val) for i in range(colonnes)] for j in range(lignes)]

def show_mat(matrice, chemin=None):
    """
    On affiche la matrice joliment avec les numéros de lignes et de colonnes.
    Si on a un chemin, on le met en rouge pour le voir.
    """
    lignes = len(matrice)
    colonnes = len(matrice[0])
    print(f"\n  {under}↓ Votre matrice {lignes} x {colonnes} ↓ {nc}\n")

    print("    ", end="")
    for j in range(len(matrice[0])):
        print(f"{yellow}{j:3}{nc}", end=" ")
    print(f"\n   {blue}╔{nc}" + f"{blue}════{nc}" * len(matrice[0]))

    for i, ligne in enumerate(matrice):
        print(f"{yellow}{i:2}{nc} {blue}║{nc}", end=" ")

        for j, val in enumerate(ligne):
            if chemin and (i,j) in chemin:
                print(f"{red}{val:3}{nc}", end=" ")
            else:
                print(f"{val:3}", end=" ")
        print()

def deplacement(ligne, colonne, matrice, memoire):
    """
    On regarde à partir d'une case quelle est le plus long déplacement possible.
    Règles : on peut aller haut, bas, gauche, droite, mais seulement vers des nombres plus petits.
    On garde en mémoire ce qu'on a déjà calculé pour pas refaire deux fois le même chemin.
    Retourne la longueur du chemin et la liste des cases qu'on a traversées.
    """
        
    if (ligne, colonne) in memoire:
        return memoire[(ligne,colonne)]
    
    max_longueur = 1
    chemin = [(ligne, colonne)]
    
    for depl_ligne, depl_colonne in directions:
        nouvelle_ligne = ligne + depl_ligne
        nouvelle_colonne = colonne + depl_colonne

        if 0 <= nouvelle_ligne < len(matrice) and 0 <= nouvelle_colonne < len(matrice[0]):
            if matrice[nouvelle_ligne][nouvelle_colonne] < matrice[ligne][colonne]:
                longueur_suivante, chemin_suivant = deplacement(nouvelle_ligne, nouvelle_colonne, matrice, memoire)
                longueur_totale = 1 + longueur_suivante
                if longueur_totale > max_longueur:
                    max_longueur = longueur_totale
                    chemin = [(ligne, colonne)] + chemin_suivant

    memoire[(ligne, colonne)] = (max_longueur, chemin)
    return memoire[(ligne, colonne)]

def chemin_plus_long(matrice):
    """
    On essaye de partir de toutes les cases pour trouver le chemin la plus longue.
    Retourne combien de cases on peut parcourir au max et quelles cases font ce chemin.
    """
    memoire = {}
    max_global = 0
    chemin_parcouru = []

    for ligne in range(len(matrice)):
        for colonne in range(len(matrice[0])):
            longueur, chemin = deplacement(ligne, colonne, matrice, memoire)
            if longueur > max_global:
                max_global = longueur
                chemin_parcouru = chemin

    return max_global, chemin_parcouru

def executer():
    execution = True
    while execution:
        print(f"\n{under}► CHEMIN LE PLUS LONG DANS UNE MATRICE ◄{nc}")
        nbr1, nbr2, nbr3 = user_input()
        mat1 = mat_generator(nbr1, nbr2, nbr3)
        longueur, chemin = chemin_plus_long(mat1)
        show_mat(mat1, chemin)

        print("\nCalculs en cours...\n")
        print(f"Longueur du chemin le plus long : {longueur} déplacements\n")
        print("Chemin → ", " → ".join(str(mat1[ligne][colonne]) for ligne,colonne in chemin))

        print(f"\n  {under}↓ Statistique ↓{nc}\n")
        elements = [valeur for ligne in mat1 for valeur in ligne]
        print(f"La valeur maximale est {max(elements)}")
        print(f"La valeur minimale est {min(elements)}")
        print(f"La moyenne est de {sum(elements) / len(elements):.2f}") 

        reponse = input(f"\nVoulez-vous continuer ? (o/n) : ").strip().lower()
        if reponse != "o":
            print("Merci ! Au revoir !")
            execution = False

if __name__ == "__main__":
    executer()
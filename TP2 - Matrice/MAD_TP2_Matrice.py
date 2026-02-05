# TP2 - MATRICE - MARC-ANDRE DUFOUR - A REMETTRE POUR LE 16 FEVRIER 2026

import random

under = "\033[4m"
red = "\033[31m"
end = "\033[0m"

max_size = 7
max_val = 99
#directions = ["haut", "bas", "gauche", "droite"] # ⬆️ ⬇️ ⬅️ ➡️
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def user_input():
    while True:
        try:

            ligne = int(input("Veuillez entrer le nombre de ligne de votre matrice : "))
            if ligne <= 0 or ligne > max_size:
                raise ValueError(f"La valeur doit être entre 1 et {max_size}") 

            colonne = int(input("Veuillez entrer le nombre de colonne de votre matrice : "))    
            if colonne <= 0 or colonne > max_size:
                raise ValueError(f"La valeur doit être entre 1 et {max_size}")

            val_max = int(input("Veuillez entrer la valeur maximale de votre matrice : "))
            if val_max <= 0 or val_max > max_val:
                raise ValueError(f"Valeur maximale autorisée : {max_val}") 
            
            return ligne, colonne, val_max
        
        except ValueError as ve:
            print(f"{red}Erreur : {ve}{end}")

        except Exception as e:
            print(f"{red}Erreur inattendue : {e}{end}")

def mat_generator(lignes, colonnes, max_val):
    return [[random.randint(1, max_val) for i in range(colonnes)] for j in range(lignes)]

def show_mat(matrice):
    print(f"\nVotre matrice :\n")
    for i, ligne in enumerate(matrice):
        print(f"{i:2} |", end=" ")
        for val in ligne:
            print(f"{val:3}", end=" ")
        print()

def deplacement(ligne, colonne, matrice, memoire):
    if ligne < 0 or ligne >= len(matrice) or colonne < 0 or colonne >= len(matrice[0]) or (ligne, colonne) in memoire:
        return
    memoire.add((ligne, colonne))
    print(f"\n Mémoire : {matrice[ligne][colonne]}")
    
    for depl_ligne, depl_colonne in directions:
        deplacement(ligne + depl_ligne, colonne + depl_colonne, matrice, memoire)


def executer():
    memoire = set()
    nbr1, nbr2, nbr3 = user_input()
    mat1 = mat_generator(nbr1, nbr2, nbr3)
    show_mat(mat1)
    print("\nCalculs en cours...\n")
    deplacement(0, 0, mat1, memoire)

if __name__ == "__main__":
    executer()

# TP2 - MATRICE - MARC-ANDRE DUFOUR - A REMETTRE POUR LE 16 FEVRIER 2026

import random

def user_input():
    ligne = int(input(f"Veuillez entrer le nombre de ligne de votre matrice : "))
    colonne = int(input(f"Veuillez entrer le nombre de colonne de votre matrice : "))
    val_max = int(input(f"Veuillez entrer la valeur maximale de votre matrice : "))
    return ligne, colonne, val_max

def mat_generator(lignes, colonnes, max_val):
    return [[random.randint(1, max_val) for i in range(colonnes)] for j in range(lignes)]

def show_mat(matrice):
    print(f"\nVotre matrice :\n")
    for i, ligne in enumerate(matrice):
        print(f"{i:2} |", end=" ")
        for val in ligne:
            print(f"{val:3}", end=" ")
        print()
    print("     " + "___" * len(matrice))

# TEST
nbr1, nbr2, nbr3 = user_input()
mat1 = mat_generator(nbr1, nbr2, nbr3)

show_mat(mat1)
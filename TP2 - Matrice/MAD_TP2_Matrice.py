# TP2 - MATRICE - MARC-ANDRE DUFOUR - A REMETTRE POUR LE 16 FEVRIER 2026

import random

max_size = 7
max_val = 55

def user_input():
    while True:
        try:
            ligne = int(input("Veuillez entrer le nombre de ligne de votre matrice : "))
            if ligne <= 0:
                raise ValueError("La valeur doit être entre 1 et 7") 
            if ligne > max_size:
                raise ValueError(f"Valeur maximale autorisée : {max_size}")
            
            colonne = int(input(f"Veuillez entrer le nombre de colonne de votre matrice : "))
            if colonne <= 0:
                raise ValueError("La valeur doit être entre 1 et 7")
            if colonne > max_size:
                raise ValueError(f"Valeur maximale autorisée : {max_size}")
            
            val_max = int(input(f"Veuillez entrer la valeur maximale de votre matrice : "))
            if val_max <= 0:
                raise ValueError("La valeur doit être entre 1 et 7") 
            if val_max > max_val:
                raise ValueError(f"Valeur maximale autorisée : {max_val}") 
            
            return ligne, colonne, val_max
        
        except ValueError as ve:
            print(f"Erreur : {ve} (ValueError1)")

def mat_generator(lignes, colonnes, max_val):
    return [[random.randint(1, max_val) for i in range(colonnes)] for j in range(lignes)]

def show_mat(matrice):
    print(f"\nVotre matrice :\n")
    for i, ligne in enumerate(matrice):
        print(f"{i:2} |", end=" ")
        for val in ligne:
            print(f"{val:3}", end=" ")
        print()


def executer():

    pass 

# TEST
nbr1, nbr2, nbr3 = user_input()
mat1 = mat_generator(nbr1, nbr2, nbr3)
show_mat(mat1)
# Ce module doit contenir les fonctions :

# créer la grille
# convertir une position (1-9) en ligne et colonne
# vérifier si une case est vide
# placer un symbole

valeur_nulle = " . "
valeur_1 = " O "
valeur_2 = " X "

def create_board():
    return [
        [valeur_nulle, valeur_nulle, valeur_nulle],
        [valeur_nulle, valeur_nulle, valeur_nulle],
        [valeur_nulle, valeur_nulle, valeur_nulle]
    ]

def position_to_index(position):
    ligne = (position - 1) // 3
    colonne = (position - 1) % 3
    return ligne, colonne

def is_empty(board, ligne, colonne):
    return board[ligne][colonne] == valeur_nulle

def place_symbol(board, ligne, colonne, symbole):
    board[ligne][colonne] = symbole

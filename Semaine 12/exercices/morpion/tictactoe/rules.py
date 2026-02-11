# Ce module doit contenir les fonctions :

# vérifier si un joueur a gagné
# vérifier s'il y a une égalité
from tictactoe.board import valeur_nulle

def check_win(board):
    # Lignes
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != valeur_nulle:
            return True

    # Colonnes
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != valeur_nulle:
            return True

    # Diagonales
    if board[0][0] == board[1][1] == board[2][2] != valeur_nulle:
        return True

    if board[0][2] == board[1][1] == board[2][0] != valeur_nulle:
        return True

    return False

def check_draw(board):
    for ligne in board:
        for case in ligne:
            if case == valeur_nulle:
                return False
    return True

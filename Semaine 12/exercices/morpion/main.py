# Ce fichier doit :

# importer les modules
# contenir la boucle principale du jeu
# gérer le joueur courant

from tictactoe.board import create_board, position_to_index, is_empty, place_symbol, valeur_1, valeur_2
from tictactoe.rules import check_win, check_draw
from tictactoe.ui import draw, ask_position, show_message

def main():
    board = create_board()
    joueur_en_cours = "Joueur 1"

    draw(board)

    while True:
        try:
            entree = int(ask_position(joueur_en_cours))

            if entree < 1 or entree > 9:
                show_message("Choisis un nombre entre 1 et 9.")
                continue

            ligne, colonne = position_to_index(entree)

            if not is_empty(board, ligne, colonne):
                show_message("Case déjà prise.")
                continue

            symbole = valeur_1 if joueur_en_cours == "Joueur 1" else valeur_2
            place_symbol(board, ligne, colonne, symbole)

            draw(board)

            if check_win(board):
                show_message(f"{joueur_en_cours} a gagné !")
                break

            if check_draw(board):
                show_message("Match nul !")
                break

            joueur_en_cours = "Joueur 1" if joueur_en_cours == "Joueur 2" else "Joueur 2"

        except ValueError:
            show_message("Entre un nombre valide.")

if __name__ == "__main__":
    main()
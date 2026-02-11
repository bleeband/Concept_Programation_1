from tictactoe.board import Board
from tictactoe.ui import ConsoleUI


class Game:
    def __init__(self):
        self.board = Board()
        self.ui = ConsoleUI()
        self.joueur_en_cour = "Joueur 1"
        self.symbols = {
            "Joueur 1": " O ",
            "Joueur 2": " X "
        }
        self.turn_count = 0  # Bonus compteur de tours

    def switch_joueur(self):
        self.joueur_en_cour = (
            "Joueur 1" if self.joueur_en_cour == "Joueur 2" else "Joueur 2"
        )

    def play(self):
        self.board.display()

        while True:
            try:
                position = int(self.ui.ask_position(self.joueur_en_cour))

                if position < 1 or position > 9:
                    self.ui.show_message("Choisis un nombre entre 1 et 9.")
                    continue

                if not self.board.place_symbol(position, self.symbols[self.joueur_en_cour]):
                    self.ui.show_message("Case déjà prise.")
                    continue

                self.turn_count += 1
                self.board.display()

                if self.board.check_win():
                    self.ui.show_message(
                        f"🔥 {self.joueur_en_cour} a gagné en {self.turn_count} tours !"
                    )
                    break

                if self.board.check_draw():
                    self.ui.show_message("Match nul !")
                    break

                self.switch_joueur()

            except ValueError:
                self.ui.show_message("Entre un nombre valide.")

    def restart(self):
        self.board.reset()
        self.joueur_en_cour = "Joueur 1"
        self.turn_count = 0

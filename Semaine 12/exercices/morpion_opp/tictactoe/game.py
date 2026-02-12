# Responsabilités :

# gérer le joueur courant
# gérer les tours
# gérer la boucle du jeu
# détecter la fin de partie
from colorama import Fore, Style
import emoji, pyfiglet
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
                    self.ui.show_message(
                        (Fore.RED + emoji.emojize(f":warning: Choisis un nombre entre 1 et 9.", language='alias') + Style.RESET_ALL)
                    )
                    continue

                if not self.board.place_symbol(position, self.symbols[self.joueur_en_cour]):
                    self.ui.show_message(
                        (Fore.RED + emoji.emojize(f":cross_mark: Case déjà prise !", language='alias') + Style.RESET_ALL)
                    )
                    continue

                self.turn_count += 1
                self.board.display()

                if self.board.check_win():
                    self.ui.show_message(
                        (Fore.BLUE + emoji.emojize(f":fire: {self.joueur_en_cour} a gagné en {self.turn_count} tours !\n", language='alias') + Style.RESET_ALL)
                        + pyfiglet.figlet_format("WINNER !", font="slant")
                    )
                    break

                if self.board.check_draw():
                    self.ui.show_message(
                        (Fore.YELLOW + emoji.emojize(f":handshake: Match nul !", language='alias') + Style.RESET_ALL)
                    )
                    break

                self.switch_joueur()

            except ValueError:
                self.ui.show_message((Fore.RED + emoji.emojize(f":warning: Entre un nombre valide.", language='alias') + Style.RESET_ALL))

    def restart(self):
        self.board.reset()
        self.joueur_en_cour = "Joueur 1"
        self.turn_count = 0

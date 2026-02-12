# Responsabilités :

# demander une position
# afficher des messages

class ConsoleUI:
    def ask_position(self, joueur):
        return input(f"{joueur} [1-9] ? > ")

    def show_message(self, message):
        print(message)

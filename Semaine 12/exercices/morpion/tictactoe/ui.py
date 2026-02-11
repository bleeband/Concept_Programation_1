# Ce module doit contenir les fonctions :

# afficher la grille
# demander une position au joueur
# afficher un message

def draw(board):
    for ligne in board:
        for case in ligne:
            print(case, end="")
        print()

def ask_position(joueur):
    return input(f"{joueur} [1-9] ? > ")

def show_message(message):
    print(message)
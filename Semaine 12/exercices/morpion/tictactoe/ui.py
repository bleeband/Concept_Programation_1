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
    while True:
        try:
            entree = int(input(f"{joueur} [1-9] ? > "))
            return entree
        
        except ValueError:
            print("Entre un nombre valide.")
            

def show_message(message):
    print(message)
# DECLARATION DE LA MATRICE

# . . .
# . . .
# . . . 
# [" . "," . "," . ",]
                            # 1 - 9
                            # 1 => 0,0
                            # 2 => 0,1
                            # 3 => 0,2
                            # 4 => 1,0
                            # 7 => 2,0    7/3 = 2  7   modulo 3 = 1
                            # 8 => 2,1
                            # 9 => 2,2
#-------------------------------------------------------------------

valeur_nulle = " . "
valeur_1 = " O "
valeur_2 = " X "
terrain_jeux = [
    [valeur_nulle, valeur_nulle, valeur_nulle],
    [valeur_nulle, valeur_nulle, valeur_nulle],
    [valeur_nulle, valeur_nulle, valeur_nulle]
]

joueur_en_cour = "Joueur 1"

# FONCTION POUR DESSINER LA MAP
def draw():
    for i in range(3):
        for j in range(3):
            print(terrain_jeux[i][j], end= "")
        print()

# FONCTION QUI EXPLORE LES POSSIBILITES GAGNANTE
def check_win():
    # VERIFIER LES LIGNES
    for i in range(3):
        if terrain_jeux[i][0] == terrain_jeux[i][1] == terrain_jeux[i][2] != valeur_nulle:
            return True
    # VERIFIER LES COLONNES
    for j in range(3):
        if terrain_jeux[0][j] == terrain_jeux[1][j] == terrain_jeux[2][j] != valeur_nulle:
            return True
    # VERIFIER LES DIAGONALES
    if terrain_jeux[0][0] == terrain_jeux[1][1] == terrain_jeux[2][2] != valeur_nulle:
            return True
    if terrain_jeux[0][2] == terrain_jeux[1][1] == terrain_jeux[2][0] != valeur_nulle:
            return True
    
# FONCTION QUI EXPLORE LES PARTIE NULLE
def check_terrain():
    for i in range(3):
        for j in range(3):
            if terrain_jeux[i][j] == valeur_nulle:
                return False
    return True

draw()

while True:
    # entree = int(input(f"{joueur_en_cour} [1-9] ? =>"))
    # DEMANDER LE CHOIX
    while True:
        try:
            entree = int(input(f"{joueur_en_cour} [1-9] ? =>"))
            if 1 <= entree <= 9:
                break
            else:
                print(" Votre choix doit etre entre 1 et 9")
                continue
        except ValueError:
            print("Choix INVALIDE, veuillez entrer un nombre entre 1 et 9.")

    ligne = (entree - 1) // 3
    colonne = (entree - 1) % 3

    # VERIFIER MATRICE
    if terrain_jeux[ligne][colonne] == valeur_nulle:
        terrain_jeux[ligne][colonne] = valeur_1 if joueur_en_cour == "Joueur 1" else valeur_2

    draw()

    # VERIFEIR LA MAP SI JOEUR GAGNE, BREAK
    if check_win():
        print(f"=== {joueur_en_cour} à GAGNER ! ===")
        break
    
    # VERIFEIR LA MAP SI PARTIE NULLE, BREAK
    if check_terrain():
        print(" === MATCH NULLE ===")
        break

    joueur_en_cour = "Joueur 1" if joueur_en_cour == "Joueur 2" else "Joueur 2"

    # print(entree)


    

    #  AJOUTER LA LOGIQUE POUR REJOUER SI CHOIX DEJA FAIT, SI PAS ENTRE 1 et 9

import random

#  JEUX DU PENDU

liste_mot = ["arbre", "global", "couvent", "maison", "axe", "bourse", "vagabond", "caissier", "bourgeon", "chanteur"]
mot_choisi = liste_mot[random.randint(0, 9)]    # 3.  Choisir un mot alleatoirment dans la liste
max_vie = 9     # 5.  Allouer 9 vie
lettre_trouve = []

while max_vie > 0:
    print(f" NOMBRE DE VIE {max_vie}")
    mot_mystere = ""
    
    for lettre in mot_choisi:       # POUR CHAQUE LETTRE DANS RANDOM

        if lettre in lettre_trouve:
            mot_mystere += lettre + " "     
        
        else:
            mot_mystere = mot_mystere + "_ "        # 4.  Cacher le mot mystere et Afficher mot cache en _ _ _ _ _

    print(mot_mystere)

    if "_" not in mot_mystere:
        print("\n VOUS AVEZ GAGNE")
        break
        
    lettre_choisi = input("Veuillez choisir une lettre : ")     # 7.  Input (choix lettre)

    if lettre_choisi in mot_choisi:

        lettre_trouve.append(lettre_choisi)     # SAUVEGARDE LA LETTRE

    else:
        max_vie -= 1
    
if max_vie < 1:
    print("VOUS AVEZ PERDU !!! ")

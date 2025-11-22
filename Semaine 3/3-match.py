# NOTE COUR 4

# ----------------------------------------------------------------------------------
# STRUCTURE DE CONTROLE

# AJOUT MATCH

error = 405

if error == 500:
    print("Erreur serveur")
elif error == 400:
    print("Mauvaise requete")
elif error == 404 or error == 406 or error == 405:
    print("Erreur non trouve")
else:
    print("Erreur inconnue")

match error:
    case 500:
        print("Erreur serveur")
    case 400:
        print("Mauvaise requete")
    case 404 | 405 :
        print("Erreur non trouve")
    case 500:
        print("Erreur Inconnue")



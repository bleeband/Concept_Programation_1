
# # Exercices sur les Fonctions en Python

# ## Exercice 1 : Définition Basique et Appel

# 1.1 : Code à Développer

# Créez une fonction `bonjour()` qui affiche "Bonjour !" lorsqu'elle est appelée. Appelez-la trois fois.

# def bonjour():
#     print("Bonjour !")

# bonjour(), bonjour(), bonjour()

# 1.2 : Code à Finaliser

# # Complétez cette fonction
# def python():
#     print("Python est génial !")

# # # Appelez la fonction
# python()


#1.3 : Code à Corriger


# Ce code contient des erreurs, corrigez-les

# def dire_bonjour():
#     print("Hello World")

# dire_bonjour()


# Exercice 2 : Retour de Valeurs

# 2.1 : Code à Développer

# Créez une fonction `carre()` qui prend un nombre en paramètre et retourne son carré. Testez avec plusieurs nombres.

# def carre(nombre):
#     return nombre * nombre

# print(carre(6))
# print(carre(4))
# print(carre(2))


# 2.2 : Code à Finaliser

# def est_pair(nombre):
#     # Retourne True si le nombre est pair, False sinon
#     return nombre % 2 == 0


# print(est_pair(4))   # Devrait afficher True
# print(est_pair(7))   # Devrait afficher False


# 2.3 : Code à Corriger

# def addition(a, b):
#     result = a + b
#     return result

# print(addition(5, 3))  # Devrait afficher 8


# Exercice 3 : Paramètres et Arguments

# 3.1 : Code à Développer

# Créez une fonction `presentation()` qui prend deux paramètres : `nom` et `age`. 
# La fonction doit afficher "Je m'appelle [nom] et j'ai [age] ans."

# def presentation(prenom, age):
#     print(f"Je m'appelle {prenom} et j'ai {age} ans. ")

# print(presentation("marc",41))

# 3.2 : Code à Finaliser

# def calculer_moyenne(note1, note2, note3):
#     # Calcule et retourne la moyenne des trois notes
#     moyenne = (note1 + note2 + note3)/3
#     return moyenne

# # Test avec différentes valeurs
# moyenne1 = calculer_moyenne(15, 12, 18)
# moyenne2 = calculer_moyenne(10, 8, 12)

# print(f"Moyenne 1: {moyenne1}")
# print(f"Moyenne 2: {moyenne2}")


# 3.3 : Code à Corriger

# def afficher_info(prenom, nom, age):
#     print(f"Nom: {prenom} {nom}")
#     print(f"Age: {age} ans")
#     return

# # Ce code ne fonctionne pas comme attendu
# afficher_info("Alice", "Dupont", 25)


# Exercice 4 : Fonctions comme Variables

# 4.1 : Code à Développer

# Créez une fonction `multiplier_par_deux()` et une fonction `ajouter_cinq()`. 
# Créez ensuite une variable `operation` qui peut contenir l'une ou l'autre fonction et l'appeler.

# def multiplier_par_2(nombre):
#     return nombre * 2

# def ajouter_5(nombre):
#     return nombre + 5

# operation = multiplier_par_2(2), ajouter_5(2)

# print(operation)

# 4.2 : Code à Finaliser

# def saluer():
#     return "Bonjour"

# def dire_au_revoir():
#     return "Au revoir"

# # Stockez la fonction saluer dans une variable
# message_func = saluer()

# # Utilisez la variable pour appeler la fonction
# message = message_func
# print(message)


# 4.3 : Code à Corriger

# def carre(x):
#     return x * x

# def cube(x):
#     return x * x * x

# # Problème ici
# operation = carre
# resultat = operation(3)  # Doit retourner 9

# operation = cube
# resultat2 = operation(2)  # Doit retourner 8

# print(resultat)
# print(resultat2)


# Exercice 5 : Paramètres Positionnels

# 5.1 : Code à Développer

# Créez une fonction `decrire_rectangle()` qui prend `longueur` et `largeur` 
# comme paramètres positionnels et affiche les dimensions.

# def decrire_rectangle(longeur, largeur):
#     print(f"Rectangle de {longeur} par {largeur}")
#     print(f"Périmètre de {(longeur + largeur) * 2}cm")
#     print(f"Aire de {longeur * largeur}cm²")

# decrire_rectangle(10, 5)
# print()
# decrire_rectangle(7, 3)


# 5.2 : Code à Finaliser

# def creer_email(prenom, nom, domaine):
#     # Crée un email au format prenom.nom@domaine.com
#     # Tous en minuscules
#     email = f"{prenom}.{nom}@{domaine}.com"
#     return email
# # Test avec différents ordres
# email1 = creer_email("jean", "dupont", "entreprise")
# #email2 = creer_email("entreprise", "jean", "dupont")  # Que se passe-t-il ? NON RESPECT DE LORDRE CAR ENT EST AU DEBUT
# email2 = creer_email("jean", "dupont","entreprise")  # Que se passe-t-il ? NON RESPECT DE LORDRE CAR ENT EST AU DEBUT

# print(f"Email 1: {email1}")
# print(f"Email 2: {email2}")


# 5.3 : Code à Corriger

# def decrire_personne(nom, age, ville):
#     print(f"{nom} a {age} ans et habite à {ville}")

# # Les arguments sont dans le mauvais ordre
# decrire_personne("Alice", 25, "Paris")


# Exercice 6 : Variables comme Arguments

# 6.1 : Code à Développer

# Créez une fonction `echanger()` qui échange les valeurs de deux variables. 
# Testez avec différentes variables.

# def echanger(a, b):
#     return b, a

# x = 10
# y = 20
# print(f"Avant: x={x}, y={y}")
# x, y = echanger(x, y)
# print(f"apres: x={x}, y={y}")


# 6.2 : Code à Finaliser

# def appliquer_tva(prix_ht, taux_tva):
#     # Calcule le prix TTC
#     return prix_ht * taux_tva

# # Utilisez des variables comme arguments
# prix_base = 100
# taux = 0.2

# prix_final = appliquer_tva(prix_base, taux)
# print(f"Prix TTC: {prix_final}")


# 6.3 : Code à Corriger

# def modifier_liste(liste):
#     liste.append("nouvel_element")

# ma_liste = [1, 2, 3]
# modifier_liste(ma_liste)

# print(ma_liste)  # Que contient ma_liste maintenant ?
#                 # 1,2,3, nouvel element


# Exercice 7 : Nombre Indéfini d'Arguments

# 7.1 : Code à Développer

# Créez une fonction `somme_nombres()` qui peut prendre n'importe
#  quel nombre d'arguments et retourne leur somme.

# def somme_nombres(*nombres):
#     total = 0
#     for n in nombres:
#         total += n
#     return total

# print(somme_nombres(8, 2))
# print(somme_nombres(100,50,25))


# 7.2 : Code à Finaliser

# def concatener_mots(*mots):
#     # Concatène tous les mots avec un espace
#     phrase = " ".join(mots)
#     return phrase

# # Test avec différents nombres d'arguments
# phrase1 = concatener_mots("Bonjour", "le", "monde")
# phrase2 = concatener_mots("Python", "c'est", "génial", "!")
# phrase3 = concatener_mots("Test")

# print(phrase1)
# print(phrase2)
# print(phrase3)

# EXERCICE 7.3 - CODE À CORRIGER
# Ce code contient des erreurs avec les paramètres indéfinis

# def afficher_infos(*infos, nom, age, **restant):
#     # Devrait afficher toutes les informations
#     print(f"Nom: {nom}")
#     print(f"Age: {age} ans")

#     # Afficher les autres infos
#     print("Autres informations:")
#     for info in infos:
#         print(f"  - {info}")

# # Test 1 - Avec plusieurs informations supplémentaires
# print("=== Test 1 ===")
# afficher_infos("Développeuse", "Paris", "Python", nom="Alice", age=25)

# # Test 2 - Sans informations supplémentaires
# print("\n=== Test 2 ===")
# afficher_infos(nom="Bob", age=30)

# # Test 3 - Problème ici
# print("\n=== Test 3 ===")
# afficher_infos("Ingénieur", "Lyon", "Java", nom="Charlie", age=28)


# Exercice 8 : Projets Complets

# 8.1 : Calculateur Géométrique (à Développer)

# Créez plusieurs fonctions pour calculer :

# def aire_rectangle(longueur, largeur):
#     print(f"Aire de {longueur * largeur}cm²")
# def perimetre_rectangle(longueur, largeur):
#     print(f"Périmètre de {(longueur + largeur) * 2}cm")
# def aire_cercle(rayon): # pi_approximatif * (rayon * rayon)
#     pi = 3.14
#     print(f"Aire du cercle : {(rayon*2)*pi}")
# def volume_sphere(rayon):
#     pi = 3.14
#     print(f"Aire du cercle : {(4/3) * pi * (rayon ** 3)}")

# aire_rectangle(5,2)
# perimetre_rectangle(5,2)
# aire_cercle(2)
# volume_sphere(2)


# 8.2 : Gestionnaire de Contacts (à Finaliser)

# def ajouter_contact(contacts, nom, telephone, email):
#     # Ajoute un contact au dictionnaire
#     contacts[nom] = {
#         "telephone": telephone,
#         "email": email
#     }
#     return contacts

# def afficher_contacts(contacts):
#     # Affiche tous les contacts
#     for nom, infos in contacts.items():
#         print(f"{nom}:")
#         print(f"  Téléphone: {infos['telephone']}")
#         print(f"  Email: {infos['email']}")

# def rechercher_contact(contacts, nom):
#     # Recherche un contact par nom
#     if nom in contacts:
#         return contacts[nom]
#     else:
#         return None

# # Utilisation
# mes_contacts = {}
# ajouter_contact(mes_contacts, "Alice", "0123456789", "alice@test.com")
# ajouter_contact(mes_contacts, "Bob", "0987654321", "bob@test.com")

# afficher_contacts(mes_contacts)
# contact = rechercher_contact(mes_contacts, "Alice")
# print(f"\nRecherche Alice: {contact}")


# 8.3 : Système de Calcul de Notes (à Corriger)

def calculer_moyenne_etudiant(notes):
    total = 0
    for note in notes:
        total += note
    return total / len(notes)

def determiner_appreciation(moyenne):
    if moyenne >= 16:
        return "Excellent"
    elif moyenne >= 14:
        return "Très bien"
    elif moyenne >= 12:
        return "Bien"
    elif moyenne >= 10:
        return "Passable"
    else:
        return "Insuffisant"

# Tests
notes_alice = [25, 27, 25]
moyenne = calculer_moyenne_etudiant(notes_alice)
appreciation = determiner_appreciation(moyenne)

print(f"Moyenne: {moyenne}")
print(f"Appréciation: {appreciation}")
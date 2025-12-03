#

#     **  LES FONCTIONS  **

# print(2+5)

# def addition(a, b):
#     print(a+b)

# addition(2, 5)

# #      **  Definition des fonctions  **

# def le_nom_de_la_fonction():
#     print("Hello World !")


# #      **   RETOURNER DES VALEURS  **

# def le_nom_de_la_fonction2():
#     return "Hello World !"

# a = le_nom_de_la_fonction()
# print(a)

# b = le_nom_de_la_fonction2()
# print(b)

# def multiple_retour():
#     return 'Salut', 'Comment ca va', 1, True

# c = multiple_retour()
# print(c)


# #      **  LES PARAMETRES  **

# def addition_entre_deux_nombres(a, b = 2):
#     return a + b

# resultat = addition_entre_deux_nombres(8, 9)
# print(resultat)
# resultat2 = addition_entre_deux_nombres(8)
# print(resultat2)


# def greetings(nom, prenom):
#     print(f"Bonjour {prenom} {nom} !")

# greetings("Marc", "Dufour")
# greetings(prenom="Marc", nom="Dufour")
# greetings("Dufour", "Marc")

# print("Salut", "Marc", end=" ")
# print("test")


a = "Je suis A"

# def my_fonc(b):
#     b = 2
#     print(b is a)

# my_fonc(a)
# print(a)

# c = [1, 2]
# def my_fonc_muable(b):
#     b.append(3)
#     print(c is b)

# my_fonc_muable(c)
# print(c)

# d = [5, 6]

# def my_fonc_muable2(b):
#     b = [7]
#     print(b is c)

# my_fonc_muable2(d)



# #      **  PASSER UN NOMBRE INDEFINI D'ARGUMENTS  **

def somme_de_tout(*args, factor = "4", **kwargs):
    print(kwargs)
    print(factor)
    print(sum(args))

somme_de_tout(5,47,54,78, name="dufour", prenom="marc")



# #      **  SCOPE  **
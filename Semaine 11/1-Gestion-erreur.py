# PARTIE 1 - GESTION DES ERREURS

# TRY / EXCEPT / ELSE / FINALLY / RAISE

# e = ZeroDivisionError("Division par zéro impossible")
# # print(e)
# raise e

#5/0 # ZeroDivisionError

#print(ZeroDivisionError.mro())

# print(24 + "test") # TypeError

#print(TypeError.mro())

# for i in range#(5) # IndexError

# print(ValueError.mro())
# print(KeyboardInterrupt.mro())

## =========================================================


from random import randint

nombre_secret = randint(0, 1000)
nombre_essais = 0

## ----------- TYPE ERROR EXEMPLE -----------------

# while True:
#     nbr = input("Devinez le nombre secret entre 0 et 1000 : ")

#     if nbr == nombre_secret:
#         print("Bravo, vous avez trouvé le nombre secret !")
#         break
#     elif nbr > nombre_secret:
#         print("Le nombre est plus petit !")
#     else:
#         print("Le nombre est plus grand !")

# print(TypeError.mro())


#------------ VALUE ERROR EXEMPLE -----------------

# while True:
#     nbr = int(input("Devinez le nombre secret entre 0 et 1000 : "))

#     if nbr == nombre_secret:
#         print("Bravo, vous avez trouvé le nombre secret !")
#         break
#     elif nbr > nombre_secret:
#         print("Le nombre est plus petit !")
#     else:
#         print("Le nombre est plus grand !")

# print(ValueError.mro())


##------------ GESTION D'ERREUR AVEC TRY EXEMPLE -----------------

# while True:
#     try:
#         nbr = int(input("Devinez le nombre secret entre 0 et 1000 : "))
#     except ValueError:
#         print("Veuillez entrer un nombre valide (ValueError)")
#     else:
#         if nbr == nombre_secret:
#             print("Bravo, vous avez trouvé le nombre secret !")
#             break
#         elif nbr > nombre_secret:
#             print("Le nombre est plus petit !")
#         else:
#             print("Le nombre est plus grand !")
#     finally:
#         print("Je suis le FINALLY")
#         nombre_essais += 1
#         print("Nombre d'essais :", nombre_essais)


## ------------ CREATION D'EXCEPTIONS ValueError as err -----------------

# while True:
#     try:
#         nbr = int(input("Devinez le nombre secret entre 0 et 1000 : "))
#     except ValueError as err:
#         print(err)
#     else:
#         if nbr == nombre_secret:
#             print("Bravo, vous avez trouvé le nombre secret !")
#             break
#         elif nbr > nombre_secret:
#             print("Le nombre est plus petit !")
#         else:
#             print("Le nombre est plus grand !")
#     finally:
#         print("Je suis le FINALLY")
#         nombre_essais += 1
#         print("Nombre d'essais :", nombre_essais)


## ------------ CREATION FONCTION -----------------

# def check_input(nbr):
#     if nbr == nombre_secret:
#         print("Bravo, vous avez trouvé le nombre secret !")
#         return True
#     elif nbr > nombre_secret:
#         print("Le nombre est plus petit !")
#     else:
#         print("Le nombre est plus grand !")

# while True:
#     try:
#         nbr = int(input("Devinez le nombre secret entre 0 et 1000 : "))
#     except ValueError as err:
#         print(err)
#     else:
#         if check_input(nbr):
#             break

#     finally:
#         print("Je suis le FINALLY")
#         nombre_essais += 1
#         print("Nombre d'essais :", nombre_essais)


# ## ------------ CREATION CLASS D'EXCEPTIONS PERSONNALISEES -----------------

# class IncorectNumberError(Exception):
#     def __init__(self, message) -> None:
#         self.message = message

# def check_input(nbr):
#     if nbr == nombre_secret:
#         print("Bravo, vous avez trouvé le nombre secret !")
#         return True
#     elif nbr > nombre_secret:
#         raise IncorectNumberError("Le nombre est plus petit !")
#     else:
#         raise IncorectNumberError("Le nombre est plus grand !")

# while True:
#     try:
#         nbr = int(input("Devinez le nombre secret entre 0 et 1000 : "))
#     except ValueError as err:
#         print(err)
#     else:
#         try:
#             if check_input(nbr):
#                 break
#         except IncorectNumberError as err:
#             print(err)

#     finally:
#         print("Je suis le FINALLY")
#         nombre_essais += 1
#         print("Nombre d'essais :", nombre_essais)


# ## ------------ CREATION CLASS D'EXCEPTIONS PERSONNALISEES -----------------

class IncorectNumberError(Exception):
    def __init__(self, message, nbr) -> None:
        self.message = message
        self.nbr = nbr

    def __str__(self) -> str:
        return f"{self.message} Vous avez entré {self.nbr}."

def check_input(nbr):
    if nbr == nombre_secret:
        print("Bravo, vous avez trouvé le nombre secret !")
        return True
    elif nbr > nombre_secret:
        raise IncorectNumberError("Le nombre est plus petit !", nbr)
    else:
        raise IncorectNumberError("Le nombre est plus grand !", nbr)

while True:
    try:
        nbr = int(input("Devinez le nombre secret entre 0 et 1000 : "))
    except ValueError as err:
        print(err)
    else:
        try:
            if check_input(nbr):
                break
        except IncorectNumberError as err:
            print(err)

    finally:
        print("Je suis le FINALLY")
        nombre_essais += 1
        print("Nombre d'essais :", nombre_essais)
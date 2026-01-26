import random
import math
import json
import os
import copy
import datetime


# IMPORT RANDOM  #

""" a = random.random()
b = random.randint(1, 10)
c = random.choice(['apple', 'banana', 'cherry'])
liste = [1, 2, 3,4,5]
d = random.shuffle(liste)

print(liste)
print(a)
print(b)
print(c)
print(d) """

#   IMPORT MATH  #

""" print(math.pi)
print(math.e)

print(math.sqrt(16))
print(math.pow(2, 3))
print(math.floor(3.7)) # arrondi inferieur
print(math.ceil(3.2))  # arrondi superieur """


# IMPORT JSON  #

""" donnees = {
    1: {"nom": "Alice", "age": 30, "ville": "Paris"},
    2: {"nom": "Bob", "age": 25, "ville": "Londres"}
}

# json_string = json.dumps(donnees) # transforme un dictionnaire en chaine de caractere JSON
# print(json_string)

# donnees_recuperees = json.loads(json_string) # transforme une chaine de caractere JSON en dictionnaire
# print(donnees_recuperees["nom"])   

with open("data.json", "w") as f:
    json.dump(donnees, f)

with open("data.json", "r") as f:
    donnees_recuperees = json.load(f)
    print(donnees_recuperees) """


# IMPORT OS  #

# CHEMIN DE FICHIERS

result = os.path.exists("data.json")  # verifie si le fichier existe
file_size = os.path.getsize("data.json")  # taille du fichier en octets

print(file_size)
print(result)
print(os.listdir("."))  # liste les fichiers dans le repertoire courant
os.mkdir("Test_Dir")  # cree un nouveau dossier


# IMPORT COPY  #


# IMPORT DATETIME  #

""" aujourdhui = datetime.date.today()
print(aujourdhui)

heure_actuelle = datetime.datetime.now()
print(heure_actuelle)

date_voulu = datetime.date(2023, 4, 25)
print(date_voulu)

date_formatee = aujourdhui.strftime("%d-%m-%Y")
print(date_formatee) """
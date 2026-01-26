# PARTIE 4

liste = [x for x in range(10)]
print(liste)

li = [5, 8, 16, 97]
li3 = [y * 3 for y in li]

print(li3)

valeur_nulle = " . "
valeur_1 = " O "
valeur_2 = " X "
terrain_jeux = [
    [valeur_nulle, valeur_nulle, valeur_nulle],
    [valeur_nulle, valeur_nulle, valeur_nulle],
    [valeur_nulle, valeur_nulle, valeur_nulle]
]

resultat2 = [" . " for i in range(3)]
resultat3 = [[" . " for i in range(3)] for j in range(3)]

print(resultat2)
print(resultat3)

liste1 = [1, 25, 14, 45, 78, 102, 145, 56]

result = [y for y in liste1 if y %2==0]
print(result)

# EXERCICE

resultat4 = [[i + j*3 for i in range(3)] for j in range(3)]
print(resultat4)

# Comprehension des dictionnaire

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {cle: valeur*2 for (cle,valeur) in dict1.items()}
dict3 = {valeur: cle for (cle, valeur) in dict1.items()}

print(dict1)
print(dict2)
print(dict3)
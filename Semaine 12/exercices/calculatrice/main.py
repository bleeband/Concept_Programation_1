import calculs
from geometrie import aire_cercle, aire_rectangle as rectangle

input1 = float(input("Entrez le premier nombre : "))
input2 = float(input("Entrez le deuxième nombre : "))

print()
print(calculs.addition(input1, input2))
print(calculs.soustraction(input1, input2))
print(calculs.multiplication(input1, input2))
print(calculs.division(input1, input2))
print()

rayon = float(input("Entrez le rayon du cercle : "))
print(aire_cercle(rayon))
print()

longueur = float(input("Entrez la longueur du rectangle : "))
largeur = float(input("Entrez la largeur du rectangle : "))
print(rectangle(longueur, largeur))



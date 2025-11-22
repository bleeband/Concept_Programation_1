
#   ENUMERATE

#   enumarate(iterable, depart = 0)

liste = list(enumerate("hello"))

print(liste)

for index, valeur in enumerate("hello"):
    print(f"l'index est : {index}, et la valeur est {valeur}")
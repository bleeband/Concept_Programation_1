# PARTIE 2 - PROGRAMMATION FONCTIONNELLE

la_liste = [1, 5, 7, 84, 52, 43]

def map_by(une_liste, une_fonction):
    nouvelle_liste = []
    for item in une_liste:
        nouvelle_liste.append(une_fonction(item))
    return nouvelle_liste

def multiplier_item(facteur):
    def multiplier(item):
        return item * facteur
    return multiplier

double = multiplier_item(2)
triple = multiplier_item(3)
quadruple = multiplier_item(4)
quintuple = multiplier_item(5)

print(map_by(la_liste, double))
print(map_by(la_liste, triple))
print(map_by(la_liste, quintuple))


# MAP

print(list(map(double, la_liste)))


# FILTER

def is_pair(item):
    return not item % 2    # item % 2 == 0

print("---- filter ----")
print(list(filter(is_pair, la_liste)))
print(tuple(filter(is_pair, la_liste)))
print(set(filter(is_pair, la_liste)))
print(filter(is_pair, la_liste))

def is_majeur(item):
    return item >= 18
print(list(filter(is_majeur, la_liste)))


# ZIP

la_liste_a = [1, 2, 3]
la_liste_b = ["a", "b", "c"]

print("---- zip ----")
print(list(zip(la_liste_a, la_liste_b, strict=True)))

la_liste_c = ["ID", "name", "email", "password"]
la_liste_d = ["12454", "Gerard", "bb@cc.com", "@123456$"]

print(list(zip(la_liste_c, la_liste_d)))



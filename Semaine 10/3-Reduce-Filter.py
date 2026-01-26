from functools import reduce

# PARTIE 3 - PROGRAMMATION FONCTIONNELLE

# --- REDUCE permet de reduire une sequence itérable à une seule valeur
print("\n-------- REDUCE -------- ")
panier = [
    {"nom": "pomme", "prix": 1.48, "quantité": 4},
    {"nom": "banane", "prix": 1.17, "quantité": 6},
    {"nom": "poulet", "prix": 11.45, "quantité": 4},    
    {"nom": "celeri", "prix": 2.28, "quantité": 2},    
]

def fn(treduce, item):
    return treduce + item["prix"] * item["quantité"]

def fn1(acc, item):
    acc["total_price"] += item["prix"] * item["quantité"]
    acc["total_quantite"] += item["quantité"]
    return acc

total = reduce(fn, panier, 0)
print(total)

total1 = reduce(fn1, panier, {"total_price": 0, "total_quantite": 0})
print(total1)


# ---- FONCTION LAMBDA ----
print("\n-------- LAMBDA -------- ")
# lambda param1, param 2 ... : expression

a = [1, 2, 3]
b = map(lambda x: x*2, a)
print(list(b))

total2 = reduce(lambda treduce, item: treduce + item['prix'] * item['quantité'], panier, 0)
print(total2)

#  EXERCICE
# Trouver les nombre pairs d'une liste, en ecrivant une seul ligne

liste1 = [1, 25, 14, 45, 78, 102, 145, 56]

print(list(filter(lambda x: x % 2 == 0, liste1)))

# def multiply_by(factor):
#     def multiply(item):
#         return item * factor
#     return multiply

def multiply_by_(factor):
    return lambda item : factor*item

double = multiply_by_(2)
print(double(50))
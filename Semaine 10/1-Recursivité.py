#  PROGRAMMATIUON FONCTIONNELLE PURE

liste = [1, 2, 3, 4, 5]
    
def doubler_liste(une_liste):
    nouvelle_liste = []
    for item in une_liste:
        nouvelle_liste.append(item * 2)

    return nouvelle_liste

def tripler_liste(une_liste):
    nouvelle_liste = []
    for item in une_liste:
        nouvelle_liste.append(item * 3)

    return nouvelle_liste

def quadrupler_liste(une_liste):
    nouvelle_liste = []
    for item in une_liste:
        nouvelle_liste.append(item * 4)

    return nouvelle_liste

def multiplier_liste(facteur):
    def multiplier(une_liste):
        nouvelle_liste = []
        for item in une_liste:
            nouvelle_liste.append(item * facteur)
            return nouvelle_liste
    return multiplier

multiplier_par_deux = multiplier_liste(2)
multiplier_par_trois = multiplier_liste(3)
multiplier_par_quatre = multiplier_liste(4)

print(multiplier_par_deux(liste))
print(multiplier_par_trois(liste))
print(multiplier_par_quatre(liste))

print(liste)  # La liste originale reste inchangée
print("-----")


# LA RECURSIVITE

# def fonction_recursive(parametre):
#     # 1. CAS DE BASE (condition d'arrêt)
#     if condition_simple:
#         return valeur_simple

#     # 2. APPEL RÉCURSIF (cas général)
#     #    Réduire le problème vers le cas de base
#     resultat_partiel = fonction_recursive(parametre_reduit)

#     # 3. COMBINAISON DES RÉSULTATS
#     return combiner(parametre, resultat_partiel)


la_liste = [1, 5, 7, 15]

def sum(une_liste):
    total = 0
    for item in une_liste:
        total += item
    return total

print(sum(liste))

def sum_recursif(une_liste):
    if une_liste:
        return une_liste[0] + sum_recursif(une_liste[1:])
    else:
        return 0

def sum_rec(une_liste):
    return une_liste[0] + sum_recursif(une_liste[1:]) if une_liste else 0

print(sum_rec(la_liste))
print(sum_recursif(la_liste))
# 1 + sum_recursif(5, 7, 15)
#       5 + sum_recursif(7, 15)
#           7 + sum_recursif(15)
#               15 + sum_recursif() -> None
#                    15  + 0



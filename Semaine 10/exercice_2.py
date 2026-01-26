# ## **Exercices de Récursivité en Python**

# ### **Niveau 1 : Récursivité Fondamentale**

# **Exercice 1.1 : Somme des n premiers nombres**
# Écrivez une fonction récursive `somme(n)` qui calcule la somme des nombres de 1 à n.
def somme(n):
    if n <= 0:
        return 0  # Cas de base : la somme jusqu'à 0 est 0
    return n + somme(n - 1)  # Cas récursif : n + somme des nombres avant n

# # Test
print(somme(5))   # 15 (1+2+3+4+5)
print(somme(10))  # 55

# **Exercice 1.2 : Factorielle**
# Implémentez la fonction factorielle de façon récursive.
def factorielle(n):
    if n == 0:
        return 1  # Cas de base : 0! = 1
    return n * factorielle(n - 1)  # Cas récursif : n! = n * (n-1)!

# # Test
print(factorielle(5))   # 120 (5*4*3*2*1)
print(factorielle(0))   # 1 (par définition)

# **Exercice 1.3 : Puissance**
# Créez une fonction récursive `puissance(x, n)` qui calcule x^n.
def puissance(x, n):
    if n == 0:
        return 1  # Cas de base : x^0 = 1
    return x * puissance(x, n - 1)  # Cas récursif : x^n = x * x^(n-1)

# # Test
print(puissance(2, 3))   # 8
print(puissance(5, 0))   # 1


# ### **Niveau 2 : Récursivité sur les Chaînes**

# **Exercice 2.1 : Inverser une chaîne**
# Écrivez une fonction récursive qui inverse une chaîne de caractères.
def inverser(s):
    if s == "":
        return ""  # Cas de base : une chaîne vide est déjà inversée
    return s[-1] + inverser(s[:-1])  # On prend le dernier caractère et on inverse le reste

# # Test
print(inverser("python"))    # "nohtyp"
print(inverser("recursif"))  # "fisrucer"

# **Exercice 2.2 : Compter les occurrences**
# Comptez récursivement le nombre d'occurrences d'un caractère dans une chaîne.
def compter_occurrences(s, c):
    if s == "":
        return 0  # Cas de base : chaîne vide = 0 occurrence
    return (1 if s[0] == c else 0) + compter_occurrences(s[1:], c)  # On compte le premier caractère puis le reste

# # Test
print(compter_occurrences("programmation", 'm'))  # 2
print(compter_occurrences("recursivite", 'r'))    # 2

# **Exercice 2.3 : Vérifier palindrome**
# Vérifiez si une chaîne est un palindrome (se lit pareil dans les deux sens).
def est_palindrome(s):
    if len(s) <= 1:
        return True  # Cas de base : chaîne vide ou d'un caractère = palindrome
    if s[0] != s[-1]:
        return False  # Si les extrémités sont différentes, ce n'est pas un palindrome
    return est_palindrome(s[1:-1])  # Vérifie le reste de la chaîne

# # Test
print(est_palindrome("radar"))    # True
print(est_palindrome("python"))   # False
print(est_palindrome(""))         # True


# ### **Niveau 3 : Récursivité sur les Listes**

# **Exercice 3.1 : Somme d'une liste**
# Calculez récursivement la somme des éléments d'une liste.
def somme_liste(lst):
    if not lst:
        return 0  # Cas de base : liste vide = somme 0
    return lst[0] + somme_liste(lst[1:])  # Premier élément + somme du reste

# # Test
print(somme_liste([1, 2, 3, 4, 5]))      # 15
print(somme_liste([10, -2, 8]))         # 16
print(somme_liste([]))                  # 0


# **Exercice 3.2 : Maximum d'une liste**
# Trouvez le maximum d'une liste de façon récursive.
def maximum_liste(lst):
    if len(lst) == 1:
        return lst[0]  # Cas de base : une seule valeur = max
    max_reste = maximum_liste(lst[1:])  # Maximum du reste
    return lst[0] if lst[0] > max_reste else max_reste  # On compare avec le premier élément

# # Test
print(maximum_liste([3, 7, 2, 9, 1]))    # 9
print(maximum_liste([-5, -2, -10]))     # -2


# **Exercice 3.3 : Recherche dans une liste**
# Recherchez récursivement si un élément est présent dans une liste.
def rechercher(lst, valeur):
    if not lst:
        return False  # Cas de base : liste vide = pas trouvé
    if lst[0] == valeur:
        return True   # Trouvé !
    return rechercher(lst[1:], valeur)  # On cherche dans le reste

# # Test
print(rechercher([1, 2, 3, 4, 5], 3))   # True
print(rechercher([1, 2, 3, 4, 5], 6))   # False


# ### **Niveau 4 : Récursivité Mathématique Avancée**

# **Exercice 4.1 : Suite de Fibonacci**
# Générez le n-ième terme de la suite de Fibonacci.
def fibonacci(n):
    if n == 0:
        return 0  # Cas de base
    if n == 1:
        return 1  # Cas de base
    return fibonacci(n-1) + fibonacci(n-2)  # Somme des deux termes précédents

# # Test
print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(6))   # 8 (0,1,1,2,3,5,8)


# **Exercice 4.2 : PGCD (Algorithme d'Euclide)**
# Calculez le PGCD de deux nombres avec l'algorithme d'Euclide récursif.
def pgcd(a, b):
    if b == 0:
        return a  # Cas de base : le reste = 0
    return pgcd(b, a % b)  # On remplace a par b et b par le reste

# # Test
print(pgcd(48, 18))    # 6
print(pgcd(1071, 462)) # 21


# **Exercice 4.3 : Tours de Hanoï**
# Résolvez le problème des Tours de Hanoï pour n disques.

# # Test
def hanoi(n, depart, intermediaire, arrivee):
    if n == 1:
        print(f"Déplacer le disque 1 de {depart} vers {arrivee}")
        return
    # Déplacer n-1 disques vers la tour intermédiaire
    hanoi(n-1, depart, arrivee, intermediaire)
    # Déplacer le plus grand disque vers la tour d’arrivée
    print(f"Déplacer le disque {n} de {depart} vers {arrivee}")
    # Déplacer les n-1 disques de la tour intermédiaire vers la tour d’arrivée
    hanoi(n-1, intermediaire, depart, arrivee)


hanoi(3, 'A', 'B', 'C')
# # Doit afficher les déplacements nécessaires


# ### **Niveau 5 : Récursivité sur les Structures Arborescentes**

# **Exercice 5.1 : Profondeur d'une structure imbriquée**
# Calculez la profondeur maximale d'une liste pouvant contenir d'autres listes.
def profondeur(lst):
    if not isinstance(lst, list) or not lst:
        return 1
    return 1 + max((profondeur(item) for item in lst if isinstance(item, list)), default=0)
# # Test
print(profondeur([1, [2, [3, 4], 5], 6]))  # 3
print(profondeur([1, 2, 3]))               # 1
print(profondeur([]))                      # 1


# **Exercice 5.2 : Aplatir une liste**
# Aplatissez récursivement une liste contenant potentiellement d'autres listes.
def aplatir(lst):
    return [x for item in lst for x in (aplatir(item) if isinstance(item, list) else [item])]

# # Test
print(aplatir([1, [2, [3, 4], 5], 6]))
# [1, 2, 3, 4, 5, 6]


# **Exercice 5.3 : Parcours d'arbre binaire**
# Créez une fonction qui retourne tous les éléments d'un arbre binaire.

def parcours_prefixe(noeud):
    if noeud is None:
        return []  # Cas de base : nœud vide
    # Préfixe : racine -> gauche -> droite
    return [noeud.valeur] + parcours_prefixe(noeud.gauche) + parcours_prefixe(noeud.droite)

# # Structure de nœud
class Noeud:
    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite

# # Test
arbre = Noeud(1, Noeud(2, Noeud(4), Noeud(5)), Noeud(3))
print(parcours_prefixe(arbre))  # [1, 2, 4, 5, 3]


# ### **Niveau 6 : Défis Récursifs**

# **Exercice 6.1 : Sous-ensembles**
# Générez tous les sous-ensembles d'un ensemble donné.
def sous_ensembles(ensemble):
    if not ensemble:
        return [[]]  # Cas de base : l'ensemble vide a un seul sous-ensemble, lui-même
    premier = ensemble[0]
    reste = ensemble[1:]
    sous_reste = sous_ensembles(reste)
    # Pour chaque sous-ensemble du reste, on peut soit l'inclure, soit ne pas l'inclure le premier élément
    return sous_reste + [[premier] + s for s in sous_reste]
# # Test
print(sous_ensembles([1, 2, 3])) # [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]


# **Exercice 6.2 : Permutations**
# Générez toutes les permutations d'une liste.
def permutations(lst):
    if not lst:
        return [[]]  # Cas de base : la permutation d'une liste vide est [[]]
    resultat = []
    for i, elem in enumerate(lst):
        reste = lst[:i] + lst[i+1:]  # On enlève l'élément courant
        for p in permutations(reste):
            resultat.append([elem] + p)
    return resultat
# # Test
print(permutations([1, 2, 3])) # [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

# **Exercice 6.3 : Retour sur trace (Backtracking)**
# Résolvez le problème des N reines sur un échiquier N×N.
def n_reines(n):
    solutions = []

    def est_valide(position, ligne, colonne):
        for l, c in enumerate(position):
            if c == colonne or abs(l - ligne) == abs(c - colonne):
                return False
        return True

    def placer(position=[], ligne=0):
        if ligne == n:
            solutions.append(position[:])  # On a placé toutes les reines
            return
        for col in range(n):
            if est_valide(position, ligne, col):
                position.append(col)
                placer(position, ligne + 1)
                position.pop()  # backtrack

    placer()
    return solutions

solutions = n_reines(4)
print(f"Nombre de solutions pour 4 reines: {len(solutions)}")


# ### **Niveau 7 : Optimisation et Mémoïsation**

# **Exercice 7.1 : Fibonacci avec mémoïsation**
# Améliorez la fonction Fibonacci avec un dictionnaire pour stocker les résultats intermédiaires.
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]  # On renvoie le résultat déjà calculé
    if n == 0:
        memo[0] = 0
    elif n == 1:
        memo[1] = 1
    else:
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]
# # Test
print(fibonacci_memo(50))  # Doit être rapide

# **Exercice 7.2 : Combinaisons (Coefficient binomial)**
# Calculez C(n, k) = n!/(k!(n-k)!) de façon récursive avec mémoïsation.
def evaluer(expr):
    expr = expr.replace(" ", "")  # supprimer les espaces

    def parser(s):
        # Fonction récursive qui évalue une expression sans parenthèses
        def calculer_terme(i):
            # Parse un nombre ou une parenthèse
            if s[i] == '(':
                j = i + 1
                count = 1
                while count > 0:
                    if s[j] == '(':
                        count += 1
                    elif s[j] == ')':
                        count -= 1
                    j += 1
                val = parser(s[i+1:j-1])
                return val, j
            # Sinon nombre
            j = i
            while j < len(s) and (s[j].isdigit() or s[j]=='.'):
                j += 1
            val = float(s[i:j]) if '.' in s[i:j] else int(s[i:j])
            return val, j

        # Gestion des * et / avec récursion
        def calculer_facteurs(i):
            val, i = calculer_terme(i)
            while i < len(s) and s[i] in '*/':
                op = s[i]
                droite, i = calculer_terme(i+1)
                val = val * droite if op=='*' else val / droite
            return val, i

        # Gestion des + et -
        i = 0
        val, i = calculer_facteurs(i)
        while i < len(s):
            op = s[i]
            droite, i = calculer_facteurs(i+1)
            val = val + droite if op=='+' else val - droite
        return val

    return parser(expr)

# # Test
print(evaluer("(2 + 3) * 4"))        # 20
print(evaluer("2 + 3 * 4"))          # 14
print(evaluer("((1+2)*(3+4))/2"))    # 10.5


# ------------------------------------------------------------

# ## **Indications et Bonnes Pratiques**

# ### **Structure Générale d'une Fonction Récursive**


# def fonction_recursive(parametre):
#     # 1. CAS DE BASE (condition d'arrêt)
#     if condition_simple:
#         return valeur_simple

#     # 2. APPEL RÉCURSIF (cas général)
#     #    Réduire le problème vers le cas de base
#     resultat_partiel = fonction_recursive(parametre_reduit)

#     # 3. COMBINAISON DES RÉSULTATS
#     return combiner(parametre, resultat_partiel)


# ### **Exemple Guidé : Exercice 1.1 (Somme des n premiers nombres)**

# def somme(n):
#     # Cas de base
#     if n <= 0:
#         return 0

#     # Appel récursif + combinaison
#     return n + somme(n - 1)

# # Traces d'exécution pour somme(3):
# # somme(3) = 3 + somme(2)
# # somme(2) = 2 + somme(1)
# # somme(1) = 1 + somme(0)
# # somme(0) = 0  ← Cas de base
# # Remontée: 1+0=1, 2+1=3, 3+3=6


# ### **Pièges Courants à Éviter**

# 1. **Oublier le cas de base** → récursion infinie
# 2. **Ne pas réduire suffisamment le problème** → récursion infinie
# 3. **Récursion trop profonde** → `RecursionError` (limite ~1000 appels)
# 4. **Duplication de calculs** → utiliser la mémoïsation

# ### **Conversion Itérative ↔ Récursive**

# Pour l'exercice 1.1 :


# # Version itérative
# def somme_iterative(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total

# # Version récursive
# def somme_recursive(n):
#     if n <= 0:
#         return 0
#     return n + somme_recursive(n-1)


# ## **Pour Aller Plus Loin**

# ### **Analyse de Complexité**

# Pour chaque exercice, essayez de déterminer :

# - Complexité temporelle (O(n), O(2^n), etc.)
# - Complexité spatiale (pile d'appels)
# - Possibilité d'optimisation (tail recursion, mémoïsation)

# ### **Débuggage Récursif**

# Ajoutez des `print()` pour tracer l'exécution :

def somme_debug(n, profondeur=0):
    indentation = "  " * profondeur
    print(f"{indentation}somme({n}) appelé")

    if n <= 0:
        print(f"{indentation}→ retourne 0")
        return 0

    resultat = n + somme_debug(n-1, profondeur+1)
    print(f"{indentation}→ retourne {resultat}")
    return resultat

somme_debug(3)

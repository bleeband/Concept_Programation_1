# operateur logiques

# a = 1
# b = 1

a = [1, 2]
b = [1, 2]
c = 1
d = 1


print(a ==  b)
print(a is b)
print(c is d)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
# print( a< b)
# print(a <= b)
# print(a > b)
# print(a >= b)
# print( a != b)

# OPERATEURS

a = 1 + 2
a = 1 + 2 * 4

# x = a + "test"
x = a + 1.5
x = a + True

x = 'je suis un ' + 'test'
x = [1] + [2, 3]

y = 12 + int(1.2)
z = 13

chaine = 'vendredi ' + str(z)
chaine = int("13") + 1

print(chaine)


# Les opérateurs d'affectation

# Un opérateur d'affectation assigne une valeur à son élément de gauche en utilisant
# la valeurde l'élément de droite

# Nous en avons vu un pour le moment :

# a = 42
# print(a)

# = assigne 42 à l'élément de gauche a

# Il en existe de nombreux autres mais seuls quelques uns sont utilisés fréquemment :

# a = 1
# a += 2
# print(a)

# += est l'opérateur d'affectation après addition. Il est en fait un raccourci pour x = x + n.

# -= est l'opérateur d'affectation après soustraction. Il est un raccourci pour x = x - n.

# Un autre exemple est l'opérateur 

# **= qui est l'opérateur d'affectation après exponentiation.
# Il permet de d'abord d'élever à la puissance spécifiée et d'affecter le résultat à la variable.
# Il est le raccourci de  x = x ** n.

# a = 2
# a **= 3
# print(a) # 8

# Les autres opérateurs d'affectation sont 

# *= , /= , %= et //= 

# Les opérateurs de comparaison

# Ils permettent de comparer deux éléments et de renvoyer un booléen suivant le résultat :
# True ou False

# Ils permettent de voir si un élément est égal, inégal, inférieur, supérieur, 
# supérieur ou égal,inférieur ou égal à un autre élément.

# Nous les verrons en détail dans la formation. Mais voyons juste un exemple :

# a = 2
# b = 3
# print(a<b) # True

# Les autres opérateurs de comparaison sont

# <= , > , >= , == , != , <> , is et is not


# Les opérateurs arithmétiques

# Ils permettent d'effectuer des calculs arithmétiques entre deux éléments numériques
# (des entiers ou des nombres à virgule flottante).

# Ils permettent d'additionner, soustraire, multiplier, diviser ou
# de calculer le modulo (reste d'une opération).

# print(2+3)      # Addition => 5
# print(12-3)     # Soustraction => 9
# print(5*3)      # Multiplication => 15
# print(12/3)     # Division => 4.0
# print(22%6)     # Modulo => 4 (reste de la division)
# print(22//6)    # Division entière => 3
# print(2**3)     # 8
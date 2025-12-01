
#  ===  DECLARATION DES SETS ====

a = {1, 2, 4, 5, 11, "A", "B"}

# print(a)

# print(2 in a)

b = set([1, 5, 8, 79, 41, -63])

# print(b)


#  ==  LES METHODES DES SETS ==

# c = b.copy()

# print(c)

# c.add(100)
# print(c)

# c.remove(100)
# print(c)

# c.discard(3)
# print(c)


#  ==  LA METHODE POP ==

# resultat = b.pop()
# print(resultat)

# b.update([11, 5, 4, 88, 54, -63])
# print(b)


#  ==  LA PARTIE INTERESSANTE DES SETS ===

e = {1, 2, "o", "b", 41, -5, 8}
f = {9, 10, "h", -5, "b", "n"}

# g = e.intersection(f)
# print(g)

# h = e & f
# print(h)

# m = e.intersection_update(f)
# print(m)

# i = e.union(f)
# print(i)

# j = e|f
# print(j)

# k = e.difference(f)
# print(k)


#  === isdijoint, issibset, issuperset ===

# print(e.isdisjoint(f))
# print((e.difference(f).isdisjoint(f)))

# print(e.issubset(f))
# print((e.intersection(f).issubset(f)))

# print(e.issuperset(f))
# print((e.union(f)).issuperset(f))


import copy

#--------------------------------
#   LISTE  []

# a = [1, 2 , "hello", 1.2, [1, 2], True]
# b = list("hello")
# c = list(range(0,10,2))

# print(a)
# print(b)
# print(c)

#-----------------------------------------
# #   INDEX SUR LISTE

# for i in a:
#     print(i)

# for i, val in enumerate(a):
#     print(i, val)

# a[2] = "lilia"
# print(a, a[2])
# print(a[:-1])
# print(a[::-1])

#----------------------------------------
#    DECOMPACTAGE

# x = ["q", "w", "e", "r", "t", "y"]
# a = x[0]
# b = x[1]
# c = x[2]

# a, b, c, *d = x
# a, b, *d, e, f = x


# print(a, b, d, e, f)

# a, b, c = "Bleu", "Rouge", "Vert"
# print(a,b,c)


#-----------------------------------------------
#  LES OPERATIONS SUR LES LISTES ET LES COPIES

x = ["1", "2", "Coucou"]
y = [True, 25, [1, 102]]
z = x + y

# print(z)

d = x
#  x    $x    $ox     PyObject X
#  d    $d    $ox     PyObject X

# print(d is x)
# d[2] = "Changement"
# print(x)
# print(x is d)


#-------------------------------------------------
#       COPIE

# e = x[:]
# print(x)
# e[2] = "un autre changement"
# print(x)
# print(e)

#  : --> shallow copie
# y = ["1", "un", 1, True, ["une ","super ","liste "]]
# f = y.copy()            # équivalent de :
# f[2] = "changement"
# f[-1][1] = "done"

# print(y)
# print(f)

# q = ["1", "un", 1, True, ["une ","super ","liste "]]
# w = copy.deepcopy(q)            # équivalent de :
# w[2] = "changement"
# w[-1][1] = "done"

# print(q)
# print(w)


#----------------------------------------------------
#   FONCTION NATIVES ET AJOUTER DES ELEMENTS

# liste = [1, 2, 3, 4, 5]

# print(len(liste))
# print(sum(liste))
# print(max(liste))
# print(min(liste))

# result = liste.append(6)
# print(liste)
# print(result)

# liste.insert(0, 0)
# print(liste)

# liste.insert(0, "start")
# print(liste)

# print(liste + [7, 8, 9])
# print(liste)
# liste.extend([7, 8, 9])
# print(liste)

#-------------------------------------------
#   SUPPRIMER DES ELEMENT DUNE LISTE

# n = ["une", "liste", 2, True, 0.2 , 2 , 15]
# print(n)
# n.remove(2)
# print(n)

# n.pop()
# print(n)

# m = n.pop(0)
# print(n)
# print(m)


#--------------------------------------------
#   RECHERCHE DANS UNE LISTE

# a = [1, 2, 3, "a", "b", [1,2]]
# b = a.index("a",2 ,5)
# print(b)

# if "a" in a[2:5]:
#     b = a.index("a",2 ,5)
#     print("dans la condition du if", b)

# print([1,2] in a)


#--------------------------------------------
#  TRIER DES LISTES

# a = [1, 2, 3, 88, 23, 44]
# n = ["une", "liste", "2", "True", "0.2" , "15"]

# a.sort()
# n.sort()
# print(a)
# print(n)


#----------------------------------------------
#   JOIN

# liste = ["une ", "fabuleuse ", "soirée! "]
# print("".join(liste))


#--------------------------------------------
#   REVERSE

# a = [1, 2, 3, 88, 23, 44]
# a.reverse
# print(a)


#--------------------------------------------
#   SORTED  ( SHALLOW COPY )

# a = [1, 2, 3, 88, 23, 44]
# print(sorted(a))


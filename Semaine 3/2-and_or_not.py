# NOTE COUR 4

# ----------------------------------------------------------------------------------
# STRUCTURE DE CONTROLE

# AND or NOT

is_inscrit = True
is_25604 = True
condition = 22

# if is_inscrit and is_25604:
#     print("L'étudiant est inscrit au cours 25604")

# else:
#     print("Contacter l'administration svp")    

# # print( True and True )      #True
# # print( True and False )     #False
# # print( False and True )     #False
# # print( False and False )    #False

# if is_inscrit or is_25604:
#     print("Bienvenue à Maisonneuve")
# else:
#     print("Contacter l'administration")

# print( True or True )      #True
# print( True or False )     #False
# print( False or True )     #False
# print( False or False )    #False

print(not True)
print(not False)

if not (condition < 18):
    print("Vous êtes majeur!!!")
else:
    print("Vous êtes mineur")
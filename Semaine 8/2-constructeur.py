#   *** LES CONSTRUCTEUR ***

# PASSER DES PARAMETRE AU CONSTRUCTEUR
class User():
    def __init__(self, name, email, age) -> None:
        #  ATTRIBUTS
        self.name = name
        self.email = email
        self.age = age        

#  INSTANCE de la CLASS USER
x = User("Mathieu", "ma@aa.com", 38)
y = User("Eva", "eva@ga.com", 26)

print(x.name)
print(x.email)
print(x.age)
print(y.name)
print(y.email)
print(y.age)
#  *** LES METHODES ***
name = "marc"

class User():
    def __init__(self, name, email, age) -> None:
        #  ATTRIBUTS
        self.name = name
        self.email = email
        self.age = age        

    def bonjour(self, short:bool=False) -> None:
        if short :
            print("Bonjour")
        else:
            print(f"Bonjour, je suis {self.name}.")
        return short

z = User("clement", "cc@cc.com", 22)
resultat = z.bonjour()
print(resultat)
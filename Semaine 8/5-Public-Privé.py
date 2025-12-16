#    ****  PRIVE PUBLIC ***

class User():

    ban = False
    
    def __init__(self, name, email, age) -> None:
        #  ATTRIBUTS
        self.name = name
        self.email = email
        self.age = age        

    def _say_hi(self):
        print("Oh ! Hi !")
    
    def bonjour(self, short:bool=False) :
        if short:
            self._say_hi()
        else:
            print(f"Bonjour, je suis {self.name}")



r = User("Neil", "neil@gg.com", 25)
# print(r._say_hi())

# r._say_hi = "Je suis une chaine de caractere"
# print(r._say_hi)

r.bonjour(False)

print(dir(r))
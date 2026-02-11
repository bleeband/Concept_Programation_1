
class Vehicules:

    def __init__(self, marque, modèle, année):
        self.marque = marque
        self.modèle = modèle
        self.année = année

    def se_decrire(self):
        print(f"{self.marque} {self.modèle} ({self.année}) ")

    def vieillir(self):
        self.année += 1
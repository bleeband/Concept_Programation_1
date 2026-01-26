# Projet réalisé par Marc-André Dufour  
# © 2025 — Fait avec du café, du code et un peu de rage contrôlée

# ETAPE 4

class Vehicule:

    _vehicules_crees = []

    def __init__(self, marque, modele, annee, immatriculation):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.immatriculation = immatriculation
        self._en_marche = False

        Vehicule._vehicules_crees.append(self)

    def se_decrire(self):
        return f"Marque : {self.marque} - modèle : {self.modele} - année : {self.annee}, immatriculation : {self.immatriculation}"

    def demarrer(self):
        if not self._en_marche:
            self._en_marche = True
            print(f"Le véhicule {self.immatriculation} démarre.")
        else:
            print(f"Le véhicule {self.immatriculation} est déjà en marche.")

    def arreter(self):
        if self._en_marche:
            self._en_marche = False
            print(f"Le véhicule {self.immatriculation} est arrêté.")
        else:
            print(f"Le véhicule {self.immatriculation} est déjà arrêté.")

    @classmethod
    def afficher_flotte(cls):
        for vehicule in cls._vehicules_crees:
            etat = "en marche" if vehicule._en_marche else "à l'arrêt"
            print(f"{vehicule.immatriculation} : {etat}")

    @staticmethod
    def verifier_immatriculation(immat):
        return "-" in immat

class Voiture(Vehicule):

    def __init__(self,marque, modele, annee, immatriculation, nombres_portes):
        super().__init__(marque, modele, annee, immatriculation)
        self.nombres_portes = nombres_portes

    def se_decrire(self):
        return super().se_decrire() + f" | Portes : {self.nombres_portes}"


class Camion(Vehicule):

    def __init__(self, marque, modele, annee, immatriculation, charge_utile):
        super().__init__(marque, modele, annee, immatriculation)
        self.charge_utile = charge_utile    # (en tonnes)

    def se_decrire(self):
        return super().se_decrire() + f" | Charge utile : {self.charge_utile}t"
    
    def demarrer(self):
        if not self._en_marche:
            self._en_marche = True
            print(f"Le camion {self.immatriculation} démarre avec un grondement.")
        else:
            print(f"Le véhicule {self.immatriculation} est déjà en marche.")


# === TEST === 

v1 = Voiture("Peugeot", "308", 2021, "EF-456-GH", 5)
v2 = Camion("Renault", "T", 2020, "ZZ-TOP-01", 15)
v1.demarrer()
Vehicule.afficher_flotte()
print(Vehicule.verifier_immatriculation("123456"))  # False
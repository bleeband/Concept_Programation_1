# Projet réalisé par Marc-André Dufour  
# © 2025 — Fait avec du café, du code et un peu de rage contrôlée

# ETAPE 3

class Vehicule:
    def __init__(self, marque, modele, annee, immatriculation):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.immatriculation = immatriculation
        self._en_marche = False  # attribut "privé"

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
        return super().se_decrire() + f" | Charge utile: {self.charge_utile} t"
    
    def demarrer(self):
        if not self._en_marche:
            self._en_marche = True
            print(f"Le camion {self.immatriculation} démarre avec un grondement.")
        else:
            print(f"Le véhicule {self.immatriculation} est déjà en marche.")


# === TEST === c = Camion("Volvo", "FH16", 2019, "XX-999-YY", 19)
c = Camion("Volvo", "FH16", 2019, "XX-999-YY", 19)
c.demarrer()  # "Le camion XX-999-YY démarre avec un grondement."
c.demarrer()  # "Le véhicule XX-999-YY est déjà en marche." (Logique de Vehicule)
c.arreter()
c.demarrer()  # Message spécifique du camion à nouveau
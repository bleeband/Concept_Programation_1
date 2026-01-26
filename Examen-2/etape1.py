# Projet réalisé par Marc-André Dufour  
# © 2025 — Fait avec du café, du code et un peu de rage contrôlée

# ETAPE 1

class Vehicule:
    def __init__(self, marque, modele, annee, immatriculation):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.immatriculation = immatriculation

    def se_decrire(self):
        return f"Marque : {self.marque} - modèle : {self.modele} - année : {self.annee}, immatriculation : {self.immatriculation}"

    def demarrer(self):
        print(f"Le véhicule {self.immatriculation} démarre")


# === TEST ===

v = Vehicule("Renault", "Clio", 2020, "AB-123-CD")
print(v.se_decrire())
v.demarrer()

class Utilisateur:
    def __init__(self, nom, prenom, email):
        self.nom = nom
        self.prenom = prenom
        self.email = email

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.email})"
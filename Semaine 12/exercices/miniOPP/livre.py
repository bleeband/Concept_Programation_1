class Livre():
    def __init__(self, titre, auteur, statut="disponible"):
        self.titre = titre
        self.auteur = auteur
        self.statut = statut

    def emprunter(self):
        if self.statut == "disponible":
            self.statut = "emprunté"
            print(f"Vous avez emprunté {self.titre} de {self.auteur}.")
        else:
            print(f"Désolé, {self.titre} de {self.auteur} est déjà emprunté.")  

    def retourner(self):
        if self.statut == "emprunté":
            self.statut = "disponible"
            print(f"Vous avez retourné {self.titre} de {self.auteur}.")
        else:
            print(f"{self.titre} de {self.auteur} n'était pas emprunté.")
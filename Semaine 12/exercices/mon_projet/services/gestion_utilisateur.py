class GestionUtilisateurs:
    def __init__(self):
        self.utilisateurs = []

    def ajouter(self, utilisateur):
        self.utilisateurs.append(utilisateur)

    def afficher(self):
        for u in self.utilisateurs:
            print(u.nom, "-", u.email)
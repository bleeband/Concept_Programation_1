from models.utilisateur import Utilisateur
from services.gestion_utilisateur import GestionUtilisateurs
from utils.validations import email_valide

gestion = GestionUtilisateurs()

u1 = Utilisateur("Marc","Dufour", "bob@cc.com")
u2 = Utilisateur("Sophie","Lavoie", "sophie@cc.com")
u3 = Utilisateur("Pierre","Dupont", "pierre;cc.com")

if email_valide(u1.email):
    gestion.ajouter(u1)
    
if email_valide(u2.email):
    gestion.ajouter(u2)

if email_valide(u3.email):
    gestion.ajouter(u3)

gestion.afficher()
from livre import Livre
from gestion import Bibliotheque


bibliotheque = Bibliotheque()

livre1 = Livre(f"Harry Potter", "J.K. Rowling", "disponible")
livre2 = Livre(f"2020 l'odyssée de l'espace", "Albert Trottier", "emprunté")

bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
print()

print("Livres disponibles dans la bibliothèque :")
bibliotheque.afficher_livres()
print()

livre1.emprunter()
livre1.emprunter()
livre2.emprunter()
print()

livre1.retourner()
livre1.retourner()

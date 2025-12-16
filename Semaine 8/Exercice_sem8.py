# # Exercices sur les Classes en Python

# ## Exercice 1 : Introduction aux Classes

# ### 1.1 : Code à Développer

# Créez une classe `Personne` très simple avec seulement une méthode `se_presenter()` qui affiche "Je suis une personne".

""" class Personne():
    def se_presenter(self) -> None:
        print("Je suis une personne")

x = Personne()
z = x.se_presenter() """


# ### 1.2 : Code à Finaliser
# # Complétez cette classe

""" class Accueil():
    def dire_bonjour(self):
        print("Bonjour !")

# Créez une instance et appelez la méthode

personne = Accueil()
personne.dire_bonjour """

# ### 1.3 : Code à Corriger
# # Ce code contient des erreurs de syntaxe de classe

""" class Animal():
    def faire_du_bruit(self):
        print("Bruit d'animal")

mon_animal = Animal()
mon_animal.faire_du_bruit() """


# ## Exercice 2 : La méthode **init**()

# ### 2.1 : Code à Développer


# Créez une classe `Livre` avec `__init__()` qui initialise `titre` et `auteur`. Créez deux livres différents.

""" class Livre():
    def __init__(self, titre, auteur) -> None:
        #  ATTRIBUTS
        self.titre = titre
        self.auteur = auteur

a = Livre("HP1", "JKR")
b = Livre("HP2", "JKR")

print(a.titre, a.auteur)
print(b.titre, b.auteur)
 """

# ### 2.2 : Code à Finaliser

""" class Etudiant():
    def __init__(self, nom, age) -> None:
        self.nom = nom
        self.age = age

# Créez un étudiant
etudiant1 = Etudiant("Alice", 20)
print(f"Nom: {etudiant1.nom} Age: {etudiant1.age}") """


# ### 2.3 : Code à Corriger

""" class Voiture():
    def __init__(self, marque, modele) -> None:
        self.marque = marque
        self.modele = modele

voiture1 = Voiture("Toyota", "Corolla")
print(f"{voiture1.marque}, {voiture1.modele}") """


# ## Exercice 3 : Méthodes d'Instance

# ### 3.1 : Code à Développer

# Créez une classe `CompteBancaire` avec :

# - __init__() qui initialise `titulaire` et `solde` (par défaut 0)
# - deposer(montant)` qui ajoute au solde
# - retirer(montant)` qui retire si possible
# - afficher_solde()` qui affiche le solde

""" class CompteBancaire():
    def __init__(self, titulaire, solde=0) -> None:
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant) -> None:
        if montant > 0:
            self.solde += montant
            print(f"{montant}$ déposés dans le compte de {self.titulaire}.")
        else:
            print("Montant invalide, voyons donc.")

    def retirer(self, montant) -> None:
        if montant <= 0:
            print("Montant invalide, tabarnak.")
        elif montant > self.solde:
            print("Fonds insuffisants. Ton compte pleure.")
        else:
            self.solde -= montant
            print(f"{montant}$ retirés du compte de {self.titulaire}.")

    def afficher_solde(self) -> None:
        print(f"Solde de {self.titulaire} : {self.solde}$")

t = CompteBancaire("Marc", 100)
s = CompteBancaire("Steph", 250)

t.afficher_solde()
t.deposer(50)
t.retirer(30)
t.afficher_solde()

s.retirer(300)
s.afficher_solde() """


# ### 3.2 : Code à Finaliser

""" class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_perimetre(self):
        peri = (self.longueur + self.longueur)*2
        return peri

    def calculer_surface(self):
        aire = self.longueur * self.largeur
        return aire

# Test
rect = Rectangle(5, 3)
print(f"Périmètre: {rect.calculer_perimetre()}")
print(f"Surface: {rect.calculer_surface()}") """

# ### 3.3 : Code à Corriger

""" class Calculatrice:
    def __init__(self):
        self.resultat = 0

    def addition(self, a, b):
        self.resultat = a + b

    def soustraction(self, a, b):
        self.resultat = a - b

calc = Calculatrice()
calc.addition(5, 3)
print(calc.resultat)
calc.soustraction(5, 3)
print(calc.resultat) """


# ## Exercice 4 : Variables et Méthodes de Classe
# ### 4.1 : Code à Développer

# Créez une classe `Employe` avec :
# - Variable de classe `nombre_employes` qui compte les employés
# - `__init__()` qui incrémente le compteur
# - Méthode de classe `afficher_nombre()` qui affiche le total

""" class Employe():
    nb_employes = 0

    def __init__(self, nom, prenom, matricule):
        self.nom = nom
        self.prenom = prenom
        self.matricule = matricule
        Employe.nb_employes += 1

    @classmethod
    def afficher_nb_employes(cls):
        print(f"Nombre total d'employés : {cls.nb_employes}")

e1 = Employe("Tremblay", "Marc", 101)
e2 = Employe("Gagnon", "Steph", 102)

Employe.afficher_nb_employes()    """


# ### 4.2 : Code à Finaliser

""" class Produit():
    # Variable de classe pour le taux de TVA
    taux_tps = 0.15

    def __init__(self, nom, prix_ht):
        self.nom = nom
        self.prix_ht = prix_ht

    @classmethod
    def changer_tps(cls, nouveau_taux):
        Produit.taux_tps = nouveau_taux

    def prix_ttc(self):
        prix_total = ((self.prix_ht * Produit.taux_tps) * 1) + self.prix_ht
        return prix_total

# Test
Produit.changer_tps(0.15)
p = Produit("Livre", 20)
print(f"Prix TTC: {p.prix_ttc()}$") """


# ### 4.3 : Code à Corriger

""" class Mathematic():
    pi = 3.14159

    def __init__(self):
        self.pi = 22/7

    @staticmethod
    def carre(x):
        return x * x

math = Mathematic()
print(math.pi)
print(math.carre(5))
print(Mathematic.pi) """


# ## Exercice 5 : Méthodes Statiques
# ### 5.1 : Code à Développer
# Créez une classe `Utilitaire` avec des méthodes statiques :

# - `est_pair(nombre)` retourne True si pair
# - `celsius_vers_fahrenheit(celsius)` fait la conversion
# - `est_email_valide(email)` vérifie basiquement un email

""" class Utilitaire():

    @staticmethod
    def est_pair(nombre):
        return nombre % 2 == 0

    @staticmethod
    def celsius_vers_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def est_email_valide(email):
        return "@" in email and "." in email

print(Utilitaire.est_pair(4))
print(Utilitaire.est_pair(7))

print(Utilitaire.celsius_vers_fahrenheit(0))
print(Utilitaire.celsius_vers_fahrenheit(25))

print(Utilitaire.est_email_valide("test@mail.com"))
print(Utilitaire.est_email_valide("testmail.com"))
 """

# ### 5.2 : Code à Finaliser

""" class Validateur:
    @staticmethod
    def valid_nombre(nombre):
        return nombre > 0

    @staticmethod
    def valid_texte(texte):
        return len(texte) >= 20

# Utilisation sans instance
if Validateur.valid_nombre(-11):
    print("Nombre valide")
else:
    print("Nombre invalide")

if Validateur.valid_texte("Je suis un texte"):
    print("Texte valide")
else:
    print("Texte invalide") """


# ### 5.3 : Code à Corriger

""" class Formateur():

    @staticmethod
    def majuscule(texte):
        return texte.upper()

    @staticmethod
    def minuscule(texte):
        return texte.lower()

# Problème ici
resultat = Formateur.majuscule("test")
print(resultat)
resultat2 = Formateur.minuscule("TEST")
print(resultat2) """


# ## Exercice 6 : Propriétés Publiques et Privées
# ### 6.1 : Code à Développer
# Créez une classe `CompteSecre` avec :

# - Attribut privé `__code_secret`
# - Méthode publique `verifier_code(code)` pour vérifier
# - Méthode pour changer le code (avec vérification)

""" class CompteSecret:
    def __init__(self, code):
        self.__code = code   # attribut privé (name mangling)

    def __code_secret(self):
        return self.__code

    def verifier_code(self, code):
        return code == self.__code_secret()

    def changer_et_verif_code(self, ancien_code, nouveau_code):
        if self.verifier_code(ancien_code):
            self.__code = nouveau_code
            return True
        return False
    
c = CompteSecret("1234")

print(c.verifier_code("1234"))
print(c.verifier_code("0000"))

print(c.changer_et_verif_code("1234", "5678"))
print(c.verifier_code("5678")) """


# ### 6.2 : Code à Finaliser

""" class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius  # privé

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, valeur):
        if valeur < -273.15:
            print("Température impossible")
        else:
            self.__celsius = valeur
            print(f"Nouvelle température: {valeur}°C")

# Utilisation
temp = Temperature(25)
print(temp.get_celsius())

temp.set_celsius(30)
print(temp.get_celsius()) """


# ### 6.3 : Code à Corriger

""" class Compte:

    def __init__(self, solde):
        self.__solde = solde

    def afficher_solde(self):
        print(f"Solde: {self.__solde}")

    def __verifier_solde(self):
        return self.__solde > 0

    # Méthode publique
    def solde_positif(self):
        return self.__verifier_solde()

# Test
compte = Compte(100)
compte.afficher_solde()
print(compte.solde_positif()) """


# ## Exercice 7 : Projets Complets
# ### 7.1 : Système d'Inventaire (à Développer)
# Créez une classe `Produit` et une classe `Inventaire` :

# - `Produit` : nom, prix, quantité
# - `Inventaire` : liste de produits, méthodes pour ajouter, supprimer, chercher, calculer valeur totale

""" class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def __str__(self):
        return f"\n{self.nom} - Prix: {self.prix:.2f}$ - Quantité: {self.quantite}"

class Inventaire:
    def __init__(self, liste_de_produits=None):
        if liste_de_produits is None:
            self.liste_de_produits = []
        else:
            self.liste_de_produits = liste_de_produits

    def ajouter_produit(self, produit):
        self.liste_de_produits.append(produit)
        print(f"\nProduit {produit.nom} ajouté à l'inventaire")

    def supprimer_produit(self, nom):
        for produit in self.liste_de_produits:
            if produit.nom == nom:
                self.liste_de_produits.remove(produit)
                print(f"\nProduit {nom} supprimé de l'inventaire")
                return
        print(f"\nAucun {nom} dans l'inventaire")

    def chercher_produit(self, nom):
        for produit in self.liste_de_produits:
            if produit.nom == nom:
                return produit
        return None

    def total_produit(self):
        total = sum(produit.prix * produit.quantite for produit in self.liste_de_produits)
        return total

# Création de quelques produits
p1 = Produit("Stylo", 1.50, 10)
p2 = Produit("Cahier", 3.00, 5)

# Création de l'inventaire
inv = Inventaire()
inv.ajouter_produit(p1)
inv.ajouter_produit(p2)

# Chercher un produit
trouve = inv.chercher_produit("Stylo")
print(trouve)  # Stylo - Prix: 1.5$ - Quantité: 10

# Supprimer un produit
inv.supprimer_produit("Cahier")

# Total de l'inventaire
print("\nTotal inventaire :", inv.total_produit(), "$") """


# ### 7.2 : Gestion de Cours (à Finaliser)

""" class Etudiant:
    def __init__(self, nom):
        self.nom = nom
        self.notes = []

    def ajouter_note(self, note):
        self.notes.append(note)

    def moyenne(self):
        if not self.notes:
            return 0
        return sum(self.notes) / len(self.notes)

class Cours:
    def __init__(self, nom):
        self.nom = nom
        self.etudiants = []

    def inscrire(self, etudiant):
        self.etudiants.append(etudiant)

    def meilleur_etudiant(self):
        if not self.etudiants:
            return None
        return max(self.etudiants, key=lambda e: e.moyenne())
    
# Test
e1 = Etudiant("Alice")
e1.ajouter_note(15)
e1.ajouter_note(18)

e2 = Etudiant("Bob")
e2.ajouter_note(12)
e2.ajouter_note(14)

cours = Cours("Math")
cours.inscrire(e1)
cours.inscrire(e2)

meilleur = cours.meilleur_etudiant()
print(f"Meilleur étudiant : {meilleur.nom} avec une moyenne de {meilleur.moyenne()}")
 """


### 7.3 : Jeu de Cartes (à Corriger)

""" class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        self.cartes = []
        couleurs = ["Coeur", "Carreau", "Pique", "Trèfle"]
        for couleur in couleurs:
            for i in range(1, 14):
                self.cartes.append(Carte(i, couleur))

    def melanger(self):
        # Simulation simple
        import random
        random.shuffle(self.cartes)

jeu = Jeu()
jeu.melanger()
print(jeu.cartes[0]) """


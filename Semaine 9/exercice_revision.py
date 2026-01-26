
# Exercices de Révision (2h)

## Partie 1 : Problèmes Inversés (20 min)

### Exercice 1.1 : Devine le Code

# Sans exécuter, devine la sortie de ce code mystère

""" def mystere(a, b):
    result = []
    for i in range(len(a)):
        if a[i] not in b:
            result.append(a[i])
    return result

liste1 = [1, 2, 3, 4, 2, 3, 5]
liste2 = [2, 3, 6]
print(mystere(liste1, liste2))      # Attendu: [1, 4, 5] """


### Exercice 1.2 : Trouve l'Erreur

# Ce code devrait calculer les statistiques mais contient 3 erreurs

""" def statistiques(temperatures):
    max = temperatures[0]
    min = temperatures[0]

    for temp in temperatures:
        if temp > max
            max = temp
        if temp < min
            min = temp

    moyenne = sum(temperatures) / temperatures.len()

    return (moyenne, max, min) """

# Corrigez les 3 erreurs

""" def statistiques(temperatures):
    tmax = temperatures[0]
    tmin = temperatures[0]

    for temp in temperatures:
        if temp > tmax:
            tmax = temp
        if temp < tmin:
            tmin = temp

    moyenne = sum(temperatures) / len(temperatures)

    return (moyenne, tmax, tmin)
print(statistiques([23, 17, 21, 7, 25]))  # Testez la fonction corrigée """


## Partie 2 : Reconstruction (25 min)

### Exercice 2.1 : À Partir du Comportement

# Écrivez le code qui produit exactement cette sortie:
"""
=== CALCULATRICE ===
5 + 3 = 8
5 - 3 = 2
5 * 3 = 15
5 / 3 = 1.666...
Moyenne: 6.5

"""

# Votre code doit utiliser:
# - Des variables
# - Des calculs
# - Un formatage de strings

""" a = 5
b = 3

addition = a + b
soustraction = a - b    
multiplication = a * b
division = a / b
moyenne = (a + b) / 2

print("=== CALCULATRICE ===")
print(f"{a} + {b} = {addition}")
print(f"{a} - {b} = {soustraction}")
print(f"{a} * {b} = {multiplication}")
print(f"{a} / {b} = {division:.3f}")
print(f"Moyenne: {moyenne}") """


### Exercice 2.2 : Puzzle de Classes

# On vous donne seulement la sortie, recréez les classes
"""
Création de Compte: Alice, solde: 100
Dépôt: 50, nouveau solde: 150
Retrait: 30, nouveau solde: 120
Retrait impossible: 200 demandé, solde: 120
Nombre de comptes créés: 2
"""

# Écrivez la classe CompteBancaire qui produit cette sortie

""" class CompteBancaire:
    comptes_crees = 0

    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde
        CompteBancaire.comptes_crees += 1
        print(f"Création de Compte: {self.nom}, solde: {self.solde}")

    def depot(self, montant):
        self.solde += montant
        print(f"Dépôt: {montant}, nouveau solde: {self.solde}")

    def retrait(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            print(f"Retrait: {montant}, nouveau solde: {self.solde}")
        else:
            print(f"Retrait impossible: {montant} demandé, solde: {self.solde}")

compte1 = CompteBancaire("Alice", 100)
compte1.depot(50)
compte1.retrait(30)
compte1.retrait(200)
compte2 = CompteBancaire("Bob", 200)
print(f"Nombre de comptes créés: {CompteBancaire.comptes_crees}") """

# Partie 3 : Problèmes Hybrides (30 min)

### Exercice 3.1 : Filtre Personnalisé

# """
# Créez une fonction filtre_complexe qui:
# 1. Prend une liste de nombres ET une liste de conditions
# 2. Chaque condition est un tuple (opérateur, valeur)
#    Ex: [(">", 10), ("<", 50), ("%", 2)] pour >10 ET <50 ET pair
# 3. Retourne les nombres qui satisfont TOUTES les conditions
# 4. Opérateurs supportés: >, <, >=, <=, ==, % (pair si %2==0)

# Exemple:
# nombres = [5, 12, 15, 20, 25, 30, 35]
# conditions = [(">", 10), ("<", 30), ("%", 2)]
# Résultat: [12, 20] (car >10 ET <30 ET pair)
# """

""" def filtre_complexe(nombres, conditions):
    resultat = []
    for nombre in nombres:
        satisfait = True
        for operateur, valeur in conditions:
            if operateur == ">" and not (nombre > valeur):
                satisfait = False
            elif operateur == "<" and not (nombre < valeur):
                satisfait = False
            elif operateur == ">=" and not (nombre >= valeur):
                satisfait = False
            elif operateur == "<=" and not (nombre <= valeur):
                satisfait = False
            elif operateur == "==" and not (nombre == valeur):
                satisfait = False
            elif operateur == "%" and not (nombre % valeur == 0):
                satisfait = False
        if satisfait:
            resultat.append(nombre)
    return resultat

# Testez la fonction
nombres = [5, 12, 15, 20, 25, 30, 35]
conditions = [(">", 10), ("<", 30), ("%", 2)]
print(filtre_complexe(nombres, conditions)) """

#============================#
""" import operator

OPS = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq
}

def filtre_complexe(nombres, conditions):
    resultat = []

    for nombre in nombres:
        for op, valeur in conditions:
            if op == "%":
                if nombre % valeur != 0:
                    break
            else:
                if not OPS[op](nombre, valeur):
                    break
        else:
            resultat.append(nombre)

    return resultat
print(filtre_complexe([5, 12, 15, 20, 25, 30, 35], [(">", 10), ("<", 30), ("%", 2)])) """


### Exercice 3.2 : Générateur de Profils

"""
Créez un système qui génère des profils aléatoires:
1. Classe Personne: nom, age, profession, ville
2. Liste de noms prédéfinis: ["Alice", "Bob", "Charlie", "Diana"]
3. Liste de professions: ["Dev", "Designer", "Manager", "Testeur"]
4. Liste de villes: ["Montréal", "Toronto", "Vancouver", "Québec"]
5. Méthode generer_personne() qui crée une personne aléatoire
6. Méthode generer_groupe(n) qui crée n personnes uniques
7. Utilisez des sets pour éviter les doublons complets
"""

""" import random

class Personne:
    def __init__(self, nom, age, profession, ville):
        self.nom = nom
        self.age = age
        self.profession = profession
        self.ville = ville

    def __repr__(self):
        return f"{self.nom}, {self.age} ans, {self.profession} à {self.ville}"

    def __eq__(self, other):
        return (
            isinstance(other, Personne) and
            self.nom == other.nom and
            self.age == other.age and
            self.profession == other.profession and
            self.ville == other.ville
        )

    def __hash__(self):
        return hash((self.nom, self.age, self.profession, self.ville))

def generer_personne():
    noms = ["Alice", "Bob", "Charlie", "Diana"]
    professions = ["Dev", "Designer", "Manager", "Testeur"]
    villes = ["Montréal", "Toronto", "Vancouver", "Québec"]

    return Personne(
        random.choice(noms),
        random.randint(20, 60),
        random.choice(professions),
        random.choice(villes)
    )

def generer_groupe(n):
    groupe = set()
    while len(groupe) < n:
        groupe.add(generer_personne())
    return list(groupe)

# class Personne:
#     noms = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"]
#     professions = ["Dev", "Designer", "Manager", "Testeur", "Analyste", "Architecte"]
#     villes = ["Montréal", "Calgary", "Toronto", "Québec", "Vancouver", "Halifax"]

#     def __init__(self, nom, age, profession, ville):
#         self.nom = nom
#         self.age = age
#         self.profession = profession
#         self.ville = ville

#     @classmethod
#     def generer_personne(cls):
#         nom = random.choice(cls.noms)
#         age = random.randint(18, 65)
#         profession = random.choice(cls.professions)
#         ville = random.choice(cls.villes)
#         return cls(nom, age, profession, ville)

#     @classmethod
#     def generer_groupe(cls, n):
#         groupe = []
#         profiles_uniques = set()

#         while len(groupe) < n:
#             personne = cls.generer_personne()
#             profile = (personne.nom, personne.age, personne.profession, personne.ville)

#             if profile not in profiles_uniques:
#                 profiles_uniques.add(profile)
#                 groupe.append(personne)

#         return groupe

#     def __str__(self):
#         return f"{self.nom}, {self.age} ans, {self.profession} à {self.ville}"    

# Test
groupe = generer_groupe(5)
for personne in groupe:
    print(personne) """


## Partie 4 : Défis Algorithmiques (45 min)

### Exercice 4.1 : Système de Notation Intelligent


"""
Créez un système de notation qui:
1. Classe Etudiant: nom, liste_notes
2. Classe Matière: nom, coefficient, liste_etudiants
3. Règles spéciales:
   - Si un étudiant a plus de 3 notes, on ignore la plus basse
   - Chaque matière a un coefficient différent
   - La note finale est arrondie à 2 décimales
   - Si coefficient > 2, la note est sur 30 sinon sur 20
4. Méthode classement() qui trie les étudiants par note finale
5. Gestion des absences (note = None)

Exemple:
maths = Matière("Maths", coefficient=3)  # Note sur 30
info = Matière("Info", coefficient=1)    # Note sur 20
"""

""" class Etudiant:
    def __init__(self, nom):
        self.nom = nom
        self.notes = []

    def ajouter_note(self, note):
        if note is not None:  # Gestion absence
            self.notes.append(note)

    def moyenne(self, ignore_min=True):
        if not self.notes:
            return 0

        notes_triees = sorted(self.notes)

        if ignore_min and len(notes_triees) > 3:
            notes_triees = notes_triees[1:]  # Ignore la plus basse

        return round(sum(notes_triees) / len(notes_triees), 2)

    def __str__(self):
        return f"{self.nom}: {self.moyenne()}"

class Matiere:
    def __init__(self, nom, coefficient=1):
        self.nom = nom
        self.coefficient = coefficient
        self.etudiants = []

    def inscrire(self, etudiant):
        self.etudiants.append(etudiant)

    def note_finale(self, etudiant):
        note_base = etudiant.moyenne()
        if self.coefficient > 2:
            return round(note_base * 30 / 20, 2)  # Sur 30
        else:
            return round(note_base, 2)  # Sur 20

    def classement(self):
        classement_trie = sorted(
            self.etudiants,
            key=lambda e: self.note_finale(e),
            reverse=True
        )
        return classement_trie

    def afficher_classement(self):
        print(f"Classement {self.nom}:")
        for i, etudiant in enumerate(self.classement(), 1):
            note = self.note_finale(etudiant)
            print(f"{i}. {etudiant.nom}: {note}/{'30' if self.coefficient > 2 else '20'}")

# Test
maths = Matiere("Maths", coefficient=3)
info = Matiere("Info", coefficient=1)

alice = Etudiant("Alice")
alice.ajouter_note(15)
alice.ajouter_note(18)
alice.ajouter_note(12)
alice.ajouter_note(10)  # Sera ignorée (4 notes > 3)

bob = Etudiant("Bob")
bob.ajouter_note(8)
bob.ajouter_note(14)
bob.ajouter_note(16)

maths.inscrire(alice)
maths.inscrire(bob)
info.inscrire(alice)
info.inscrire(bob)

maths.afficher_classement()"""


### Exercice 4.2 : Héritage Circulaire


"""
Créez un système de formes géométriques avec:
1. Classe Forme: couleur, méthode aire(), méthode perimetre()
2. Classe Rectangle (hérite de Forme): longueur, largeur
3. Classe Carre (hérite de Rectangle) - un carré EST-UN rectangle
4. Classe Cercle (hérite de Forme): rayon
5. Particularités:
   - Pour Carre, longueur = largeur automatiquement
   - Si on modifie largeur d'un Carre, longueur change aussi
   - Utilisez @property et @setter
   - Forme est abstraite (aire() et perimetre() doivent être implémentés)

Test:
carre = Carre("rouge", 5)
print(carre.aire())  # 25
carre.largeur = 10
print(carre.longueur)  # Doit aussi être 10
"""

""" import math

class Forme:
    def __init__(self, couleur):
        self.couleur = couleur

    def aire(self):
        raise NotImplementedError("La méthode aire() doit être implémentée")

    def perimetre(self):
        raise NotImplementedError("La méthode perimetre() doit être implémentée")
    def __str__(self):
        return f"{self.__class__.__name__} {self.couleur}"

class Rectangle(Forme):
    def __init__(self, couleur, longueur, largeur):
        super().__init__(couleur)
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

    def __repr__(self):
        return f"Rectangle({self.longueur} x {self.largeur}, {self.couleur})"

class Carre(Rectangle):
    def __init__(self, couleur, cote):
        self._cote = cote
        super().__init__(couleur, cote, cote)

    @property
    def largeur(self):
        return self._cote

    @largeur.setter
    def largeur(self, valeur):
        self._cote = valeur

    @property
    def longueur(self):
        return self._cote

    @longueur.setter
    def longueur(self, valeur):
        self._cote = valeur

    def aire(self):
        return self._cote ** 2

    def perimetre(self):
        return 4 * self._cote

    def __repr__(self):
        return f"Carre({self._cote}, {self.couleur})"

class Cercle(Forme):
    def __init__(self, couleur, rayon):
        super().__init__(couleur)
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def perimetre(self):
        return 2 * math.pi * self.rayon

    def __repr__(self):
        return f"Cercle(rayon={self.rayon}, {self.couleur})"
# Test

carre = Carre("rouge", 5)
print(carre.aire())  # 25
carre.largeur = 10
print(carre.longueur)  # Doit aussi être 10 """

""" class Forme:
    def __init__(self, couleur):
        self.couleur = couleur

    def aire(self):
        raise NotImplementedError("Méthode abstraite")

    def perimetre(self):
        raise NotImplementedError("Méthode abstraite")

    def __str__(self):
        return f"{self.__class__.__name__} {self.couleur}"

class Rectangle(Forme):
    def __init__(self, couleur, longueur, largeur):
        super().__init__(couleur)
        self._longueur = longueur
        self._largeur = largeur

    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self, valeur):
        if valeur > 0:
            self._longueur = valeur

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self, valeur):
        if valeur > 0:
            self._largeur = valeur

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

class Carre(Rectangle):
    def __init__(self, couleur, cote):
        super().__init__(couleur, cote, cote)

    @property
    def cote(self):
        return self.longueur

    @cote.setter
    def cote(self, valeur):
        if valeur > 0:
            self.longueur = valeur
            self.largeur = valeur

    # Surcharge des setters pour garder égalité
    @Rectangle.longueur.setter
    def longueur(self, valeur):
        if valeur > 0:
            self._longueur = valeur
            self._largeur = valeur

    @Rectangle.largeur.setter
    def largeur(self, valeur):
        if valeur > 0:
            self._largeur = valeur
            self._longueur = valeur

class Cercle(Forme):
    def __init__(self, couleur, rayon):
        super().__init__(couleur)
        self.rayon = rayon

    def aire(self):
        import math
        return math.pi * self.rayon ** 2

    def perimetre(self):
        import math
        return 2 * math.pi * self.rayon

# Test
carre = Carre("rouge", 5)
print(f"Aire: {carre.aire()}")  # 25
print(f"Périmètre: {carre.perimetre()}")  # 20

carre.largeur = 10
print(f"Longueur après modification largeur: {carre.longueur}")  # 10
print(f"Aire nouvelle: {carre.aire()}")  # 100

cercle = Cercle("bleu", 3)
print(f"Aire cercle: {cercle.aire():.2f}")
print(f"Périmètre cercle: {cercle.perimetre():.2f}") """

## Partie 5 : Projet Synthèse (30 min)

### Exercice 5.1 : Jeu "Bataille des Classes"

"""
Créez un jeu où différentes classes s'affrontent:

1. Classe Personnage (abstraite):
   - nom, points_vie, force, defense
   - méthode attaquer(adversaire)
   - méthode est_vivant()

2. Classes spécialisées:
   - Guerrier: +20% force, -10% defense
   - Mage: attaques magiques (ignore 50% defense)
   - Archer: 30% chance d'esquiver une attaque

3. Classe Combat:
   - personnage1, personnage2
   - méthode demarrer() -> tours jusqu'à la mort
   - affiche les dégâts chaque tour

4. Système de niveaux:
   - Chaque victoire donne de l'XP
   - À 100 XP, niveau +1, points_vie +10, force +5

Règles:
- Dégâts = force_attaquant - (defense_defenseur / 2)
- Minimum 1 dégât par attaque
- Combat aléatoire qui commence
"""

""" import random

class Personnage:
    def __init__(self, nom, points_vie, force, defense):
        self.nom = nom
        self.points_vie = points_vie
        self.force = force
        self.defense = defense
        self.xp = 0
        self.niveau = 1

    def attaquer(self, adversaire):
        raise NotImplementedError("attaquer() doit être implémentée")

    def est_vivant(self):
        return self.points_vie > 0

    def gagner_xp(self, montant):
        self.xp += montant
        while self.xp >= 100:
            self.xp -= 100
            self.niveau += 1
            self.points_vie += 10
            self.force += 5
            print(f"🎉 {self.nom} passe niveau {self.niveau} !")

class Guerrier(Personnage):
    def __init__(self, nom):
        super().__init__(nom, points_vie=120, force=25, defense=20)
        self.force *= 1.2
        self.defense *= 0.9

    def attaquer(self, adversaire):
        degats = self.force - (adversaire.defense / 2)
        degats = max(1, int(degats))
        adversaire.points_vie -= degats
        return degats

class Mage(Personnage):
    def __init__(self, nom):
        super().__init__(nom, points_vie=90, force=30, defense=10)

    def attaquer(self, adversaire):
        defense_effective = adversaire.defense * 0.5
        degats = self.force - (defense_effective / 2)
        degats = max(1, int(degats))
        adversaire.points_vie -= degats
        return degats

class Archer(Personnage):
    def __init__(self, nom):
        super().__init__(nom, points_vie=100, force=22, defense=15)

    def esquive(self):
        return random.random() < 0.3

    def attaquer(self, adversaire):
        degats = self.force - (adversaire.defense / 2)
        degats = max(1, int(degats))
        adversaire.points_vie -= degats
        return degats

class Combat:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def demarrer(self):
        attaquant, defenseur = random.sample([self.p1, self.p2], 2)
        tour = 1

        print(f"⚔️ Combat entre {self.p1.nom} et {self.p2.nom} !")
        print(f"🎲 {attaquant.nom} commence\n")

        while attaquant.est_vivant() and defenseur.est_vivant():
            print(f"--- Tour {tour} ---")

            # Esquive de l’archer
            if isinstance(defenseur, Archer) and defenseur.esquive():
                print(f"{defenseur.nom} esquive l'attaque !")
            else:
                degats = attaquant.attaquer(defenseur)
                print(f"{attaquant.nom} inflige {degats} dégâts à {defenseur.nom}")

            print(f"{defenseur.nom} : {max(0, defenseur.points_vie)} PV\n")

            attaquant, defenseur = defenseur, attaquant
            tour += 1

        gagnant = attaquant if attaquant.est_vivant() else defenseur
        print(f"🏆 {gagnant.nom} remporte le combat !")
        gagnant.gagner_xp(50)

g = Guerrier("Link")
m = Mage("Gandalf")
a = Archer("Robin")

combat = Combat(g, m)
combat.demarrer()

print("\nDeuxième combat\n")

combat2 = Combat(a, g)
combat2.demarrer() """

""" import random

class Personnage:
    def __init__(self, nom, points_vie=100, force=10, defense=5):
        self.nom = nom
        self.points_vie = points_vie
        self.force = force
        self.defense = defense
        self.niveau = 1
        self.experience = 0

    def attaquer(self, adversaire):
        # Calcul des dégâts
        degats = self.force - (adversaire.defense / 2)
        degats = max(1, degats)  # Minimum 1 dégât

        adversaire.points_vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} pour {degats:.1f} dégâts")

        if not adversaire.est_vivant():
            self.gagner_experience(50)
            print(f"{adversaire.nom} est vaincu! {self.nom} gagne 50 XP")

    def est_vivant(self):
        return self.points_vie > 0

    def gagner_experience(self, xp):
        self.experience += xp
        if self.experience >= 100:
            self.niveau += 1
            self.experience -= 100
            self.points_vie += 10
            self.force += 5
            print(f"{self.nom} atteint le niveau {self.niveau}!")

    def __str__(self):
        return f"{self.nom} Niv.{self.niveau} (PV: {self.points_vie:.1f})"

class Guerrier(Personnage):
    def __init__(self, nom):
        super().__init__(nom, points_vie=120, force=12, defense=6)
        # Bonus/malus
        self.force = int(self.force * 1.2)  # +20%
        self.defense = int(self.defense * 0.9)  # -10%

class Mage(Personnage):
    def attaquer(self, adversaire):
        # Les mages ignorent 50% de la défense
        degats = self.force - (adversaire.defense * 0.5)
        degats = max(1, degats)

        adversaire.points_vie -= degats
        print(f"{self.nom} lance un sort sur {adversaire.nom} pour {degats:.1f} dégâts")

        if not adversaire.est_vivant():
            self.gagner_experience(50)

class Archer(Personnage):
    def __init__(self, nom):
        super().__init__(nom, points_vie=90, force=15, defense=3)

    def attaquer(self, adversaire):
        # 30% chance d'esquiver pour l'adversaire
        if random.random() < 0.3:
            print(f"{adversaire.nom} esquive l'attaque de {self.nom}!")
            return

        super().attaquer(adversaire)

class Combat:
    def __init__(self, personnage1, personnage2):
        self.p1 = personnage1
        self.p2 = personnage2
        self.tour = 0

    def demarrer(self):
        print(f"=== COMBAT: {self.p1.nom} vs {self.p2.nom} ===")

        # Qui commence ?
        attaquant = random.choice([self.p1, self.p2])
        defenseur = self.p2 if attaquant == self.p1 else self.p1

        while self.p1.est_vivant() and self.p2.est_vivant():
            self.tour += 1
            print(f"\n--- Tour {self.tour} ---")

            attaquant.attaquer(defenseur)

            # Échange des rôles
            attaquant, defenseur = defenseur, attaquant

        vainqueur = self.p1 if self.p1.est_vivant() else self.p2
        print(f"\n=== {vainqueur.nom} remporte le combat en {self.tour} tours! ===")
        return vainqueur

# Test
guerrier = Guerrier("Conan")
mage = Mage("Merlin")
archer = Archer("Legolas")

combat1 = Combat(guerrier, mage)
combat1.demarrer()

print(f"\nStatut après combat:")
print(guerrier)
print(mage) """
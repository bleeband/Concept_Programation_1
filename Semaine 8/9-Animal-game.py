import random
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(BASE_DIR, "savegame.json")
tour_actuel = 1
class Animal():

    def __init__(self, nom, age, sexe, espece, position=(0,0)) -> None:
        self.est_vivant = True
        self.a_jouer = False
        self.nom = nom
        self.age = age
        self.sexe = sexe
        self.espece = espece.lower()
        self.position = position
        self.sante = 100
        self.energie = 100
        self.bonheur = 50
        self.territoire = []
        self.vitesse = 5
        self.amis = []
        self.ennemis = []
        self.niveau = 1
        self.experience = 0
        self.points_competence = 0
        self.competences = {
            'chasse': 0,
            'defense': 0,
            'intelligence': 0
        }
    
    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "nom": self.nom,
            "age": self.age,
            "sexe": self.sexe,
            "espece": self.espece,
            "position": self.position,
            "sante": self.sante,
            "energie": self.energie,
            "bonheur": self.bonheur,
            "territoire": self.territoire,
            "vitesse": self.vitesse,
            "niveau": self.niveau,
            "experience": self.experience,
            "points_competence": self.points_competence,
            "competences": self.competences,
            "est_vivant": self.est_vivant,
            "amis": [a.nom for a in self.amis],
            "ennemis": [e.nom for e in self.ennemis],
        }
    
    def manger(self):
        if not self.est_vivant:
            print(f"{self.nom} ne peut plus manger")
            return False
        
        self.energie = min(100, self.energie + 10)
        print(f"{self.nom} mange bien et gagne +10 d'énergie  -->  Énergie actuelle : {self.energie}")
        self.verifier_vie()
        return True
        
    def dormir(self):
        if not self.est_vivant:
            print(f"{self.nom} ne peut plus dormir")
            return

        # Dormir recharge 20 d'énergie, mais coûte 10 d'énergie (pour l'action)
        self.energie = min(100, self.energie  + 20)
        print(f"{self.nom} dort paisiblement et gagne +20 d'énergie  -->  Énergie actuelle : {self.energie}")
        self.verifier_vie()

    def soigner(self):
        if not self.est_vivant:
            print(f"{self.nom} ne peut plus être soigné")
            return
        self.sante = min(100, self.sante + 30)
        print(f"{self.nom} a été soigné et gagne +30 de santé  -->  Santé actuelle : {self.sante}")

    def vieillir(self):
        if not self.est_vivant:
            return

        self.age += 1
        self.energie = max(0, self.energie - 5)

        # Perte de santé en %
        perte_sante = self.sante * 0.05
        self.sante -= perte_sante

        # Malus vieillesse
        if self.age > 10:
            self.sante -= 2
            print(f"⚠️ {self.nom} commence à être vieux...")

        self.sante = max(0, self.sante)

        print(
            f"⏳ {self.nom} vieillit → "
            f"Âge: {self.age}, "
            f"Santé: {self.sante:.1f}, "
            f"Énergie: {self.energie}"
        )

        self.verifier_vie()

    def verifier_vie(self):
        if self.sante <= 0:
            self.est_vivant = False
            self.sante = 0
            print(f"{self.nom} est mort...")

    def se_faire_ami(self, animal):
        if animal in self.ennemis:
            self.ennemis.remove(animal)
            animal.ennemis.remove(self)
        if animal != self and animal not in self.amis:
            self.amis.append(animal)
            animal.amis.append(self)
            print(f"{self.nom} et {animal.nom} sont maintenant des amis !")

    def se_faire_ennemi(self, animal):
        if animal in self.amis:
            self.amis.remove(animal)
            animal.amis.remove(self)
        if animal != self and animal not in self.ennemis:
            self.ennemis.append(animal)
            animal.ennemis.append(self)
            print(f"{self.nom} et {animal.nom} sont maintenant des ennemis !")

    def interagir(self, animal):
        if not self.est_vivant or not animal.est_vivant:
            return
        interactions = {
            "chien": {
                "jeu": "à la balle",
                "attaque": "mordre"
            },
            "chat": {
                "jeu": "dans la boîte",
                "attaque": "griffer"
            }
        }

        if animal.espece not in interactions:
            return

        data = interactions[animal.espece]

        if animal in self.amis:
            print(f"{self.nom} joue avec {animal.nom} {data['jeu']} et ils sont heureux !")
            bonus = self.niveau * 0.5
            self.bonheur = min(100, self.bonheur + 10 + bonus)
            animal.bonheur = min(100, animal.bonheur + 10 + bonus)
            self.energie -= 5
            animal.energie -= 5

        elif animal in self.ennemis:
            print(f"{self.nom} se chicane avec {animal.nom} et il se fait {data['attaque']} !")
            self.bonheur -= 10
            animal.bonheur -= 10
            self.sante -= 5
            animal.sante -= 5
            self.verifier_vie()
            animal.verifier_vie()

        else:
            if random.random() > 0.5:
                self.se_faire_ami(animal)
            else:
                self.se_faire_ennemi(animal)

    def peut_se_reproduire(self):
        return self.age >= 2 and self.est_vivant

    def reproduire(self, autre_animal):
        if not self.peut_se_reproduire() or not autre_animal.peut_se_reproduire():
            return None

        if self.sexe == autre_animal.sexe:
            return None

        if self.espece != autre_animal.espece:
            return None
        
        if autre_animal in self.ennemis:
            print(f"{self.nom} et {autre_animal.nom} ne peuvent pas se reproduire, ce sont des ennemis !")
            return None

        nom_bebe = f"{self.nom[:3]}{autre_animal.nom[:3]}"
        sexe_bebe = 'M' if random.random() > 0.5 else 'F'

        return Animal(nom_bebe, 0, sexe_bebe, self.espece)

    def gagner_experience(self, montant):
        self.experience += montant
        while self.experience >= 100:
            self.experience -= 100
            self.niveau += 1
            self.points_competence += 5
            print(f"{self.nom} atteint le niveau {self.niveau} et gagne +5 points de compétence")

    def entrainer(self, competence, heures=1):
        if competence in self.competences:
            gain = heures * 5
            self.competences[competence] = min(100, self.competences[competence] + gain)
            self.gagner_experience(heures * 10)
            print(f"{self.nom} s'est entraîné en {competence} et gagne +{gain}")
        
        else:
            print(f"Compétence {competence} inconnue")

    def efficacite(self, competence):
        if competence not in self.competences:
            return 0

        bonus_espece = 0
        bonus_niveau = 0

        if self.est_dans_son_territoire():
            if self.espece == "chat" and competence == "chasse":
                bonus_espece += 5
            elif self.espece == "chien" and competence == "defense":
                bonus_espece += 5

        # Bonus de niveau seulement pour compétences liées à l'espèce
        if (self.espece == "chat" and competence == "chasse") or \
           (self.espece == "chien" and competence == "defense"):
            bonus_niveau = self.niveau * 2

        return self.competences[competence] + bonus_espece + bonus_niveau

    def se_deplacer(self, x, y):
        distance = abs(x - self.position[0]) + abs(y - self.position[1])
        if distance <= self.vitesse:
            self.position = (x, y)
            print(f"{self.nom} se déplace vers ({x}, {y})")
            return True
        else:
            print(f"{self.nom} ne peut pas aller aussi loin! Vitesse max: {self.vitesse}")
            return False

    def marquer_territoire(self):
        if self.position not in self.territoire:
            self.territoire.append(self.position)
            print(f"{self.nom} a marqué son territoire en {self.position}")
        else:
            print(f"{self.nom} avait déjà marqué cette position")

    def est_dans_son_territoire(self, x=None, y=None):
        if x is None or y is None:
            x, y = self.position
        for tx, ty in self.territoire:
            if abs(tx - x) <= 1 and abs(ty - y) <= 1:  # 1 case autour
                return True
        return False
    
    def __str__(self) -> str:
        competences_str = []
        for c in self.competences:
            valeur = self.competences[c]
            bonus = self.efficacite(c) - valeur
            if bonus > 0:
                competences_str.append(f"{c}: {valeur} (+{bonus})")
            else:
                competences_str.append(f"{c}: {valeur}")
        
        amis_noms = [a.nom for a in self.amis]
        ennemis_noms = [e.nom for e in self.ennemis]
        
        return (
            f"nom: {self.nom}, age: {self.age}, sexe: {self.sexe}\n"
            f"Amis: {amis_noms}, Ennemis: {ennemis_noms}\n"
            f"XP: {self.experience}/100, Points compétence: {self.points_competence}\n"
            f"Compétences: {', '.join(competences_str)}"
        )
 
    def __eq__(self, value) -> bool:
        if not isinstance(value, Animal):
            return False
        return self.nom == value.nom and self.age == value.age
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        if age >= 0:
            self.age = age

    def set_position(self, position):
        if position >= 0:
            self.position = position

class Chien(Animal):
    chien_img = """
  / \\__
 (    @\\___
 /         O
/   (_____/
 /_____/
"""

    def __init__(self, nom, age, sexe, race, position=(0,0)) -> None:
        super().__init__(nom, age, sexe, "chien")
        self.race = race
        self.position = position
    
    def to_dict(self):
        data = super().to_dict()
        data["race"] = self.race
        return data

    def aboyer(self):
        print(f"{self.nom} aboie : Woof ! Woof !")

    def reproduire(self, autre_animal):
        bebe = super().reproduire(autre_animal)
        if bebe:
            race_bebe = f"{self.race[:3]}{getattr(autre_animal, 'race', '')[:3]}"
            return Chien(bebe.nom, 0, bebe.sexe, race_bebe)
        return None

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}, race: {self.race}"

class Chat(Animal):
    chat_img = """
 /\\_/\\
( o.o )
 > ^ <
"""
    def __init__(self, nom, age, sexe, couleur, position=(0,0)) -> None:
        super().__init__(nom, age, sexe, "chat")
        self.couleur = couleur
        self.position = position

    def to_dict(self):
        data = super().to_dict()
        data["couleur"] = self.couleur
        return data

    def miauler(self):
        print(f"{self.nom} miaule : Miaaouuu !")

    def reproduire(self, autre_animal):
        bebe = super().reproduire(autre_animal)
        if bebe:
            couleur_bebe = f"{self.couleur[:3]}{getattr(autre_animal, 'couleur', '')[:3]}"
            return Chat(bebe.nom, 0, bebe.sexe, couleur_bebe)
        return None

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}, couleur: {self.couleur}"

class Compagnon:
    def __init__(self, proprietaire) -> None:
        self.proprietaire = proprietaire

    def jouer(self):
        print(f"Je joue avec {self.proprietaire}")

class AnimalDomestique(Animal, Compagnon):
    domes_img = """
   O     /\\_/\\
  /|\\   ( o.o )
  / \\    > ^ <
"""
    def __init__(self, nom, age, sexe, espece, proprietaire):
        Animal.__init__(self, nom, age, sexe, espece)
        Compagnon.__init__(self, proprietaire)

    def __str__(self):
        parent_str = Animal.__str__(self)
        return f"{parent_str}, propriétaire: {self.proprietaire}"

def afficher_map(animaux, largeur=10, hauteur=10):
    """Affiche une carte ASCII avec animaux sur les cases vertes"""
    
    # Couleurs ANSI
    RESET = "\033[0m"
    HERBE = "\033[42m"        # Fond vert pour la case vide
    CHIEN_COLOR = "\033[94m"  # Bleu pour chien
    CHAT_COLOR = "\033[91m"   # Rouge pour chat
    MORT_COLOR = "\033[90m"   # Gris pour animal mort

    # Créer la grille vide avec fond vert
    grid = [[" " for _ in range(largeur)] for _ in range(hauteur)]
    color_grid = [[HERBE for _ in range(largeur)] for _ in range(hauteur)]
    
    # Marquer les territoires avec un "T" (fond vert, texte vert foncé)
    for animal in animaux:
        for (x, y) in animal.territoire:
            if 0 <= x < largeur and 0 <= y < hauteur:
                grid[y][x] = "T"
                color_grid[y][x] = "\033[42;30m"  # fond vert + texte noir

    # Placer les animaux
    for animal in animaux:
        x, y = animal.position
        if 0 <= x < largeur and 0 <= y < hauteur:
            symbole = animal.nom[0].upper()
            if not animal.est_vivant:
                couleur = MORT_COLOR
                symbole = "X"
            else:
                couleur = CHIEN_COLOR if animal.espece == "chien" else CHAT_COLOR
            grid[y][x] = symbole
            color_grid[y][x] = f"{HERBE}{couleur}"  # superposer lettre sur fond vert

    # Afficher la grille
    print("\n=== Carte du terrain ===")
    
    # Numéros de colonnes
    print("   ", end="")
    for i in range(largeur):
        print(f"{i:2} ", end="")
    print()
    
    # Lignes
    for y in range(hauteur):
        print(f"{y:2} ", end="")
        for x in range(largeur):
            print(f"{color_grid[y][x]} {grid[y][x]} {RESET}", end="")
        print()
    print("(T = territoire, lettres = animaux, X = mort)\n")

def tour_par_tour(animaux, tours_pour_vieillir=3):
    global tour_actuel

    # Réinitialiser le flag d'action
    for animal in animaux:
        animal.a_joue = False

    print(f"\n🔥 ===== TOUR {tour_actuel} ===== 🔥\n")

    for animal in animaux:
        if not animal.est_vivant:
            continue

        print(f"\n➡️ Tour de {animal.nom} ({animal.espece})")
        menu_animal(animal, animaux)

    # Fatigue et stress naturel
    for animal in animaux:
        if animal.est_vivant:
            animal.energie = max(0, animal.energie - 2)   # fatigue naturelle
            animal.bonheur = max(0, animal.bonheur - 1)   # stress léger
            print(f"{animal.nom} perd un peu d'énergie et de bonheur → Énergie: {animal.energie}, Bonheur: {animal.bonheur}")

    # Vieillissement tous les X tours
    if tour_actuel % tours_pour_vieillir == 0:
        print("\n⏳ Les animaux vieillissent...")
        for animal in animaux:
            animal.vieillir()

    tour_actuel += 1

def menu_principal(animaux):
    if animaux is None:
        animaux = [
            un_chien,
            un_chien2,
            un_chien3,
            un_chat,
            un_chat2,
            un_chat3
        ]
    while True:
        afficher_map(animaux)

        print("\n=== MENU PRINCIPAL ===")
        print("1. Lancer un tour")
        print("2. Afficher état des animaux")
        print("0. Quitter")

        choix = input("Choix: ")

        if choix == "1":
            tour_par_tour(animaux)

        elif choix == "2":
            for a in animaux:
                print("\n" + str(a))

        elif choix == "0":
            sauvegarder_partie(animaux)
            print("Fin de la simulation 👋")
            break

        else:
            print("Choix invalide")

def menu_animal(animal, liste_animaux):
    while True:
        if animal.a_joue:
            print("⏳ Tu as déjà joué ce tour.")
            return
        afficher_map(liste_animaux)
        print("\n=== MENU ===")
        print(f"1. Manger")
        print(f"2. Dormir")
        print(f"3. Soigner")
        print(f"4. Vieillir")
        print(f"5. S'entraîner")
        print(f"6. Se déplacer")
        print(f"7. Marquer territoire")
        print(f"8. Interagir avec un autre animal")
        print(f"9. Afficher infos")
        print(f"0. Quitter")

        choix = input("Choisis une option: ")

        if choix == "1":
            animal.manger()
            animal.a_joue = True
        elif choix == "2":
            animal.dormir()
            animal.a_joue = True
        elif choix == "3":
            animal.soigner()
            animal.a_joue = True
        elif choix == "4":
            animal.vieillir()
            animal.a_joue = True
        elif choix == "5":
            comp = input(f"Quelle compétence entraîner {list(animal.competences.keys())}? ")
            h = int(input("Combien d'heures d'entraînement? "))
            animal.entrainer(comp, h)
            animal.a_joue = True
        elif choix == "6":
            x = int(input("Nouvelle position x: "))
            y = int(input("Nouvelle position y: "))
            animal.se_deplacer(x, y)
            animal.a_joue = True
        elif choix == "7":
            animal.marquer_territoire()
            animal.a_joue = True
        elif choix == "8":
            print("Animaux disponibles: ", [a.nom for a in liste_animaux if a != animal])
            cible = input("Nom de l'animal pour interagir: ")
            cible_animal = next((a for a in liste_animaux if a.nom == cible), None)
            if cible_animal:
                animal.interagir(cible_animal)
            else:
                print("Animal introuvable")
            animal.a_joue = True
        elif choix == "9":
            print(animal)
        elif choix == "0":
            print(f"🔁 Fin du tour de {animal.nom}")
            break
        else:
            print("Choix invalide")

def animal_from_dict(data):
    if data["type"] == "Chien":
        a = Chien(
            data["nom"],
            data["age"],
            data["sexe"],
            data["race"],
            position=tuple(data["position"])
        )
    elif data["type"] == "Chat":
        a = Chat(
            data["nom"],
            data["age"],
            data["sexe"],
            data["couleur"],
            position=tuple(data["position"])
        )
    else:
        a = Animal(
            data["nom"],
            data["age"],
            data["sexe"],
            data["espece"],
            position=tuple(data["position"])
        )

    # Restaurer les stats
    a.sante = data["sante"]
    a.energie = data["energie"]
    a.bonheur = data["bonheur"]
    a.territoire = data["territoire"]
    a.vitesse = data["vitesse"]
    a.niveau = data["niveau"]
    a.experience = data["experience"]
    a.points_competence = data["points_competence"]
    a.competences = data["competences"]
    a.est_vivant = data["est_vivant"]

    return a

def sauvegarder_partie(animaux):
    data = {
    "tour": tour_actuel,
    "animaux": [a.to_dict() for a in animaux]
}
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("💾 Partie sauvegardée")

def restaurer_liens(animaux):
    nom_to_animal = {a.nom: a for a in animaux}
    for a in animaux:
        a.amis = [nom_to_animal[n] for n in getattr(a, "amis", []) if n in nom_to_animal]
        a.ennemis = [nom_to_animal[n] for n in getattr(a, "ennemis", []) if n in nom_to_animal]

def charger_partie():
    global tour_actuel
    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    tour_actuel = data.get("tour", 1)
    animaux = [animal_from_dict(d) for d in data["animaux"]]
    print("📂 Partie chargée")
    return animaux

if __name__ == "__main__":

    animaux = charger_partie()

    if animaux is None:
        print("🆕 Aucune sauvegarde trouvée — nouvelle partie")
        
        un_chien = Chien("Fido", 5, "M", "Golden Retrieve", position=(0,1))
        un_chien2 = Chien("Roa", 4, "F", "Rottweiler", position=(3,5))
        un_chien3 = Chien("Miquette", 12, "F", "Caniche", position=(5,8))
        un_chat = Chat("Bob", 2, "M", "orange", position=(1,0))
        un_chat2 = Chat("Fleur", 4, "F", "noir", position=(8,5))
        un_chat3 = Chat("Jack", 6, "M", "blanc")

        animaux = [
            un_chien,
            un_chien2,
            un_chien3,
            un_chat,
            un_chat2,
            un_chat3
        ]
    else:
        print("🔁 Sauvegarde détectée — reprise de la partie")

    menu_principal(animaux)

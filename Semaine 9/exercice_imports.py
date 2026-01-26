# Exercices sur les Imports en Python

## Exercice 1 : Module `random`

### 1.1 : Lancer de dés


# Écrivez un programme qui simule:
# 1. Le lancer de 2 dés à 6 faces
# 2. Affiche chaque résultat
# 3. Calcule et affiche la somme
# 4. Si c'est un double, affiche "DOUBLE!"

""" # Import nécessaire
import random

# Votre code ici
de1 = random.randint(1, 6)
de2 = random.randint(1, 6)
somme = de1 + de2
print(f"Résultat du dé 1 : {de1}")
print(f"Résultat du dé 2 : {de2}")
print(f"Somme : {somme}")
if de1 == de2:
    print("DOUBLE!")
 """


### 1.2 : Tirage au sort

# Créez un tirage au sort pour une liste d'étudiants
""" etudiants = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# 1. Mélangez la liste aléatoirement
# 2. Choisissez un gagnant au hasard
# 3. Choisissez 2 gagnants différents
# 4. Affichez l'ordre de passage aléatoire

import random

# Votre code ici
random.shuffle(etudiants)
gagnant = random.choice(etudiants)
gagnants_diff = random.sample(etudiants, 2)
print("Gagnant au hasard :", gagnant)
print("Deux gagnants différents :", gagnants_diff)  
print("Ordre de passage aléatoire :", etudiants) """


## Exercice 2 : Module `math`

### 2.1 : Calculs géométriques


# Écrivez un programme qui calcule:
# 1. L'aire d'un cercle (π × r²)
# 2. Le périmètre d'un cercle (2 × π × r)
# 3. L'hypoténuse d'un triangle rectangle (√(a² + b²))
# 4. Arrondissez π à 2 décimales

""" import math

rayon = 5
cote_a = 3
cote_b = 4

aire_cercle = math.pi * rayon**2
perimetre_cercle = 2 * math.pi * rayon
hypotenuse_triangle = math.hypot(cote_a, cote_b)

print(f"Aire du cercle : {aire_cercle:.2f}")
print(f"Périmètre du cercle : {perimetre_cercle:.2f}")
print(f"Hypoténuse du triangle : {hypotenuse_triangle:.2f}")

#==========================#
pi = round(math.pi, 2)

rayon = 5
a = 3
b = 4

# 1. Aire d'un cercle
aire_cercle = pi * rayon ** 2

# 2. Périmètre d'un cercle
perimetre_cercle = 2 * pi * rayon

# 3. Hypoténuse d'un triangle rectangle
hypotenuse = math.sqrt(a ** 2 + b ** 2)

print(f"Aire du cercle : {aire_cercle:.2f}")
print(f"Périmètre du cercle : {perimetre_cercle:.2f}")
print(f"Hypoténuse du triangle : {hypotenuse:.2f}") """

### 2.2 : Conversions

# Convertissez:
# 1. 180 degrés en radians
# 2. π radians en degrés
# 3. Calculez sin(90°)
# 4. Calculez cos(π)

""" import math

# Votre code ici

degres = 180

radians = math.radians(degres)  # équivalent à 180 * pi / 180
print(f"{degres}° en radians : {radians}")

rads = math.pi
degres_from_rads = math.degrees(rads)  # équivalent à π * 180 / pi
print(f"π radians en degrés : {degres_from_rads}")

sin_90 = math.sin(math.radians(90))
print(f"sin(90°) = {sin_90}")

cos_pi = math.cos(math.pi)
print(f"cos(π) = {cos_pi}") """

## Exercice 3 : Module `json`

### 3.1 : Sauvegarde de données


# Créez un programme qui:
# 1. Crée un dictionnaire d'étudiant
# 2. Le sauvegarde dans un fichier JSON
# 3. Le relit depuis le fichier
# 4. Affiche les données lues

""" import json

etudiant = {
    "nom": "Alice",
    "age": 20,
    "notes": [15, 18, 12],
    "present": True
}

# Votre code ici

with open("etudiant.json", "w") as f:
    json.dump(etudiant, f)
with open("etudiant.json", "r") as f:
    etudiant_lu = json.load(f)
print("Données lues depuis le fichier JSON :", etudiant_lu) """


### 3.2 : Journal d'événements


# Créez un journal qui:
# 1. Ajoute des événements à un fichier JSON
# 2. Chaque événement a: date, type, message
# 3. Peut lire tout l'historique
# 4. Compte le nombre d'événements

""" import json
import datetime
import time

# Votre code ici

journal = []

# Ajouter des événements
journal.append({
    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "type": "info",
    "message": "Événement 1"
})

time.sleep(2)

journal.append({
    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "type": "erreur",
    "message": "Événement 2"
})

# Sauvegarder dans un fichier JSON
with open("journal.json", "w") as f:
    json.dump(journal, f)

# Lire l'historique
with open("journal.json", "r") as f:
    journal_lu = json.load(f)

print("Historique des événements:")
for event in journal_lu:
    print(f"Date: {event['date']}, Type: {event['type']}, Message: {event['message']}")

print(f"Nombre d'événements : {len(journal_lu)}") """


## Exercice 4 : Module `os`

### 4.1 : Vérificateur de fichiers

# Écrivez un programme qui:
# 1. Vérifie si un fichier existe
# 2. Si oui, affiche sa taille
# 3. Si non, le crée avec du contenu
# 4. Liste les fichiers du dossier courant

""" import os

# Votre code ici

# Nom du fichier à vérifier
nom_fichier = "mon_fichier.txt"

# 1. Vérifier si le fichier existe
if os.path.exists(nom_fichier):
    taille = os.path.getsize(nom_fichier)
    print(f"Le fichier '{nom_fichier}' existe et sa taille est de {taille} octets.")
else:
    contenu = "Ceci est un nouveau fichier créé automatiquement.\n"
    with open(nom_fichier, "w") as f:
        f.write(contenu)
    print(f"Le fichier '{nom_fichier}' n'existait pas et a été créé avec du contenu.")

# 4. Lister les fichiers du dossier courant
fichiers = [f for f in os.listdir('.') if os.path.isfile(f)]
print("\nFichiers dans le dossier courant :")
for f in fichiers:
    print(f"- {f}") """


### 4.2 : Gestionnaire de projets

# Créez un gestionnaire qui:
# 1. Crée un dossier pour un projet
# 2. Crée des fichiers README.md et main.py dans le dossier
# 3. Vérifie que le dossier a été créé
# 4. Nettoie en supprimant le dossier (optionnel)

""" import os

# Votre code ici

# Nom du projet / dossier
nom_projet = "MonProjet"

# 1. Créer le dossier pour le projet
if not os.path.exists(nom_projet):
    os.makedirs(nom_projet)
    print(f"Dossier '{nom_projet}' créé.")
else:
    print(f"Dossier '{nom_projet}' existe déjà.")

# 2. Créer les fichiers README.md et main.py
readme_path = os.path.join(nom_projet, "README.md")
main_path = os.path.join(nom_projet, "main.py")

with open(readme_path, "w") as f:
    f.write(f"# {nom_projet}\n\nDescription du projet.\n")
print(f"Fichier '{readme_path}' créé.")

with open(main_path, "w") as f:
    f.write("# Point d'entrée du projet\n")
print(f"Fichier '{main_path}' créé.")

# 3. Vérifier que le dossier a bien été créé
if os.path.exists(nom_projet) and os.path.isdir(nom_projet):
    print(f"Vérification : le dossier '{nom_projet}' existe bien.")

# 4. Nettoyage optionnel : supprimer le dossier et ses fichiers
supprimer = input("Voulez-vous supprimer le dossier pour nettoyer ? (oui/non) : ").lower()
if supprimer in ["oui", "o", "yes", "y"]:
    # Supprimer tous les fichiers du dossier
    for fichier in os.listdir(nom_projet):
        chemin = os.path.join(nom_projet, fichier)
        if os.path.isfile(chemin):
            os.remove(chemin)
    # Supprimer le dossier vide
    os.rmdir(nom_projet)
    print(f"Dossier '{nom_projet}' supprimé.")
else:
    print("Le dossier reste en place.") """


## Exercice 5 : Module `copy`

### 5.1 : Copies de listes

# Montrez la différence entre:
# 1. Une référence (l1 = l2)
# 2. Une copie superficielle
# 3. Une copie profonde

""" import copy

originale = [[1, 2], [3, 4]]

# Votre code ici
# Modifiez une sous-liste et observez les effets
# Référence : l1 pointe vers le même objet que originale

l1 = originale
print("\nAvant modification")
print("originale :", originale)
# Modifier un élément
l1[0][0] = 100

print("\nAprès modification via l1 :")
print("originale :", originale)
print("l1       :", l1)

# Copie superficielle
l2 = copy.copy(originale)

# Modifier un élément du sous-liste
l2[0][1] = 200

print("\nAprès modification via l2 (copie superficielle) :")
print("originale :", originale)
print("l2       :", l2)

# Copie profonde
l3 = copy.deepcopy(originale)

# Modifier un élément du sous-liste
l3[1][0] = 300

print("\nAprès modification via l3 (copie profonde) :")
print("originale :", originale)
print("l3       :", l3) """

""" # 1. Référence (même objet)
reference = originale
print(f"1. Référence: originale is référence = {originale is reference}")

# 2. Copie superficielle
copie_simple = copy.copy(originale)
print(f"2. Copie simple: originale is copie_simple = {originale is copie_simple}")

# 3. Copie profonde
copie_profonde = copy.deepcopy(originale)
print(f"3. Copie profonde: originale is copie_profonde = {originale is copie_profonde}")

# Modification pour montrer la différence
print("\n=== APRÈS MODIFICATION ===")
originale[0][0] = 100  # Modifie la sous-liste

print(f"Originale: {originale}")
print(f"Référence: {reference}")          # Modifiée aussi
print(f"Copie simple: {copie_simple}")    # Sous-liste modifiée!
print(f"Copie profonde: {copie_profonde}") # Inchangée """

### 5.2 : Système de sauvegarde


# Créez un système qui:
# 1. Garde une copie de sauvegarde des données
# 2. Permet de restaurer la version précédente
# 3. Montre la différence entre les versions

""" import copy

donnees = {
    "utilisateurs": ["Alice", "Bob"],
    "config": {"theme": "sombre", "langue": "fr"}
}

# Votre code ici
# Historique des versions
historique = []

def sauvegarder(data):
    #Crée une copie indépendante et l'ajoute à l'historique
    historique.append(copy.deepcopy(data))
    print("Sauvegarde effectuée.")

def restaurer(version=-1):
    #Restaure la dernière version ou une version spécifique
    if historique:
        restored = copy.deepcopy(historique[version])
        print(f"Restauration de la version {version} réussie.")
        return restored
    else:
        print("Aucun historique disponible.")
        return None

def difference(v1, v2):
    #Affiche les différences entre deux versions (très simple)
    print("\nDifférences :")
    for cle in v1:
        if v1[cle] != v2.get(cle):
            print(f"- Clé '{cle}': {v1[cle]} -> {v2[cle]}")

# --- Exemple d'utilisation ---

print("Données initiales :", donnees)

# 1. Sauvegarder la version initiale
sauvegarder(donnees)

# 2. Modifier les données
donnees["utilisateurs"].append("Charlie")
donnees["config"]["theme"] = "clair"
print("\nAprès modification :", donnees)

# 3. Sauvegarder la nouvelle version
sauvegarder(donnees)

# 4. Montrer la différence avec la version précédente
difference(historique[-2], historique[-1])

# 5. Restaurer la version précédente
donnees = restaurer(-2)
print("\nDonnées après restauration :", donnees) """

## Exercice 6 : Combinaisons d'imports

### 6.1 : Jeu de dés amélioré

# Créez un jeu qui:
# 1. Lance 3 dés (random)
# 2. Calcule les statistiques (math)
# 3. Sauvegarde les résultats (json)
# 4. Vérifie si le fichier de scores existe (os)

""" import random
import math
import json
import os

# Votre code ici
# Nom du fichier pour sauvegarder les scores
fichier_scores = "scores.json"

# 1. Lancer 3 dés
des = [random.randint(1, 6) for _ in range(3)]
print("Résultats des dés :", des)

# 2. Calculer les statistiques
somme = sum(des)
moyenne = sum(des) / len(des)
ecart_type = math.sqrt(sum((x - moyenne) ** 2 for x in des) / len(des))
max_des = max(des)
min_des = min(des)

print(f"Somme : {somme}")
print(f"Moyenne : {moyenne:.2f}")
print(f"Écart-type : {ecart_type:.2f}")
print(f"Max : {max_des}, Min : {min_des}")

# 3. Créer un dictionnaire pour sauvegarder
resultat = {
    "des": des,
    "somme": somme,
    "moyenne": round(moyenne, 2),
    "ecart_type": round(ecart_type, 2),
    "max": max_des,
    "min": min_des
}

# 4. Vérifier si le fichier existe et charger l'historique
if os.path.exists(fichier_scores):
    with open(fichier_scores, "r") as f:
        scores = json.load(f)
else:
    scores = []

# Ajouter le nouveau résultat
scores.append(resultat)

# Sauvegarder dans le fichier
with open(fichier_scores, "w") as f:
    json.dump(scores, f, indent=4)

print(f"\nRésultat sauvegardé dans '{fichier_scores}'") """

### 6.2 : Système de configuration

# Créez un système de configuration qui:
# 1. Lit un fichier JSON de configuration
# 2. Si non existant, crée une config par défaut
# 3. Sauvegarde une copie de backup
# 4. Génère des IDs aléatoires pour les utilisateurs

import json
import os
import random
import copy

# Votre code ici

""" class SystemeConfiguration:
    def __init__(self, fichier_config="config.json"):
        self.fichier_config = fichier_config
        self.config = self.charger_config()
        self.backup = None

    def charger_config(self):
        #Charge la configuration depuis le fichier
        if os.path.exists(self.fichier_config):
            try:
                with open(self.fichier_config, "r") as f:
                    config = json.load(f)
                print(f"Configuration chargée depuis {self.fichier_config}")
                return config
            except json.JSONDecodeError:
                print(f"Erreur de lecture de {self.fichier_config}")
                return self.config_par_defaut()
        else:
            print(f"Fichier {self.fichier_config} non trouvé. Création config par défaut.")
            return self.config_par_defaut()

    def config_par_defaut(self):
        #Retourne la configuration par défaut
        return {
            "application": {
                "nom": "MonApp",
                "version": "1.0",
                "debug": False
            },
            "utilisateurs": [],
            "parametres": {
                "theme": "sombre",
                "langue": "fr",
                "notifications": True
            }
        }

    def sauvegarder_config(self):
        #Sauvegarde la configuration actuelle
        # Créer un backup avant de sauvegarder
        self.backup = copy.deepcopy(self.config)

        with open(self.fichier_config, "w") as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)

        print(f"Configuration sauvegardée dans {self.fichier_config}")

    def creer_backup(self):
        #Crée un fichier de backup séparé
        if self.config:
            backup_file = f"config_backup_{random.randint(1000, 9999)}.json"
            with open(backup_file, "w") as f:
                json.dump(self.config, f, indent=2)
            print(f"Backup créé: {backup_file}")
            return backup_file
        return None

    def restaurer_backup(self, fichier_backup):
        #Restaure depuis un fichier backup
        if os.path.exists(fichier_backup):
            with open(fichier_backup, "r") as f:
                self.config = json.load(f)
            print(f"Configuration restaurée depuis {fichier_backup}")
            self.sauvegarder_config()
            return True
        else:
            print(f"Fichier backup {fichier_backup} non trouvé")
            return False

    def ajouter_utilisateur(self, nom):
        #Ajoute un utilisateur avec un ID aléatoire
        user_id = random.randint(10000, 99999)
        utilisateur = {
            "id": user_id,
            "nom": nom,
            "date_creation": "2024-01-15"
        }

        self.config["utilisateurs"].append(utilisateur)
        print(f"Utilisateur ajouté: {nom} (ID: {user_id})")
        self.sauvegarder_config()

        return user_id

    def modifier_parametre(self, cle, valeur):
        #Modifie un paramètre
        if cle in self.config["parametres"]:
            ancienne_valeur = self.config["parametres"][cle]
            self.config["parametres"][cle] = valeur
            print(f"Paramètre '{cle}' changé: {ancienne_valeur} → {valeur}")
            self.sauvegarder_config()
            return True
        else:
            print(f"Paramètre '{cle}' non trouvé")
            return False

    def afficher_config(self):
        #Affiche la configuration actuelle
        print("\n=== CONFIGURATION ACTUELLE ===")
        print(f"Application: {self.config['application']['nom']} v{self.config['application']['version']}")
        print(f"Utilisateurs: {len(self.config['utilisateurs'])}")
        print("Paramètres:")
        for cle, valeur in self.config['parametres'].items():
            print(f"  - {cle}: {valeur}")

# Test du système
systeme = SystemeConfiguration()

# Afficher la config initiale
systeme.afficher_config()

# Modifier des paramètres
systeme.modifier_parametre("theme", "clair")
systeme.modifier_parametre("langue", "en")

# Ajouter des utilisateurs
systeme.ajouter_utilisateur("Alice")
systeme.ajouter_utilisateur("Bob")

# Créer un backup
backup_file = systeme.creer_backup()

# Afficher la config modifiée
systeme.afficher_config()

# Restaurer depuis backup (optionnel)
# systeme.restaurer_backup(backup_file) """
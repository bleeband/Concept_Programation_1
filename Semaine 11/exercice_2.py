# ## **Partie 1 : Compréhension de base des exceptions**

# ### **Exercice 1.1 : Gestion d'erreurs de division**

# Écrivez un programme qui demande à l'utilisateur deux nombres et effectue leur division. Gérez les cas où :

# 1. L'utilisateur entre des valeurs non numériques
# 2. Le dénominateur est zéro
# 3. Tout se passe bien

# Affichez un message approprié dans chaque cas.

""" try:
    nbr_un = int(input("Entrez le premier nombre : "))
    nbr_deux = int(input("Entrez le deuxième nombre : "))

    resultat = nbr_un / nbr_deux
    print(f"Résultat : {resultat}")

except ValueError:
    print("Erreur : vous devez entrer des nombres valides.")

except ZeroDivisionError:
    print("Erreur : division par zéro impossible.")

else:
    print("Division effectuée avec succès.") """


# ### **Exercice 1.2 : Conversion sécurisée**

# Créez une fonction `conversion_securisee` qui prend une chaîne de caractères et tente de la convertir en entier. Si la conversion échoue, la fonction doit retourner `None` au lieu de lever une exception.

# Testez votre fonction avec :
# - `"123"`
# - `"12.5"`
# - `"abc"`
# - `"12a3"`

""" def conversion_securisee(chaine):
    try:
        return int(chaine)
    except ValueError:
        return None
    
tests = ["123", "12.5", "abc", "12a3"]

for valeur in tests:
    resultat = conversion_securisee(valeur)
    print(f"{valeur} -> {resultat}") """


# ### **Exercice 1.3 : Accès sécurisé à une liste**

# Écrivez une fonction `acces_liste` qui prend une liste et un index en paramètres. 
# La fonction doit retourner l'élément à cet index si possible, sinon retourner la chaîne `"Index hors limites"`.

""" def acces_liste(liste, index):
    if 0 <= index < len(liste):
        return liste[index]
    else:
        return "Index hors limites"
    
ma_liste = [10, 20, 30]

print(acces_liste(ma_liste, 1))
print(acces_liste(ma_liste, 5))
print(acces_liste(ma_liste, -1)) """

# --------------------------------------------------------------------------------------------------------------
# ## **Partie 2 : Utilisation de try-except-else-finally**

# ### **Exercice 2.1 : Gestion complète de fichiers**

# Écrivez un programme qui :

# 1. Demande à l'utilisateur un nom de fichier
# 2. Tente d'ouvrir et de lire le fichier
# 3. Si le fichier n'existe pas, affiche un message d'erreur
# 4. Si le fichier existe, compte le nombre de lignes
# 5. Finalement, affiche toujours "Opération terminée"

# Utilisez les blocs `try`, `except`, `else` et `finally`.

""" def lire_fichier():
    nom_fichier = input("Entrez le nom du fichier à lire : ")
    fichier = None

    try:
        fichier = open(nom_fichier, 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")
    except PermissionError:
        print(f"Erreur : Permission refusée pour lire '{nom_fichier}'.")
    else:
        contenu = fichier.readlines()
        nombre_lignes = len(contenu)
        print(f"Le fichier contient {nombre_lignes} lignes.")
    finally:
        if fichier:
            fichier.close()
        print("Opération terminée.") """


# ### **Exercice 2.2 : Calculatrice robuste**

# Créez une calculatrice qui gère les exceptions de manière exhaustive :

""" def calculatrice():
    
    print("\n=== CALCULATRICE SIMPLE ===")

    while True:
            print("\nOpérations disponibles :")
            print("1. Addition (+)")
            print("2. Soustraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Modulo (%)")
            print("6. Puissance (**)")            
            print("Q. Quitter")

            try:
                choix_menu = input("Veuillez faire votre choix : ").lower()

                if choix_menu == "q":
                    print("Merci ! Au revoir !")
                    break

                choix_menu = int(choix_menu)

                if choix_menu not in [1, 2, 3, 4, 5, 6]:
                    raise ValueError("Veuillez faire un choix parmi le menu")
                
                try:
                    nbr_un = float(input("Entrez votre premier nombre : "))
                    nbr_deux = float(input("Entrez votre deuxième nombre : "))
                except ValueError:
                    raise ValueError("Veuillez entrer un nombre valide")

                if choix_menu == 1:
                    resultat = nbr_un + nbr_deux
                    operateur = "+"

                elif choix_menu == 2:
                    resultat = nbr_un - nbr_deux
                    operateur = "-"

                elif choix_menu == 3:
                    resultat = nbr_un * nbr_deux
                    operateur = "*"

                elif choix_menu == 4:
                    if nbr_deux == 0:
                        raise ZeroDivisionError("Attention : division par zéro interdite")
                    resultat = nbr_un / nbr_deux  # peut lever ZeroDivisionError
                    operateur = "/"

                elif choix_menu == 5:
                    resultat = nbr_un % nbr_deux
                    operateur = "%"

                elif choix_menu == 6:
                    resultat = nbr_un ** nbr_deux
                    operateur = "**"

                print(f"Résultat : {nbr_un} {operateur} {nbr_deux} = {resultat}")

            except ValueError as ve:
                print(f"Erreur : {ve}")

            except ZeroDivisionError as zde:
                print(f"Erreur : {zde}")

            except Exception as e:
                print(f"Erreur inattendue : {e}")

            continuer = input("\nOn continu ? (o/n) : ").lower()
            if continuer != "o":
                print("Merci ! Au revoir !")
                break """


# ### **Exercice 2.3 : Validation d'entrée utilisateur**

# Écrivez une fonction `demander_age` qui :

# - Demande l'âge de l'utilisateur
# - Accepte uniquement les entiers entre 0 et 120
# - Utilise des exceptions pour gérer les entrées invalides
# - Redemande jusqu'à obtenir une valeur valide

""" def demander_age():
    while True:
        try:
            age_str = input("Entrez votre âge (0-120) : ")
            age = int(age_str)

            if age < 0:
                print("Erreur : L'âge ne peut pas être négatif.")
            elif age > 120:
                print("Erreur : L'âge ne peut pas dépasser 120 ans.")
            else:
                return age

        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

# Test
age_valide = demander_age()
print(f"Âge validé : {age_valide}") """


# --------------------------------------------------------------------------------------------------------------
# ## **Partie 3 : Création et levée d'exceptions personnalisées**

# ### **Exercice 3.1 : Classe CompteBancaire**

# Créez une classe `CompteBancaire` avec :

# - Un attribut `solde`
# - Une méthode `retirer(montant)` qui lève une exception `SoldeInsuffisantError` si le montant > solde
# - Une méthode `deposer(montant)` qui lève une exception `MontantNegatifError` si montant ≤ 0

# Créez les exceptions personnalisées nécessaires.

""" class SoldeInsuffisantError(Exception):
    pass

class MontantNegatifError(Exception):
    pass

class CompteBancaire:
    def __init__(self, solde_initial=0):
        self.solde = solde_initial

    def deposer(self, montant):
        if montant <= 0:
            raise MontantNegatifError(f"Le montant à déposer doit être positif : {montant}")
        self.solde += montant
        print(f"Dépôt de {montant} effectué. Nouveau solde : {self.solde}")

    def retirer(self, montant):
        if montant <= 0:
            raise MontantNegatifError(f"Le montant à retirer doit être positif : {montant}")
        if montant > self.solde:
            raise SoldeInsuffisantError(
                f"Solde insuffisant. Solde actuel : {self.solde}, tentative : {montant}"
            )
        self.solde -= montant
        print(f"Retrait de {montant} effectué. Nouveau solde : {self.solde}")
        return montant

    def afficher_solde(self):
        print(f"Solde actuel : {self.solde}")

# Test
compte = CompteBancaire(100)
try:
    compte.deposer(50)
    compte.retirer(30)
    compte.retirer(200)  # Devrait lever SoldeInsuffisantError
except (MontantNegatifError, SoldeInsuffisantError) as e:
    print(f"Erreur bancaire : {e}") """


# ### **Exercice 3.2 : Validation de mot de passe**

# Écrivez une fonction `valider_mot_de_passe` qui lève des exceptions personnalisées si :

# 1. Le mot de passe a moins de 8 caractères (`MotDePasseTropCourtError`)
# 2. Le mot de passe ne contient pas de chiffre (`PasDeChiffreError`)
# 3. Le mot de passe ne contient pas de majuscule (`PasDeMajusculeError`)

# Testez avec différents mots de passe.
""" class MotDePasseTropCourtError(Exception):
    pass

class PasDeChiffreError(Exception):
    pass

class PasDeMajusculeError(Exception):
    pass

def valider_mot_de_passe(mot_de_passe):
    if len(mot_de_passe) < 8:
        raise MotDePasseTropCourtError("Le mot de passe doit contenir au moins 8 caractères.")

    if not any(char.isdigit() for char in mot_de_passe):
        raise PasDeChiffreError("Le mot de passe doit contenir au moins un chiffre.")

    if not any(char.isupper() for char in mot_de_passe):
        raise PasDeMajusculeError("Le mot de passe doit contenir au moins une majuscule.")

    return True

# Tests
mots_de_passe = ["abc", "abcdefgh", "Abcdefgh", "ABCD1234", "Abc12345"]

for mdp in mots_de_passe:
    try:
        if valider_mot_de_passe(mdp):
            print(f"'{mdp}' : Mot de passe valide")
    except (MotDePasseTropCourtError, PasDeChiffreError, PasDeMajusculeError) as e:
        print(f"'{mdp}' : {e}") """

# ### **Exercice 3.3 : Système d'inscription**

# Créez un système d'inscription avec les règles suivantes :

# - Nom d'utilisateur : 3-20 caractères, pas d'espaces
# - Âge : 13-100 ans
# - Email : doit contenir '@' et '.'

# Lever des exceptions personnalisées pour chaque violation.

""" class NomUtilisateurInvalideError(Exception):
    pass

class AgeInvalideError(Exception):
    pass

class EmailInvalideError(Exception):
    pass

class SystemeInscription:
    def __init__(self):
        self.utilisateurs = []

    def valider_nom_utilisateur(self, nom):
        if len(nom) < 3 or len(nom) > 20:
            raise NomUtilisateurInvalideError("Le nom d'utilisateur doit contenir entre 3 et 20 caractères.")
        if ' ' in nom:
            raise NomUtilisateurInvalideError("Le nom d'utilisateur ne doit pas contenir d'espaces.")
        return True

    def valider_age(self, age):
        if age < 13 or age > 100:
            raise AgeInvalideError("L'âge doit être compris entre 13 et 100 ans.")
        return True

    def valider_email(self, email):
        if '@' not in email or '.' not in email:
            raise EmailInvalideError("L'email doit contenir un '@' et un '.'")
        if email.count('@') != 1:
            raise EmailInvalideError("L'email doit contenir exactement un '@'")
        return True

    def inscrire(self, nom, age, email):
        try:
            self.valider_nom_utilisateur(nom)
            self.valider_age(age)
            self.valider_email(email)

            utilisateur = {"nom": nom, "age": age, "email": email}
            self.utilisateurs.append(utilisateur)
            print(f"Utilisateur {nom} inscrit avec succès !")

        except (NomUtilisateurInvalideError, AgeInvalideError, EmailInvalideError) as e:
            print(f"Erreur d'inscription : {e}")
            return False
        return True

# Test
systeme = SystemeInscription()
systeme.inscrire("JohnDoe", 25, "john@example.com")      # Valide
systeme.inscrire("JD", 25, "john@example.com")           # Nom trop court
systeme.inscrire("John Doe", 25, "john@example.com")     # Contient espace
systeme.inscrire("JohnDoe", 10, "john@example.com")      # Âge invalide
systeme.inscrire("JohnDoe", 25, "johnexample.com")       # Email invalide """


# --------------------------------------------------------------------------------------------------------------
# ## **Partie 4 : Propagation et chaînage d'exceptions**

# ### **Exercice 4.1 : Fonctions imbriquées**

# Créez trois fonctions imbriquées :

""" def fonction_a():
    return fonction_b()

def fonction_b():
    try:
        return fonction_c()
    except ZeroDivisionError:
        raise ValueError("Une erreur mathématique s'est produite dans les calculs.") from None

def fonction_c():
    return 1 / 0

# Test
try:
    fonction_a()
except ValueError as e:
    print(f"Erreur attrapée : {e}") """


# ### **Exercice 4.2 : Chaînage d'exceptions**

# Écrivez un programme qui :

# 1. Tente d'ouvrir un fichier de configuration
# 2. Si le fichier n'existe pas, tente d'utiliser une configuration par défaut
# 3. Si la configuration par défaut échoue aussi, lever une exception qui montre les deux erreurs en chaîne

""" class ConfigurationError(Exception):
    pass

def charger_configuration_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        raise ConfigurationError(f"Fichier de configuration '{nom_fichier}' introuvable") from e

def charger_configuration_defaut():
    try:
        # Simuler un problème avec la configuration par défaut
        config_par_defaut = "{invalid_json}"
        return eval(config_par_defaut)  # Cette ligne va échouer
    except Exception as e:
        raise ConfigurationError("La configuration par défaut est corrompue") from e

def charger_configuration():
    try:
        return charger_configuration_fichier("config.txt")
    except ConfigurationError as e1:
        try:
            print("Tentative avec configuration par défaut...")
            return charger_configuration_defaut()
        except ConfigurationError as e2:
            raise ConfigurationError("Impossible de charger la configuration") from e2

# Test
try:
    config = charger_configuration()
    print("Configuration chargée avec succès")
except ConfigurationError as e:
    print(f"Erreur finale : {e}")
    print(f"Exception originale : {e.__cause__}") """


# ### **Exercice 4.3 : Gestionnaire de contexte simple**

# Créez un gestionnaire de contexte `FichierSecurise` qui :

# - Ouvre un fichier en lecture
# - Garantit sa fermeture même en cas d'erreur
# - Relève les exceptions avec un message ajouté

# Utilisez-le comme ceci :

# with FichierSecurise("fichier.txt") as f:
#     contenu = f.read()

""" class FichierSecurise:
    def __init__(self, nom_fichier, mode='r'):
        self.nom_fichier = nom_fichier
        self.mode = mode
        self.fichier = None

    def __enter__(self):
        try:
            self.fichier = open(self.nom_fichier, self.mode, encoding='utf-8')
            return self.fichier
        except Exception as e:
            raise IOError(f"Impossible d'ouvrir le fichier {self.nom_fichier}") from e

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fichier:
            self.fichier.close()
        if exc_type is not None:
            print(f"Une exception s'est produite : {exc_type.__name__}")
        return False  # Ne pas supprimer l'exception

# Test
try:
    with FichierSecurise("fichier_inexistant.txt") as f:
        contenu = f.read()
        print(contenu)
except IOError as e:
    print(f"Erreur d'E/S : {e}") """



# --------------------------------------------------------------------------------------------------------------
# ## **Partie 5 : Exercices de synthèse**

# ### **Exercice 5.1 : Gestionnaire de tâches**

# Créez un gestionnaire de tâches qui lit un fichier JSON (simulez avec un dictionnaire ). Gérez toutes les exceptions possibles :

# - Fichier inexistant
# - Format JSON invalide
# - Champs manquants dans les tâches
# - Types de données incorrects

""" import json

class FormatTacheError(Exception):
    pass

class ChampManquantError(Exception):
    pass

class GestionnaireTaches:
    def __init__(self, fichier_taches):
        self.fichier_taches = fichier_taches
        self.taches = []

    def charger_taches(self):
        try:
            with open(self.fichier_taches, 'r', encoding='utf-8') as f:
                contenu = f.read()

            donnees = json.loads(contenu)

            if not isinstance(donnees, list):
                raise FormatTacheError("Le fichier doit contenir une liste de tâches")

            for i, tache in enumerate(donnees):
                if not isinstance(tache, dict):
                    raise FormatTacheError(f"La tâche à l'index {i} doit être un dictionnaire")

                champs_requis = ["id", "description", "terminee"]
                for champ in champs_requis:
                    if champ not in tache:
                        raise ChampManquantError(f"Champ '{champ}' manquant dans la tâche {i}")

                if not isinstance(tache["terminee"], bool):
                    raise FormatTacheError(f"Le champ 'terminee' doit être booléen dans la tâche {i}")

            self.taches = donnees
            print(f"{len(self.taches)} tâches chargées avec succès")

        except FileNotFoundError:
            print("Fichier de tâches non trouvé, liste vide utilisée")
            self.taches = []
        except json.JSONDecodeError as e:
            raise FormatTacheError(f"Format JSON invalide : {e}")

    def ajouter_tache(self, description):
        nouvelle_id = max([t["id"] for t in self.taches], default=0) + 1
        nouvelle_tache = {
            "id": nouvelle_id,
            "description": description,
            "terminee": False
        }
        self.taches.append(nouvelle_tache)
        print(f"Tâche '{description}' ajoutée (ID: {nouvelle_id})")

    def afficher_taches(self):
        if not self.taches:
            print("Aucune tâche")
            return

        for tache in self.taches:
            statut = "✓" if tache["terminee"] else " "
            print(f"{statut} {tache['id']}: {tache['description']}")

# Test
gestionnaire = GestionnaireTaches("taches.json")
try:
    gestionnaire.charger_taches()
    gestionnaire.ajouter_tache("Apprendre les exceptions Python")
    gestionnaire.afficher_taches()
except (FormatTacheError, ChampManquantError) as e:
    print(f"Erreur de format : {e}")
except Exception as e:
    print(f"Erreur inattendue : {type(e).__name__} - {e}") """


# ### **Exercice 5.2 : Calculatrice scientifique étendue**

# Étendez la calculatrice de l'exercice 2.2 pour gérer :

# - Les racines carrées (erreur sur nombres négatifs)
# - Les logarithmes (erreur sur nombres ≤ 0)
# - Les puissances
# - Créez une hiérarchie d'exceptions personnalisées
""" class ErreurMathematique(Exception):
    pass

class NombreNegatifError(ErreurMathematique):
    pass

class NombreNonPositifError(ErreurMathematique):
    pass

def calculatrice_scientifique():
    while True:
        print("\n=== Calculatrice Scientifique ===")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Racine carrée (√)")
        print("6. Logarithme (log)")
        print("7. Puissance (^)")
        print("8. Quitter")

        choix = input("Choix (1-8) : ")

        if choix == '8':
            print("Au revoir !")
            break

        try:
            if choix in ['5', '6']:  # Opérations unaires
                a = float(input("Nombre : "))
            else:
                a = float(input("Premier nombre : "))
                if choix != '7':  # Pas besoin de deuxième nombre pour racine/log
                    b = float(input("Deuxième nombre : "))

            if choix == '1':
                resultat = a + b
            elif choix == '2':
                resultat = a - b
            elif choix == '3':
                resultat = a * b
            elif choix == '4':
                if b == 0:
                    raise ZeroDivisionError("Division par zéro")
                resultat = a / b
            elif choix == '5':
                if a < 0:
                    raise NombreNegatifError("La racine carrée d'un nombre négatif n'est pas définie")
                resultat = a ** 0.5
            elif choix == '6':
                if a <= 0:
                    raise NombreNonPositifError("Le logarithme n'est défini que pour les nombres positifs")
                import math
                resultat = math.log(a)
            elif choix == '7':
                b = float(input("Exposant : "))
                resultat = a ** b
            else:
                print("Choix invalide")
                continue

            print(f"Résultat : {resultat}")

        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
        except ZeroDivisionError as e:
            print(f"Erreur mathématique : {e}")
        except (NombreNegatifError, NombreNonPositifError) as e:
            print(f"Erreur de domaine : {e}")
        except Exception as e:
            print(f"Erreur inattendue : {type(e).__name__} - {e}")

# Test
calculatrice_scientifique() """

# ### **Exercice 5.3 : Système de réservation**

# Simulez un système de réservation de billets avec :

# - Un nombre limité de places
# - Validation des données utilisateur
# - Gestion des conflits (deux réservations simultanées)
# - Sauvegarde/chargement depuis fichier

# Utilisez des exceptions pour tous les cas d'erreur.
""" import json

class ReservationError(Exception):
    pass

class PlaceIndisponibleError(ReservationError):
    pass

class DonneesInvalidesError(ReservationError):
    pass

class SystemeReservation:
    def __init__(self, fichier_reservations="reservations.json", places_total=100):
        self.fichier_reservations = fichier_reservations
        self.places_total = places_total
        self.reservations = []

    def charger_reservations(self):
        try:
            with open(self.fichier_reservations, 'r', encoding='utf-8') as f:
                self.reservations = json.load(f)
            print(f"{len(self.reservations)} réservations chargées")
        except FileNotFoundError:
            self.reservations = []
            print("Fichier de réservations non trouvé, initialisation vide")
        except json.JSONDecodeError:
            raise DonneesInvalidesError("Format de fichier invalide")

    def sauvegarder_reservations(self):
        try:
            with open(self.fichier_reservations, 'w', encoding='utf-8') as f:
                json.dump(self.reservations, f, indent=2)
            print("Réservations sauvegardées")
        except Exception as e:
            raise ReservationError(f"Erreur lors de la sauvegarde : {e}")

    def verifier_disponibilite(self, nombre_places):
        places_prises = sum(r['places'] for r in self.reservations)
        return places_prises + nombre_places <= self.places_total

    def reserver(self, nom, email, nombre_places):
        if not nom or not email:
            raise DonneesInvalidesError("Nom et email sont requis")

        if nombre_places <= 0:
            raise DonneesInvalidesError("Le nombre de places doit être positif")

        if not self.verifier_disponibilite(nombre_places):
            raise PlaceIndisponibleError(
                f"Plus assez de places disponibles. Demandé : {nombre_places}"
            )

        reservation = {
            "id": len(self.reservations) + 1,
            "nom": nom,
            "email": email,
            "places": nombre_places
        }

        self.reservations.append(reservation)
        print(f"Réservation confirmée pour {nom} ({nombre_places} places)")
        return reservation

    def annuler_reservation(self, reservation_id):
        for i, reservation in enumerate(self.reservations):
            if reservation["id"] == reservation_id:
                del self.reservations[i]
                print(f"Réservation {reservation_id} annulée")
                return

        raise ReservationError(f"Réservation {reservation_id} non trouvée")

    def afficher_statistiques(self):
        places_prises = sum(r['places'] for r in self.reservations)
        places_disponibles = self.places_total - places_prises
        print(f"Places prises : {places_prises}")
        print(f"Places disponibles : {places_disponibles}")
        print(f"Nombre de réservations : {len(self.reservations)}")

# Test
systeme = SystemeReservation(places_total=50)

try:
    systeme.charger_reservations()
    systeme.reserver("Alice", "alice@email.com", 2)
    systeme.reserver("Bob", "bob@email.com", 5)
    systeme.reserver("Charlie", "charlie@email.com", 100)  # Devrait échouer
except (PlaceIndisponibleError, DonneesInvalidesError) as e:
    print(f"Erreur de réservation : {e}")
except ReservationError as e:
    print(f"Erreur système : {e}")

systeme.afficher_statistiques() """


# --------------------------------------------------------------------------------------------------------------
# ## **Partie 6 : Bonnes pratiques et cas avancés**

# ### **Exercice 6.1 : Exception ou valeur de retour ?**

# Pour chaque scénario, décidez si une exception ou une valeur de retour spéciale est plus appropriée :

# 1. Recherche d'un élément dans une liste (élément non trouvé)
# 2. Conversion d'une chaîne en entier (chaîne invalide)
# 3. Ouverture d'un fichier (fichier inexistant)
# 4. Division de deux nombres (division par zéro)
# 5. Accès à une clé de dictionnaire (clé absente)

# Implémentez les deux approches et discutez des avantages/inconvénients.
# 1. Recherche dans une liste - Exception
""" def trouver_element_exception(liste, element):
    try:
        index = liste.index(element)
        return index
    except ValueError:
        raise ValueError(f"Élément {element} non trouvé dans la liste")

# 1. Recherche dans une liste - Valeur de retour
def trouver_element_valeur(liste, element):
    try:
        return liste.index(element)
    except ValueError:
        return -1

# 2. Conversion chaîne en entier - Exception
def convertir_int_exception(chaine):
    try:
        return int(chaine)
    except ValueError:
        raise ValueError(f"Impossible de convertir '{chaine}' en entier")

# 2. Conversion chaîne en entier - Valeur de retour
def convertir_int_valeur(chaine):
    try:
        return int(chaine)
    except ValueError:
        return None

# 3. Ouverture de fichier - Exception (recommandée)
def ouvrir_fichier_exception(nom_fichier):
    try:
        with open(nom_fichier, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Fichier '{nom_fichier}' introuvable")

# 4. Accès dictionnaire - Exception
def acces_dict_exception(dictionnaire, cle):
    try:
        return dictionnaire[cle]
    except KeyError:
        raise KeyError(f"Clé '{cle}' non trouvée")

# 4. Accès dictionnaire - Valeur de retour (get())
def acces_dict_valeur(dictionnaire, cle):
    return dictionnaire.get(cle, None) """

# Discussion :
# - Utiliser des exceptions pour les erreurs "exceptionnelles"
# - Utiliser des valeurs de retour pour les cas "normaux" d'échec
# - Les exceptions sont meilleures pour la lisibilité et évitent les codes d'erreur magiques

# ### **Exercice 6.2 : Nettoyage de ressources**

# Écrivez un programme qui :

# 1. Ouvre deux fichiers
# 2. Copie le contenu du premier dans le second
# 3. Garantit que les deux fichiers sont fermés même en cas d'erreur
# 4. Supprime le fichier de sortie si la copie échoue
""" import os

def copier_fichier_secu(source, destination):
    fichier_source = None
    fichier_dest = None
    copie_reussie = False

    try:
        # Ouvrir les fichiers
        fichier_source = open(source, 'r', encoding='utf-8')
        fichier_dest = open(destination, 'w', encoding='utf-8')

        # Copier le contenu
        contenu = fichier_source.read()
        fichier_dest.write(contenu)

        copie_reussie = True
        print(f"Fichier copié de '{source}' vers '{destination}'")

    except FileNotFoundError:
        print(f"Erreur : Le fichier source '{source}' n'existe pas.")
    except PermissionError:
        print(f"Erreur : Permission insuffisante pour accéder aux fichiers.")
    except Exception as e:
        print(f"Erreur inattendue lors de la copie : {type(e).__name__} - {e}")

    finally:
        # Fermer les fichiers quoi qu'il arrive
        if fichier_source:
            fichier_source.close()
        if fichier_dest:
            fichier_dest.close()

        # Nettoyer si la copie a échoué
        if not copie_reussie and os.path.exists(destination):
            try:
                os.remove(destination)
                print(f"Fichier de destination '{destination}' nettoyé.")
            except Exception as e:
                print(f"Erreur lors du nettoyage : {e}")
# Test
copier_fichier_secu("fichier_source.txt", "fichier_dest.txt") """


# ### **Exercice 6.3 : Journalisation des exceptions**

# Créez un décorateur `journaliser_exceptions` qui :

# - Enveloppe une fonction
# - Capture toutes les exceptions
# - Les journalise dans un fichier `erreurs.log` avec la date et les détails
# - Relève l'exception originale

""" import datetime

def journaliser_exceptions(fichier_log="erreurs.log"):
    def decorateur(fonction):
        def wrapper(*args, **kwargs):
            try:
                return fonction(*args, **kwargs)
            except Exception as e:
                # Formater le message de journal
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                nom_fonction = fonction.__name__
                type_exception = type(e).__name__
                message_exception = str(e)

                message_log = (
                    f"[{timestamp}] Exception dans {nom_fonction} : "
                    f"{type_exception} - {message_exception}\n"
                )

                # Écrire dans le fichier de log
                try:
                    with open(fichier_log, 'a', encoding='utf-8') as f:
                        f.write(message_log)
                except Exception as log_error:
                    print(f"Erreur lors de la journalisation : {log_error}")

                # Relancer l'exception originale
                raise

        return wrapper
    return decorateur

# Exemple d'utilisation
@journaliser_exceptions("calculs.log")
def diviser(a, b):
    return a / b

@journaliser_exceptions("operations.log")
def operation_risquee():
    resultat = diviser(10, 0)
    return resultat

# Test
try:
    operation_risquee()
except ZeroDivisionError:
    print("Exception attrapée dans le programme principal") """

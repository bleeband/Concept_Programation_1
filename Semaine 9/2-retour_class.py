
# Exercices de Révision - Programmation Orientée Objet en Python

# Objectif : Retravailler les concepts de base de la POO vus en classe à travers des problèmes concrets.

""" class AppareilElectronique:

    nombre_appareil = 0

    def __init__(self, nom, systeme_exploitation, niveau_batterie = 100) -> None:
        self.nom = nom
        self.systeme_exploitation = systeme_exploitation
        self._niveau_batterie = niveau_batterie
        AppareilElectronique.nombre_appareil += 1

    def decrire(self):
        return f"{self.nom} fonctionne sous {self.systeme_exploitation}"
    
    def utiliser(self, duree):
        consomme = duree * 2
        self._niveau_batterie -= consomme

        if self._niveau_batterie < 0:
            self._niveau_batterie = 0

    def recharger(self, duree):
        recharge = duree * 10
        self._niveau_batterie += recharge

        if self._niveau_batterie > 100:
            self._niveau_batterie = 100

    @classmethod
    def obtenir_statistiques(cls):

        print(f"Nombre total d'appareils créés : {cls.nombre_appareil}.")
    
    @property
    def niveau_batterie(self):
        return self._niveau_batterie
    
    @niveau_batterie.setter
    def niveau_batterie(self, valeur):
        
        if not isinstance(valeur, int):
            raise ValueError("Le niveau de batterie doit être un entier.")
        if valeur < 0 or valeur > 100:
            raise ValueError("Le niveau de batterie doit être compris entre 0 et 100.")
        self._niveau_batterie = valeur
 
class Smartphone(AppareilElectronique):

    def __init__(self, nom, systeme_exploitation, numero_de_telephone):
        super().__init__(nom, systeme_exploitation)
        self.numero_de_telephone = numero_de_telephone
    
    def decrire(self):
        return f"Smartphone {self.nom} ({self.systeme_exploitation}) - Numéro : {self.numero_de_telephone}"
    
class Tablette(AppareilElectronique):

    def __init__(self, nom, systeme_exploitation, taille_ecran):
        super().__init__(nom, systeme_exploitation)
        self.taille_ecran = taille_ecran

    def decrire(self):
        return f"Tablette {self.nom} ({self.systeme_exploitation}) - Ecran de : {self.taille_ecran} pouces "

telephone = AppareilElectronique("telephhone", "samsung", 80)
tel2 = Tablette("iphone","ios", 10.5)

print(telephone.niveau_batterie)

telephone.niveau_batterie = 55
print(telephone.niveau_batterie)

telephone.obtenir_statistiques() """


# Exercices Complémentaires - Types de méthodes, attributs et paramètres

# Ces exercices viennent **renforcer la compréhension fine des mécanismes internes** des classes. Ils permettent de bien distinguer ce qui appartient 
# à l'instance (`self`), à la classe entière (`cls`), ou à aucun des deux (`@staticmethod`), et d'expérimenter avec différentes façons de recevoir des paramètres.

""" class CapteurMeteo:
    unite = "Celsius"
    SEUIL_ALERTE = 40.0

    def __init__(self, identifiant) -> None:
        self.identifiant = identifiant
        self._temperature = None

    def mesurer(self, nouvelle_temp):
        self._temperature = nouvelle_temp

        if nouvelle_temp > CapteurMeteo.SEUIL_ALERTE:
            print(f"Le seuil d'alerte depasse {CapteurMeteo.SEUIL_ALERTE}")

    def afficher(self):
        return f"Le capteur {self.identifiant} affiche {self._temperature} ° {self.unite}"

    @classmethod

    def changer_unite(cls, nouvelle_unite):
        if nouvelle_unite not in ("Celsius", "Fahrenheit"):
            raise ValueError("Unité invalide. Utilisez 'Celsius' ou 'Fahrenheit'.")

        cls.unite = nouvelle_unite

    # Méthode statique
    @staticmethod
    def convertir_en_fahrenheit(temperature_celsius):
        return (temperature_celsius * 9 / 5) + 32     

class StationMeteo:
    def __init__(self, ville, *capteurs):
        self.ville = ville
        self.capteurs = list(capteurs)

    def ajouter_capteurs(self, *nouveaux_capteurs):
        self.capteurs.extend(nouveaux_capteurs)

    def resume(self, details=False):
        print(f"Station de {self.ville} : {len(self.capteurs)} capteur(s)")

        if details:
            for capteur in self.capteurs:
                print(capteur.afficher())

    # 🔍 Exercice 9
    def inspecter(self, nom_attribut=None):
        # Cas 1 : aucun attribut demandé
        if nom_attribut is None:
            for cle, valeur in self.__dict__.items():
                print(f"{cle} = {valeur}")

        # Cas 2 : attribut précis
        else:
            if hasattr(self, nom_attribut):
                print(f"{nom_attribut} = {getattr(self, nom_attribut)}")
            else:
                print(f"Attribut '{nom_attribut}' inexistant")

c1 = CapteurMeteo("A1")
c2 = CapteurMeteo("B2")
c3 = CapteurMeteo("C3")
print("-----")
c1.mesurer(22)
c2.mesurer(35)
c3.mesurer(42)
print("-----")
station = StationMeteo("Montréal", c1, c2)
station.ajouter_capteurs(c3)
print("-----")
station.resume()
print("-----")
station.resume(details=True)
print("-----")
station.inspecter()
print("----")
station.inspecter("ville")
station.inspecter("capteurs")
station.inspecter("inexistant")
print("-----")
CapteurMeteo.changer_unite("Fahrenheit")
print(CapteurMeteo.convertir_en_fahrenheit(20)) """


##############

""" class BorneRecharge:
    puissance_max = 50 #(kW)
    SEUIL_SURCHAUFFE = 80.0 #(°C)

    def __init__(self, identifiant, temperature=20.0):
        self.identifiant = identifiant
        self.temperature = temperature
        self.en_service = True
    
    def mettre_a_jour_temperature(self, nouvelle_temp):
        self.temperature = nouvelle_temp

        if nouvelle_temp > self.SEUIL_SURCHAUFFE:
            print(f"⚠️ SURCHAUFFE : borne {self.identifiant}")
            self.en_service = False

    def etat(self):
        return f"Borne {self.identifiant} - Température : {self.temperature} °C - En service : {self.en_service}"
    
    @classmethod
    def changer_puissance(cls, nouvelle_puissance):
        cls.puissance_max = nouvelle_puissance
        if nouvelle_puissance <= 0:
            raise ValueError("La valeur ne peut etre inférieur à 0") 

    @staticmethod
    def convertir_en_fahrenheit(temperature_celsius):
        return (temperature_celsius * 9 / 5) + 32   
    
class StationRecharge:
    def __init__(self, nom, *bornes):
        self.nom = nom
        self.bornes = list(bornes)

    def ajouter_bornes(self, *nouvelle_bornes):
        self.bornes.extend(nouvelle_bornes)

    def resume(self, details=False):
        print(f"Station {self.nom} : {len(self.bornes)} bornes")

        if details:
            for bornes in self.bornes:
                print(bornes.etat())

borne1 = BorneRecharge("Borne 1")
borne2 = BorneRecharge("Borne 2", 45)
borne3 = BorneRecharge("Borne 3", 33)

station1 = StationRecharge("Travail", borne1, borne2)
station1.ajouter_bornes(borne3)
print("-----")
borne2.changer_puissance(5)
borne1.mettre_a_jour_temperature(110)

station1.resume()

station1.resume(details=True) """


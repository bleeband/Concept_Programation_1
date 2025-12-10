# Module principal du projet.

def main():
    """Point d'entrée du programme."""
    print("Bienvenue!")

if __name__ == "__main__":
    main()

def saluer(nom: str) -> str:
    # Retourne un message de salutation
    return f"Bonjour, {nom} !"

def main():
    print("Bienvenue!")
    print(saluer("Utilisateur"))
    
def valider_email(email: str) -> bool:
    """Vérifie format email."""
    return "@" in email

def formater_tel(num: str) -> str:
    """Formate un téléphone."""
    chiffres = "".join(c for c in num if c.isdigit())
    return f"{chiffres[:2]} {chiffres[2:4]}..."
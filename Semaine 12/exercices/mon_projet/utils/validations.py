def email_valide(email):
    # return "@" in email and "." in email
    if "@" in email and "." in email:
        return True
    else:
        raise ValueError("Adresse courriel invalide")
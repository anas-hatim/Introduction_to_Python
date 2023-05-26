#!/usr/bin/env python3
def set_password():
    while True:  # Boucle tant que la condition est vraie
        try:
            password = input("Entrez un mot de passe : ")  # Demande à l'utilisateur d'entrer un mot de passe
            if len(password) < 8:  # Vérifie si la longueur du mot de passe est inférieure à 8
                raise ValueError("Le mot de passe est trop court.")  # Lève une exception ValueError si la condition est vraie
            # Autres conditions de validation du mot de passe ici
            
            # Si toutes les conditions sont satisfaites, sortir de la boucle
            break
        except ValueError as error:  # Capture l'exception ValueError
            print(f"Erreur : {str(error)}")  # Affiche le message d'erreur de l'exception
            
    print("Mot de passe valide !")  # Affiche un message indiquant que le mot de passe est valide

# Exemple d'utilisation
set_password()

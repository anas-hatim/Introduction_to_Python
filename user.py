#!/usr/bin/env python3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def reset_password(self):
        new_password = input("Entrez votre nouveau mot de passe : ")
        self.password = new_password
        print("Mot de passe réinitialisé avec succès.")


# Exemple d'utilisation de la classe User
username = input("Entrez votre nom d'utilisateur : ")
password = input("Entrez votre mot de passe : ")

user = User(username, password)

print("Informations de l'utilisateur :")
print("Nom d'utilisateur :", user.username)
print("Mot de passe :", user.password)

user.reset_password()

print("Nouvelles informations de l'utilisateur :")
print("Nom d'utilisateur :", user.username)
print("Nouveau mot de passe :", user.password)

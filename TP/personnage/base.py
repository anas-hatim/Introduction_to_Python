#!/usr/bin/env python3

# Définition de la classe Personnage
class Personnage:
    def __init__(self, nom):
        self.nom = nom
        self.points_de_vie = 100  # Les points de vie du personnage sont initialisés à 100

    def combattre(self, cible):
        cible.subir_degats(10)  # Le personnage inflige 10 dégâts à la cible

    def subir_degats(self, degats):
        self.points_de_vie -= degats  # Le personnage subit les dégâts passés en paramètre


# Définition de la classe Enemy qui hérite de Personnage
class Enemy(Personnage):
    pass  # La classe Enemy ne possède pas de méthodes supplémentaires, elle hérite de celles de Personnage


# Définition de la classe Hero qui hérite de Personnage
class Hero(Personnage):
    def __init__(self, nom):
        super().__init__(nom)
        self.points_de_mana = 100  # Les points de mana du héros sont initialisés à 100

    def soigner(self):
        if self.points_de_mana >= 100:  # Vérifie si le héros a assez de mana pour se soigner
            self.points_de_mana -= 100  # Déduit 100 points de mana pour se soigner
            self.points_de_vie += 33  # Ajoute 33 points de vie au héros


# Exemple d'utilisation
# ennemi = Enemy("Ennemi")  # Crée une instance de la classe Enemy avec le nom "Ennemi"
# heros = Hero("Héros")  # Crée une instance de la classe Hero avec le nom "Héros"
# heros.combattre(ennemi)  # Le héros attaque l'ennemi
# print(ennemi.points_de_vie)  # Affiche les points de vie de l'ennemi après l'attaque (devrait afficher 90)
# heros.soigner()  # Le héros se soigne
# print(heros.points_de_vie)  # Affiche les points de vie du héros après s'être soigné (devrait afficher 133)
# print(heros.points_de_mana)  # Affiche les points de mana du héros après s'être soigné (devrait afficher 0)

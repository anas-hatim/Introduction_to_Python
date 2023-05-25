#!/usr/bin/env python3

# Importation de la classe Personnage depuis le module personnage.base
from personnage.base import Personnage

# Définition de la classe Hero qui hérite de Personnage
class Hero(Personnage):
    def __init__(self, nom):
        super().__init__(nom)
        self.points_de_vie = 100  # Les points de vie du héros sont initialisés à 100
        self.mana = 100  # Le mana du héros est initialisé à 100

    def combattre(self, cible):
        cible.subir_degats(10)  # Le héros inflige 10 dégâts à la cible

    def soigner(self):
        if self.mana >= 100:
            self.points_de_vie += 33  # Le héros se soigne de 33 points de vie
            self.mana -= 100  # Le coût en mana de la guérison est déduit
            print(f"{self.nom} se soigne de 33 points de vie.")
        else:
            print("Pas assez de mana pour se soigner.")

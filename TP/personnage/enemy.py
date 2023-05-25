#!/usr/bin/env python3

# Importation de la classe Personnage depuis le module personnage.base
from personnage.base import Personnage

# Définition de la classe Enemy qui hérite de Personnage
class Enemy(Personnage):
    def __init__(self, nom):
        super().__init__(nom)
        self.points_de_vie = 100  # Les points de vie de l'ennemi sont initialisés à 100

    def combattre(self, cible):
        cible.subir_degats(10)  # L'ennemi inflige 10 dégâts à la cible

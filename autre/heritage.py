#!/usr/bin/env python3

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def manger(self):
        print(f"{self.nom} mange.")

    @classmethod
    def information(cls):
        print("C'est un animal.")


class Chien(Animal):
    def aboyer(self):
        print(f"{self.nom} aboie.")


chien = Chien("Rex")
chien.manger()  # Appelle la méthode manger() de la classe Animal
chien.aboyer()  # Appelle la méthode aboyer() de la classe Chien

Chien.information()  # Appelle la méthode information() de la classe Animal (héritée par Chien)

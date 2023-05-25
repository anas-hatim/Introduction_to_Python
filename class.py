#!/usr/bin/env python3

# Définition de la classe Vehicule
class Vehicule:
    def __init__(self, marque, vitesse):
        self.marque = marque
        self.vitesse = vitesse
        # Initialisation des attributs 'marque' et 'vitesse' avec les valeurs passées en paramètres

    def conduire(self):
        # Méthode pour conduire le véhicule
        print(f"{self.marque} roule à une vitesse de {self.vitesse} km/h.")

    def klaxonner(self):
        # Méthode pour klaxonner du véhicule (implémentation générique)
        print("Klaxon inconnu.")


# Définition de la classe Voiture, qui hérite de la classe Vehicule
class Voiture(Vehicule):
    def klaxonner(self):
        # Redéfinition de la méthode klaxonner spécifique à la Voiture
        print("Tutu")


# Définition de la classe Camion, qui hérite de la classe Vehicule
class Camion(Vehicule):
    def klaxonner(self):
        # Redéfinition de la méthode klaxonner spécifique au Camion
        print("Whooooo")
        

# Création d'une instance de Vehicule avec la marque "Véhicule générique" et une vitesse de 0 km/h
vehicule = Vehicule("Véhicule générique", 0)

# Création d'une instance de Voiture avec la marque "Renault" et une vitesse de 120 km/h
voiture = Voiture("Renault", 120)

# Création d'une instance de Camion avec la marque "Volvo" et une vitesse de 80 km/h
camion = Camion("Volvo", 80)

# Appel de la méthode conduire() pour le véhicule générique
vehicule.conduire()

# Appel de la méthode klaxonner() pour le véhicule générique
vehicule.klaxonner()

# Appel de la méthode conduire() pour la voiture Renault
voiture.conduire()

# Appel de la méthode klaxonner() pour la voiture Renault
voiture.klaxonner()

# Appel de la méthode conduire() pour le camion Volvo
camion.conduire()

# Appel de la méthode klaxonner() pour le camion Volvo
camion.klaxonner()

# Fin du programme
print("Fin du programme")

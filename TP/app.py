#!/usr/bin/env python3

from personnage.hero import Hero  # Importe la classe Hero depuis le module hero
from personnage.enemy import Enemy  # Importe la classe Enemy depuis le module enemy

# Création d'instances de héros et d'ennemi
hero = Hero("Héros courageux")  # Crée une instance de la classe Hero avec le nom "Héros courageux"
enemy = Enemy("Vilain méchant")  # Crée une instance de la classe Enemy avec le nom "Vilain méchant"

# Introduction
print("Bienvenue dans l'aventure !")
print(f"Vous incarnez {hero.nom}, un héros courageux qui se bat pour la justice.")
print(f"Au loin, vous apercevez {enemy.nom}, un vilain méchant qui terrorise la ville.")

# Début du combat
print(f"Vous engagez le combat avec {enemy.nom} !")

# Combat
while hero.points_de_vie > 0 and enemy.points_de_vie > 0:  # Boucle tant que le héros et l'ennemi ont des points de vie
    hero.combattre(enemy)  # Le héros attaque l'ennemi en appelant la méthode combattre de la classe Hero
    print(f"{hero.nom} attaque {enemy.nom}. Points de vie de {enemy.nom}: {enemy.points_de_vie}")
    if enemy.points_de_vie > 0:  # Vérifie si l'ennemi est encore en vie
        enemy.combattre(hero)  # L'ennemi contre-attaque le héros en appelant la méthode combattre de la classe Enemy
        print(f"{enemy.nom} contre-attaque {hero.nom}. Points de vie de {hero.nom}: {hero.points_de_vie}")

# Résultat du combat
if hero.points_de_vie > 0:  # Vérifie si le héros est encore en vie
    print(f"Félicitations ! {hero.nom} a triomphé de {enemy.nom}. Vous avez sauvé la ville !")
else:
    print(f"Oh non ! {hero.nom} a été vaincu par {enemy.nom}. La ville est en danger !")

# Fin de l'histoire
print("Fin de l'aventure. Merci d'avoir joué !")

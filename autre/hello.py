#!/usr/bin/env python3

# Types de bases
num = 1  # Assignation d'une valeur entière à la variable 'num'
string = "toto"  # Assignation d'une valeur de type chaîne de caractères à la variable 'string'
numFloat = 1.0  # Assignation d'une valeur décimale à la variable 'numFloat'
boolTrue = True  # Assignation de la valeur booléenne 'True' à la variable 'boolTrue'
boolFalse = False  # Assignation de la valeur booléenne 'False' à la variable 'boolFalse'
liste = [1,2,3,4,"cinq"]  # Assignation d'une liste contenant différents types de valeurs à la variable 'liste'
tupple = (1,2,3,4)  # Assignation d'un tuple à la variable 'tupple'
dictionnaire = {
    "clef1": "valeur1",
    "clef2": 33
}  # Assignation d'un dictionnaire avec des paires clé-valeur à la variable 'dictionnaire'

# Operation de base sur les nombres
addition = num + 3  # Addition de la valeur de 'num' avec 3 et assignation du résultat à 'addition'
soustraction = num - 3  # Soustraction de la valeur de 'num' par 3 et assignation du résultat à 'soustraction'
multiplication = num * 3  # Multiplication de la valeur de 'num' par 3 et assignation du résultat à 'multiplication'
division = num / 3  # Division de la valeur de 'num' par 3 et assignation du résultat à 'division'
reste = num % 2  # Calcul du reste de la division de 'num' par 2 et assignation du résultat à 'reste'
num += 5  # Incrémentation de 'num' de 5 (équivalent à 'num = num + 5')
print(addition)  # Affichage du résultat de l'addition
print(soustraction)  # Affichage du résultat de la soustraction
print(multiplication)  # Affichage du résultat de la multiplication
print(division)  # Affichage du résultat de la division
print(reste)  # Affichage du résultat du calcul du reste
print(num)  # Affichage de la valeur actuelle de 'num'
print()  # Affichage d'une ligne vide pour améliorer la lisibilité

# Operation de base sur les strings
concatenation = string + " suite"  # Concaténation de la variable 'string' avec une autre chaîne de caractères et assignation du résultat à 'concatenation'
fstring = f"La valeur de division est: {division}"  # Utilisation d'une f-string pour formater une chaîne de caractères avec la valeur de 'division'
print(concatenation)  # Affichage de la concaténation des chaînes
print(fstring)  # Affichage de la f-string
print()  # Affichage d'une ligne vide pour améliorer la lisibilité

# Operation de base sur les listes
liste.append(0)  # Ajout de la valeur 0 à la fin de la liste 'liste' avec la méthode 'append'
print(liste)  # Affichage de la liste mise à jour
liste.insert(2, "toto")  # Insertion de la chaîne de caractères 'toto' à la position 2 dans la liste 'liste' avec la méthode 'insert'
print(liste)  # Affichage de la liste mise à jour
liste.pop(3)  # Suppression de l'élément à l'index 3 dans la liste 'liste' avec la méthode 'pop'
print(liste)  # Affichage de la liste mise à jour
print()  # Affichage d'une ligne vide pour améliorer la lisibilité

# Tuple non modifiable
# Les tuples sont des structures de données immuables, donc il n'y a pas d'opérations de modification spécifiques

# Opération de base sur les dictionnaires
print(dictionnaire)  # Affichage du dictionnaire 'dictionnaire'
print(dictionnaire["clef1"])  # Affichage de la valeur associée à la clé "clef1" dans le dictionnaire
dictionnaire["nouvvelleclef"] = "nouvelle valeur"  # Ajout d'une nouvelle paire clé-valeur au dictionnaire
print(dictionnaire)  # Affichage du dictionnaire mis à jour
del dictionnaire["clef2"]  # Suppression de la paire clé-valeur associée à la clé "clef2" dans le dictionnaire avec l'opérateur 'del'
print(dictionnaire)  # Affichage du dictionnaire mis à jour

# Récupérer entrée utilisateur:
entreeString = input("Donner la valeur")  # Récupération d'une valeur saisie par l'utilisateur et assignation à la variable 'entreeString'

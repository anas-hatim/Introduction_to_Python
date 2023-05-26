#!/usr/bin/env python3
# Ouverture du fichier "example.txt" en mode écriture (w) avec l'instruction `with`
# L'utilisation de `with` garantit que le fichier sera fermé automatiquement
# même en cas d'erreur ou d'exception
with open("example.txt", "w") as file:
    # Écriture de la chaîne de caractères "Hello, World!" dans le fichier
    file.write("ma premier line 🏗️")

    # Écriture d'une nouvelle ligne dans le fichier
    file.write("\n")

    # Écriture de plusieurs lignes en utilisant la méthode `writelines()`
    # On passe une liste de chaînes de caractères, chaque chaîne représente une ligne
    file.writelines(["This is line 1\n", "This is line 2\n", "This is line 3\n"])

    # Fermeture automatique du fichier à la fin du bloc `with`

# Ouverture du fichier "example.txt" en mode lecture (r) avec l'instruction `with`
# pour lire le contenu du fichier
with open("example.txt", "r") as file:
    # Lecture du contenu du fichier avec la méthode `read()`
    content = file.read()

    # Affichage du contenu du fichier
    print(content)

# Ouverture du fichier "example.txt" en mode ajout (a) avec l'instruction `with`
# pour ajouter du contenu à la fin du fichier
with open("example.txt", "a") as file:
    # Écriture d'une nouvelle ligne en utilisant la méthode `write()`
    file.write("tiens j'ai ajouter un cadeau 🖕")

# Ouverture du fichier "example.txt" en mode lecture (r) avec l'instruction `with`
# pour vérifier le contenu mis à jour
with open("example.txt", "r") as file:
    # Lecture du contenu mis à jour
    updated_content = file.read()

    # Affichage du contenu mis à jour
    print(updated_content)
 
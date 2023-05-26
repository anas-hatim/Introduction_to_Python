#!/usr/bin/env python3
import socket

# Création d'un objet de socket en utilisant la famille d'adresses IP v4 (AF_INET) et le protocole TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Adresse IP et port du serveur sur lequel nous voulons lier notre socket
server_ip = "10.10.10.1"
server_port = 8888

# Association du socket à l'adresse IP et au port spécifiés
s.bind((server_ip, server_port))

# Mise en écoute du socket pour les connexions entrantes, avec une file d'attente de 1 connexion
s.listen(1)

# Attente de la première connexion entrante et acceptation de celle-ci
client_socket, client_address = s.accept()
print("Connexion établie avec le client:", client_address)

# Envoi de données au client connecté
message = "Bonjour, client!"
client_socket.sendall(message.encode())

# Fermeture de la connexion avec le client
client_socket.close()

# Fermeture du socket serveur
s.close()

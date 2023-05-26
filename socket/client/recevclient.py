#!/usr/bin/env python3
import socket

# Création d'un objet de socket en utilisant la famille d'adresses IP v4 (AF_INET) et le protocole TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Adresse IP et port du serveur auquel nous souhaitons nous connecter
server_ip = "10.10.10.1"
server_port = 8888

# Connexion au serveur en utilisant l'adresse IP et le port spécifiés
s.connect((server_ip, server_port))

# Réception de la réponse du serveur (jusqu'à 1024 octets)
response = s.recv(1024).decode()

# Affichage de la réponse du serveur
print("Réponse du serveur:", response)

# Fermeture de la connexion avec le serveur
s.close()

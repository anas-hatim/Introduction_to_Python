#!/usr/bin/env python3
import socket

# Création d'un objet de socket en utilisant la famille d'adresses IP v4 (AF_INET) et le protocole TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Adresse IP et port du serveur auquel nous souhaitons nous connecter
server_ip = "10.10.10.1"
server_port = 8888

# Connexion au serveur en utilisant l'adresse IP et le port spécifiés
s.connect((server_ip, server_port))

# Message à envoyer au serveur
message = "Hello, serveur! c'est leewack"

# Conversion du message en une séquence d'octets (encodage UTF-8) avant de l'envoyer
s.sendall(message.encode())

# Fermeture de la connexion avec le serveur
s.close()

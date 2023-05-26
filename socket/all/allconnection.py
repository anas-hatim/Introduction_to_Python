#!/usr/bin/env python3
import socket

# Adresses IP et ports des clients
clients = [
    ("10.10.10.1", 8888, "Paul GRESSIER"),
    ("10.10.10.2", 8888, "Paul GRESSIER"),
    ("10.10.10.3", 8888, "ABOUKHEIR Zeinab"),
    ("10.10.10.4", 8888, "BOULOM Alex"),
    ("10.10.10.5", 8888, "CHIROT Mélina"),
    ("10.10.10.6", 8888, "DE LARREA Marc"),
    ("10.10.10.7", 8888, "GUILLON Alain"),
    ("10.10.10.9", 8888, "IKHELEF Yannis"),
    ("10.10.10.10", 8888, "JOUVE Zachary"),
    ("10.10.10.11", 8888, "MAJOREL Sophie"),
    ("10.10.10.12", 8888, "MAZRI Ryan"),
    ("10.10.10.13", 8888, "TAGUINE Tarek"),
    ("10.10.10.14", 8888, "DENIS Axel")
]

# Adresse IP et port du serveur
server_ip = "10.10.10.1"
server_port = 8888

# Fonction d'envoi de message
def send_message(ip, port, message):
    # Créer un socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Se connecter au client
        client_socket.connect((ip, port))
        # Envoyer le message
        client_socket.sendall(message.encode())
        # Fermer la connexion
        client_socket.close()
    except ConnectionRefusedError:
        print(f"Impossible de se connecter à {ip}:{port}")

# Fonction de réception de message
def receive_message(ip, port):
    # Créer un socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Se connecter au client
        client_socket.connect((ip, port))
        # Recevoir la réponse
        response = client_socket.recv(1024).decode()
        # Afficher la réponse personnalisée
        print(f"Réponse de {ip}:{port} ({get_client_name(ip)}): {get_custom_response(response)}")
        # Fermer la connexion
        client_socket.close()
    except ConnectionRefusedError:
        print(f"Impossible de se connecter à {ip}:{port}")

# Fonction pour obtenir le nom du client en fonction de son adresse IP
def get_client_name(ip):
    for client in clients:
        if client[0] == ip:
            return client[2]
    return "Client inconnu"

# Fonction pour personnaliser la réponse du client
def get_custom_response(response):
    if response == "Bonjour, client!🐼🐼🐼🐼":
        return "Salut toi aussi, j'espère que tu passes une excellente journée 🐦🐦🐦!"
    elif response == "Hello, serveur!":
        return "Salut serveur ! As-tu entendu parler de cette blague drôle 🐸🐸🐸🐸🐸?"
    else:
        return "Réponse mystérieuse... peut-être qu'un extraterrestre l'a interceptée🐛🐛🐛🐛 !"

# Envoyer un message personnalisé à chaque client
for client in clients:
    ip, port, name = client
    message = f"Salut {name} ! Devine quoi ? Les pingouins ont envahi le serveur !"
    send_message(ip, port, message)

# Recevoir les réponses personnalisées de chaque client
for client in clients:
    ip, port, _ = client
    receive_message(ip, port)

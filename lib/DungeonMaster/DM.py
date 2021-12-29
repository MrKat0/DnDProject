import os
import socket
import sys
import json
import asyncio
import threading
from PySide2.QtWidgets import QWidget
from socket import socket as s

loop = asyncio.new_event_loop()
players = {}


class DM:
    def __init__(self):
        self.host = s(socket.AF_INET, socket.SOCK_STREAM)
        self.host.bind((socket.gethostname(), 52525))
        print('Server ip: ', socket.gethostbyname(socket.gethostname()))
        self.host.listen(5)

    def broadcast(self, message, author):
        for client in players.keys():
            if players[client] != players[author]:
                client.send(message)

    def infoHandler(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message, client)
            except:
                self.disconnect(client)
                break


    def disconnect(self, client):
        username = players[client]
        print(f'{username} leave.')
        players.pop(client)
        client.close()

    def newConnections(self):
        while True:
            client, address = self.host.accept()

            username = client.recv(1024).decode('utf-8')

            players[client] = username

            print(f"{username} is connected with {str(address)}")

            message = f"ChatBot: {username} joined the chat!".encode("utf-8")
            self.broadcast(message, client)
            client.send("Connected to server".encode("utf-8"))

            thread = threading.Thread(target=self.infoHandler, args=(client,))
            thread.daemon = True
            thread.start()

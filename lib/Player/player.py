import json
import socket
import threading
from socket import socket as s
from dice import Dice
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *

d = Dice()

class PlayerGui(QMainWindow):
    username = 'Salem'

class Player:
    def __init__(self, username):
        self.username = username
        self.player = s(socket.AF_INET, socket.SOCK_STREAM)
        self.player.settimeout(600)
        self.player.connect((socket.gethostname(), 52525))
        self.player.send(self.username.encode("utf-8"))
        write_thread = threading.Thread(target=self.write_messages)
        write_thread.start()
        thread = threading.Thread(target=self.receive_messages)
        thread.daemon = True
        thread.start()

    def receive_messages(self):
        while True:
            try:
                message = self.player.recv(1024).decode('utf-8')

                if message == "@username":
                    self.player.send(self.username.encode("utf-8"))
                else:
                    print(message)
            except:
                print("An error Ocurred")
                self.player.close
                break

    def receiveInfo(self):
        while True:
            try:
                msg = self.player.recv(1024).decode('utf-8')

                if msg == 'file':
                    with open(self.username + '.json', 'r') as f:
                        playerFile = json.loads(f.read())
                elif msg == 'dice':
                    d.Roll()
            except:
                exit()

    def write_messages(self):
        while True:
            message = f"{self.username}: {input('')}"
            self.player.send(message.encode('utf-8'))

    def sendInfo(self):
        with open(f'./Players/{self.username}.json', 'rb') as f:
            self.player.send('file')
            self.player.send(f)



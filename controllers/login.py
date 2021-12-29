import re
import socket
import threading
from lib.Views.loginForm import LoginForm
from PySide2.QtWidgets import QWidget
from socket import socket as s

class Login(QWidget, LoginForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.join)
    
    def join(self):
        username = self.username.text()
        ipAdress = self.ipadress.text()
        connection_data = (ipAdress, 52525)

        if username != '' and ipAdress != '':
            match = re.match(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$', ipAdress)
            if bool(match) is True:
                from controllers.player import Player
                self.playerWindow = Player(username, connection_data)
                self.playerWindow.show()
                self.close()
            else:
                self.ipadress.setText('')

        elif username != '' and ipAdress == '':
            pass
        elif username == '' and ipAdress != '':
            pass

    def receiveInstruction(self):
        while True:
            try:
                instruction = self.client.recv(1024).decode('utf-8')
            except:
                self.client.close()
                break
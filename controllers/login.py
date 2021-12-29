import re
import socket
import threading
from controllers.popup import Popup
from lib.Views.loginForm import LoginForm
from PySide2.QtWidgets import QWidget
from socket import socket as s

FORMAT = 'UTF-8'

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
                client = s(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(500)
                client.connect(connection_data)
                client.send(username.encode(FORMAT))
                login_msg = client.recv(1024).decode(FORMAT)
                if login_msg == '!DISCONNECT':
                    self.error = Popup('Error')
                    self.error.setText('Username already taken')
                    self.error.show()
                elif login_msg == '!CONNECTED':
                    from controllers.player import Player
                    self.playerWindow = Player(client, username, connection_data)
                    self.playerWindow.show()
                    self.close()
                
            else:
                self.ipadress.setText('')
                self.error = Popup('Invalid IP')
                self.error.setText('Insert a valid ip adress')
                self.error.show()

        elif username != '' and ipAdress == '':
            self.error = Popup('Missing ip')
            self.error.setText('Insert a ip adress')
            self.error.show()
        elif username == '' and ipAdress != '':
            self.error = Popup('Missing username')
            self.error.setText('Insert a username')
            self.error.show()
import socket
import threading
import json
from socket import socket as s
from controllers.master import FORMAT
from lib.Views.playerForm import PlayerForm
from PySide2.QtWidgets import QWidget

throws = []

class Player(QWidget, PlayerForm):
    def __init__(self, username:str, connection_data:tuple):
        self.last_send = None
        super().__init__()
        self.username = username
        self.setupUi(self)
        self.client = s(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(500)
        self.client.connect(connection_data)
        self.client.send(username.encode('utf-8'))
        login_msg = self.client.recv(1024).decode(FORMAT)
        if login_msg == '!DISCONNECT':
            self.usernameSlot.setText('Username already taken')
        elif login_msg == '!CONNECTED':
            self.fileCharge()
        self.throwButton.clicked.connect(self.rollDice)
        self.disconnectButton.clicked.connect(self.disconnectAction)
        
    def rollDice(self):
        from controllers.dice import DiceWindow
        self.rolling = DiceWindow()
        self.rolling.show()
        throws = self.rolling.report()
        for t in throws:
            print(t)

    def disconnectAction(self):
        self.client.send(bytes('!DISCONNECT', 'utf-8'))
        self.client.close()
        from controllers.selection import Selection
        self.selection = Selection()
        self.selection.show()
        self.close()
    
    def fileCharge(self):
        try:
            with open(f'./Players/{self.username}.json', 'r') as f:
                character = json.loads(f.read())
                f.close()
        except:
            self.disconnectAction()
        stats = character['stats']
        qual = character['qualities']
        
        self.usernameSlot.setText(self.username)
        self.life_value.setText(f'{stats["hp"]["max"]}/{stats["hp"]["current"]}')
        self.mana_value.setText(f'{stats["mana"]["max"]}/{stats["mana"]["current"]}')
        self.def_value.setText(f'{stats["defense"]}')
        self.stamina_value.setText(f'{stats["stamina"]}')
        self.instinct_value.setText(f'{stats["instinct"]}')
        self.gold_value.setText(f'{stats["gold"]}')
        self.attack_value.setText(f'{stats["attack"]}')
        self.str_value.setText(f'{qual["strength"]}')
        self.int_value.setText(f'{qual["intelligence"]}')
        self.tech_value.setText(f'{qual["technical"]}')
        self.agt_value.setText(f'{qual["agility"]}')
        self.spd_value.setText(f'{qual["speed"]}')
        self.res_value.setText(f'{qual["resistance"]}')
        self.chs_value.setText(f'{qual["charisma"]}')
    
    
        
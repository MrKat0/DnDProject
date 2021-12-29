import datetime
import socket
import threading
import os
import json
from datetime import date
from socket import socket as s
from controllers.master import DISCONNECT_MESSAGE
from lib.Views.playerForm import PlayerForm
from PySide2.QtWidgets import QWidget

today = date.today()
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

class Player(QWidget, PlayerForm):
    def __init__(self, client:s, username:str, connection_data:tuple):
        self.throwCommand = ''
        self.throws = []
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.client = client
        self.connection_data = connection_data
        self.throwButton.setDisabled(True)
        self.throwButton.clicked.connect(self.rollDice)
        self.disconnectButton.clicked.connect(self.disconnectAction)
        self.fileCharge()
        listener = threading.Thread(target=self.infoHandler, args=())
        listener.daemon = True
        listener.start()
        
    def rollDice(self):
        from controllers.dice import DiceWindow
        self.rolling = DiceWindow(self.client, self, self.throwCommand)
        self.rolling.show()
        
                
    def disconnectAction(self):
        self.client.send(bytes(DISCONNECT_MESSAGE, FORMAT))
        self.client.close()
        from controllers.selection import Selection
        self.selection = Selection()
        self.selection.show()
        self.close()
        
    def infoHandler(self):
        while True:
            try:
                info = self.client.recv(1024).decode(FORMAT)
                if '!' in info:
                    print(info)
                if info == '!THROW':
                    self.throwButton.setEnabled(True)
                    instructions = self.client.recv(1024).decode(FORMAT)
                    self.throwCommand = instructions
                    
                    
                elif info == DISCONNECT_MESSAGE:
                    self.disconnectAction()
                    break
            except socket.error:
                self.disconnectAction()
                break
    
    def fileCharge(self):
        if f'{self.username}.json' not in os.listdir('./Players/'):
            print('not found', os.listdir('./Players/'))
            self.disconnectAction()
        
        with open(f'./Players/{self.username}.json', 'r') as f:
            character = json.loads(f.read())
            f.close()
        
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
    
    
        
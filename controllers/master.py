import json
import socket
import threading
from socket import socket as s
from lib.Views.masterForm import MasterForm
from PySide2.QtWidgets import QWidget

players = {}
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

class Master(QWidget, MasterForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dm = s(socket.AF_INET, socket.SOCK_STREAM)
        self.dm.bind((socket.gethostname(), 52525))
        self.dm.listen(5)
        self.ipValue.setText(f'{socket.gethostbyname(socket.gethostname())}:52525')
        self.players.itemClicked.connect(self.fileSelection)
        self.disconnectButton.clicked.connect(self.disconnectAction)
        self.listener = threading.Thread(target=self.newConnections, args=())
        self.listener.daemon = True
        self.listener.start()
        
    def infoHandler(self, client):
        while True:
            info = client.recv(1024).decode(FORMAT)
            if info == DISCONNECT_MESSAGE:
                self.disconnect(client)
                
    def disconnect(self, client):
        for k in players.keys():
            if players[k] == client:
                username = k
                break
        for i in range(0, len(players.keys())):
            if username == self.players.item(i).text():
                index = i
                break
        print(f'{username} leave.')
        players.pop(username)
        self.players.model().removeRow(index)
        client.close()
    
    
    def sendThrow(self):
        pass

    def disconnectAction(self):
        self.dm.close()
        from controllers.selection import Selection
        self.selection = Selection()
        self.selection.show()
        self.close()
    
    def newConnections(self):
        while True:
            current_usernames = []
            client, address = self.dm.accept()

            username = client.recv(1024).decode(FORMAT)
            for k in players.keys():
                current_usernames.append(k)
            if username not in current_usernames:
                players[username] = client
                
                print(f"{username} is connected with {str(address)}")

                self.players.addItem(username)
                
                client.send(bytes('!CONNECTED', FORMAT))
                
                thread = threading.Thread(target=self.infoHandler, args=(client,))
                thread.daemon = True
                thread.start()
            else:
                print('Username already connected')
                client.send(bytes(DISCONNECT_MESSAGE, FORMAT))
                self.disconnect(client)
                break

    def fileSelection(self):
        selectFile = self.players.currentItem().text()
        with open(f'./Players/{selectFile}.json', 'r') as f:
            character = json.loads(f.read())
            f.close()
        stats = character['stats']
        qual = character['qualities']
        history = character['history']

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
        self.historyBox.setPlainText(history)
        
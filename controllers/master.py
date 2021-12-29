import json
import socket
import threading
import asyncio
from requests import get
from socket import socket as s
from lib.Views.masterForm import MasterForm
from PySide2.QtWidgets import QWidget

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

class Master(QWidget, MasterForm):
    def __init__(self):
        super().__init__()
        self.users = {}
        self.sorted = False
        self.playerThrows = {}
        self.setupUi(self)
        self.fileCharge('default')
        self.dm = s(socket.AF_INET, socket.SOCK_STREAM)
        serverIP = get("https://api.ipify.org").text
        self.dm.bind((socket.gethostname(), 52525))
        self.dm.listen(5)
        self.ipValue.setText(f'{serverIP}:52525')
        self.players.itemClicked.connect(self.fileSelection)
        self.disconnectButton.clicked.connect(self.disconnectAction)
        self.listener = threading.Thread(target=self.newConnections, args=())
        self.listener.daemon = True
        self.listener.start()
        self.alphabetButton.clicked.connect(self.sortByAlphabet)
        self.throwButton.clicked.connect(self.sendThrow)
        
    def infoHandler(self, client):
        while True:
            try:
                info = client.recv(1024).decode(FORMAT)
                if '!' in info:
                    print(info)
                if info == '!THROW':
                    throw = client.recv(1024).decode(FORMAT)
                    for k in self.users.keys():
                        if self.users[k] == client:
                            username = k
                            break
                    throw = json.loads(throw.replace('\'', '\"'))
                    self.playerThrows[username].append(throw)
                    self.throwHistorial.addItem(f'{throw["Dices"]} Throws:{throw["Throws"]} Total:{throw["Total"]}')
                    
                elif info == DISCONNECT_MESSAGE:
                    self.disconnect(client)
                    break
            except socket.error:
                self.disconnect(client)
                break
            
    def sortByAlphabet(self):
        temp = []
        for i in range(0, len(self.users.keys())):
            temp.append(self.players.item(i).text())
        temp.sort(reverse=self.sorted)
        self.sorted = not self.sorted
        self.players.clear()
        for t in temp:
            self.players.addItem(t)
                
    def disconnect(self, client):
        for k in self.users.keys():
            if self.users[k] == client:
                username = k
                break
        if self.players.currentItem().text() == username:
            self.fileCharge('default')
        for i in range(0, len(self.users.keys())):
            if username == self.players.item(i).text():
                index = i
                break
        print(f'{username} leave.')
        self.users.pop(username)
        self.players.model().removeRow(index)
        client.close()
    
    
    def sendThrow(self):
        username = self.players.currentItem().text()
        client = self.users[username]
        client.send('!THROW'.encode(FORMAT))
        print(f'{username} gonna roll!')
        throw = f'{self.numberThrow.currentText()}{self.layerThrow.currentText()}'.encode(FORMAT)
        print(throw)
        client.send(throw)
        

    def disconnectAction(self):
        self.dm.sendall(DISCONNECT_MESSAGE.encode(FORMAT))
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
            for k in self.users.keys():
                current_usernames.append(k)
            if username not in current_usernames:
                self.users[username] = client
                self.playerThrows[username] = []
                
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
        self.throwHistorial.clear()
        fileName = self.players.currentItem().text()
        self.fileCharge(fileName)
        
        
    def fileCharge(self, fileName):
        with open(f'./Players/{fileName}.json', 'r') as f:
            character = json.loads(f.read())
            f.close()
        if fileName != 'default':
            for throw in self.playerThrows[character['name']]:
                self.throwHistorial.addItem(str(throw))
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
        
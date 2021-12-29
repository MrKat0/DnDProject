import json
import socket
import os
from socket import socket as s
from datetime import date
import threading
from controllers.player import Player
from lib.dice import Dice
from lib.Views.diceForm import DiceForm
from PySide2.QtWidgets import QWidget

today = date.today()
FORMAT = 'UTF-8'

class DiceWindow(QWidget, DiceForm):
    def __init__(self, client:s, player:Player, throwInstructions:str):
        super().__init__()
        self.setupUi(self)
        self.client = client
        self.player = player
        self.number, self.layer = throwInstructions.split('d')
        self.number = int(self.number)
        self.layer = int(self.layer)
        self.n.setCurrentIndex(self.number - 1)
        if self.layer == 4:
            self.l.setCurrentIndex(0)
        elif self.layer == 6:
            self.l.setCurrentIndex(1)
        elif self.layer == 8:
            self.l.setCurrentIndex(2)
        elif self.layer == 10:
            self.l.setCurrentIndex(3)
        elif self.layer == 12:
            self.l.setCurrentIndex(4)
        elif self.layer == 20:
            self.l.setCurrentIndex(5)
        elif self.layer == 100:    
            self.l.setCurrentIndex(6)
        self.dice = Dice()
        self.button.clicked.connect(self.roll)
        self.l.setDisabled(True)
        self.n.setDisabled(True)
    
    def roll(self):
        n = self.n.currentIndex()
        l = self.l.currentIndex()
        throw = {}
        
        if l == 0:
            throw = self.dice.Roll(n + 1, 4)
        elif l == 1:
            throw = self.dice.Roll(n + 1, 6)
        elif l == 2:
            throw = self.dice.Roll(n + 1, 8)
        elif l == 3:
            throw = self.dice.Roll(n + 1, 10)
        elif l == 4:
            throw = self.dice.Roll(n + 1, 12)
        elif l == 5:
            throw = self.dice.Roll(n + 1, 20)
        elif l == 6:    
            throw = self.dice.Roll(n + 1, 100)
            
        self.result.setText(f'{throw["Throws"]}')
        self.total.setText(f'Total: {throw["Total"]}')
        if f'{today.strftime("%d-%m-%Y")}.txt' not in os.listdir('./logs'):
            with open(f'./logs/{today.strftime("%d-%m-%Y")}.txt', 'w+') as f:
                f.write(f'{str(throw)}\n')
                f.close()
        else:
            with open(f'./logs/{today.strftime("%d-%m-%Y")}.txt', 'a') as f:
                f.write(f'{str(throw)}\n')
                f.close()
        self.client.send('!THROW'.encode(FORMAT))
        self.client.send(str(throw).encode(FORMAT))
        self.player.throws.append(throw)
        self.player.throwRegister.addItem(f'{throw["Dices"]} Throws:{throw["Throws"]} Total:{throw["Total"]}')
        self.player.throwCommand = ''
        self.button.setDisabled(True)
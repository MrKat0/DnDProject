import json
import socket
from lib.dice import Dice
from lib.Views.diceForm import DiceForm
from PySide2.QtWidgets import QWidget

class DiceWindow(QWidget, DiceForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dice = Dice()
        self.button.clicked.connect(self.roll)
    
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
        return throw
    
    def report(self):
        return self.dice.history
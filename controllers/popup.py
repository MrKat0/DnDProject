from lib.Views.popupForm import PopupForm
from PySide2.QtWidgets import QWidget

class Popup(QWidget, PopupForm):
    def __init__(self, header:str):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(header)
        self.acceptButton.clicked.connect(self.acceptAction)
        
    def acceptAction(self):
        self.close()
        
    def setText(self, message:str):
        self.textLabel.setText(message)
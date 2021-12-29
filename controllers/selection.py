from lib.Views.selectionForm import SelectionForm
from PySide2.QtWidgets import QWidget

class Selection(QWidget, SelectionForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.join.clicked.connect(self.joinAction)
        self.host.clicked.connect(self.hostAction)
        
            
    def joinAction(self):
        from controllers.login import Login
        self.loginWindow = Login()
        self.loginWindow.show()
        self.close()

    def hostAction(self):
        from controllers.master import Master
        self.masterWindow = Master()
        self.masterWindow.show()
        self.close()
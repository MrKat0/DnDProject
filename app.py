import sys
from controllers.selection import Selection
from PySide2.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Selection()
    window.show()
    app.exec_()
        

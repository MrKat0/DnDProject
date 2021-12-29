# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diceForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class DiceForm(object):
    def setupUi(self, diceForm):
        if not diceForm.objectName():
            diceForm.setObjectName(u"diceForm")
        diceForm.resize(400, 300)
        self.l = QComboBox(diceForm)
        self.l.addItem("")
        self.l.addItem("")
        self.l.addItem("")
        self.l.addItem("")
        self.l.addItem("")
        self.l.addItem("")
        self.l.addItem("")
        self.l.setObjectName(u"l")
        self.l.setGeometry(QRect(130, 210, 51, 22))
        self.n = QComboBox(diceForm)
        self.n.addItem("")
        self.n.addItem("")
        self.n.addItem("")
        self.n.addItem("")
        self.n.addItem("")
        self.n.setObjectName(u"n")
        self.n.setGeometry(QRect(70, 210, 31, 22))
        self.total = QLabel(diceForm)
        self.total.setObjectName(u"total")
        self.total.setGeometry(QRect(196, 149, 141, 41))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.total.setFont(font)
        self.result = QLabel(diceForm)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(80, 60, 251, 61))
        font1 = QFont()
        font1.setPointSize(20)
        self.result.setFont(font1)
        self.result.setScaledContents(True)
        self.result.setAlignment(Qt.AlignCenter)
        self.button = QPushButton(diceForm)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(70, 150, 111, 51))

        self.retranslateUi(diceForm)

        QMetaObject.connectSlotsByName(diceForm)
    # setupUi

    def retranslateUi(self, diceForm):
        diceForm.setWindowTitle(QCoreApplication.translate("diceForm", u"Form", None))
        self.l.setItemText(0, QCoreApplication.translate("diceForm", u"d4", None))
        self.l.setItemText(1, QCoreApplication.translate("diceForm", u"d6", None))
        self.l.setItemText(2, QCoreApplication.translate("diceForm", u"d8", None))
        self.l.setItemText(3, QCoreApplication.translate("diceForm", u"d10", None))
        self.l.setItemText(4, QCoreApplication.translate("diceForm", u"d12", None))
        self.l.setItemText(5, QCoreApplication.translate("diceForm", u"d20", None))
        self.l.setItemText(6, QCoreApplication.translate("diceForm", u"d100", None))

        self.n.setItemText(0, QCoreApplication.translate("diceForm", u"1", None))
        self.n.setItemText(1, QCoreApplication.translate("diceForm", u"2", None))
        self.n.setItemText(2, QCoreApplication.translate("diceForm", u"3", None))
        self.n.setItemText(3, QCoreApplication.translate("diceForm", u"4", None))
        self.n.setItemText(4, QCoreApplication.translate("diceForm", u"5", None))

        self.n.setCurrentText(QCoreApplication.translate("diceForm", u"1", None))
        self.total.setText(QCoreApplication.translate("diceForm", u"Total: 0", None))
        self.result.setText(QCoreApplication.translate("diceForm", u"0", None))
        self.button.setText(QCoreApplication.translate("diceForm", u"Roll", None))
    # retranslateUi


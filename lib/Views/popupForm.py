# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popupForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class PopupForm(object):
    def setupUi(self, popupForm):
        if not popupForm.objectName():
            popupForm.setObjectName(u"popupForm")
        popupForm.setWindowModality(Qt.NonModal)
        popupForm.setEnabled(True)
        popupForm.resize(184, 94)
        popupForm.setCursor(QCursor(Qt.ArrowCursor))
        popupForm.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.gridLayout = QGridLayout(popupForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.acceptButton = QPushButton(popupForm)
        self.acceptButton.setObjectName(u"acceptButton")

        self.gridLayout.addWidget(self.acceptButton, 1, 0, 1, 1)

        self.textLabel = QLabel(popupForm)
        self.textLabel.setObjectName(u"textLabel")
        self.textLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textLabel, 0, 0, 1, 1)


        self.retranslateUi(popupForm)

        QMetaObject.connectSlotsByName(popupForm)
    # setupUi

    def retranslateUi(self, popupForm):
        popupForm.setWindowTitle(QCoreApplication.translate("popupForm", u"Error", None))
        self.acceptButton.setText(QCoreApplication.translate("popupForm", u"Accept", None))
        self.textLabel.setText(QCoreApplication.translate("popupForm", u"Error", None))
    # retranslateUi


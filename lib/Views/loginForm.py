# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class LoginForm(object):
    def setupUi(self, loginForm):
        if not loginForm.objectName():
            loginForm.setObjectName(u"loginForm")
        loginForm.resize(403, 203)
        self.layoutWidget = QWidget(loginForm)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(7, 8, 391, 191))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.loginButton = QPushButton(self.layoutWidget)
        self.loginButton.setObjectName(u"loginButton")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.loginButton)

        self.username = QLineEdit(self.layoutWidget)
        self.username.setObjectName(u"username")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.username)

        self.ipadress = QLineEdit(self.layoutWidget)
        self.ipadress.setObjectName(u"ipadress")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ipadress)


        self.verticalLayout.addLayout(self.formLayout)


        self.retranslateUi(loginForm)

        QMetaObject.connectSlotsByName(loginForm)
    # setupUi

    def retranslateUi(self, loginForm):
        loginForm.setWindowTitle(QCoreApplication.translate("loginForm", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("loginForm", u"IP adress", None))
        self.label.setText(QCoreApplication.translate("loginForm", u"Name", None))
        self.loginButton.setText(QCoreApplication.translate("loginForm", u"Login", None))
    # retranslateUi


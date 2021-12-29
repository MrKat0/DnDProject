# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectionForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class SelectionForm(object):
    def setupUi(self, selectionForm):
        if not selectionForm.objectName():
            selectionForm.setObjectName(u"selectionForm")
        selectionForm.resize(400, 300)
        self.formLayoutWidget = QWidget(selectionForm)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 80, 341, 141))
        self.horizontalLayout = QHBoxLayout(self.formLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.host = QPushButton(self.formLayoutWidget)
        self.host.setObjectName(u"host")

        self.horizontalLayout.addWidget(self.host)

        self.join = QPushButton(self.formLayoutWidget)
        self.join.setObjectName(u"join")

        self.horizontalLayout.addWidget(self.join)


        self.retranslateUi(selectionForm)

        QMetaObject.connectSlotsByName(selectionForm)
    # setupUi

    def retranslateUi(self, selectionForm):
        selectionForm.setWindowTitle(QCoreApplication.translate("selectionForm", u"Form", None))
        self.host.setText(QCoreApplication.translate("selectionForm", u"Host", None))
        self.join.setText(QCoreApplication.translate("selectionForm", u"Join", None))
    # retranslateUi


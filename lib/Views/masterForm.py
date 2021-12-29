# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'masterForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MasterForm(object):
    def setupUi(self, masterForm):
        if not masterForm.objectName():
            masterForm.setObjectName(u"masterForm")
        masterForm.resize(572, 490)
        self.verticalLayoutWidget_2 = QWidget(masterForm)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(400, 100, 160, 201))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.inventory = QListWidget(self.verticalLayoutWidget_2)
        self.inventory.setObjectName(u"inventory")

        self.verticalLayout_2.addWidget(self.inventory)

        self.formLayoutWidget_4 = QWidget(masterForm)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(10, 10, 161, 41))
        self.horizontalLayout = QHBoxLayout(self.formLayoutWidget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ip = QLabel(self.formLayoutWidget_4)
        self.ip.setObjectName(u"ip")

        self.horizontalLayout.addWidget(self.ip)

        self.ipValue = QLabel(self.formLayoutWidget_4)
        self.ipValue.setObjectName(u"ipValue")
        self.ipValue.setLayoutDirection(Qt.LeftToRight)
        self.ipValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.ipValue)

        self.verticalLayoutWidget = QWidget(masterForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 70, 161, 311))
        self.gridLayout_4 = QGridLayout(self.verticalLayoutWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.players = QListWidget(self.verticalLayoutWidget)
        self.players.setObjectName(u"players")

        self.gridLayout_4.addWidget(self.players, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.alphabetButton = QPushButton(self.verticalLayoutWidget)
        self.alphabetButton.setObjectName(u"alphabetButton")

        self.horizontalLayout_3.addWidget(self.alphabetButton)

        self.spdButton = QPushButton(self.verticalLayoutWidget)
        self.spdButton.setObjectName(u"spdButton")

        self.horizontalLayout_3.addWidget(self.spdButton)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.formLayoutWidget_3 = QWidget(masterForm)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(400, 10, 161, 61))
        self.gridLayout_3 = QGridLayout(self.formLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.formLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.def_value = QLabel(self.formLayoutWidget_3)
        self.def_value.setObjectName(u"def_value")

        self.gridLayout_3.addWidget(self.def_value, 0, 1, 1, 1)

        self.label_5 = QLabel(self.formLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.stamina_value = QLabel(self.formLayoutWidget_3)
        self.stamina_value.setObjectName(u"stamina_value")

        self.gridLayout_3.addWidget(self.stamina_value, 1, 1, 1, 1)

        self.label_6 = QLabel(self.formLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)

        self.gold_value = QLabel(self.formLayoutWidget_3)
        self.gold_value.setObjectName(u"gold_value")

        self.gridLayout_3.addWidget(self.gold_value, 2, 1, 1, 1)

        self.formLayoutWidget_2 = QWidget(masterForm)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(190, 10, 191, 81))
        self.gridLayout_2 = QGridLayout(self.formLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mana = QLabel(self.formLayoutWidget_2)
        self.mana.setObjectName(u"mana")

        self.gridLayout_2.addWidget(self.mana, 1, 0, 1, 1)

        self.label_3 = QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.instinct_value = QLabel(self.formLayoutWidget_2)
        self.instinct_value.setObjectName(u"instinct_value")

        self.gridLayout_2.addWidget(self.instinct_value, 2, 1, 1, 1)

        self.life_value = QLabel(self.formLayoutWidget_2)
        self.life_value.setObjectName(u"life_value")

        self.gridLayout_2.addWidget(self.life_value, 0, 1, 1, 1)

        self.mana_value = QLabel(self.formLayoutWidget_2)
        self.mana_value.setObjectName(u"mana_value")

        self.gridLayout_2.addWidget(self.mana_value, 1, 1, 1, 1)

        self.life = QLabel(self.formLayoutWidget_2)
        self.life.setObjectName(u"life")

        self.gridLayout_2.addWidget(self.life, 0, 0, 1, 1)

        self.label_7 = QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.attack_value = QLabel(self.formLayoutWidget_2)
        self.attack_value.setObjectName(u"attack_value")

        self.gridLayout_2.addWidget(self.attack_value, 3, 1, 1, 1)

        self.disconnectButton = QPushButton(masterForm)
        self.disconnectButton.setObjectName(u"disconnectButton")
        self.disconnectButton.setGeometry(QRect(490, 460, 75, 23))
        self.label_8 = QLabel(masterForm)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(190, 310, 91, 16))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.historyBox = QPlainTextEdit(masterForm)
        self.historyBox.setObjectName(u"historyBox")
        self.historyBox.setEnabled(True)
        self.historyBox.setGeometry(QRect(190, 330, 371, 121))
        self.historyBox.setReadOnly(True)
        self.verticalLayoutWidget_3 = QWidget(masterForm)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(190, 100, 191, 201))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.intButton = QRadioButton(self.verticalLayoutWidget_3)
        self.intButton.setObjectName(u"intButton")
        self.intButton.setMaximumSize(QSize(23, 23))

        self.gridLayout.addWidget(self.intButton, 1, 2, 1, 1)

        self.int_value = QLabel(self.verticalLayoutWidget_3)
        self.int_value.setObjectName(u"int_value")
        self.int_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.int_value, 1, 1, 1, 1)

        self.tech_value = QLabel(self.verticalLayoutWidget_3)
        self.tech_value.setObjectName(u"tech_value")
        self.tech_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.tech_value, 2, 1, 1, 1)

        self.int_2 = QLabel(self.verticalLayoutWidget_3)
        self.int_2.setObjectName(u"int_2")
        self.int_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.int_2, 1, 0, 1, 1)

        self.techButton = QRadioButton(self.verticalLayoutWidget_3)
        self.techButton.setObjectName(u"techButton")
        self.techButton.setMaximumSize(QSize(23, 23))

        self.gridLayout.addWidget(self.techButton, 2, 2, 1, 1)

        self.str = QLabel(self.verticalLayoutWidget_3)
        self.str.setObjectName(u"str")
        self.str.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.str, 0, 0, 1, 1)

        self.agtButton = QRadioButton(self.verticalLayoutWidget_3)
        self.agtButton.setObjectName(u"agtButton")
        self.agtButton.setMaximumSize(QSize(23, 23))

        self.gridLayout.addWidget(self.agtButton, 3, 2, 1, 1)

        self.label_10 = QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.resButton = QRadioButton(self.verticalLayoutWidget_3)
        self.resButton.setObjectName(u"resButton")
        self.resButton.setMaximumSize(QSize(23, 23))

        self.gridLayout.addWidget(self.resButton, 5, 2, 1, 1)

        self.chsButton = QRadioButton(self.verticalLayoutWidget_3)
        self.chsButton.setObjectName(u"chsButton")
        self.chsButton.setMaximumSize(QSize(23, 23))

        self.gridLayout.addWidget(self.chsButton, 6, 2, 1, 1)

        self.label_13 = QLabel(self.verticalLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)

        self.strButton = QRadioButton(self.verticalLayoutWidget_3)
        self.strButton.setObjectName(u"strButton")
        self.strButton.setMaximumSize(QSize(23, 23))

        self.gridLayout.addWidget(self.strButton, 0, 2, 1, 1)

        self.label_12 = QLabel(self.verticalLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)

        self.res_value = QLabel(self.verticalLayoutWidget_3)
        self.res_value.setObjectName(u"res_value")
        self.res_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.res_value, 5, 1, 1, 1)

        self.str_value = QLabel(self.verticalLayoutWidget_3)
        self.str_value.setObjectName(u"str_value")
        self.str_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.str_value, 0, 1, 1, 1)

        self.agt_value = QLabel(self.verticalLayoutWidget_3)
        self.agt_value.setObjectName(u"agt_value")
        self.agt_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.agt_value, 3, 1, 1, 1)

        self.label_11 = QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.spdButton_2 = QRadioButton(self.verticalLayoutWidget_3)
        self.spdButton_2.setObjectName(u"spdButton_2")
        self.spdButton_2.setMaximumSize(QSize(23, 23))

        self.gridLayout.addWidget(self.spdButton_2, 4, 2, 1, 1)

        self.spd_value = QLabel(self.verticalLayoutWidget_3)
        self.spd_value.setObjectName(u"spd_value")
        self.spd_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.spd_value, 4, 1, 1, 1)

        self.chs_value = QLabel(self.verticalLayoutWidget_3)
        self.chs_value.setObjectName(u"chs_value")
        self.chs_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.chs_value, 6, 1, 1, 1)

        self.label_9 = QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.throwButton = QPushButton(self.verticalLayoutWidget_3)
        self.throwButton.setObjectName(u"throwButton")

        self.verticalLayout_3.addWidget(self.throwButton)


        self.retranslateUi(masterForm)

        QMetaObject.connectSlotsByName(masterForm)
    # setupUi

    def retranslateUi(self, masterForm):
        masterForm.setWindowTitle(QCoreApplication.translate("masterForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("masterForm", u"Inventory", None))
        self.ip.setText(QCoreApplication.translate("masterForm", u"IP:", None))
        self.ipValue.setText(QCoreApplication.translate("masterForm", u"1.1.1.1", None))
        self.label_2.setText(QCoreApplication.translate("masterForm", u"Players", None))
        self.alphabetButton.setText(QCoreApplication.translate("masterForm", u"A-Z", None))
        self.spdButton.setText(QCoreApplication.translate("masterForm", u"SPD", None))
        self.label_4.setText(QCoreApplication.translate("masterForm", u"Defense", None))
        self.def_value.setText("")
        self.label_5.setText(QCoreApplication.translate("masterForm", u"Stamina", None))
        self.stamina_value.setText("")
        self.label_6.setText(QCoreApplication.translate("masterForm", u"Gold", None))
        self.gold_value.setText("")
        self.mana.setText(QCoreApplication.translate("masterForm", u"Mana", None))
        self.label_3.setText(QCoreApplication.translate("masterForm", u"Instinct", None))
        self.instinct_value.setText("")
        self.life_value.setText("")
        self.mana_value.setText("")
        self.life.setText(QCoreApplication.translate("masterForm", u"Life", None))
        self.label_7.setText(QCoreApplication.translate("masterForm", u"Attack", None))
        self.attack_value.setText("")
        self.disconnectButton.setText(QCoreApplication.translate("masterForm", u"disconnect", None))
        self.label_8.setText(QCoreApplication.translate("masterForm", u"HISTORY", None))
        self.intButton.setText("")
        self.int_value.setText("")
        self.tech_value.setText("")
        self.int_2.setText(QCoreApplication.translate("masterForm", u"INT", None))
        self.techButton.setText("")
        self.str.setText(QCoreApplication.translate("masterForm", u"STR", None))
        self.agtButton.setText("")
        self.label_10.setText(QCoreApplication.translate("masterForm", u"TECH", None))
        self.resButton.setText("")
        self.chsButton.setText("")
        self.label_13.setText(QCoreApplication.translate("masterForm", u"CHS", None))
        self.strButton.setText("")
        self.label_12.setText(QCoreApplication.translate("masterForm", u"SPD", None))
        self.res_value.setText("")
        self.str_value.setText("")
        self.agt_value.setText("")
        self.label_11.setText(QCoreApplication.translate("masterForm", u"AGT", None))
        self.spdButton_2.setText("")
        self.spd_value.setText("")
        self.chs_value.setText("")
        self.label_9.setText(QCoreApplication.translate("masterForm", u"RES", None))
        self.throwButton.setText(QCoreApplication.translate("masterForm", u"Throw Dice", None))
    # retranslateUi


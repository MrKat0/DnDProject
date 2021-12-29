# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playerForm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class PlayerForm(object):
    def setupUi(self, playerForm):
        if not playerForm.objectName():
            playerForm.setObjectName(u"playerForm")
        playerForm.resize(570, 448)
        self.verticalLayoutWidget_2 = QWidget(playerForm)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(409, 100, 151, 201))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.inventory = QListView(self.verticalLayoutWidget_2)
        self.inventory.setObjectName(u"inventory")

        self.verticalLayout_2.addWidget(self.inventory)

        self.verticalLayoutWidget = QWidget(playerForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 100, 160, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.throwRegister = QListView(self.verticalLayoutWidget)
        self.throwRegister.setObjectName(u"throwRegister")
        self.throwRegister.setEnabled(False)

        self.verticalLayout.addWidget(self.throwRegister)

        self.formLayoutWidget_3 = QWidget(playerForm)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(410, 10, 151, 61))
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

        self.formLayoutWidget_4 = QWidget(playerForm)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(10, 10, 161, 21))
        self.horizontalLayout = QHBoxLayout(self.formLayoutWidget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.player = QLabel(self.formLayoutWidget_4)
        self.player.setObjectName(u"player")
        self.player.setScaledContents(True)

        self.horizontalLayout.addWidget(self.player)

        self.usernameSlot = QLabel(self.formLayoutWidget_4)
        self.usernameSlot.setObjectName(u"usernameSlot")
        self.usernameSlot.setLayoutDirection(Qt.LeftToRight)
        self.usernameSlot.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.usernameSlot)

        self.formLayoutWidget_2 = QWidget(playerForm)
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

        self.life = QLabel(self.formLayoutWidget_2)
        self.life.setObjectName(u"life")

        self.gridLayout_2.addWidget(self.life, 0, 0, 1, 1)

        self.label_7 = QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.attack_value = QLabel(self.formLayoutWidget_2)
        self.attack_value.setObjectName(u"attack_value")

        self.gridLayout_2.addWidget(self.attack_value, 3, 1, 1, 1)

        self.life_value = QLabel(self.formLayoutWidget_2)
        self.life_value.setObjectName(u"life_value")

        self.gridLayout_2.addWidget(self.life_value, 0, 1, 1, 1)

        self.mana_value = QLabel(self.formLayoutWidget_2)
        self.mana_value.setObjectName(u"mana_value")

        self.gridLayout_2.addWidget(self.mana_value, 1, 1, 1, 1)

        self.disconnectButton = QPushButton(playerForm)
        self.disconnectButton.setObjectName(u"disconnectButton")
        self.disconnectButton.setGeometry(QRect(480, 410, 75, 23))
        self.formLayoutWidget = QWidget(playerForm)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(190, 100, 191, 199))
        self.gridLayout = QGridLayout(self.formLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tech_value = QLabel(self.formLayoutWidget)
        self.tech_value.setObjectName(u"tech_value")
        self.tech_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.tech_value, 2, 7, 1, 1)

        self.spdButton = QRadioButton(self.formLayoutWidget)
        self.spdButton.setObjectName(u"spdButton")

        self.gridLayout.addWidget(self.spdButton, 4, 5, 1, 1)

        self.int_value = QLabel(self.formLayoutWidget)
        self.int_value.setObjectName(u"int_value")
        self.int_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.int_value, 1, 7, 1, 1)

        self.res_value = QLabel(self.formLayoutWidget)
        self.res_value.setObjectName(u"res_value")
        self.res_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.res_value, 5, 7, 1, 1)

        self.agt_value = QLabel(self.formLayoutWidget)
        self.agt_value.setObjectName(u"agt_value")
        self.agt_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.agt_value, 3, 7, 1, 1)

        self.agtButton = QRadioButton(self.formLayoutWidget)
        self.agtButton.setObjectName(u"agtButton")

        self.gridLayout.addWidget(self.agtButton, 3, 5, 1, 1)

        self.strButton = QRadioButton(self.formLayoutWidget)
        self.strButton.setObjectName(u"strButton")
        self.strButton.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.strButton, 0, 5, 1, 1)

        self.str_value = QLabel(self.formLayoutWidget)
        self.str_value.setObjectName(u"str_value")
        self.str_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.str_value, 0, 7, 1, 1)

        self.resButton = QRadioButton(self.formLayoutWidget)
        self.resButton.setObjectName(u"resButton")

        self.gridLayout.addWidget(self.resButton, 5, 5, 1, 1)

        self.techButton = QRadioButton(self.formLayoutWidget)
        self.techButton.setObjectName(u"techButton")

        self.gridLayout.addWidget(self.techButton, 2, 5, 1, 1)

        self.chs_value = QLabel(self.formLayoutWidget)
        self.chs_value.setObjectName(u"chs_value")
        self.chs_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.chs_value, 6, 7, 1, 1)

        self.intButton = QRadioButton(self.formLayoutWidget)
        self.intButton.setObjectName(u"intButton")

        self.gridLayout.addWidget(self.intButton, 1, 5, 1, 1)

        self.chsButton = QRadioButton(self.formLayoutWidget)
        self.chsButton.setObjectName(u"chsButton")

        self.gridLayout.addWidget(self.chsButton, 6, 5, 1, 1)

        self.spd_value = QLabel(self.formLayoutWidget)
        self.spd_value.setObjectName(u"spd_value")
        self.spd_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.spd_value, 4, 7, 1, 1)

        self.throwButton = QPushButton(self.formLayoutWidget)
        self.throwButton.setObjectName(u"throwButton")

        self.gridLayout.addWidget(self.throwButton, 7, 7, 1, 1)

        self.freeRollButton = QRadioButton(self.formLayoutWidget)
        self.freeRollButton.setObjectName(u"freeRollButton")

        self.gridLayout.addWidget(self.freeRollButton, 7, 5, 1, 1)


        self.retranslateUi(playerForm)

        QMetaObject.connectSlotsByName(playerForm)
    # setupUi

    def retranslateUi(self, playerForm):
        playerForm.setWindowTitle(QCoreApplication.translate("playerForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("playerForm", u"Inventory", None))
        self.label_2.setText(QCoreApplication.translate("playerForm", u"Throws", None))
        self.label_4.setText(QCoreApplication.translate("playerForm", u"Defense", None))
        self.def_value.setText("")
        self.label_5.setText(QCoreApplication.translate("playerForm", u"Stamina", None))
        self.stamina_value.setText("")
        self.label_6.setText(QCoreApplication.translate("playerForm", u"Gold", None))
        self.gold_value.setText("")
        self.player.setText(QCoreApplication.translate("playerForm", u"Player", None))
        self.usernameSlot.setText("")
        self.mana.setText(QCoreApplication.translate("playerForm", u"Mana", None))
        self.label_3.setText(QCoreApplication.translate("playerForm", u"Instinct", None))
        self.instinct_value.setText("")
        self.life.setText(QCoreApplication.translate("playerForm", u"Life", None))
        self.label_7.setText(QCoreApplication.translate("playerForm", u"Attack", None))
        self.attack_value.setText("")
        self.life_value.setText("")
        self.mana_value.setText("")
        self.disconnectButton.setText(QCoreApplication.translate("playerForm", u"disconnect", None))
        self.tech_value.setText("")
        self.spdButton.setText(QCoreApplication.translate("playerForm", u"SPD", None))
        self.int_value.setText("")
        self.res_value.setText("")
        self.agt_value.setText("")
        self.agtButton.setText(QCoreApplication.translate("playerForm", u"AGT", None))
        self.strButton.setText(QCoreApplication.translate("playerForm", u"STR", None))
        self.str_value.setText("")
        self.resButton.setText(QCoreApplication.translate("playerForm", u"RES", None))
        self.techButton.setText(QCoreApplication.translate("playerForm", u"TECH", None))
        self.chs_value.setText("")
        self.intButton.setText(QCoreApplication.translate("playerForm", u"INT", None))
        self.chsButton.setText(QCoreApplication.translate("playerForm", u"CHS", None))
        self.spd_value.setText("")
        self.throwButton.setText(QCoreApplication.translate("playerForm", u"Throw Dice", None))
        self.freeRollButton.setText(QCoreApplication.translate("playerForm", u"Free Roll", None))
    # retranslateUi


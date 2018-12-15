#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QButtonGroup, QGroupBox, QSlider
from PyQt5.QtWidgets import QLabel, QApplication, QLineEdit, QRadioButton
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui
from random import randint

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)
        self.days = 0
        self.totalPapers = 0

        self.perfect = {'1': [[6, 2], [1, 4, 5, 8], [3, 7]], '2': [[1, 2, 8], [6, 7], [3, 4, 5]],
                        '3': [[4, 5, 6, 1, 3], [8], [2, 7]], '4': [[7], [], [1, 2, 3, 4, 5, 6, 8]],
                        '5': [[1, 7], [8, 2], [3, 4, 5, 6]], '6': [[2, 8, 1, 7], [3], [4, 5, 6]],
                        '7': [[6, 3, 7, 4, 5], [1], [2, 8]], '8': [[8, 2, 6, 4], [1, 5], [3, 7]]}
        self.levelOfKnowledge = 0
        self.setFont(QtGui.QFont("Bahnschrift Light SemiCondensed", 20))
        self.setMouseTracking(True)
        self.setWindowTitle('Game maker')
        self.setGeometry(10, 10, 1024, 768)
        palette = QPalette()
        img = QImage('mainWindow.png')
        scaled = img.scaled(self.size(), Qt.KeepAspectRatioByExpanding, transformMode=Qt.SmoothTransformation)
        palette.setBrush(QPalette.Window, QBrush(scaled))
        self.setPalette(palette)
        pixmap = QPixmap('shopButton.png')
        self.shopButton = QLabel('', self)
        self.shopButton.setPixmap(pixmap)
        self.shopButton.setMouseTracking(True)
        self.shopButton.move(500, 7)
        pixmap = QPixmap('devButton.png')
        self.devButton = QLabel('', self)
        self.devButton.setMouseTracking(True)
        self.devButton.setPixmap(pixmap)
        self.devButton.move(700, 7)
        self.cash = 100
        self.money = QLabel("Деньги:\n    100$", self)
        self.money.move(10, 7)
        self.subs = QLabel("Фанаты:\n   0", self)
        self.subs.move(140, 7)
        self.date = QLabel("Дни:\n     0", self)
        self.date.move(280, 7)
        self.table = QLabel('Создайте свою первую игру! \n  \nЗаработано за все дни: \n 0', self)
        self.table.move(150, 200)
        self.table.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;'
                                 'background-color: rgb(207, 162, 98);')
        self.shop = QWidget(self)
        self.shop.move(10000, 10000)
        self.shop.resize(400, 353)
        self.shop.setMouseTracking(True)
        self.shopItem1 = QLabel('', self.shop)
        self.shopItem1.setPixmap(QPixmap('shopItem1.png'))
        self.shopItem1.move(10, 10)
        self.shopItem1.setMouseTracking(True)
        self.shopItem2 = QLabel('', self.shop)
        self.shopItem2.setPixmap(QPixmap('shopItem22.png'))
        self.shopItem2.move(200, 10)
        self.shopItem2.setMouseTracking(True)
        self.shopItem3 = QLabel('', self.shop)
        self.shopItem3.setPixmap(QPixmap('shopItem4.png'))
        self.shopItem3.move(10, 250)
        self.shopItem3.setMouseTracking(True)
        self.shopItem4 = QLabel('', self.shop)
        self.shopItem4.setPixmap(QPixmap('shopItem4.png'))
        self.shopItem4.move(200, 250)
        self.shopItem4.setMouseTracking(True)
        self.shopExit = QLabel('', self.shop)
        self.shopExit.setPixmap(QPixmap('shopExit.png'))
        self.shopExit.move(360, 10)
        self.shopExit.setMouseTracking(True)
        self.shop.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;'
                                'background-color: rgb(207, 162, 98);')
        self.shopOn = False

        self.devPage1 = QWidget(self)
        self.devPage1.move(10000, 10000)
        self.devPage1.resize(600, 330)
        self.devPage1.setMouseTracking(True)
        self.devPage1.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;'
                                    'background-color: rgb(207, 162, 98);')
        self.theme = 0
        self.style = 0
        self.type = 0
        self.platform = 0
        self.styles = QGroupBox('Жанры', self.devPage1)
        self.styles.move(10, 10)
        self.styles.setMouseTracking(True)
        self.style1 = QRadioButton('Приключения', self.styles)
        self.style1.move(10, 20)
        self.style1.toggle()
        self.style2 = QRadioButton('Шутер', self.styles)
        self.style2.move(100, 20)
        self.style3 = QRadioButton('Слэшэр', self.styles)
        self.style3.move(10, 45)
        self.style4 = QRadioButton('MMO', self.styles)
        self.style4.move(100, 45)
        self.style5 = QRadioButton('MOBA', self.styles)
        self.style5.move(10, 70)
        self.style6 = QRadioButton('RPG', self.styles)
        self.style6.move(100, 70)
        self.style7 = QRadioButton('Симулятор', self.styles)
        self.style7.move(10, 95)
        self.style8 = QRadioButton('Кооператив', self.styles)
        self.style8.move(100, 95)
        self.styles.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.styles.setFont(QtGui.QFont("Bahnschrift Light SemiCondensed", 12))
        self.style1.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.style2.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.style3.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.style4.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.style5.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.style6.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.style7.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.style8.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.style1.adjustSize()
        self.style2.adjustSize()
        self.style3.adjustSize()
        self.style4.adjustSize()
        self.style5.adjustSize()
        self.style6.adjustSize()
        self.style7.adjustSize()
        self.style8.adjustSize()
        self.styles.adjustSize()

        self.themes = QGroupBox('Темы', self.devPage1)
        self.themes.move(300, 10)
        self.themes.setMouseTracking(True)
        self.theme1 = QRadioButton('Космос', self.themes)
        self.theme1.move(10, 20)
        self.theme1.toggle()
        self.theme2 = QRadioButton('Вестерн', self.themes)
        self.theme2.move(120, 20)
        self.theme3 = QRadioButton('Фэнтэзи', self.themes)
        self.theme3.move(10, 45)
        self.theme4 = QRadioButton('Ферма', self.themes)
        self.theme4.move(120, 45)
        self.theme5 = QRadioButton('Детектив', self.themes)
        self.theme5.move(10, 70)
        self.theme6 = QRadioButton('Война', self.themes)
        self.theme6.move(120, 70)
        self.theme7 = QRadioButton('Средневековье', self.themes)
        self.theme7.move(10, 95)
        self.theme8 = QRadioButton('Будущее', self.themes)
        self.theme8.move(120, 95)
        self.themes.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.themes.setFont(QtGui.QFont("Bahnschrift Light SemiCondensed", 12))
        self.theme1.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.theme2.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.theme3.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.theme4.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.theme5.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.theme6.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.theme7.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.theme8.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.theme1.adjustSize()
        self.theme2.adjustSize()
        self.theme3.adjustSize()
        self.theme4.adjustSize()
        self.theme5.adjustSize()
        self.theme6.adjustSize()
        self.theme7.adjustSize()
        self.theme8.adjustSize()
        self.themes.adjustSize()

        self.platforms = QGroupBox('Платформы', self.devPage1)
        self.platforms.move(10, 150)
        self.platforms.setMouseTracking(True)
        self.platform1 = QRadioButton('MacOs', self.platforms)
        self.platform1.move(10, 20)
        self.platform1.toggle()
        self.platform2 = QRadioButton('Android', self.platforms)
        self.platform2.move(120, 20)
        self.platform3 = QRadioButton('IOS', self.platforms)
        self.platform3.move(10, 45)
        self.platform4 = QRadioButton('PC', self.platforms)
        self.platform4.move(120, 45)
        self.platforms.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.platforms.setFont(QtGui.QFont("Bahnschrift Light SemiCondensed", 12))
        self.platform1.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.platform2.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.platform3.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.platform4.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.platform1.adjustSize()
        self.platform2.adjustSize()
        self.platform3.adjustSize()
        self.platform4.adjustSize()
        self.platforms.adjustSize()

        self.types = QGroupBox('Тип', self.devPage1)
        self.types.move(300, 150)
        self.types.setMouseTracking(True)
        self.type1 = QRadioButton('Инди', self.types)
        self.type1.move(10, 20)
        self.type1.toggle()
        self.type2 = QRadioButton('A', self.types)
        self.type2.move(120, 20)
        self.type3 = QRadioButton('AA', self.types)
        self.type3.move(10, 45)
        self.type4 = QRadioButton('AAA', self.types)
        self.type4.move(120, 45)
        self.types.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.types.setFont(QtGui.QFont("Bahnschrift Light SemiCondensed", 12))
        self.type1.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.type2.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.type3.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.type4.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.type1.adjustSize()
        self.type2.adjustSize()
        self.type3.adjustSize()
        self.type4.adjustSize()
        self.types.adjustSize()

        self.pushToDev = QPushButton('Начать', self.devPage1)
        self.pushToDev.setMouseTracking(True)
        self.pushToDev.move(280, 270)
        self.pushToDev.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;'
                                     'background-color: rgb(207, 162, 198);')
        self.pushToDev.clicked.connect(self.showDevPage2)

        self.devPage2 = QWidget(self)
        self.devPage2.move(10000, 10000)
        self.devPage2.resize(600, 330)
        self.devPage2.setMouseTracking(True)
        self.devPage2.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;'
                                    'background-color: rgb(207, 162, 98);')
        self.devPage1On = False
        self.devPage2On = False

        self.levelOne = QGroupBox('Знания I', self.devPage2)
        self.levelOne.move(10, 10)
        self.levelOne.setMouseTracking(True)
        self.techno11 = QCheckBox('2D(5$)', self.levelOne)
        self.techno11.move(10, 20)
        self.techno11.setMouseTracking(True)
        self.techno12 = QCheckBox('6 Bit Sound(15$)', self.levelOne)
        self.techno12.move(150, 20)
        self.techno13 = QCheckBox('HD(25$)', self.levelOne)
        self.techno13.move(10, 80)
        self.techno14 = QCheckBox('C++(35$)', self.levelOne)
        self.techno14.move(150, 80)
        self.levelOne.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.levelOne.setFont(QtGui.QFont("Bahnschrift Light SemiCondensed", 12))
        self.techno11.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno12.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno13.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno14.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno14.adjustSize()
        self.techno13.adjustSize()
        self.techno12.adjustSize()
        self.techno11.adjustSize()
        self.levelOne.adjustSize()
        self.techno12.setMouseTracking(True)
        self.techno13.setMouseTracking(True)
        self.techno14.setMouseTracking(True)

        self.levelTwo = QGroupBox('Знания II', self.devPage2)
        self.levelTwo.move(10, 170)
        self.levelTwo.setMouseTracking(True)
        self.techno21 = QCheckBox('3D(5$)', self.levelTwo)
        self.techno21.move(10, 20)
        self.techno21.setMouseTracking(True)
        self.techno22 = QCheckBox('8 Bit Sound(15$)', self.levelTwo)
        self.techno22.move(150, 20)
        self.techno23 = QCheckBox('Full HD(25$)', self.levelTwo)
        self.techno23.move(10, 80)
        self.techno24 = QCheckBox('C(35$)', self.levelTwo)
        self.techno24.move(150, 80)
        self.levelTwo.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.levelTwo.setFont(QtGui.QFont("Bahnschrift Light SemiCondensed", 12))
        self.techno21.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno22.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno23.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno24.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno24.adjustSize()
        self.techno23.adjustSize()
        self.techno22.adjustSize()
        self.techno21.adjustSize()
        self.levelTwo.adjustSize()
        self.techno22.setMouseTracking(True)
        self.techno23.setMouseTracking(True)
        self.techno24.setMouseTracking(True)

        self.levelThree = QGroupBox('Знания III', self.devPage2)
        self.levelThree.move(280, 10)
        self.levelThree.setMouseTracking(True)
        self.techno31 = QCheckBox('4D(5$)', self.levelThree)
        self.techno31.move(10, 20)
        self.techno31.setMouseTracking(True)
        self.techno32 = QCheckBox('16 Bit Sound(15$)', self.levelThree)
        self.techno32.move(150, 20)
        self.techno33 = QCheckBox('2K HD(25$)', self.levelThree)
        self.techno33.move(10, 80)
        self.techno34 = QCheckBox('C#(35$)', self.levelThree)
        self.techno34.move(150, 80)
        self.levelThree.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.levelThree.setFont(QtGui.QFont("Bahnschrift Light SemiCondensed", 12))
        self.techno31.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno32.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno33.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno34.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno34.adjustSize()
        self.techno33.adjustSize()
        self.techno32.adjustSize()
        self.techno31.adjustSize()
        self.techno31.setMouseTracking(True)
        self.techno32.setMouseTracking(True)
        self.techno34.setMouseTracking(True)
        self.techno33.setMouseTracking(True)
        self.levelThree.adjustSize()

        self.timeToEnd = 0
        self.timeDev = False

        self.levelFour = QGroupBox('Знания IV', self.devPage2)
        self.levelFour.move(280, 170)
        self.levelFour.setMouseTracking(True)
        self.techno41 = QCheckBox('5D(5$)', self.levelFour)
        self.techno41.setMouseTracking(True)
        self.techno41.move(10, 20)
        self.techno42 = QCheckBox('24 Bit Sound(15$)', self.levelFour)
        self.techno42.move(150, 20)
        self.techno43 = QCheckBox('Ultra HD(25$)', self.levelFour)
        self.techno43.move(10, 80)
        self.techno44 = QCheckBox('Python(35$)', self.levelFour)
        self.techno44.move(150, 80)
        self.levelFour.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;')
        self.levelFour.setFont(QtGui.QFont("Bahnschrift Light SemiCondensed", 12))
        self.techno41.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno42.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno43.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno44.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')
        self.techno44.adjustSize()
        self.techno43.adjustSize()
        self.techno42.adjustSize()
        self.techno41.adjustSize()
        self.techno42.setMouseTracking(True)
        self.techno44.setMouseTracking(True)
        self.techno43.setMouseTracking(True)
        self.levelFour.adjustSize()

        self.pushToStartDev = QPushButton('Начать', self.devPage2)
        self.pushToStartDev.setMouseTracking(True)
        self.pushToStartDev.move(280, 290)
        self.pushToStartDev.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;'
                                          'background-color: rgb(207, 162, 198);')
        self.pushToStartDev.clicked.connect(self.showDevPage3)

        self.timeToEnd = 5
        self.totalMoney = QLabel('Итого: 0', self.devPage2)
        self.totalMoney.move(100, 290)
        self.totalMoney.setStyleSheet('border-style: solid; border-width: 1px; border-color: black;'
                                      'background-color: rgb(207, 162, 198);')

        self.devPage1Exit = QLabel('', self.devPage1)
        self.devPage1Exit.setPixmap(QPixmap('shopExit.png'))
        self.devPage1Exit.move(560, 5)
        self.devPage1Exit.adjustSize()
        self.devPage1Exit.setMouseTracking(True)

        self.devPage2Exit = QLabel('', self.devPage2)
        self.devPage2Exit.setPixmap(QPixmap('shopExit.png'))
        self.devPage2Exit.move(560, 5)
        self.devPage2Exit.adjustSize()
        self.devPage2Exit.setMouseTracking(True)

        self.devPage3 = QWidget(self)
        self.devPage3.move(10000, 10000)
        self.devPage3.resize(600, 330)
        self.devPage3.setMouseTracking(True)
        self.devPage3.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;'
                                    'background-color: rgb(207, 162, 98);')

        self.warning = QLabel('', self.devPage2)
        self.warning.move(400, 290)
        self.warning.setFont(QtGui.QFont("Bahnschrift Light SemiCondensed", 10))
        self.warning.setStyleSheet('border-style: solid; border-width: 0px; border-color: black;')

        self.timeDev = False
        self.timeSale = False
        self.fans = 0




    def mouseMoveEvent(self, event):
        if 500 <= event.x() <= 645 and 7 <= event.y() <= 95:
            self.shopButton.setPixmap(QPixmap('shopButton2.png'))
        elif 700 <= event.x() <= 845 and 7 <= event.y() <= 95:
            self.devButton.setPixmap(QPixmap('devButton2.png'))
        elif 310 <= event.x() <= 455 and 211 <= event.y() <= 297 and self.shopOn:
            self.shopItem1.setPixmap(QPixmap('shopItem12.png'))
        elif 500 <= event.x() <= 644 and 211 <= event.y() <= 297 and self.shopOn:
            self.shopItem2.setPixmap(QPixmap('shopItem2.png'))
        elif 310 <= event.x() <= 455 and 461 <= event.y() <= 547 and self.shopOn:
            self.shopItem3.setPixmap(QPixmap('shopItem32.png'))
        elif 500 <= event.x() <= 644 and 461 <= event.y() <= 547 and self.shopOn:
            self.shopItem4.setPixmap(QPixmap('shopItem42.png'))
        elif self.devPage2On:
            self.totalMon = self.cashToDev
            if self.techno11.isChecked():
                self.totalMon += 5
            if self.techno12.isChecked():
                self.totalMon += 10
            if self.techno13.isChecked():
                self.totalMon += 20
            if self.techno14.isChecked():
                self.totalMon += 35
            if self.techno21.isChecked():
                self.totalMon += 100
            if self.techno22.isChecked():
                self.totalMon += 300
            if self.techno23.isChecked():
                self.totalMon += 500
            if self.techno24.isChecked():
                self.totalMon += 1000
            if self.techno31.isChecked():
                self.totalMon += 3500
            if self.techno32.isChecked():
                self.totalMon += 7000
            if self.techno33.isChecked():
                self.totalMon += 13000
            if self.techno34.isChecked():
                self.totalMon += 20000
            if self.techno41.isChecked():
                self.totalMon += 50000
            if self.techno42.isChecked():
                self.totalMon += 60000
            if self.techno43.isChecked():
                self.totalMon += 70000
            if self.techno44.isChecked():
                self.totalMon += 90000
            self.totalMoney.setText('Итого: ' + str(self.totalMon))
            self.totalMoney.adjustSize()
        else:
            self.shopButton.setPixmap(QPixmap('shopButton.png'))
            self.shopItem1.setPixmap(QPixmap('shopItem1.png'))
            self.devButton.setPixmap(QPixmap('devButton.png'))
            self.shopItem2.setPixmap(QPixmap('shopItem22.png'))
            self.shopItem3.setPixmap(QPixmap('shopItem3.png'))
            self.shopItem4.setPixmap(QPixmap('shopItem4.png'))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if 500 <= event.x() <= 645 and 7 <= event.y() <= 95:
                self.showShop()
            elif 700 <= event.x() <= 845 and 7 <= event.y() <= 95:
                self.showDev()
            elif 660 <= event.x() <= 690 and 211 <= event.y() <= 241 and self.shopOn:
                self.shopOn = False
                self.shop.move(10000, 10000)
            elif 760 <= event.x() <= 790 and 105 <= event.y() <= 135 and self.devPage1On:
                self.devPage1On = False
                self.devPage1.move(1000, 1000)
                self.timer.start()
            elif 760 <= event.x() <= 790 and 105 <= event.y() <= 135 and self.devPage2On:
                self.devPage2On = False
                self.timer.start()
                self.devPage2.move(10000, 10000)
            elif 310 <= event.x() <= 455 and 211 <= event.y() <= 297 and self.shopOn:
                if self.levelOfKnowledge < 1 and self.cash >= 5:
                    self.levelOfKnowledge = 1
                    self.cash -= 5
                    self.money.setText('Деньги: \n   ' + str(self.cash))
            elif 500 <= event.x() <= 644 and 211 <= event.y() <= 297 and self.shopOn:
                if self.levelOfKnowledge < 2 and self.cash >= 500:
                    self.levelOfKnowledge = 2
                    self.cash -= 500
                    self.money.setText('Деньги: \n   ' + str(self.cash))
            elif 310 <= event.x() <= 455 and 461 <= event.y() <= 547 and self.shopOn:
                if self.levelOfKnowledge < 3 and self.cash >= 20000:
                    self.levelOfKnowledge = 3
                    self.cash -= 20000
                    self.money.setText('Деньги: \n   ' + str(self.cash))
            elif 500 <= event.x() <= 644 and 461 <= event.y() <= 547 and self.shopOn:
                if self.levelOfKnowledge < 4 and self.cash >= 200000:
                    self.levelOfKnowledge = 4
                    self.cash -= 200000
                    self.money.setText('Деньги: \n   ' + str(self.cash))



    def showShop(self):
        self.shopOn = True
        self.shop.move(300, 200)

    def showDev(self):
        self.devPage1On = True
        self.timer.stop()
        self.platform1.setEnabled(False)
        self.platform2.setEnabled(False)
        self.platform3.setEnabled(False)
        self.platform4.setEnabled(False)
        self.type1.setEnabled(False)
        self.type2.setEnabled(False)
        self.type3.setEnabled(False)
        self.type4.setEnabled(False)
        if self.levelOfKnowledge >= 1:
            self.platform1.setEnabled(True)
            self.type1.setEnabled(True)
        if self.levelOfKnowledge >= 2:
            self.platform2.setEnabled(True)
            self.type2.setEnabled(True)
        if self.levelOfKnowledge >= 3:
            self.platform3.setEnabled(True)
            self.type3.setEnabled(True)
        if self.levelOfKnowledge >= 4:
            self.platform4.setEnabled(True)
            self.type4.setEnabled(True)
        self.devPage1.move(200, 100)

    def tick(self):
        self.days += 1
        self.date.setText('Дни:\n   ' + str(self.days))
        if self.timeDev:
            if self.timeToEnd > 1:
                self.timeToEnd -= 1
                self.table.setText('Дней до релиза: \n' + str(self.timeToEnd))
                self.table.adjustSize()
            else:
                self.relise()
        elif self.timeSale:
            if self.timeToEnd > 0:
                self.timeToEnd -= 1
                self.sale()
            else:
                self.table.setText('Конец продаж! \n  \nЗаработано за все дни: \n' + str(self.totalPapers))
                self.table.adjustSize()
                self.timeSale = False
                self.timeToEnd = 5

    def showDevPage2(self):
        self.cashToDev = 0
        if self.levelOfKnowledge > 0:
            if self.theme1.isChecked():
                self.theme = 1
            elif self.theme2.isChecked():
                self.theme = 2
            elif self.theme3.isChecked():
                self.theme = 3
            elif self.theme4.isChecked():
                self.theme = 4
            elif self.theme5.isChecked():
                self.theme = 5
            elif self.theme6.isChecked():
                self.theme = 6
            elif self.theme7.isChecked():
                self.theme = 7
            elif self.theme8.isChecked():
                self.theme = 8
            if self.style1.isChecked():
                self.style = 1
            elif self.style2.isChecked():
                self.style = 2
            elif self.style3.isChecked():
                self.style = 3
            elif self.style4.isChecked():
                self.style = 4
            elif self.style5.isChecked():
                self.style = 5
            elif self.style6.isChecked():
                self.style = 6
            elif self.style7.isChecked():
                self.style = 7
            elif self.style8.isChecked():
                self.style = 8
            elif self.type1.isChecked():
                self.type = 1
                self.cashToDev += 10
            elif self.type2.isChecked():
                self.type = 2
                self.cashToDev += 300
            elif self.type3.isChecked():
                self.type = 3
                self.cashToDev += 4000
            elif self.type4.isChecked():
                self.cashToDev += 40000
                self.type = 4
            if self.platform1.isChecked():
                self.platform = 1
                self.cashToDev += 10
            elif self.platform2.isChecked():
                self.platform = 2
                self.cashToDev += 400
            elif self.platform3.isChecked():
                self.platform = 3
                self.cashToDev += 10000
            elif self.platform4.isChecked():
                self.platform = 4
                self.cashToDev += 60000
            self.devPage1On = False
            self.totalMoney.setText('Итого: ' + str(self.cashToDev))
            self.totalMoney.adjustSize()
            self.devPage1.move(10000, 10000)
            self.levelOne.setEnabled(False)
            self.levelTwo.setEnabled(False)
            self.levelThree.setEnabled(False)
            self.levelFour.setEnabled(False)

            self.type4.setEnabled(False)
            if self.levelOfKnowledge >= 1:
                self.levelOne.setEnabled(True)
            if self.levelOfKnowledge >= 2:
                self.levelTwo.setEnabled(True)
            if self.levelOfKnowledge >= 3:
                self.levelThree.setEnabled(True)
            if self.levelOfKnowledge >= 4:
                self.levelFour.setEnabled(True)
            self.devPage2On = True
            self.devPage2.move(200, 100)

    def showDevPage3(self):
        self.totalTechno = 0
        if self.techno11.isChecked():
            self.totalTechno += 0.5
        if self.techno12.isChecked():
            self.totalTechno += 0.5
        if self.techno13.isChecked():
            self.totalTechno += 0.5
        if self.techno14.isChecked():
            self.totalTechno += 1
        if self.techno21.isChecked():
            self.totalTechno += 4
        if self.techno22.isChecked():
            self.totalTechno += 4
        if self.techno23.isChecked():
            self.totalTechno += 4
        if self.techno24.isChecked():
            self.totalTechno += 8
        if self.techno31.isChecked():
            self.totalTechno += 64
        if self.techno32.isChecked():
            self.totalTechno += 64
        if self.techno33.isChecked():
            self.totalTechno += 64
        if self.techno34.isChecked():
            self.totalTechno += 64
        if self.techno41.isChecked():
            self.totalTechno += 256
        if self.techno42.isChecked():
            self.totalTechno += 256
        if self.techno43.isChecked():
            self.totalTechno += 512
        if self.techno44.isChecked():
            self.totalTechno += 512
        if self.cash < self.totalMon:
            self.warning.setText('Недостаточно денег')
            self.warning.adjustSize()
        elif self.totalTechno == 0:
            self.warning.setText('Выберите хотя бы 1 технологию')
            self.warning.adjustSize()
        else:
            self.cash -= self.totalMon
            self.money.setText("Деньги: \n" + str(self.cash))
            self.startDev()

    def relise(self):
        self.table.setText('Релиз! \n  \nЗаработано за все дни: \n' + str(self.totalPapers))
        self.table.adjustSize()
        self.timeDev = False
        self.timeToEnd = 5
        self.timeSale = True

    def startDev(self):
        self.timeDev = True
        self.tick()
        self.timer.start()
        self.devPage2On = False
        self.devPage2.move(10000, 10000)
        self.table.setText('Дней до релиза: \n' + str(self.timeToEnd))
        self.table.adjustSize()

    def sale(self):
        myltiply1 = 10 + self.platform + self.type
        if self.style in self.perfect[str(self.theme)][0]:
            myltiply2 = 2
        elif self.style in self.perfect[str(self.theme)][1]:
            myltiply2 = 1
        else:
            myltiply2 = 0.5
        a = int(randint(self.totalTechno * 10, self.totalTechno * 20) * myltiply2 / 10 * myltiply1 + (self.fans * 10 + 1))
        if myltiply2 > 1:
            self.fans += a//10
        elif myltiply2 < 1:
            self.fans -= a//10
        self.totalPapers += a
        self.cash += a
        self.subs.setText('Фанаты: \n  ' + str(self.fans))
        self.money.setText('Деньги: \n   ' + str(self.cash))
        self.money.adjustSize()
        self.table.setText('Заработано сегодня: \n' + str(a) + '\nЗаработано за все дни: \n' + str(self.totalPapers))
        self.table.adjustSize()






if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

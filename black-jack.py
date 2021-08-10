import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Black Jack by Molodoy Python')
        self.setGeometry(500, 400, 1200, 800)
        # фон стола
        self.pixmap_table = QPixmap('tochnoonosamoe.jpg')
        self.table = QLabel(self)
        self.table.setPixmap(self.pixmap_table)
        self.table.resize(1200, 800)
        # кнопка старта
        self.start = QPushButton('GO', self)
        self.start.setGeometry(900, 635, 100, 100)
        self.start.setFont(QtGui.QFont("Arial", 30, QtGui.QFont.Bold))
        self.start.setStyleSheet('Background-Color:rgb(54,117,170);color:rgb(255,206,66);border-radius:50px')
        # кнопка стопа
        self.stop = QPushButton('STOP', self)
        self.stop.setGeometry(990, 580, 100, 100)
        self.stop.setFont(QtGui.QFont("Arial", 30, QtGui.QFont.Bold))
        self.stop.setStyleSheet('Background-Color:rgb(54,117,170);color:rgb(255,206,66);border-radius:50px')
        # кнопка добора
        self.add = QPushButton('ADD', self)
        self.add.setGeometry(800, 670, 100, 100)
        self.add.setFont(QtGui.QFont("Times", 30, QtGui.QFont.Bold))
        self.add.setStyleSheet('Background-Color:rgb(54,117,170);color:rgb(255,206,66);border-radius:50px')
        # кнопка новой игры
        self.restart = QPushButton('RES', self)
        self.restart.setGeometry(1075, 520, 100, 100)
        self.restart.setFont(QtGui.QFont("Arial", 30, QtGui.QFont.Bold))
        self.restart.setStyleSheet('Background-Color:rgb(54,117,170);color:rgb(255,206,66);border-radius:50px')
        # банк игрока
        self.player_bank = QLabel('100', self)
        self.player_bank.setMinimumSize(200, 50)
        self.player_bank.move(20, 50)
        self.player_bank.setStyleSheet('border:2px solid yellow;background-Color:rgb(54,117,170);color:rgb(255,206,66);'
                                       'font-size: 40pt;border-radius:20px')
        # надпись банк игрока
        self.bank = QLabel('BANK', self)
        self.bank.setMinimumSize(200, 50)
        self.bank.move(60, 5)
        self.bank.setStyleSheet('font-size:40pt;color:white')
        #  окно ставок
        self.bet_window = QLabel(self)
        self.bet_window.setMinimumSize(200, 100)
        self.bet_window.move(570, 690)
        self.bet_window.setStyleSheet('border:2px solid yellow;background-Color:rgb(54,117,170);color:rgb(255,206,66);'
                                      'font-size: 40pt;border-radius:50px')
        #  надпись ставка
        self.bet_ = QLabel('BET', self)
        self.bet_.setMinimumSize(70, 50)
        self.bet_.move(630, 645)
        self.bet_.setStyleSheet('font-size: 40pt;color:white')
        # окно карт игрока 1
        self.player_field = QLabel(self)
        self.player_field.setGeometry(100, 300, 200, 350)
        self.player_field.setStyleSheet('font-size:50pt')
        # окно карт игрока 2
        self.player_field2 = QLabel(self)
        self.player_field2.setGeometry(150, 300, 200, 350)
        self.player_field2.setStyleSheet('font-size:50pt')
        # окно карт игрока 3
        self.player_field3 = QLabel(self)
        self.player_field3.setGeometry(200, 300, 200, 350)
        self.player_field3.setStyleSheet('font-size:50pt')
        # окно карт игрока 4
        self.player_field4 = QLabel(self)
        self.player_field4.setGeometry(250, 300, 200, 350)
        self.player_field4.setStyleSheet('font-size:50pt')
        # окно карт игрока 5
        self.player_field5 = QLabel(self)
        self.player_field5.setGeometry(300, 300, 200, 350)
        self.player_field5.setStyleSheet('font-size:50pt')
        # окно карт игрока 6
        self.player_field6 = QLabel(self)
        self.player_field6.setGeometry(350, 300, 200, 350)
        self.player_field6.setStyleSheet('font-size:50pt')
        # сумма карт игрока
        self.sum_player = QLabel(self)
        self.sum_player.setGeometry(150, 250, 100, 50)
        self.sum_player.setStyleSheet('font-size:50pt;color:white;')
        # сумма карт дилера
        self.sum_dealer = QLabel(self)
        self.sum_dealer.setGeometry(630, 250, 100, 50)
        self.sum_dealer.setStyleSheet('font-size:50pt;color:white;')
        # окно диллера
        self.dealer_field = QLabel(self)
        self.dealer_field.setGeometry(600, 300, 200, 350)
        self.dealer_field.setStyleSheet('font-size:50pt')
        # окно диллера2
        self.dealer_field2 = QLabel(self)
        self.dealer_field2.setGeometry(650, 300, 200, 350)
        self.dealer_field2.setStyleSheet('font-size:50pt')
        # окно диллера3
        self.dealer_field3 = QLabel(self)
        self.dealer_field3.setGeometry(700, 300, 200, 350)
        self.dealer_field3.setStyleSheet('font-size:50pt')
        # окно диллера4
        self.dealer_field4 = QLabel(self)
        self.dealer_field4.setGeometry(750, 300, 200, 350)
        self.dealer_field4.setStyleSheet('font-size:50pt')
        # окно диллера5
        self.dealer_field5 = QLabel(self)
        self.dealer_field5.setGeometry(800, 300, 200, 350)
        self.dealer_field5.setStyleSheet('font-size:50pt')

        # фишка(5)
        self.chip_5 = QPushButton(self)
        self.chip_5.setIcon(QtGui.QIcon('chips/chip_5.png'))
        self.chip_5.setIconSize(QSize(100, 100))
        self.chip_5.setGeometry(20, 530, 110, 110)
        self.chip_5.setStyleSheet('border-radius:50px')

        # фишка(10)
        self.chip_10 = QPushButton(self)
        self.chip_10.setIcon(QtGui.QIcon('chips/chip_10.png'))
        self.chip_10.setIconSize(QSize(100, 100))
        self.chip_10.setGeometry(120, 600, 100, 100)
        self.chip_10.setStyleSheet('border-radius:50px')
        # фишка(20)
        self.chip_20 = QPushButton(self)
        self.chip_20.setIcon(QtGui.QIcon('chips/chip_20.png'))
        self.chip_20.setIconSize(QSize(100, 100))
        self.chip_20.setGeometry(220, 650, 100, 100)
        self.chip_20.setStyleSheet('border-radius:50px')
        # фишка(50)
        self.chip_50 = QPushButton(self)
        self.chip_50.setIcon(QtGui.QIcon('chips/chip_50.png'))
        self.chip_50.setIconSize(QSize(100, 100))
        self.chip_50.setGeometry(330, 680, 100, 100)
        self.chip_50.setStyleSheet('border-radius:50px')
        # фишка(100)
        self.chip_100 = QPushButton(self)
        self.chip_100.setIcon(QtGui.QIcon('chips/chip_100.png'))
        self.chip_100.setIconSize(QSize(100, 100))
        self.chip_100.setGeometry(440, 690, 100, 100)
        self.chip_100.setStyleSheet('border-radius:50px')

        # подключение кнопок
        self.chip_5.clicked.connect(self.stavka_five)
        self.chip_10.clicked.connect(self.stavka_ten)
        self.chip_20.clicked.connect(self.stavka_twenty)
        self.chip_50.clicked.connect(self.stavka_fifty)
        self.chip_100.clicked.connect(self.stavka_one_hundred)
        self.start.clicked.connect(self.start_game)
        self.stop.clicked.connect(self.dealer_move)
        self.stop.clicked.connect(self.stop_game)
        self.add.clicked.connect(self.add_move)
        self.add.clicked.connect(self.cards)
        self.start.clicked.connect(self.cards)
        self.restart.clicked.connect(self.new_game)
        self.stop.clicked.connect(self.cards2)

    player_bank_ = 100
    bet = 0
    player_cards = 0
    dealer_cards = 0
    dealer_spisok = []
    player_spisok = []


    def stavka_five(self):
        if self.player_bank.text() == 'lower bet' and self.player_bank_ < 5:
            self.bet += 0
        elif self.player_bank_ >= 5:
            self.bet += 5
            b = self.bet
            self.bet_window.setText(str(b))
        elif self.player_bank_ >= 5 and self.player_bank.text() == 'lower bet':
            self.bet += 5
            b = self.bet
            self.bet_window.setText(str(b))
        if self.player_bank_ == 0:
            b = self.player_bank_
            self.player_bank_ += 0
            self.player_bank.setText(str(b))
        elif self.player_bank_ < 5:
            self.player_bank.setText('lower bet')
        elif self.player_bank_ > 0:
            self.player_bank_ += -5
            a = self.player_bank_
            self.player_bank.setText(str(a))
        elif self.player_bank_ == 0:
            b = self.player_bank_
            self.player_bank_ += 0
            self.player_bank.setText(str(b))

    def stavka_ten(self):
        if self.player_bank.text() == 'lower bet' and self.player_bank_ < 10:
            self.bet += 0
        elif self.player_bank_ >= 10:
            self.bet += 10
            b = self.bet
            self.bet_window.setText(str(b))
        elif self.player_bank_ >= 10 and self.player_bank.text() == 'lower bet':
            self.bet += 10
            b = self.bet
            self.bet_window.setText(str(b))
        if self.player_bank_ == 0:
            b = self.player_bank_
            self.player_bank_ += 0
            self.player_bank.setText(str(b))
        elif self.player_bank_ < 10:
            self.player_bank.setText('lower bet')
        elif self.player_bank_ > 0:
            self.player_bank_ += -10
            a = self.player_bank_
            self.player_bank.setText(str(a))

    def stavka_twenty(self):

        if self.player_bank.text() == 'lower bet' and self.player_bank_ < 20:
            self.bet += 0
        elif self.player_bank_ >= 20:
            self.bet += 20
            b = self.bet
            self.bet_window.setText(str(b))
        elif self.player_bank_ >= 20 and self.player_bank.text() == 'lower bet':
            self.bet += 20
            b = self.bet
            self.bet_window.setText(str(b))
        if self.player_bank_ == 0:
            b = self.player_bank_
            self.player_bank_ += 0
            self.player_bank.setText(str(b))
        elif self.player_bank_ < 20:
            self.player_bank.setText('lower bet')
        elif self.player_bank_ > 0:
            self.player_bank_ += -20
            a = self.player_bank_
            self.player_bank.setText(str(a))

    def stavka_fifty(self):
        if self.player_bank.text() == 'lower bet' and self.player_bank_ < 50:
            self.bet += 0
        elif self.player_bank_ >= 50:
            self.bet += 50
            b = self.bet
            self.bet_window.setText(str(b))
        elif self.player_bank_ >= 50 and self.player_bank.text() == 'lower bet':
            self.bet += 50
            b = self.bet
            self.bet_window.setText(str(b))
        if self.player_bank_ == 0:
            b = self.player_bank_
            self.player_bank_ += 0
            self.player_bank.setText(str(b))
        elif self.player_bank_ < 50:
            self.player_bank.setText('lower bet')
        elif self.player_bank_ > 0:
            self.player_bank_ += -50
            a = self.player_bank_
            self.player_bank.setText(str(a))

    def stavka_one_hundred(self):
        if self.player_bank.text() == 'lower bet' and self.player_bank_ < 100:
            self.bet += 0
        elif self.player_bank_ >= 100:
            self.bet += 100
            b = self.bet
            self.bet_window.setText(str(b))
        elif self.player_bank_ >= 100 and self.player_bank.text() == 'lower bet':
            self.bet += 100
            b = self.bet
            self.bet_window.setText(str(b))
        if self.player_bank_ == 0:
            b = self.player_bank_
            self.player_bank_ += 0
            self.player_bank.setText(str(b))
        elif self.player_bank_ < 100:
            self.player_bank.setText('lower bet')
        elif self.player_bank_ > 0:
            self.player_bank_ += -100
            a = self.player_bank_
            self.player_bank.setText(str(a))

    def new_game(self):
        self.player_field.hide()
        self.player_field2.hide()
        self.player_field3.hide()
        self.player_field4.hide()
        self.player_field5.hide()
        self.player_field6.hide()
        self.dealer_field.hide()
        self.dealer_field2.hide()
        self.dealer_field3.hide()
        self.dealer_field4.hide()
        self.dealer_field5.hide()
        self.sum_player.setText('')
        self.sum_dealer.setText('')
        self.player_cards = 0
        self.dealer_cards = 0
        self.dealer_spisok = []
        self.player_spisok = []
        self.bet_window.setText('')
        self.bet = 0

    def start_game(self):
        a = random.randrange(1, 12)
        b = random.randrange(1, 12)
        if self.bet_window.text() == '':
            pass
        else:
            if self.player_cards > 0:
                pass
            else:
                self.player_field.show()
                self.player_field2.show()
                self.player_cards += a
                self.player_cards += b
                self.player_spisok.append(a)
                self.player_spisok.append(b)
                self.player_field.setText(str(a))
                self.player_field2.setText(str(b))
                self.sum_player.setText(str(self.player_cards))

    def stop_game(self):
        if self.player_cards == 0:
            pass
        elif 21 < self.player_cards:
            self.player_bank.setText(str(self.player_bank_))
            self.bet_window.setText('')
            self.bet = 0
        elif self.player_cards < self.dealer_cards > 21:
            self.player_bank_ += self.bet * 2
            self.bet_window.setText('')
            self.bet = 0
        elif 21 >= self.player_cards > self.dealer_cards:
            self.player_bank_ += self.bet * 2
            self.player_bank.setText(str(self.player_bank_))
            self.bet_window.setText('')
            self.bet = 0
        elif self.player_cards == self.dealer_cards:
            self.player_bank_ += self.bet
            self.bet_window.setText('')
            self.bet = 0
        else:
            self.player_bank.setText(str(self.player_bank_))
            self.bet_window.setText('')
            self.bet = 0

    def dealer_move(self):

        b = random.randrange(1, 12)
        c = random.randrange(1, 12)
        d = random.randrange(1, 12)
        e = random.randrange(1, 12)
        f = random.randrange(1, 12)
        if self.player_cards == 0:
            pass
        else:
            if len(self.dealer_spisok) == 0:
                self.dealer_field.show()
                self.dealer_field2.show()
                self.dealer_cards += b
                self.dealer_cards += c
                self.dealer_spisok.append(b)
                self.dealer_spisok.append(c)
                self.dealer_field.setText(str(b))
                self.dealer_field2.setText(str(c))
                self.sum_dealer.setText(str(self.dealer_cards))
                while self.dealer_cards <= 16:
                    if len(self.dealer_spisok) == 5:
                        pass
                    elif len(self.dealer_spisok) == 4:
                        self.player_field5.show()
                        self.dealer_cards += d
                        self.player_spisok.append(d)
                        self.dealer_field5.setText(str(d))
                        self.sum_dealer.setText(str(self.dealer_cards))
                    elif len(self.dealer_spisok) == 3:
                        self.player_field4.show()
                        self.dealer_cards += e
                        self.dealer_spisok.append(e)
                        self.dealer_field4.setText(str(e))
                        self.sum_dealer.setText(str(self.dealer_cards))
                    elif len(self.dealer_spisok) == 2:
                        self.dealer_field3.show()
                        self.dealer_cards += f
                        self.dealer_spisok.append(f)
                        self.dealer_field3.setText(str(f))
                        self.sum_dealer.setText(str(self.dealer_cards))

    def add_move(self):

        a = random.randrange(1, 12)
        if self.player_cards == 0:
            pass
        else:
            if len(self.player_spisok) == 6:
                pass
            elif len(self.player_spisok) == 5:
                self.player_cards += a
                self.player_spisok.append(a)
                self.player_field6.setText(str(a))
                self.sum_player.setText(str(self.player_cards))
                self.player_field6.show()

            elif len(self.player_spisok) == 4:
                self.player_cards += a
                self.player_spisok.append(a)
                self.player_field5.setText(str(a))
                self.sum_player.setText(str(self.player_cards))
                self.player_field5.show()

            elif len(self.player_spisok) == 3:
                self.player_cards += a
                self.player_spisok.append(a)
                self.player_field4.setText(str(a))
                self.sum_player.setText(str(self.player_cards))
                self.player_field4.show()

            elif self.player_field3.text() == '':
                self.player_field3.show()
                self.player_cards += a
                self.player_spisok.append(a)
                self.player_field3.setText(str(a))
                self.sum_player.setText(str(self.player_cards))

    # Карты игрока
    def cards(self):
        card2 = QPixmap('cards/2.png')
        card2.setDevicePixelRatio(3)
        card3 = QPixmap('cards/3.png')
        card3.setDevicePixelRatio(3)
        card4 = QPixmap('cards/4.png')
        card4.setDevicePixelRatio(3)
        card5 = QPixmap('cards/5.png')
        card5.setDevicePixelRatio(3)
        card6 = QPixmap('cards/6.png')
        card6.setDevicePixelRatio(3)
        card7 = QPixmap('cards/7.png')
        card7.setDevicePixelRatio(3)
        card8 = QPixmap('cards/8.png')
        card8.setDevicePixelRatio(3)
        card9 = QPixmap('cards/9.png')
        card9.setDevicePixelRatio(3)
        card10 = QPixmap('cards/10.png')
        card10.setDevicePixelRatio(3)
        cardA = QPixmap('cards/A.png')
        cardA.setDevicePixelRatio(3)
        if self.player_field.text() == '1':
            self.player_field.setPixmap(cardA)
            self.player_field.adjustSize()
        elif self.player_field2.text() == '1':
            self.player_field2.setPixmap(cardA)
            self.player_field2.adjustSize()
        elif self.player_field3.text() == '1':
            self.player_field3.setPixmap(cardA)
            self.player_field3.adjustSize()
        elif self.player_field4.text() == '1':
            self.player_field4.setPixmap(cardA)
            self.player_field4.adjustSize()
        elif self.player_field5.text() == '1':
            self.player_field5.setPixmap(cardA)
            self.player_field5.adjustSize()
        elif self.player_field6.text() == '1':
            self.player_field6.setPixmap(cardA)
            self.player_field6.adjustSize()
        if self.player_field.text() == '2':
            self.player_field.setPixmap(card2)
            self.player_field.adjustSize()
        elif self.player_field2.text() == '2':
            self.player_field2.setPixmap(card2)
            self.player_field2.adjustSize()
        elif self.player_field3.text() == '2':
            self.player_field3.setPixmap(cardA)
            self.player_field3.adjustSize()
        elif self.player_field4.text() == '2':
            self.player_field4.setPixmap(cardA)
            self.player_field4.adjustSize()
        elif self.player_field5.text() == '2':
            self.player_field5.setPixmap(cardA)
            self.player_field5.adjustSize()
        elif self.player_field6.text() == '2':
            self.player_field6.setPixmap(cardA)
            self.player_field6.adjustSize()
        if self.player_field.text() == '3':
            self.player_field.setPixmap(card3)
            self.player_field.adjustSize()
        elif self.player_field2.text() == '3':
            self.player_field2.setPixmap(card3)
            self.player_field2.adjustSize()
        elif self.player_field3.text() == '3':
            self.player_field3.setPixmap(card3)
            self.player_field3.adjustSize()
        elif self.player_field4.text() == '3':
            self.player_field4.setPixmap(card3)
            self.player_field4.adjustSize()
        elif self.player_field5.text() == '3':
            self.player_field5.setPixmap(card3)
            self.player_field5.adjustSize()
        elif self.player_field6.text() == '3':
            self.player_field6.setPixmap(card3)
            self.player_field6.adjustSize()
        if self.player_field.text() == '4':
            self.player_field.setPixmap(card4)
            self.player_field.adjustSize()
        elif self.player_field2.text() == '4':
            self.player_field2.setPixmap(card4)
            self.player_field2.adjustSize()
        elif self.player_field3.text() == '4':
            self.player_field3.setPixmap(card4)
            self.player_field3.adjustSize()
        elif self.player_field4.text() == '4':
            self.player_field4.setPixmap(card4)
            self.player_field4.adjustSize()
        elif self.player_field5.text() == '4':
            self.player_field5.setPixmap(card4)
            self.player_field5.adjustSize()
        elif self.player_field6.text() == '4':
            self.player_field6.setPixmap(card4)
            self.player_field6.adjustSize()
        if self.player_field.text() == '5':
            self.player_field.setPixmap(card5)
            self.player_field.adjustSize()
        elif self.player_field2.text() == '5':
            self.player_field2.setPixmap(card5)
            self.player_field2.adjustSize()
        elif self.player_field3.text() == '5':
            self.player_field3.setPixmap(card5)
            self.player_field3.adjustSize()
        elif self.player_field4.text() == '5':
            self.player_field4.setPixmap(card5)
            self.player_field4.adjustSize()
        elif self.player_field5.text() == '5':
            self.player_field5.setPixmap(card5)
            self.player_field5.adjustSize()
        elif self.player_field6.text() == '5':
            self.player_field6.setPixmap(card5)
            self.player_field6.adjustSize()
        if self.player_field.text() == '6':
            self.player_field.setPixmap(card6)
            self.player_field.adjustSize()
        elif self.player_field2.text() == '6':
            self.player_field2.setPixmap(card6)
            self.player_field2.adjustSize()
        elif self.player_field3.text() == '6':
            self.player_field3.setPixmap(card6)
            self.player_field3.adjustSize()
        elif self.player_field4.text() == '6':
            self.player_field4.setPixmap(card6)
            self.player_field4.adjustSize()
        elif self.player_field5.text() == '6':
            self.player_field5.setPixmap(card6)
            self.player_field5.adjustSize()
        elif self.player_field6.text() == '6':
            self.player_field6.setPixmap(card6)
            self.player_field6.adjustSize()
        if self.player_field.text() == '7':
            self.player_field.setPixmap(card7)
            self.player_field.adjustSize()
        elif self.player_field2.text() == '7':
            self.player_field2.setPixmap(card7)
            self.player_field2.adjustSize()
        elif self.player_field3.text() == '7':
            self.player_field3.setPixmap(card7)
            self.player_field3.adjustSize()
        elif self.player_field4.text() == '7':
            self.player_field4.setPixmap(card7)
            self.player_field4.adjustSize()
        elif self.player_field5.text() == '7':
            self.player_field5.setPixmap(card7)
            self.player_field5.adjustSize()
        elif self.player_field6.text() == '7':
            self.player_field6.setPixmap(card7)
            self.player_field6.adjustSize()
        if self.player_field.text() == '8':
            self.player_field.setPixmap(card8)
            self.player_field.adjustSize()
        elif self.player_field2.text() == '8':
            self.player_field2.setPixmap(card8)
            self.player_field2.adjustSize()
        elif self.player_field3.text() == '8':
            self.player_field3.setPixmap(card8)
            self.player_field3.adjustSize()
        elif self.player_field4.text() == '8':
            self.player_field4.setPixmap(card8)
            self.player_field4.adjustSize()
        elif self.player_field5.text() == '8':
            self.player_field5.setPixmap(card8)
            self.player_field5.adjustSize()
        elif self.player_field6.text() == '8':
            self.player_field6.setPixmap(card8)
            self.player_field6.adjustSize()
        if self.player_field.text() == '9':
            self.player_field.setPixmap(card9)
            self.player_field.adjustSize()
        elif self.player_field2.text() == '9':
            self.player_field2.setPixmap(card9)
            self.player_field2.adjustSize()
        elif self.player_field3.text() == '9':
            self.player_field3.setPixmap(card9)
            self.player_field3.adjustSize()
        elif self.player_field4.text() == '9':
            self.player_field4.setPixmap(card9)
            self.player_field4.adjustSize()
        elif self.player_field5.text() == '9':
            self.player_field5.setPixmap(card9)
            self.player_field5.adjustSize()
        elif self.player_field6.text() == '9':
            self.player_field6.setPixmap(card9)
            self.player_field6.adjustSize()
        if self.player_field.text() == '10':
            self.player_field.setPixmap(card10)
            self.player_field.adjustSize()
        elif self.player_field2.text() == '10':
            self.player_field2.setPixmap(card10)
            self.player_field2.adjustSize()
        elif self.player_field3.text() == '10':
            self.player_field3.setPixmap(card10)
            self.player_field3.adjustSize()
        elif self.player_field4.text() == '10':
            self.player_field4.setPixmap(card10)
            self.player_field4.adjustSize()
        elif self.player_field5.text() == '10':
            self.player_field5.setPixmap(card10)
            self.player_field5.adjustSize()
        elif self.player_field6.text() == '10':
            self.player_field6.setPixmap(card10)
            self.player_field6.adjustSize()
        if self.player_field.text() == '11':
            self.player_field.setPixmap(cardA)
            self.player_field.adjustSize()
        elif self.player_field2.text() == '11':
            self.player_field2.setPixmap(cardA)
            self.player_field2.adjustSize()
        elif self.player_field3.text() == '11':
            self.player_field3.setPixmap(cardA)
            self.player_field3.adjustSize()
        elif self.player_field4.text() == '11':
            self.player_field4.setPixmap(cardA)
            self.player_field4.adjustSize()
    # Карты дилера
    def cards2(self):
        card2 = QPixmap('cards/2.png')
        card2.setDevicePixelRatio(3)
        card3 = QPixmap('cards/3.png')
        card3.setDevicePixelRatio(3)
        card4 = QPixmap('cards/4.png')
        card4.setDevicePixelRatio(3)
        card5 = QPixmap('cards/5.png')
        card5.setDevicePixelRatio(3)
        card6 = QPixmap('cards/6.png')
        card6.setDevicePixelRatio(3)
        card7 = QPixmap('cards/7.png')
        card7.setDevicePixelRatio(3)
        card8 = QPixmap('cards/8.png')
        card8.setDevicePixelRatio(3)
        card9 = QPixmap('cards/9.png')
        card9.setDevicePixelRatio(3)
        card10 = QPixmap('cards/10.png')
        card10.setDevicePixelRatio(3)
        cardj = QPixmap('cards/J.png')
        cardj.setDevicePixelRatio(3)
        cardQ = QPixmap('cards/Q.png')
        cardQ.setDevicePixelRatio(3)
        cardK = QPixmap('cards/K.png')
        cardK.setDevicePixelRatio(3)
        cardA = QPixmap('cards/A.png')
        cardA.setDevicePixelRatio(3)
        if self.dealer_field.text() == '1':
            self.dealer_field.setPixmap(cardA)
            self.dealer_field.adjustSize()
        elif self.dealer_field2.text() == '1':
            self.dealer_field2.setPixmap(cardA)
            self.dealer_field2.adjustSize()
        elif self.dealer_field3.text() == '1':
            self.dealer_field3.setPixmap(cardA)
            self.dealer_field3.adjustSize()
        elif self.dealer_field4.text() == '1':
            self.dealer_field4.setPixmap(cardA)
            self.dealer_field4.adjustSize()
        elif self.dealer_field5.text() == '1':
            self.dealer_field5.setPixmap(cardA)
            self.dealer_field5.adjustSize()
        if self.dealer_field.text() == '2':
            self.dealer_field.setPixmap(card2)
            self.dealer_field.adjustSize()
        elif self.dealer_field2.text() == '2':
            self.dealer_field2.setPixmap(card2)
            self.dealer_field2.adjustSize()
        elif self.dealer_field3.text() == '2':
            self.dealer_field3.setPixmap(cardA)
            self.dealer_field3.adjustSize()
        elif self.dealer_field4.text() == '2':
            self.dealer_field4.setPixmap(cardA)
            self.dealer_field4.adjustSize()
        elif self.dealer_field5.text() == '2':
            self.dealer_field5.setPixmap(cardA)
            self.dealer_field5.adjustSize()
        if self.dealer_field.text() == '3':
            self.dealer_field.setPixmap(card3)
            self.dealer_field.adjustSize()
        elif self.dealer_field2.text() == '3':
            self.dealer_field2.setPixmap(card3)
            self.dealer_field2.adjustSize()
        elif self.dealer_field3.text() == '3':
            self.dealer_field3.setPixmap(card3)
            self.dealer_field3.adjustSize()
        elif self.dealer_field4.text() == '3':
            self.dealer_field4.setPixmap(card3)
            self.dealer_field4.adjustSize()
        elif self.dealer_field5.text() == '3':
            self.dealer_field5.setPixmap(card3)
            self.dealer_field5.adjustSize()
        if self.dealer_field.text() == '4':
            self.dealer_field.setPixmap(card4)
            self.dealer_field.adjustSize()
        elif self.dealer_field2.text() == '4':
            self.dealer_field2.setPixmap(card4)
            self.dealer_field2.adjustSize()
        elif self.dealer_field3.text() == '4':
            self.dealer_field3.setPixmap(card4)
            self.dealer_field3.adjustSize()
        elif self.dealer_field4.text() == '4':
            self.dealer_field4.setPixmap(card4)
            self.dealer_field4.adjustSize()
        elif self.dealer_field5.text() == '4':
            self.dealer_field5.setPixmap(card4)
            self.dealer_field5.adjustSize()
        if self.dealer_field.text() == '5':
            self.dealer_field.setPixmap(card5)
            self.dealer_field.adjustSize()
        elif self.dealer_field2.text() == '5':
            self.dealer_field2.setPixmap(card5)
            self.dealer_field2.adjustSize()
        elif self.dealer_field3.text() == '5':
            self.dealer_field3.setPixmap(card5)
            self.dealer_field3.adjustSize()
        elif self.dealer_field4.text() == '5':
            self.dealer_field4.setPixmap(card5)
            self.dealer_field4.adjustSize()
        elif self.dealer_field5.text() == '5':
            self.dealer_field5.setPixmap(card5)
            self.dealer_field5.adjustSize()
        if self.dealer_field.text() == '6':
            self.dealer_field.setPixmap(card6)
            self.dealer_field.adjustSize()
        elif self.dealer_field2.text() == '6':
            self.dealer_field2.setPixmap(card6)
            self.dealer_field2.adjustSize()
        elif self.dealer_field3.text() == '6':
            self.dealer_field3.setPixmap(card6)
            self.dealer_field3.adjustSize()
        elif self.dealer_field4.text() == '6':
            self.dealer_field4.setPixmap(card6)
            self.dealer_field4.adjustSize()
        elif self.dealer_field5.text() == '6':
            self.dealer_field5.setPixmap(card6)
            self.dealer_field5.adjustSize()
        if self.dealer_field.text() == '7':
            self.dealer_field.setPixmap(card7)
            self.dealer_field.adjustSize()
        elif self.dealer_field2.text() == '7':
            self.dealer_field2.setPixmap(card7)
            self.dealer_field2.adjustSize()
        elif self.dealer_field3.text() == '7':
            self.dealer_field3.setPixmap(card7)
            self.dealer_field3.adjustSize()
        elif self.dealer_field4.text() == '7':
            self.dealer_field4.setPixmap(card7)
            self.dealer_field4.adjustSize()
        elif self.dealer_field5.text() == '7':
            self.dealer_field5.setPixmap(card7)
            self.dealer_field5.adjustSize()
        if self.dealer_field.text() == '8':
            self.dealer_field.setPixmap(card8)
            self.dealer_field.adjustSize()
        elif self.dealer_field2.text() == '8':
            self.dealer_field2.setPixmap(card8)
            self.dealer_field2.adjustSize()
        elif self.dealer_field3.text() == '8':
            self.dealer_field3.setPixmap(card8)
            self.dealer_field3.adjustSize()
        elif self.dealer_field4.text() == '8':
            self.dealer_field4.setPixmap(card8)
            self.dealer_field4.adjustSize()
        elif self.dealer_field5.text() == '8':
            self.dealer_field5.setPixmap(card8)
            self.dealer_field5.adjustSize()
        if self.dealer_field.text() == '9':
            self.dealer_field.setPixmap(card9)
            self.dealer_field.adjustSize()
        elif self.dealer_field2.text() == '9':
            self.dealer_field2.setPixmap(card9)
            self.dealer_field2.adjustSize()
        elif self.dealer_field3.text() == '9':
            self.dealer_field3.setPixmap(card9)
            self.dealer_field3.adjustSize()
        elif self.dealer_field4.text() == '9':
            self.dealer_field4.setPixmap(card9)
            self.dealer_field4.adjustSize()
        elif self.dealer_field5.text() == '9':
            self.dealer_field5.setPixmap(card9)
            self.dealer_field5.adjustSize()
        if self.dealer_field.text() == '10':
            self.dealer_field.setPixmap(card10)
            self.dealer_field.adjustSize()
        elif self.dealer_field2.text() == '10':
            self.dealer_field2.setPixmap(card10)
            self.dealer_field2.adjustSize()
        elif self.dealer_field3.text() == '10':
            self.dealer_field3.setPixmap(card10)
            self.dealer_field3.adjustSize()
        elif self.dealer_field4.text() == '10':
            self.dealer_field4.setPixmap(card10)
            self.dealer_field4.adjustSize()
        elif self.dealer_field5.text() == '10':
            self.dealer_field5.setPixmap(card10)
            self.dealer_field5.adjustSize()
        if self.dealer_field.text() == '11':
            self.dealer_field.setPixmap(cardA)
            self.dealer_field.adjustSize()
        elif self.dealer_field2.text() == '11':
            self.dealer_field2.setPixmap(cardA)
            self.dealer_field2.adjustSize()
        elif self.dealer_field3.text() == '11':
            self.dealer_field3.setPixmap(cardA)
            self.dealer_field3.adjustSize()
        elif self.dealer_field4.text() == '11':
            self.dealer_field4.setPixmap(cardA)
            self.dealer_field4.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())

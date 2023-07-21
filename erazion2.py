import sys
import threading
from threading import Thread
import traceback
from threading import Timer
import os
import win10toast
import tkinter as tk
from time import sleep
from tkinter import ttk
import time
import ErazionResourse
from PyQt5 import QtCore, QtGui, QtWidgets


Ugodie = {
    1: '[55] Проклятое Угодье страданий',
    2: '29',
    3: '§7после свержения существа §c[55] Проклятое Угодье страданий §7выбивает предмет'
}

Boel = {
    1: '[76] Проклятый Боей"ль',
    2: '21',
    3: '§7после свержения существа §c[76] Проклятый Боей"ль §7выбивает предмет'
}

Skelet = {
    1: '[73] Проклятый король скелетов',
    2: '33',
    3: '§7после свержения существа §c[73] Проклятый король скелетов §7выбивает предмет'
}

Leviaf = {
    1: '[75] Левиаффтониарий',
    2: '151',
    3: '§7после свержения существа §c[75] Левиаффтониарий §7выбивает предмет'
}

Sunduk = {
    1: '[70] Проклятый сундук',
    2: '153',
    3: '§7после свержения существа §c[70] Проклятый сундук §7выбивает предмет'
}

Demon = {
    1: '[95] Демон мирового отчуждения',
    2: '175',
    3: '§7после свержения существа §c[95] Демон мирового отчуждения §7выбивает предмет'
}

Magistr = {
    1: '[68] Безумный магистр',
    2: '80',
    3: '§7после свержения существа §c[68] Безумный магистр §7выбивает предмет'
}

Keca = {
    1: '[70] Кецалькоатль',
    2: '96',
    3: '§7после свержения существа §c[70] Кецалькоатль §7выбивает предмет'
}

Spider = {
    1: '[85] Мачеха Тарантулов',
    2: '53',
    3: '§7после свержения существа §c[85] Мачеха Тарантулов §7выбивает предмет'
}

Shadow = {
    1: '[60] Пустая тень',
    2: '28',
    3: '§7после свержения существа §c[60] Пустая тень §7выбивает предмет'
}

Vladika = {
    1: '[65] Владыка светлого мира',
    2: '28',
    3: '§7после свержения существа §c[65] Владыка светлого мира §7выбивает предмет'
}

Zeya = {
    1: '[72] Богиня Зея',
    2: '60',
    3: '§7после свержения существа §c[72] Богиня Зея §7выбивает предмет'
}

Afina = {
    1: '[72] Богиня Афина',
    2: '60',
    3: '§7после свержения существа §c[72] Богиня Афина §7выбивает предмет'
}

Zeus = {
    1: '[90] Всемогущий Бог грома, молний ЗЕВС',
    2: '180',
    3: '§7после свержения существа §c[90] Всемогущий Бог грома, молний ЗЕВС §7выбивает предмет'
}

Night = {
    1: '[52] Повелитель ночи',
    2: '20',
    3: '§7после свержения существа §c[52] Повелитель ночи §7выбивает предмет'
}

Poison = {
    1: '[54] Ядовитая Мантикора',
    2: '20',
    3: '§7после свержения существа §c[54] Ядовитая Мантикора §7выбивает предмет'
}

Djon = {
    1: '[58] Могущественный берсерк - Джон',
    2: '30',
    3: '§7после свержения существа §c[58] Могущественный берсерк - Джон §7выбивает предмет'
}

Aid = {
    1: '[75] Аид',
    2: '60',
    3: '§7после свержения существа §c[75] Аид  §7выбивает предмет'
}

Jesus = {
    1: '[51] Иисус, cын божий',
    2: '36',
    3: '§7после свержения существа §c[51] Иисус, cын божий §7выбивает предмет'
}

Arkus = {
    1: '[44] Аркус',
    2: '25',
    3: '§7после свержения существа §c[44] Аркус §7выбивает предмет'
}

Satana = {
    1: '[58] Могущественный берсерк - Джон',
    2: '21',
    3: '§7после свержения существа §c[58] Могущественный берсерк - Джон §7выбивает предмет'
}

Archangel = {
    1: '[27] Архангел',
    2: '19',
    3: '§7после свержения существа §c[27] Архангел §7выбивает предмет'
}

King = {
    1: '[31] Король рая',
    2: '15',
    3: '§7после свержения существа §c[31] Король рая §7выбивает предмет'
}

Zevs = {
    1: '[16] Зевс',
    2: '5',
    3: '§7Вы убили §c[16] Зевс §7для задания "Телепорт в Олимп"'
}

Guardian = {
    1: '[29] Хранитель воздуха',
    2: '18',
    3: '§7Вы убили §c[29] Хранитель воздуха §7для задания "Телепорт в Олимп"'
}


class MyGlobalsVars():
    aUgodie = int(Ugodie[2]) * 60
    aBoel = int(Boel[2]) * 60
    aSkelet = int(Skelet[2]) * 60
    aLeviaf = int(Leviaf[2]) * 60
    aSunduk = int(Sunduk[2]) * 60
    aDemon = int(Demon[2]) * 60
    aMagistr = int(Magistr[2]) * 60
    aKeca = int(Keca[2]) * 60
    aSpider = int(Spider[2]) * 60
    aShadow = int(Shadow[2]) * 60
    aVladika = int(Vladika[2]) * 60
    aZeya = int(Zeya[2]) * 60
    aAfina = int(Afina[2]) * 60
    aZeus = int(Zeus[2]) * 60
    aNight = int(Night[2]) * 60
    aPoison = int(Poison[2]) * 60
    aDjon = int(Djon[2]) * 60
    aAid = int(Aid[2]) * 60
    aJesus = int(Jesus[2]) * 60
    aArkus = int(Arkus[2]) * 60
    aSatana = int(Satana[2]) * 60
    aArchangel = int(Archangel[2]) * 60
    aKing = int(King[2]) * 60
    aZevs = int(Zevs[2]) * 60
    aGuardian = int(Guardian[2]) * 60


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(800, 800)
        MainWindow.setMaximumSize(800, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/123/newchest41.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UgodieBar = QtWidgets.QSlider(self.centralwidget)
        self.UgodieBar.setGeometry(QtCore.QRect(200, 50, 121, 16))
        self.UgodieBar.setMinimum(1)
        self.UgodieBar.setMaximum(29)
        self.UgodieBar.setOrientation(QtCore.Qt.Horizontal)
        self.UgodieBar.setObjectName("UgodieBar")
        self.UgodieBar.setValue(int(Ugodie[2]))
        self.UgodieBar.valueChanged.connect(self.updateLabelUgodie)
        self.UgodieStart = QtWidgets.QPushButton(self.centralwidget)
        self.UgodieStart.setGeometry(QtCore.QRect(10, 40, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.UgodieStart.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/123/ruby254_helm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UgodieStart.setIcon(icon1)
        self.UgodieStart.setIconSize(QtCore.QSize(32, 32))
        self.UgodieStart.setObjectName("UgodieStart")
        self.UgodieStop = QtWidgets.QPushButton(self.centralwidget)
        self.UgodieStop.setGeometry(QtCore.QRect(330, 40, 61, 41))
        self.UgodieStop.setObjectName("UgodieStop")
        self.UgodieLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.UgodieLabelTimer.setGeometry(QtCore.QRect(200, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.UgodieLabelTimer.setFont(font)
        self.UgodieLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.UgodieLabelTimer.setText("")
        self.UgodieLabelTimer.setObjectName("UgodieLabelTimer")
        self.BoelStart = QtWidgets.QPushButton(self.centralwidget)
        self.BoelStart.setGeometry(QtCore.QRect(10, 90, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BoelStart.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/123/new8_helm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BoelStart.setIcon(icon2)
        self.BoelStart.setIconSize(QtCore.QSize(32, 32))
        self.BoelStart.setObjectName("BoelStart")
        self.BoelStop = QtWidgets.QPushButton(self.centralwidget)
        self.BoelStop.setGeometry(QtCore.QRect(330, 90, 61, 41))
        self.BoelStop.setObjectName("BoelStop")
        self.BoelLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.BoelLabelTimer.setGeometry(QtCore.QRect(200, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.BoelLabelTimer.setFont(font)
        self.BoelLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.BoelLabelTimer.setText("")
        self.BoelLabelTimer.setObjectName("BoelLabelTimer")
        self.BoelBar = QtWidgets.QSlider(self.centralwidget)
        self.BoelBar.setGeometry(QtCore.QRect(200, 100, 121, 16))
        self.BoelBar.setMinimum(1)
        self.BoelBar.setMaximum(21)
        self.BoelBar.setOrientation(QtCore.Qt.Horizontal)
        self.BoelBar.setObjectName("BoelBar")
        self.BoelBar.setValue(int(Boel[2]))
        self.BoelBar.valueChanged.connect(self.updateLabelBoel)
        self.SkeletBar = QtWidgets.QSlider(self.centralwidget)
        self.SkeletBar.setGeometry(QtCore.QRect(200, 150, 121, 16))
        self.SkeletBar.setMinimum(1)
        self.SkeletBar.setMaximum(33)
        self.SkeletBar.setOrientation(QtCore.Qt.Horizontal)
        self.SkeletBar.setObjectName("SkeletBar")
        self.SkeletBar.setValue(int(Skelet[2]))
        self.SkeletBar.valueChanged.connect(self.updateLabelSkelet)
        self.SkeletStart = QtWidgets.QPushButton(self.centralwidget)
        self.SkeletStart.setGeometry(QtCore.QRect(10, 140, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SkeletStart.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/123/newhelm37.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SkeletStart.setIcon(icon3)
        self.SkeletStart.setIconSize(QtCore.QSize(32, 32))
        self.SkeletStart.setObjectName("SkeletStart")
        self.SkeletStop = QtWidgets.QPushButton(self.centralwidget)
        self.SkeletStop.setGeometry(QtCore.QRect(330, 140, 61, 41))
        self.SkeletStop.setObjectName("SkeletStop")
        self.SkeletLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.SkeletLabelTimer.setGeometry(QtCore.QRect(200, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.SkeletLabelTimer.setFont(font)
        self.SkeletLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.SkeletLabelTimer.setText("")
        self.SkeletLabelTimer.setObjectName("SkeletLabelTimer")
        self.LeviafBar = QtWidgets.QSlider(self.centralwidget)
        self.LeviafBar.setGeometry(QtCore.QRect(200, 200, 121, 16))
        self.LeviafBar.setMinimum(1)
        self.LeviafBar.setMaximum(151)
        self.LeviafBar.setOrientation(QtCore.Qt.Horizontal)
        self.LeviafBar.setObjectName("LeviafBar")
        self.LeviafBar.setValue(int(Leviaf[2]))
        self.LeviafBar.valueChanged.connect(self.updateLabelLeviaf)
        self.LeviafStart = QtWidgets.QPushButton(self.centralwidget)
        self.LeviafStart.setGeometry(QtCore.QRect(10, 190, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LeviafStart.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/123/newboots36.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LeviafStart.setIcon(icon4)
        self.LeviafStart.setIconSize(QtCore.QSize(32, 32))
        self.LeviafStart.setObjectName("LeviafStart")
        self.LeviafStop = QtWidgets.QPushButton(self.centralwidget)
        self.LeviafStop.setGeometry(QtCore.QRect(330, 190, 61, 41))
        self.LeviafStop.setObjectName("LeviafStop")
        self.LeviafLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.LeviafLabelTimer.setGeometry(QtCore.QRect(200, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.LeviafLabelTimer.setFont(font)
        self.LeviafLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.LeviafLabelTimer.setText("")
        self.LeviafLabelTimer.setObjectName("LeviafLabelTimer")
        self.SundukBar = QtWidgets.QSlider(self.centralwidget)
        self.SundukBar.setGeometry(QtCore.QRect(200, 250, 121, 16))
        self.SundukBar.setMinimum(1)
        self.SundukBar.setMaximum(153)
        self.SundukBar.setOrientation(QtCore.Qt.Horizontal)
        self.SundukBar.setObjectName("SundukBar")
        self.SundukBar.setValue(int(Sunduk[2]))
        self.SundukBar.valueChanged.connect(self.updateLabelSunduk)
        self.SundukStart = QtWidgets.QPushButton(self.centralwidget)
        self.SundukStart.setGeometry(QtCore.QRect(10, 240, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.SundukStart.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/123/zcnitem45.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SundukStart.setIcon(icon5)
        self.SundukStart.setIconSize(QtCore.QSize(32, 32))
        self.SundukStart.setObjectName("SundukStart")
        self.SundukStop = QtWidgets.QPushButton(self.centralwidget)
        self.SundukStop.setGeometry(QtCore.QRect(330, 240, 61, 41))
        self.SundukStop.setObjectName("SundukStop")
        self.SundukLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.SundukLabelTimer.setGeometry(QtCore.QRect(200, 240, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.SundukLabelTimer.setFont(font)
        self.SundukLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.SundukLabelTimer.setText("")
        self.SundukLabelTimer.setObjectName("SundukLabelTimer")
        self.DemonBar = QtWidgets.QSlider(self.centralwidget)
        self.DemonBar.setGeometry(QtCore.QRect(200, 300, 121, 16))
        self.DemonBar.setMinimum(1)
        self.DemonBar.setMaximum(175)
        self.DemonBar.setOrientation(QtCore.Qt.Horizontal)
        self.DemonBar.setObjectName("DemonBar")
        self.DemonBar.setValue(int(Demon[2]))
        self.DemonBar.valueChanged.connect(self.updateLabelDemon)
        self.DemonStart = QtWidgets.QPushButton(self.centralwidget)
        self.DemonStart.setGeometry(QtCore.QRect(10, 290, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.DemonStart.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/123/hitem12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DemonStart.setIcon(icon6)
        self.DemonStart.setIconSize(QtCore.QSize(32, 32))
        self.DemonStart.setObjectName("DemonStart")
        self.DemonStop = QtWidgets.QPushButton(self.centralwidget)
        self.DemonStop.setGeometry(QtCore.QRect(330, 290, 61, 41))
        self.DemonStop.setObjectName("DemonStop")
        self.DemonLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.DemonLabelTimer.setGeometry(QtCore.QRect(200, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.DemonLabelTimer.setFont(font)
        self.DemonLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.DemonLabelTimer.setText("")
        self.DemonLabelTimer.setObjectName("DemonLabelTimer")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 0, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(211, 29, 13);")
        self.label_7.setObjectName("label_7")
        self.KecaBar = QtWidgets.QSlider(self.centralwidget)
        self.KecaBar.setGeometry(QtCore.QRect(600, 100, 121, 16))
        self.KecaBar.setMinimum(1)
        self.KecaBar.setMaximum(96)
        self.KecaBar.setOrientation(QtCore.Qt.Horizontal)
        self.KecaBar.setObjectName("KecaBar")
        self.KecaBar.setValue(int(Keca[2]))
        self.KecaBar.valueChanged.connect(self.updateLabelKeca)
        self.MagistrBar = QtWidgets.QSlider(self.centralwidget)
        self.MagistrBar.setGeometry(QtCore.QRect(600, 50, 121, 16))
        self.MagistrBar.setMinimum(1)
        self.MagistrBar.setMaximum(80)
        self.MagistrBar.setOrientation(QtCore.Qt.Horizontal)
        self.MagistrBar.setObjectName("MagistrBar")
        self.MagistrBar.setValue(int(Magistr[2]))
        self.MagistrBar.valueChanged.connect(self.updateLabelMagistr)
        self.KecaStop = QtWidgets.QPushButton(self.centralwidget)
        self.KecaStop.setGeometry(QtCore.QRect(730, 90, 61, 41))
        self.KecaStop.setObjectName("KecaStop")
        self.SpiderStop = QtWidgets.QPushButton(self.centralwidget)
        self.SpiderStop.setGeometry(QtCore.QRect(730, 140, 61, 41))
        self.SpiderStop.setObjectName("SpiderStop")
        self.KecaLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.KecaLabelTimer.setGeometry(QtCore.QRect(600, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.KecaLabelTimer.setFont(font)
        self.KecaLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.KecaLabelTimer.setText("")
        self.KecaLabelTimer.setObjectName("KecaLabelTimer")
        self.SpiderStart = QtWidgets.QPushButton(self.centralwidget)
        self.SpiderStart.setGeometry(QtCore.QRect(410, 140, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.SpiderStart.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/123/romog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SpiderStart.setIcon(icon7)
        self.SpiderStart.setIconSize(QtCore.QSize(32, 32))
        self.SpiderStart.setObjectName("SpiderStart")
        self.MagistrLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.MagistrLabelTimer.setGeometry(QtCore.QRect(600, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.MagistrLabelTimer.setFont(font)
        self.MagistrLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.MagistrLabelTimer.setText("")
        self.MagistrLabelTimer.setObjectName("MagistrLabelTimer")
        self.MagistrStop = QtWidgets.QPushButton(self.centralwidget)
        self.MagistrStop.setGeometry(QtCore.QRect(730, 40, 61, 41))
        self.MagistrStop.setObjectName("MagistrStop")
        self.KecaStart = QtWidgets.QPushButton(self.centralwidget)
        self.KecaStart.setGeometry(QtCore.QRect(410, 90, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.KecaStart.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/123/newboots17.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KecaStart.setIcon(icon8)
        self.KecaStart.setIconSize(QtCore.QSize(32, 32))
        self.KecaStart.setObjectName("KecaStart")
        self.MagistrStart = QtWidgets.QPushButton(self.centralwidget)
        self.MagistrStart.setGeometry(QtCore.QRect(410, 40, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.MagistrStart.setFont(font)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/123/ruby257_chest.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MagistrStart.setIcon(icon9)
        self.MagistrStart.setIconSize(QtCore.QSize(32, 32))
        self.MagistrStart.setObjectName("MagistrStart")
        self.SpiderBar = QtWidgets.QSlider(self.centralwidget)
        self.SpiderBar.setGeometry(QtCore.QRect(600, 150, 121, 16))
        self.SpiderBar.setMinimum(1)
        self.SpiderBar.setMaximum(53)
        self.SpiderBar.setOrientation(QtCore.Qt.Horizontal)
        self.SpiderBar.setObjectName("SpiderBar")
        self.SpiderBar.setValue(int(Spider[2]))
        self.SpiderBar.valueChanged.connect(self.updateLabelSpider)
        self.SpiderLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.SpiderLabelTimer.setGeometry(QtCore.QRect(600, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.SpiderLabelTimer.setFont(font)
        self.SpiderLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.SpiderLabelTimer.setText("")
        self.SpiderLabelTimer.setObjectName("SpiderLabelTimer")
        self.UgodieLabel = QtWidgets.QLabel(self.centralwidget)
        self.UgodieLabel.setGeometry(QtCore.QRect(200, 30, 121, 16))
        self.UgodieLabel.setObjectName("UgodieLabel")
        self.BoelLabel = QtWidgets.QLabel(self.centralwidget)
        self.BoelLabel.setGeometry(QtCore.QRect(200, 80, 121, 16))
        self.BoelLabel.setObjectName("BoelLabel")
        self.SkeletLabel = QtWidgets.QLabel(self.centralwidget)
        self.SkeletLabel.setGeometry(QtCore.QRect(200, 130, 121, 16))
        self.SkeletLabel.setObjectName("SkeletLabel")
        self.LeviafLabel = QtWidgets.QLabel(self.centralwidget)
        self.LeviafLabel.setGeometry(QtCore.QRect(200, 180, 121, 16))
        self.LeviafLabel.setObjectName("LeviafLabel")
        self.SundukLabel = QtWidgets.QLabel(self.centralwidget)
        self.SundukLabel.setGeometry(QtCore.QRect(200, 230, 121, 16))
        self.SundukLabel.setObjectName("SundukLabel")
        self.DemonLabel = QtWidgets.QLabel(self.centralwidget)
        self.DemonLabel.setGeometry(QtCore.QRect(200, 280, 121, 16))
        self.DemonLabel.setObjectName("DemonLabel")
        self.MagistrLabel = QtWidgets.QLabel(self.centralwidget)
        self.MagistrLabel.setGeometry(QtCore.QRect(600, 30, 121, 16))
        self.MagistrLabel.setObjectName("MagistrLabel")
        self.KecaLabel = QtWidgets.QLabel(self.centralwidget)
        self.KecaLabel.setGeometry(QtCore.QRect(600, 80, 121, 16))
        self.KecaLabel.setObjectName("KecaLabel")
        self.SpiderLabel = QtWidgets.QLabel(self.centralwidget)
        self.SpiderLabel.setGeometry(QtCore.QRect(600, 130, 121, 16))
        self.SpiderLabel.setObjectName("SpiderLabel")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(580, 0, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_20.setObjectName("label_20")
        self.VladikaStart = QtWidgets.QPushButton(self.centralwidget)
        self.VladikaStart.setGeometry(QtCore.QRect(410, 290, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.VladikaStart.setFont(font)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/123/ruby174_chest.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.VladikaStart.setIcon(icon10)
        self.VladikaStart.setIconSize(QtCore.QSize(32, 32))
        self.VladikaStart.setObjectName("VladikaStart")
        self.VladikaLabel = QtWidgets.QLabel(self.centralwidget)
        self.VladikaLabel.setGeometry(QtCore.QRect(600, 280, 121, 16))
        self.VladikaLabel.setObjectName("VladikaLabel")
        self.VladikaStop = QtWidgets.QPushButton(self.centralwidget)
        self.VladikaStop.setGeometry(QtCore.QRect(730, 290, 61, 41))
        self.VladikaStop.setObjectName("VladikaStop")
        self.VladikaBar = QtWidgets.QSlider(self.centralwidget)
        self.VladikaBar.setGeometry(QtCore.QRect(600, 300, 121, 16))
        self.VladikaBar.setMinimum(1)
        self.VladikaBar.setMaximum(28)
        self.VladikaBar.setOrientation(QtCore.Qt.Horizontal)
        self.VladikaBar.setObjectName("VladikaBar")
        self.VladikaBar.setValue(int(Vladika[2]))
        self.VladikaBar.valueChanged.connect(self.updateLabelVladika)
        self.VladikaLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.VladikaLabelTimer.setGeometry(QtCore.QRect(600, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.VladikaLabelTimer.setFont(font)
        self.VladikaLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.VladikaLabelTimer.setText("")
        self.VladikaLabelTimer.setObjectName("VladikaLabelTimer")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(580, 200, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_23.setObjectName("label_23")
        self.ShadowStart = QtWidgets.QPushButton(self.centralwidget)
        self.ShadowStart.setGeometry(QtCore.QRect(410, 240, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ShadowStart.setFont(font)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/123/Ruby172_Chest.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ShadowStart.setIcon(icon11)
        self.ShadowStart.setIconSize(QtCore.QSize(32, 32))
        self.ShadowStart.setObjectName("ShadowStart")
        self.ShadowLabel = QtWidgets.QLabel(self.centralwidget)
        self.ShadowLabel.setGeometry(QtCore.QRect(600, 230, 121, 16))
        self.ShadowLabel.setObjectName("ShadowLabel")
        self.ShadowStop = QtWidgets.QPushButton(self.centralwidget)
        self.ShadowStop.setGeometry(QtCore.QRect(730, 240, 61, 41))
        self.ShadowStop.setObjectName("ShadowStop")
        self.ShadowLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.ShadowLabelTimer.setGeometry(QtCore.QRect(600, 240, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.ShadowLabelTimer.setFont(font)
        self.ShadowLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.ShadowLabelTimer.setText("")
        self.ShadowLabelTimer.setObjectName("ShadowLabelTimer")
        self.ShadowBar = QtWidgets.QSlider(self.centralwidget)
        self.ShadowBar.setGeometry(QtCore.QRect(600, 250, 121, 16))
        self.ShadowBar.setMinimum(1)
        self.ShadowBar.setMaximum(28)
        self.ShadowBar.setOrientation(QtCore.Qt.Horizontal)
        self.ShadowBar.setObjectName("ShadowBar")
        self.ShadowBar.setValue(int(Shadow[2]))
        self.ShadowBar.valueChanged.connect(self.updateLabelShadow)
        self.AfinaBar = QtWidgets.QSlider(self.centralwidget)
        self.AfinaBar.setGeometry(QtCore.QRect(200, 440, 121, 16))
        self.AfinaBar.setMinimum(1)
        self.AfinaBar.setMaximum(60)
        self.AfinaBar.setOrientation(QtCore.Qt.Horizontal)
        self.AfinaBar.setObjectName("AfinaBar")
        self.AfinaBar.setValue(int(Afina[2]))
        self.AfinaBar.valueChanged.connect(self.updateLabelAfina)
        self.ZeyaBar = QtWidgets.QSlider(self.centralwidget)
        self.ZeyaBar.setGeometry(QtCore.QRect(200, 390, 121, 16))
        self.ZeyaBar.setMinimum(1)
        self.ZeyaBar.setMaximum(60)
        self.ZeyaBar.setOrientation(QtCore.Qt.Horizontal)
        self.ZeyaBar.setObjectName("ZeyaBar")
        self.ZeyaBar.setValue(int(Zeya[2]))
        self.ZeyaBar.valueChanged.connect(self.updateLabelZeya)
        self.ZeyaLabel = QtWidgets.QLabel(self.centralwidget)
        self.ZeyaLabel.setGeometry(QtCore.QRect(200, 370, 121, 16))
        self.ZeyaLabel.setObjectName("ZeyaLabel")
        self.AfinaStop = QtWidgets.QPushButton(self.centralwidget)
        self.AfinaStop.setGeometry(QtCore.QRect(330, 430, 61, 41))
        self.AfinaStop.setObjectName("AfinaStop")
        self.ZeusStop = QtWidgets.QPushButton(self.centralwidget)
        self.ZeusStop.setGeometry(QtCore.QRect(330, 480, 61, 41))
        self.ZeusStop.setObjectName("ZeusStop")
        self.AfinaLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.AfinaLabelTimer.setGeometry(QtCore.QRect(200, 430, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.AfinaLabelTimer.setFont(font)
        self.AfinaLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.AfinaLabelTimer.setText("")
        self.AfinaLabelTimer.setObjectName("AfinaLabelTimer")
        self.ZeusStart = QtWidgets.QPushButton(self.centralwidget)
        self.ZeusStart.setGeometry(QtCore.QRect(10, 480, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ZeusStart.setFont(font)
        self.ZeusStart.setIcon(icon)
        self.ZeusStart.setIconSize(QtCore.QSize(32, 32))
        self.ZeusStart.setObjectName("ZeusStart")
        self.ZeyaLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.ZeyaLabelTimer.setGeometry(QtCore.QRect(200, 380, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.ZeyaLabelTimer.setFont(font)
        self.ZeyaLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.ZeyaLabelTimer.setText("")
        self.ZeyaLabelTimer.setObjectName("ZeyaLabelTimer")
        self.ZeyaStop = QtWidgets.QPushButton(self.centralwidget)
        self.ZeyaStop.setGeometry(QtCore.QRect(330, 380, 61, 41))
        self.ZeyaStop.setObjectName("ZeyaStop")
        self.AfinaStart = QtWidgets.QPushButton(self.centralwidget)
        self.AfinaStart.setGeometry(QtCore.QRect(10, 430, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.AfinaStart.setFont(font)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/123/ruby101_chest.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AfinaStart.setIcon(icon12)
        self.AfinaStart.setIconSize(QtCore.QSize(32, 32))
        self.AfinaStart.setObjectName("AfinaStart")
        self.ZeyaStart = QtWidgets.QPushButton(self.centralwidget)
        self.ZeyaStart.setGeometry(QtCore.QRect(10, 380, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ZeyaStart.setFont(font)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/123/ruby101_leggins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ZeyaStart.setIcon(icon13)
        self.ZeyaStart.setIconSize(QtCore.QSize(32, 32))
        self.ZeyaStart.setObjectName("ZeyaStart")
        self.ZeusLabel = QtWidgets.QLabel(self.centralwidget)
        self.ZeusLabel.setGeometry(QtCore.QRect(200, 470, 121, 16))
        self.ZeusLabel.setObjectName("ZeusLabel")
        self.ZeusBar = QtWidgets.QSlider(self.centralwidget)
        self.ZeusBar.setGeometry(QtCore.QRect(200, 490, 121, 16))
        self.ZeusBar.setMinimum(1)
        self.ZeusBar.setMaximum(180)
        self.ZeusBar.setOrientation(QtCore.Qt.Horizontal)
        self.ZeusBar.setObjectName("ZeusBar")
        self.ZeusBar.setValue(int(Zeus[2]))
        self.ZeusBar.valueChanged.connect(self.updateLabelZeus)
        self.AfinaLabel = QtWidgets.QLabel(self.centralwidget)
        self.AfinaLabel.setGeometry(QtCore.QRect(200, 420, 121, 16))
        self.AfinaLabel.setObjectName("AfinaLabel")
        self.ZeusLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.ZeusLabelTimer.setGeometry(QtCore.QRect(200, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.ZeusLabelTimer.setFont(font)
        self.ZeusLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.ZeusLabelTimer.setText("")
        self.ZeusLabelTimer.setObjectName("ZeusLabelTimer")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(180, 340, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_32.setObjectName("label_32")
        self.NightStop = QtWidgets.QPushButton(self.centralwidget)
        self.NightStop.setGeometry(QtCore.QRect(730, 380, 61, 41))
        self.NightStop.setObjectName("NightStop")
        self.DjonBar = QtWidgets.QSlider(self.centralwidget)
        self.DjonBar.setGeometry(QtCore.QRect(600, 490, 121, 16))
        self.DjonBar.setMinimum(1)
        self.DjonBar.setMaximum(30)
        self.DjonBar.setOrientation(QtCore.Qt.Horizontal)
        self.DjonBar.setObjectName("DjonBar")
        self.DjonBar.setValue(int(Djon[2]))
        self.DjonBar.valueChanged.connect(self.updateLabelDjon)
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(580, 340, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(0, 190, 0);")
        self.label_33.setObjectName("label_33")
        self.DjonStop = QtWidgets.QPushButton(self.centralwidget)
        self.DjonStop.setGeometry(QtCore.QRect(730, 480, 61, 41))
        self.DjonStop.setObjectName("DjonStop")
        self.NightLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.NightLabelTimer.setGeometry(QtCore.QRect(600, 380, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.NightLabelTimer.setFont(font)
        self.NightLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.NightLabelTimer.setText("")
        self.NightLabelTimer.setObjectName("NightLabelTimer")
        self.PoisonLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.PoisonLabelTimer.setGeometry(QtCore.QRect(600, 430, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.PoisonLabelTimer.setFont(font)
        self.PoisonLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.PoisonLabelTimer.setText("")
        self.PoisonLabelTimer.setObjectName("PoisonLabelTimer")
        self.NightStart = QtWidgets.QPushButton(self.centralwidget)
        self.NightStart.setGeometry(QtCore.QRect(410, 380, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NightStart.setFont(font)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/123/nitemzc37.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NightStart.setIcon(icon14)
        self.NightStart.setIconSize(QtCore.QSize(32, 32))
        self.NightStart.setObjectName("NightStart")
        self.PoisonLabel = QtWidgets.QLabel(self.centralwidget)
        self.PoisonLabel.setGeometry(QtCore.QRect(600, 420, 121, 16))
        self.PoisonLabel.setObjectName("PoisonLabel")
        self.NightBar = QtWidgets.QSlider(self.centralwidget)
        self.NightBar.setGeometry(QtCore.QRect(600, 390, 121, 16))
        self.NightBar.setMinimum(1)
        self.NightBar.setMaximum(20)
        self.NightBar.setOrientation(QtCore.Qt.Horizontal)
        self.NightBar.setObjectName("NightBar")
        self.NightBar.setValue(int(Night[2]))
        self.NightBar.valueChanged.connect(self.updateLabelNight)
        self.PoisonStart = QtWidgets.QPushButton(self.centralwidget)
        self.PoisonStart.setGeometry(QtCore.QRect(410, 430, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.PoisonStart.setFont(font)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/123/nitemzc72.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PoisonStart.setIcon(icon15)
        self.PoisonStart.setIconSize(QtCore.QSize(32, 32))
        self.PoisonStart.setObjectName("PoisonStart")
        self.PoisonStop = QtWidgets.QPushButton(self.centralwidget)
        self.PoisonStop.setGeometry(QtCore.QRect(730, 430, 61, 41))
        self.PoisonStop.setObjectName("PoisonStop")
        self.DjonLabel = QtWidgets.QLabel(self.centralwidget)
        self.DjonLabel.setGeometry(QtCore.QRect(600, 470, 121, 16))
        self.DjonLabel.setObjectName("DjonLabel")
        self.PoisonBar = QtWidgets.QSlider(self.centralwidget)
        self.PoisonBar.setGeometry(QtCore.QRect(600, 440, 121, 16))
        self.PoisonBar.setMinimum(1)
        self.PoisonBar.setMaximum(20)
        self.PoisonBar.setOrientation(QtCore.Qt.Horizontal)
        self.PoisonBar.setObjectName("PoisonBar")
        self.PoisonBar.setValue(int(Poison[2]))
        self.PoisonBar.valueChanged.connect(self.updateLabelPoison)
        self.NightLabel = QtWidgets.QLabel(self.centralwidget)
        self.NightLabel.setGeometry(QtCore.QRect(600, 370, 121, 16))
        self.NightLabel.setObjectName("NightLabel")
        self.DjonStart = QtWidgets.QPushButton(self.centralwidget)
        self.DjonStart.setGeometry(QtCore.QRect(410, 480, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DjonStart.setFont(font)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/123/nitemzc45.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DjonStart.setIcon(icon16)
        self.DjonStart.setIconSize(QtCore.QSize(32, 32))
        self.DjonStart.setObjectName("DjonStart")
        self.DjonLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.DjonLabelTimer.setGeometry(QtCore.QRect(600, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.DjonLabelTimer.setFont(font)
        self.DjonLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.DjonLabelTimer.setText("")
        self.DjonLabelTimer.setObjectName("DjonLabelTimer")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(360, 540, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color: rgb(255, 24, 255);")
        self.label_40.setObjectName("label_40")
        self.AidStop = QtWidgets.QPushButton(self.centralwidget)
        self.AidStop.setGeometry(QtCore.QRect(330, 590, 61, 41))
        self.AidStop.setObjectName("AidStop")
        self.SatanaBar = QtWidgets.QSlider(self.centralwidget)
        self.SatanaBar.setGeometry(QtCore.QRect(600, 650, 121, 16))
        self.SatanaBar.setMinimum(1)
        self.SatanaBar.setMaximum(21)
        self.SatanaBar.setOrientation(QtCore.Qt.Horizontal)
        self.SatanaBar.setObjectName("SatanaBar")
        self.SatanaBar.setValue(int(Satana[2]))
        self.SatanaBar.valueChanged.connect(self.updateLabelSatana)
        self.SatanaStop = QtWidgets.QPushButton(self.centralwidget)
        self.SatanaStop.setGeometry(QtCore.QRect(730, 640, 61, 41))
        self.SatanaStop.setObjectName("SatanaStop")
        self.AidLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.AidLabelTimer.setGeometry(QtCore.QRect(200, 590, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.AidLabelTimer.setFont(font)
        self.AidLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.AidLabelTimer.setText("")
        self.AidLabelTimer.setObjectName("AidLabelTimer")
        self.JesusLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.JesusLabelTimer.setGeometry(QtCore.QRect(200, 640, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.JesusLabelTimer.setFont(font)
        self.JesusLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.JesusLabelTimer.setText("")
        self.JesusLabelTimer.setObjectName("JesusLabelTimer")
        self.AidStart = QtWidgets.QPushButton(self.centralwidget)
        self.AidStart.setGeometry(QtCore.QRect(10, 590, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AidStart.setFont(font)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/123/Pennywise.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AidStart.setIcon(icon17)
        self.AidStart.setIconSize(QtCore.QSize(36, 36))
        self.AidStart.setObjectName("AidStart")
        self.JesusLabel = QtWidgets.QLabel(self.centralwidget)
        self.JesusLabel.setGeometry(QtCore.QRect(200, 630, 121, 16))
        self.JesusLabel.setObjectName("JesusLabel")
        self.AidBar = QtWidgets.QSlider(self.centralwidget)
        self.AidBar.setGeometry(QtCore.QRect(200, 600, 121, 16))
        self.AidBar.setMinimum(1)
        self.AidBar.setMaximum(60)
        self.AidBar.setOrientation(QtCore.Qt.Horizontal)
        self.AidBar.setObjectName("AidBar")
        self.AidBar.setValue(int(Aid[2]))
        self.AidBar.valueChanged.connect(self.updateLabelAid)
        self.JesusStart = QtWidgets.QPushButton(self.centralwidget)
        self.JesusStart.setGeometry(QtCore.QRect(10, 640, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.JesusStart.setFont(font)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/123/Arrow317.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.JesusStart.setIcon(icon18)
        self.JesusStart.setIconSize(QtCore.QSize(32, 32))
        self.JesusStart.setObjectName("JesusStart")
        self.JesusStop = QtWidgets.QPushButton(self.centralwidget)
        self.JesusStop.setGeometry(QtCore.QRect(330, 640, 61, 41))
        self.JesusStop.setObjectName("JesusStop")
        self.SatanaLabel = QtWidgets.QLabel(self.centralwidget)
        self.SatanaLabel.setGeometry(QtCore.QRect(600, 630, 121, 16))
        self.SatanaLabel.setObjectName("SatanaLabel")
        self.JesusBar = QtWidgets.QSlider(self.centralwidget)
        self.JesusBar.setGeometry(QtCore.QRect(200, 650, 121, 16))
        self.JesusBar.setMinimum(1)
        self.JesusBar.setMaximum(36)
        self.JesusBar.setOrientation(QtCore.Qt.Horizontal)
        self.JesusBar.setObjectName("JesusBar")
        self.JesusBar.setValue(int(Jesus[2]))
        self.JesusBar.valueChanged.connect(self.updateLabelJesus)
        self.AidLabel = QtWidgets.QLabel(self.centralwidget)
        self.AidLabel.setGeometry(QtCore.QRect(200, 580, 121, 16))
        self.AidLabel.setObjectName("AidLabel")
        self.SatanaStart = QtWidgets.QPushButton(self.centralwidget)
        self.SatanaStart.setGeometry(QtCore.QRect(410, 640, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.SatanaStart.setFont(font)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/123/Arrow236.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SatanaStart.setIcon(icon19)
        self.SatanaStart.setIconSize(QtCore.QSize(32, 32))
        self.SatanaStart.setObjectName("SatanaStart")
        self.SatanaLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.SatanaLabelTimer.setGeometry(QtCore.QRect(600, 640, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.SatanaLabelTimer.setFont(font)
        self.SatanaLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.SatanaLabelTimer.setText("")
        self.SatanaLabelTimer.setObjectName("SatanaLabelTimer")
        self.ArkusStop = QtWidgets.QPushButton(self.centralwidget)
        self.ArkusStop.setGeometry(QtCore.QRect(730, 590, 61, 41))
        self.ArkusStop.setObjectName("ArkusStop")
        self.ArkusLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.ArkusLabelTimer.setGeometry(QtCore.QRect(600, 590, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.ArkusLabelTimer.setFont(font)
        self.ArkusLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.ArkusLabelTimer.setText("")
        self.ArkusLabelTimer.setObjectName("ArkusLabelTimer")
        self.ArkusStart = QtWidgets.QPushButton(self.centralwidget)
        self.ArkusStart.setGeometry(QtCore.QRect(410, 590, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ArkusStart.setFont(font)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/123/Arrow301.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ArkusStart.setIcon(icon20)
        self.ArkusStart.setIconSize(QtCore.QSize(32, 32))
        self.ArkusStart.setObjectName("ArkusStart")
        self.ArkusBar = QtWidgets.QSlider(self.centralwidget)
        self.ArkusBar.setGeometry(QtCore.QRect(600, 600, 121, 16))
        self.ArkusBar.setMinimum(1)
        self.ArkusBar.setMaximum(25)
        self.ArkusBar.setOrientation(QtCore.Qt.Horizontal)
        self.ArkusBar.setObjectName("ArkusBar")
        self.ArkusBar.setValue(int(Arkus[2]))
        self.ArkusBar.valueChanged.connect(self.updateLabelArkus)
        self.ArkusLabel = QtWidgets.QLabel(self.centralwidget)
        self.ArkusLabel.setGeometry(QtCore.QRect(600, 580, 121, 16))
        self.ArkusLabel.setObjectName("ArkusLabel")
        self.ZevsStop = QtWidgets.QPushButton(self.centralwidget)
        self.ZevsStop.setGeometry(QtCore.QRect(730, 690, 61, 41))
        self.ZevsStop.setObjectName("ZevsStop")
        self.ZevsLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.ZevsLabelTimer.setGeometry(QtCore.QRect(600, 690, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.ZevsLabelTimer.setFont(font)
        self.ZevsLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.ZevsLabelTimer.setText("")
        self.ZevsLabelTimer.setObjectName("ZevsLabelTimer")
        self.ArchangelStop = QtWidgets.QPushButton(self.centralwidget)
        self.ArchangelStop.setGeometry(QtCore.QRect(330, 690, 61, 41))
        self.ArchangelStop.setObjectName("ArchangelStop")
        self.ZevsLabel = QtWidgets.QLabel(self.centralwidget)
        self.ZevsLabel.setGeometry(QtCore.QRect(600, 680, 121, 16))
        self.ZevsLabel.setObjectName("ZevsLabel")
        self.KingLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.KingLabelTimer.setGeometry(QtCore.QRect(200, 740, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.KingLabelTimer.setFont(font)
        self.KingLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.KingLabelTimer.setText("")
        self.KingLabelTimer.setObjectName("KingLabelTimer")
        self.ZevsStart = QtWidgets.QPushButton(self.centralwidget)
        self.ZevsStart.setGeometry(QtCore.QRect(410, 690, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ZevsStart.setFont(font)
        self.ZevsStart.setIcon(icon10)
        self.ZevsStart.setIconSize(QtCore.QSize(32, 32))
        self.ZevsStart.setObjectName("ZevsStart")
        self.KingStop = QtWidgets.QPushButton(self.centralwidget)
        self.KingStop.setGeometry(QtCore.QRect(330, 740, 61, 41))
        self.KingStop.setObjectName("KingStop")
        self.GuardianLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.GuardianLabelTimer.setGeometry(QtCore.QRect(600, 740, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.GuardianLabelTimer.setFont(font)
        self.GuardianLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.GuardianLabelTimer.setText("")
        self.GuardianLabelTimer.setObjectName("GuardianLabelTimer")
        self.ZevsBar = QtWidgets.QSlider(self.centralwidget)
        self.ZevsBar.setGeometry(QtCore.QRect(600, 700, 121, 16))
        self.ZevsBar.setMinimum(1)
        self.ZevsBar.setMaximum(5)
        self.ZevsBar.setOrientation(QtCore.Qt.Horizontal)
        self.ZevsBar.setObjectName("ZevsBar")
        self.ZevsBar.setValue(int(Zevs[2]))
        self.ZevsBar.valueChanged.connect(self.updateLabelZevs)
        self.KingBar = QtWidgets.QSlider(self.centralwidget)
        self.KingBar.setGeometry(QtCore.QRect(200, 750, 121, 16))
        self.KingBar.setMinimum(1)
        self.KingBar.setMaximum(15)
        self.KingBar.setOrientation(QtCore.Qt.Horizontal)
        self.KingBar.setObjectName("KingBar")
        self.KingBar.setValue(int(King[2]))
        self.KingBar.valueChanged.connect(self.updateLabelKing)
        self.GuardianLabel = QtWidgets.QLabel(self.centralwidget)
        self.GuardianLabel.setGeometry(QtCore.QRect(600, 730, 121, 16))
        self.GuardianLabel.setObjectName("GuardianLabel")
        self.KingStart = QtWidgets.QPushButton(self.centralwidget)
        self.KingStart.setGeometry(QtCore.QRect(10, 740, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.KingStart.setFont(font)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/123/ruby174_leggins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KingStart.setIcon(icon21)
        self.KingStart.setIconSize(QtCore.QSize(32, 32))
        self.KingStart.setObjectName("KingStart")
        self.ArchangelLabelTimer = QtWidgets.QLabel(self.centralwidget)
        self.ArchangelLabelTimer.setGeometry(QtCore.QRect(200, 690, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.ArchangelLabelTimer.setFont(font)
        self.ArchangelLabelTimer.setStyleSheet("color: rgb(255, 0, 0);")
        self.ArchangelLabelTimer.setText("")
        self.ArchangelLabelTimer.setObjectName("ArchangelLabelTimer")
        self.KingLabel = QtWidgets.QLabel(self.centralwidget)
        self.KingLabel.setGeometry(QtCore.QRect(200, 730, 121, 16))
        self.KingLabel.setObjectName("KingLabel")
        self.ArchangelLabel = QtWidgets.QLabel(self.centralwidget)
        self.ArchangelLabel.setGeometry(QtCore.QRect(200, 680, 121, 16))
        self.ArchangelLabel.setObjectName("ArchangelLabel")
        self.ArchangelStart = QtWidgets.QPushButton(self.centralwidget)
        self.ArchangelStart.setGeometry(QtCore.QRect(10, 690, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ArchangelStart.setFont(font)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/123/ruby174_boots.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ArchangelStart.setIcon(icon22)
        self.ArchangelStart.setIconSize(QtCore.QSize(36, 36))
        self.ArchangelStart.setObjectName("ArchangelStart")
        self.GuardianBar = QtWidgets.QSlider(self.centralwidget)
        self.GuardianBar.setGeometry(QtCore.QRect(600, 750, 121, 16))
        self.GuardianBar.setMinimum(1)
        self.GuardianBar.setMaximum(18)
        self.GuardianBar.setOrientation(QtCore.Qt.Horizontal)
        self.GuardianBar.setObjectName("GuardianBar")
        self.GuardianBar.setValue(int(Guardian[2]))
        self.GuardianBar.valueChanged.connect(self.updateLabelGuardian)
        self.ArchangelBar = QtWidgets.QSlider(self.centralwidget)
        self.ArchangelBar.setGeometry(QtCore.QRect(200, 700, 121, 16))
        self.ArchangelBar.setMinimum(1)
        self.ArchangelBar.setMaximum(19)
        self.ArchangelBar.setOrientation(QtCore.Qt.Horizontal)
        self.ArchangelBar.setObjectName("ArchangelBar")
        self.ArchangelBar.setValue(int(Archangel[2]))
        self.ArchangelBar.valueChanged.connect(self.updateLabelArchangel)
        self.GuardianStop = QtWidgets.QPushButton(self.centralwidget)
        self.GuardianStop.setGeometry(QtCore.QRect(730, 740, 61, 41))
        self.GuardianStop.setObjectName("GuardianStop")
        self.GuardianStart = QtWidgets.QPushButton(self.centralwidget)
        self.GuardianStart.setGeometry(QtCore.QRect(410, 740, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Clear Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.GuardianStart.setFont(font)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/123/ruby174_helm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GuardianStart.setIcon(icon23)
        self.GuardianStart.setIconSize(QtCore.QSize(32, 32))
        self.GuardianStart.setObjectName("GuardianStart")
        self.ZeusLabelTimer.raise_()
        self.AfinaLabelTimer.raise_()
        self.ZeyaLabelTimer.raise_()
        self.DjonLabelTimer.raise_()
        self.SatanaLabelTimer.raise_()
        self.ShadowLabelTimer.raise_()
        self.VladikaLabelTimer.raise_()
        self.MagistrLabelTimer.raise_()
        self.KecaLabelTimer.raise_()
        self.SpiderLabelTimer.raise_()
        self.BoelLabelTimer.raise_()
        self.SkeletLabelTimer.raise_()
        self.LeviafLabelTimer.raise_()
        self.SundukLabelTimer.raise_()
        self.DemonLabelTimer.raise_()
        self.UgodieLabelTimer.raise_()
        self.UgodieBar.raise_()
        self.UgodieStart.raise_()
        self.UgodieStop.raise_()
        self.BoelStart.raise_()
        self.BoelStop.raise_()
        self.BoelBar.raise_()
        self.SkeletBar.raise_()
        self.SkeletStart.raise_()
        self.SkeletStop.raise_()
        self.LeviafBar.raise_()
        self.LeviafStart.raise_()
        self.LeviafStop.raise_()
        self.SundukBar.raise_()
        self.SundukStart.raise_()
        self.SundukStop.raise_()
        self.DemonBar.raise_()
        self.DemonStart.raise_()
        self.DemonStop.raise_()
        self.label_7.raise_()
        self.KecaBar.raise_()
        self.MagistrBar.raise_()
        self.KecaStop.raise_()
        self.SpiderStop.raise_()
        self.SpiderStart.raise_()
        self.MagistrStop.raise_()
        self.KecaStart.raise_()
        self.MagistrStart.raise_()
        self.SpiderBar.raise_()
        self.UgodieLabel.raise_()
        self.BoelLabel.raise_()
        self.SkeletLabel.raise_()
        self.LeviafLabel.raise_()
        self.SundukLabel.raise_()
        self.DemonLabel.raise_()
        self.MagistrLabel.raise_()
        self.KecaLabel.raise_()
        self.SpiderLabel.raise_()
        self.label_20.raise_()
        self.VladikaStart.raise_()
        self.VladikaLabel.raise_()
        self.VladikaStop.raise_()
        self.VladikaBar.raise_()
        self.label_23.raise_()
        self.ShadowStart.raise_()
        self.ShadowLabel.raise_()
        self.ShadowStop.raise_()
        self.ShadowBar.raise_()
        self.AfinaBar.raise_()
        self.ZeyaBar.raise_()
        self.ZeyaLabel.raise_()
        self.AfinaStop.raise_()
        self.ZeusStop.raise_()
        self.ZeusStart.raise_()
        self.ZeyaStop.raise_()
        self.AfinaStart.raise_()
        self.ZeyaStart.raise_()
        self.ZeusLabel.raise_()
        self.ZeusBar.raise_()
        self.AfinaLabel.raise_()
        self.label_32.raise_()
        self.NightStop.raise_()
        self.DjonBar.raise_()
        self.label_33.raise_()
        self.DjonStop.raise_()
        self.NightLabelTimer.raise_()
        self.PoisonLabelTimer.raise_()
        self.NightStart.raise_()
        self.PoisonLabel.raise_()
        self.NightBar.raise_()
        self.PoisonStart.raise_()
        self.PoisonStop.raise_()
        self.DjonLabel.raise_()
        self.PoisonBar.raise_()
        self.NightLabel.raise_()
        self.DjonStart.raise_()
        self.label_40.raise_()
        self.AidStop.raise_()
        self.SatanaBar.raise_()
        self.SatanaStop.raise_()
        self.AidLabelTimer.raise_()
        self.JesusLabelTimer.raise_()
        self.AidStart.raise_()
        self.JesusLabel.raise_()
        self.AidBar.raise_()
        self.JesusStart.raise_()
        self.JesusStop.raise_()
        self.SatanaLabel.raise_()
        self.JesusBar.raise_()
        self.AidLabel.raise_()
        self.SatanaStart.raise_()
        self.ArkusStop.raise_()
        self.ArkusLabelTimer.raise_()
        self.ArkusStart.raise_()
        self.ArkusBar.raise_()
        self.ArkusLabel.raise_()
        self.ZevsStop.raise_()
        self.ZevsLabelTimer.raise_()
        self.ArchangelStop.raise_()
        self.ZevsLabel.raise_()
        self.KingLabelTimer.raise_()
        self.ZevsStart.raise_()
        self.KingStop.raise_()
        self.GuardianLabelTimer.raise_()
        self.ZevsBar.raise_()
        self.KingBar.raise_()
        self.GuardianLabel.raise_()
        self.KingStart.raise_()
        self.ArchangelLabelTimer.raise_()
        self.KingLabel.raise_()
        self.ArchangelLabel.raise_()
        self.ArchangelStart.raise_()
        self.GuardianBar.raise_()
        self.ArchangelBar.raise_()
        self.GuardianStop.raise_()
        self.GuardianStart.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rpg Erazion"))
        self.UgodieStart.setText(_translate("MainWindow", "  [55]Угодье страданий  "))
        self.UgodieStop.setText(_translate("MainWindow", "Stop"))
        self.BoelStart.setText(_translate("MainWindow", " [76]Проклятый Боейль "))
        self.BoelStop.setText(_translate("MainWindow", "Stop"))
        self.SkeletStart.setText(_translate("MainWindow", "  [73]Король скелетов  "))
        self.SkeletStop.setText(_translate("MainWindow", "Stop"))
        self.LeviafStart.setText(_translate("MainWindow", " [75]Левиаффтониарий "))
        self.LeviafStop.setText(_translate("MainWindow", "Stop"))
        self.SundukStart.setText(_translate("MainWindow", " [70]Проклятый сундук "))
        self.SundukStop.setText(_translate("MainWindow", "Stop"))
        self.DemonStart.setText(_translate("MainWindow", " [95]Демон отчуждения "))
        self.DemonStop.setText(_translate("MainWindow", "Stop"))
        self.label_7.setText(_translate("MainWindow", "Долина мертвых"))
        self.KecaStop.setText(_translate("MainWindow", "Stop"))
        self.SpiderStop.setText(_translate("MainWindow", "Stop"))
        self.SpiderStart.setText(_translate("MainWindow", "[85]Мачеха Тарантулов"))
        self.MagistrStop.setText(_translate("MainWindow", "Stop"))
        self.KecaStart.setText(_translate("MainWindow", "   [70]Кецалькоатль   "))
        self.MagistrStart.setText(_translate("MainWindow", "[68]Безумный магистр"))
        self.UgodieLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Ugodie[2])))
        self.BoelLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Boel[2])))
        self.SkeletLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Skelet[2])))
        self.LeviafLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Leviaf[2])))
        self.SundukLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Sunduk[2])))
        self.DemonLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Demon[2])))
        self.MagistrLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Magistr[2])))
        self.KecaLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Keca[2])))
        self.SpiderLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Spider[2])))
        self.label_20.setText(_translate("MainWindow", "Рейд"))
        self.VladikaStart.setText(_translate("MainWindow", "     [85]Владыка          "))
        self.VladikaLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Vladika[2])))
        self.VladikaStop.setText(_translate("MainWindow", "Stop"))
        self.label_23.setText(_translate("MainWindow", "Т1 сет"))
        self.ShadowStart.setText(_translate("MainWindow", "     [60]Пустая тень     "))
        self.ShadowLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Shadow[2])))
        self.ShadowStop.setText(_translate("MainWindow", "Stop"))
        self.ZeyaLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Zeya[2])))
        self.AfinaStop.setText(_translate("MainWindow", "Stop"))
        self.ZeusStop.setText(_translate("MainWindow", "Stop"))
        self.ZeusStart.setText(_translate("MainWindow", "   [90]Бог грома, ЗЕВС   "))
        self.ZeyaStop.setText(_translate("MainWindow", "Stop"))
        self.AfinaStart.setText(_translate("MainWindow", "     [72]Богиня Афина     "))
        self.ZeyaStart.setText(_translate("MainWindow", "        [72]Богиня Зея       "))
        self.ZeusLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Zeus[2])))
        self.AfinaLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Afina[2])))
        self.label_32.setText(_translate("MainWindow", "Олимп"))
        self.NightStop.setText(_translate("MainWindow", "Stop"))
        self.label_33.setText(_translate("MainWindow", "Печати"))
        self.DjonStop.setText(_translate("MainWindow", "Stop"))
        self.NightStart.setText(_translate("MainWindow", " [52]Повелитель ночи "))
        self.PoisonLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Poison[2])))
        self.PoisonStart.setText(_translate("MainWindow", "  [54]Ядовитая мантикора "))
        self.PoisonStop.setText(_translate("MainWindow", "Stop"))
        self.DjonLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Djon[2])))
        self.NightLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Night[2])))
        self.DjonStart.setText(_translate("MainWindow", "  [58]Берсерк - Джон  "))
        self.label_40.setText(_translate("MainWindow", "БОССЫ"))
        self.AidStop.setText(_translate("MainWindow", "Stop"))
        self.SatanaStop.setText(_translate("MainWindow", "Stop"))
        self.AidStart.setText(_translate("MainWindow", "       [75]Аид             "))
        self.JesusLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Jesus[2])))
        self.JesusStart.setText(_translate("MainWindow", "   [51]Иисус, сын божий   "))
        self.JesusStop.setText(_translate("MainWindow", "Stop"))
        self.SatanaLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Satana[2])))
        self.AidLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Aid[2])))
        self.SatanaStart.setText(_translate("MainWindow", "         [47]Сатана            "))
        self.ArkusStop.setText(_translate("MainWindow", "Stop"))
        self.ArkusStart.setText(_translate("MainWindow", "           [44]Аркус           "))
        self.ArkusLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Arkus[2])))
        self.ZevsStop.setText(_translate("MainWindow", "Stop"))
        self.ArchangelStop.setText(_translate("MainWindow", "Stop"))
        self.ZevsLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Zevs[2])))
        self.ZevsStart.setText(_translate("MainWindow", "        [16]Зевс                 "))
        self.KingStop.setText(_translate("MainWindow", "Stop"))
        self.GuardianLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Guardian[2])))
        self.KingStart.setText(_translate("MainWindow", "         [31]Король рая         "))
        self.KingLabel.setText(_translate("MainWindow", "Текущее значение: " + str(King[2])))
        self.ArchangelLabel.setText(_translate("MainWindow", "Текущее значение: " + str(Archangel[2])))
        self.ArchangelStart.setText(_translate("MainWindow", "     [27]Архангел     "))
        self.GuardianStop.setText(_translate("MainWindow", "Stop"))
        self.GuardianStart.setText(_translate("MainWindow", "[27]Хранитель воздуха"))
        self.UgodieStart.clicked.connect(self.UgodieStarting)
        self.UgodieStop.clicked.connect(self.UgodieStopping)
        self.BoelStart.clicked.connect(self.BoelStarting)
        self.BoelStop.clicked.connect(self.BoelStopping)
        self.SkeletStart.clicked.connect(self.SkeletStarting)
        self.SkeletStop.clicked.connect(self.SkeletStopping)
        self.LeviafStart.clicked.connect(self.LeviafStarting)
        self.LeviafStop.clicked.connect(self.LeviafStopping)
        self.SundukStart.clicked.connect(self.SundukStarting)
        self.SundukStop.clicked.connect(self.SundukStopping)
        self.MagistrStart.clicked.connect(self.MagistrStarting)
        self.MagistrStop.clicked.connect(self.MagistrStopping)
        self.KecaStart.clicked.connect(self.KecaStarting)
        self.KecaStop.clicked.connect(self.KecaStopping)
        self.DemonStart.clicked.connect(self.DemonStarting)
        self.DemonStop.clicked.connect(self.DemonStopping)
        self.SpiderStart.clicked.connect(self.SpiderStarting)
        self.SpiderStop.clicked.connect(self.SpiderStopping)
        self.ShadowStart.clicked.connect(self.ShadowStarting)
        self.ShadowStop.clicked.connect(self.ShadowStopping)
        self.VladikaStart.clicked.connect(self.VladikaStarting)
        self.VladikaStop.clicked.connect(self.VladikaStopping)
        self.ZeyaStart.clicked.connect(self.ZeyaStarting)
        self.ZeyaStop.clicked.connect(self.ZeyaStopping)
        self.AfinaStart.clicked.connect(self.AfinaStarting)
        self.AfinaStop.clicked.connect(self.AfinaStopping)
        self.ZeusStart.clicked.connect(self.ZeusStarting)
        self.ZeusStop.clicked.connect(self.ZeusStopping)
        self.NightStart.clicked.connect(self.NightStarting)
        self.NightStop.clicked.connect(self.NightStopping)
        self.PoisonStart.clicked.connect(self.PoisonStarting)
        self.PoisonStop.clicked.connect(self.PoisonStopping)
        self.DjonStart.clicked.connect(self.DjonStarting)
        self.DjonStop.clicked.connect(self.DjonStopping)
        self.AidStart.clicked.connect(self.AidStarting)
        self.AidStop.clicked.connect(self.AidStopping)
        self.JesusStart.clicked.connect(self.JesusStarting)
        self.JesusStop.clicked.connect(self.JesusStopping)
        self.ArkusStart.clicked.connect(self.ArkusStarting)
        self.ArkusStop.clicked.connect(self.ArkusStopping)
        self.SatanaStart.clicked.connect(self.SatanaStarting)
        self.SatanaStop.clicked.connect(self.SatanaStopping)
        self.ArchangelStart.clicked.connect(self.ArchangelStarting)
        self.ArchangelStop.clicked.connect(self.ArchangelStopping)
        self.KingStart.clicked.connect(self.KingStarting)
        self.KingStop.clicked.connect(self.KingStopping)
        self.ZevsStart.clicked.connect(self.ZevsStarting)
        self.ZevsStop.clicked.connect(self.ZevsStopping)
        self.GuardianStart.clicked.connect(self.GuardianStarting)
        self.GuardianStop.clicked.connect(self.GuardianStopping)

############################Ugodie###################################

    def UgodieStarting(self):
        self.UgodieLabel.hide()
        self.UgodieBar.hide()
        self.UgodieLabelTimer.show()
        self.UgodieStart.setEnabled(False)
        MyGlobalsVars.aUgodie = int(Ugodie[2]) * 60
        UgodieStart = threading.Thread(target=self.UgodieTime, args=())
        UgodieStart.start()

    def UgodieStopping(self):
        self.UgodieLabel.show()
        self.UgodieBar.show()
        self.UgodieLabelTimer.hide()
        self.UgodieStart.setEnabled(True)
        self.UgodieBar.setValue(int(Ugodie[2]))
        MyGlobalsVars.aUgodie = 0

    def UgodieTime(self):
        while MyGlobalsVars.aUgodie > 0:
            m, s = divmod(MyGlobalsVars.aUgodie, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.UgodieLabelTimer.setText(min_sec_format)
            if self.UgodieLabelTimer.text() == "05:00":
                UgodieNotify = win10toast.ToastNotifier()
                UgodieNotify.show_toast("Через 5 минут зареспавнится босс: ", Ugodie[1])
                MyGlobalsVars.aUgodie -= 3
            time.sleep(1)
            MyGlobalsVars.aUgodie -= 1
        self.UgodieLabel.show()
        self.UgodieBar.show()
        self.UgodieLabelTimer.hide()
        self.UgodieStart.setEnabled(True)
        self.UgodieBar.setValue(int(Ugodie[2]))
        MyGlobalsVars.aUgodie = 0
        if self.UgodieLabelTimer.text() == "00:01":
            UgodieNotify = win10toast.ToastNotifier()
            UgodieNotify.show_toast("Зареспавнился босс: ", Ugodie[1])

    def updateLabelUgodie(self, value):
        self.UgodieLabel.setText("Текущее значение: " + str(value))
        Ugodie[2] = str(value)

############################Boel#######################################

    def BoelStarting(self):
        self.BoelLabel.hide()
        self.BoelBar.hide()
        self.BoelLabelTimer.show()
        self.BoelStart.setEnabled(False)
        MyGlobalsVars.aBoel = int(Boel[2]) * 60
        BoelStart = threading.Thread(target=self.BoelTime, args=())
        BoelStart.start()

    def BoelStopping(self):
        self.BoelLabel.show()
        self.BoelBar.show()
        self.BoelLabelTimer.hide()
        self.BoelStart.setEnabled(True)
        self.BoelBar.setValue(int(Boel[2]))
        MyGlobalsVars.aBoel = 0

    def BoelTime(self):
        while MyGlobalsVars.aBoel > 0:
            m, s = divmod(MyGlobalsVars.aBoel, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.BoelLabelTimer.setText(min_sec_format)
            if self.BoelLabelTimer.text() == "05:00":
                BoelNotify = win10toast.ToastNotifier()
                BoelNotify.show_toast("Через 5 минут зареспавнится босс: ", Boel[1])
                MyGlobalsVars.aBoel -= 3
            time.sleep(1)
            MyGlobalsVars.aBoel -= 1
        self.BoelLabel.show()
        self.BoelBar.show()
        self.BoelLabelTimer.hide()
        self.BoelStart.setEnabled(True)
        self.BoelBar.setValue(int(Boel[2]))
        MyGlobalsVars.aBoel = 0
        if self.BoelLabelTimer.text() == "00:01":
            BoelNotify = win10toast.ToastNotifier()
            BoelNotify.show_toast("Зареспавнился босс: ", Boel[1])

    def updateLabelBoel(self, value):
        self.BoelLabel.setText("Текущее значение: " + str(value))
        Boel[2] = str(value)

############################Skelet#######################################

    def SkeletStarting(self):
        self.SkeletLabel.hide()
        self.SkeletBar.hide()
        self.SkeletLabelTimer.show()
        self.SkeletStart.setEnabled(False)
        MyGlobalsVars.aSkelet = int(Skelet[2]) * 60
        SkeletStart = threading.Thread(target=self.SkeletTime, args=())
        SkeletStart.start()

    def SkeletStopping(self):
        self.SkeletLabel.show()
        self.SkeletBar.show()
        self.SkeletLabelTimer.hide()
        self.SkeletStart.setEnabled(True)
        self.SkeletBar.setValue(int(Skelet[2]))
        MyGlobalsVars.aSkelet = 0

    def SkeletTime(self):
        while MyGlobalsVars.aSkelet > 0:
            m, s = divmod(MyGlobalsVars.aSkelet, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.SkeletLabelTimer.setText(min_sec_format)
            if self.SkeletLabelTimer.text() == "05:00":
                SkeletNotify = win10toast.ToastNotifier()
                SkeletNotify.show_toast("Через 5 минут зареспавнится босс: ", Skelet[1])
                MyGlobalsVars.aSkelet -= 3
            time.sleep(1)
            MyGlobalsVars.aSkelet -= 1
        self.SkeletLabel.show()
        self.SkeletBar.show()
        self.SkeletLabelTimer.hide()
        self.SkeletStart.setEnabled(True)
        self.SkeletBar.setValue(int(Skelet[2]))
        MyGlobalsVars.aSkelet = 0
        if self.SkeletLabelTimer.text() == "00:01":
            SkeletNotify = win10toast.ToastNotifier()
            SkeletNotify.show_toast("Зареспавнился босс: ", Skelet[1])

    def updateLabelSkelet(self, value):
        self.SkeletLabel.setText("Текущее значение: " + str(value))
        Skelet[2] = str(value)

############################Leviaf#######################################

    def LeviafStarting(self):
        self.LeviafLabel.hide()
        self.LeviafBar.hide()
        self.LeviafLabelTimer.show()
        self.LeviafStart.setEnabled(False)
        MyGlobalsVars.aLeviaf = int(Leviaf[2]) * 60
        LeviafStart = threading.Thread(target=self.LeviafTime, args=())
        LeviafStart.start()

    def LeviafStopping(self):
        self.LeviafLabel.show()
        self.LeviafBar.show()
        self.LeviafLabelTimer.hide()
        self.LeviafStart.setEnabled(True)
        self.LeviafBar.setValue(int(Leviaf[2]))
        MyGlobalsVars.aLeviaf = 0

    def LeviafTime(self):
        while MyGlobalsVars.aLeviaf > 0:
            m, s = divmod(MyGlobalsVars.aLeviaf, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.LeviafLabelTimer.setText(min_sec_format)
            if self.LeviafLabelTimer.text() == "05:00":
                MyGlobalsVars.aLeviaf -= 3
                LeviafNotify = win10toast.ToastNotifier()
                LeviafNotify.show_toast("Через 5 минут зареспавнится босс: ", Leviaf[1])
            time.sleep(1)
            MyGlobalsVars.aLeviaf -= 1
        self.LeviafLabel.show()
        self.LeviafBar.show()
        self.LeviafLabelTimer.hide()
        self.LeviafStart.setEnabled(True)
        self.LeviafBar.setValue(int(Leviaf[2]))
        MyGlobalsVars.aLeviaf = 0
        if self.LeviafLabelTimer.text() == "00:01":
            LeviafNotify = win10toast.ToastNotifier()
            LeviafNotify.show_toast("Зареспавнился босс: ", Leviaf[1])

    def updateLabelLeviaf(self, value):
        self.LeviafLabel.setText("Текущее значение: " + str(value))
        Leviaf[2] = str(value)

############################Sunduk#######################################

    def SundukStarting(self):
        self.SundukLabel.hide()
        self.SundukBar.hide()
        self.SundukLabelTimer.show()
        self.SundukStart.setEnabled(False)
        MyGlobalsVars.aSunduk = int(Sunduk[2]) * 60
        SundukStart = threading.Thread(target=self.SundukTime, args=())
        SundukStart.start()

    def SundukStopping(self):
        self.SundukLabel.show()
        self.SundukBar.show()
        self.SundukLabelTimer.hide()
        self.SundukStart.setEnabled(True)
        self.SundukBar.setValue(int(Sunduk[2]))
        MyGlobalsVars.aSunduk = 0

    def SundukTime(self):
        while MyGlobalsVars.aSunduk > 0:
            m, s = divmod(MyGlobalsVars.aSunduk, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.SundukLabelTimer.setText(min_sec_format)
            if self.SundukLabelTimer.text() == "05:00":
                SundukNotify = win10toast.ToastNotifier()
                SundukNotify.show_toast("Через 5 минут зареспавнится босс: ", Sunduk[1])
                MyGlobalsVars.aSunduk -= 3
            time.sleep(1)
            MyGlobalsVars.aSunduk -= 1
        self.SundukLabel.show()
        self.SundukBar.show()
        self.SundukLabelTimer.hide()
        self.SundukStart.setEnabled(True)
        self.SundukBar.setValue(int(Sunduk[2]))
        MyGlobalsVars.aSunduk = 0
        if self.SundukLabelTimer.text() == "00:01":
            SundukNotify = win10toast.ToastNotifier()
            SundukNotify.show_toast("Зареспавнился босс: ", Sunduk[1])

    def updateLabelSunduk(self, value):
        self.SundukLabel.setText("Текущее значение: " + str(value))
        Sunduk[2] = str(value)

############################Demon#######################################

    def DemonStarting(self):
        self.DemonLabel.hide()
        self.DemonBar.hide()
        self.DemonLabelTimer.show()
        self.DemonStart.setEnabled(False)
        MyGlobalsVars.aDemon = int(Demon[2]) * 60
        DemonStart = threading.Thread(target=self.DemonTime, args=())
        DemonStart.start()

    def DemonStopping(self):
        self.DemonLabel.show()
        self.DemonBar.show()
        self.DemonLabelTimer.hide()
        self.DemonStart.setEnabled(True)
        self.DemonBar.setValue(int(Demon[2]))
        MyGlobalsVars.aDemon = 0

    def DemonTime(self):
        while MyGlobalsVars.aDemon > 0:
            m, s = divmod(MyGlobalsVars.aDemon, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.DemonLabelTimer.setText(min_sec_format)
            if self.DemonLabelTimer.text() == "05:00":
                DemonNotify = win10toast.ToastNotifier()
                DemonNotify.show_toast("Через 5 минут зареспавнится босс: ", Demon[1])
                MyGlobalsVars.aDemon -= 3
            time.sleep(1)
            MyGlobalsVars.aDemon -= 1
        self.DemonLabel.show()
        self.DemonBar.show()
        self.DemonLabelTimer.hide()
        self.DemonStart.setEnabled(True)
        self.DemonBar.setValue(int(Demon[2]))
        MyGlobalsVars.aDemon = 0
        if self.DemonLabelTimer.text() == "00:01":
            DemonNotify = win10toast.ToastNotifier()
            DemonNotify.show_toast("Зареспавнился босс: ", Demon[1])

    def updateLabelDemon(self, value):
        self.DemonLabel.setText("Текущее значение: " + str(value))
        Demon[2] = str(value)

############################Magistr#######################################

    def MagistrStarting(self):
        self.MagistrLabel.hide()
        self.MagistrBar.hide()
        self.MagistrLabelTimer.show()
        self.MagistrStart.setEnabled(False)
        MyGlobalsVars.aMagistr = int(Magistr[2]) * 60
        MagistrStart = threading.Thread(target=self.MagistrTime, args=())
        MagistrStart.start()

    def MagistrStopping(self):
        self.MagistrLabel.show()
        self.MagistrBar.show()
        self.MagistrLabelTimer.hide()
        self.MagistrStart.setEnabled(True)
        self.MagistrBar.setValue(int(Magistr[2]))
        MyGlobalsVars.aMagistr = 0

    def MagistrTime(self):
        while MyGlobalsVars.aMagistr > 0:
            m, s = divmod(MyGlobalsVars.aMagistr, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.MagistrLabelTimer.setText(min_sec_format)
            if self.MagistrLabelTimer.text() == "05:00":
                MagistrNotify = win10toast.ToastNotifier()
                MagistrNotify.show_toast("Через 5 минут зареспавнится босс: ", Magistr[1])
                MyGlobalsVars.aMagistr -= 3
            time.sleep(1)
            MyGlobalsVars.aMagistr -= 1
            self.MagistrLabel.show()
            self.MagistrBar.show()
            self.MagistrLabelTimer.hide()
            self.MagistrStart.setEnabled(True)
            self.MagistrBar.setValue(int(Magistr[2]))
            MyGlobalsVars.aMagistr = 0
            if self.MagistrLabelTimer.text() == "00:01":
                MagistrNotify = win10toast.ToastNotifier()
                MagistrNotify.show_toast("Зареспавнился босс: ", Magistr[1])

    def updateLabelMagistr(self, value):
        self.MagistrLabel.setText("Текущее значение: " + str(value))
        Magistr[2] = str(value)

############################Keca#######################################

    def KecaStarting(self):
        self.KecaLabel.hide()
        self.KecaBar.hide()
        self.KecaLabelTimer.show()
        self.KecaStart.setEnabled(False)
        MyGlobalsVars.aKeca = int(Keca[2]) * 60
        KecaStart = threading.Thread(target=self.KecaTime, args=())
        KecaStart.start()

    def KecaStopping(self):
        self.KecaLabel.show()
        self.KecaBar.show()
        self.KecaLabelTimer.hide()
        self.KecaStart.setEnabled(True)
        self.KecaBar.setValue(int(Keca[2]))
        MyGlobalsVars.aKeca = 0

    def KecaTime(self):
        while MyGlobalsVars.aKeca > 0:
            m, s = divmod(MyGlobalsVars.aKeca, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.KecaLabelTimer.setText(min_sec_format)
            if self.KecaLabelTimer.text() == "05:00":
                KecaNotify = win10toast.ToastNotifier()
                KecaNotify.show_toast("Через 5 минут зареспавнится босс: ", Keca[1])
                MyGlobalsVars.aKeca -= 3
            time.sleep(1)
            MyGlobalsVars.aKeca -= 1
        self.KecaLabel.show()
        self.KecaBar.show()
        self.KecaLabelTimer.hide()
        self.KecaStart.setEnabled(True)
        self.KecaBar.setValue(int(Keca[2]))
        MyGlobalsVars.aKeca = 0
        if self.KecaLabelTimer.text() == "00:01":
            KecaNotify = win10toast.ToastNotifier()
            KecaNotify.show_toast("Зареспавнился босс: ", Keca[1])

    def updateLabelKeca(self, value):
        self.KecaLabel.setText("Текущее значение: " + str(value))
        Keca[2] = str(value)

############################Spider#######################################

    def SpiderStarting(self):
        self.SpiderLabel.hide()
        self.SpiderBar.hide()
        self.SpiderLabelTimer.show()
        self.SpiderStart.setEnabled(False)
        MyGlobalsVars.aSpider = int(Spider[2]) * 60
        SpiderStart = threading.Thread(target=self.SpiderTime, args=())
        SpiderStart.start()

    def SpiderStopping(self):
        self.SpiderLabel.show()
        self.SpiderBar.show()
        self.SpiderLabelTimer.hide()
        self.SpiderStart.setEnabled(True)
        self.SpiderBar.setValue(int(Spider[2]))
        MyGlobalsVars.aSpider = 0

    def SpiderTime(self):
        while MyGlobalsVars.aSpider > 0:
            m, s = divmod(MyGlobalsVars.aSpider, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.SpiderLabelTimer.setText(min_sec_format)
            if self.SpiderLabelTimer.text() == "05:00":
                SpiderNotify = win10toast.ToastNotifier()
                SpiderNotify.show_toast("Через 5 минут зареспавнится босс: ", Spider[1])
                MyGlobalsVars.aSpider -= 3
            time.sleep(1)
            MyGlobalsVars.aSpider -= 1
        self.SpiderLabel.show()
        self.SpiderBar.show()
        self.SpiderLabelTimer.hide()
        self.SpiderStart.setEnabled(True)
        self.SpiderBar.setValue(int(Spider[2]))
        MyGlobalsVars.aSpider = 0
        if self.SpiderLabelTimer.text() == "00:01":
            SpiderNotify = win10toast.ToastNotifier()
            SpiderNotify.show_toast("Зареспавнился босс: ", Spider[1])

    def updateLabelSpider(self, value):
        self.SpiderLabel.setText("Текущее значение: " + str(value))
        Spider[2] = str(value)

############################Shadow#######################################

    def ShadowStarting(self):
        self.ShadowLabel.hide()
        self.ShadowBar.hide()
        self.ShadowLabelTimer.show()
        self.ShadowStart.setEnabled(False)
        MyGlobalsVars.aShadow = int(Shadow[2]) * 60
        ShadowStart = threading.Thread(target=self.ShadowTime, args=())
        ShadowStart.start()

    def ShadowStopping(self):
        self.ShadowLabel.show()
        self.ShadowBar.show()
        self.ShadowLabelTimer.hide()
        self.ShadowStart.setEnabled(True)
        self.ShadowBar.setValue(int(Shadow[2]))
        MyGlobalsVars.aShadow = 0

    def ShadowTime(self):
        while MyGlobalsVars.aShadow > 0:
            m, s = divmod(MyGlobalsVars.aShadow, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.ShadowLabelTimer.setText(min_sec_format)
            if self.ShadowLabelTimer.text() == "05:00":
                ShadowNotify = win10toast.ToastNotifier()
                ShadowNotify.show_toast("Через 5 минут зареспавнится босс: ", Shadow[1])
                MyGlobalsVars.aShadow -= 3
            time.sleep(1)
            MyGlobalsVars.aShadow -= 1
        self.ShadowLabel.show()
        self.ShadowBar.show()
        self.ShadowLabelTimer.hide()
        self.ShadowStart.setEnabled(True)
        self.ShadowBar.setValue(int(Shadow[2]))
        MyGlobalsVars.aShadow = 0
        if self.ShadowLabelTimer.text() == "00:01":
            ShadowNotify = win10toast.ToastNotifier()
            ShadowNotify.show_toast("Зареспавнился босс: ", Shadow[1])

    def updateLabelShadow(self, value):
        self.ShadowLabel.setText("Текущее значение: " + str(value))
        Shadow[2] = str(value)

############################Vladika#######################################

    def VladikaStarting(self):
        self.VladikaLabel.hide()
        self.VladikaBar.hide()
        self.VladikaLabelTimer.show()
        self.VladikaStart.setEnabled(False)
        MyGlobalsVars.aVladika = int(Vladika[2]) * 60
        VladikaStart = threading.Thread(target=self.VladikaTime, args=())
        VladikaStart.start()

    def VladikaStopping(self):
        self.VladikaLabel.show()
        self.VladikaBar.show()
        self.VladikaLabelTimer.hide()
        self.VladikaStart.setEnabled(True)
        self.VladikaBar.setValue(int(Vladika[2]))
        MyGlobalsVars.aVladika = 0

    def VladikaTime(self):
        while MyGlobalsVars.aVladika > 0:
            m, s = divmod(MyGlobalsVars.aVladika, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.VladikaLabelTimer.setText(min_sec_format)
            if self.VladikaLabelTimer.text() == "05:00":
                VladikaNotify = win10toast.ToastNotifier()
                VladikaNotify.show_toast("Через 5 минут зареспавнится босс: ", Vladika[1])
                MyGlobalsVars.aVladika -= 3
            time.sleep(1)
            MyGlobalsVars.aVladika -= 1
        self.VladikaLabel.show()
        self.VladikaBar.show()
        self.VladikaLabelTimer.hide()
        self.VladikaStart.setEnabled(True)
        self.VladikaBar.setValue(int(Vladika[2]))
        MyGlobalsVars.aVladika = 0
        if self.VladikaLabelTimer.text() == "00:01":
            VladikaNotify = win10toast.ToastNotifier()
            VladikaNotify.show_toast("Зареспавнился босс: ", Vladika[1])

    def updateLabelVladika(self, value):
        self.VladikaLabel.setText("Текущее значение: " + str(value))
        Vladika[2] = str(value)

############################Zeya#######################################

    def ZeyaStarting(self):
        self.ZeyaLabel.hide()
        self.ZeyaBar.hide()
        self.ZeyaLabelTimer.show()
        self.ZeyaStart.setEnabled(False)
        MyGlobalsVars.aZeya = int(Zeya[2]) * 60
        ZeyaStart = threading.Thread(target=self.ZeyaTime, args=())
        ZeyaStart.start()

    def ZeyaStopping(self):
        self.ZeyaLabel.show()
        self.ZeyaBar.show()
        self.ZeyaLabelTimer.hide()
        self.ZeyaStart.setEnabled(True)
        self.ZeyaBar.setValue(int(Zeya[2]))
        MyGlobalsVars.aZeya = 0

    def ZeyaTime(self):
        while MyGlobalsVars.aZeya > 0:
            m, s = divmod(MyGlobalsVars.aZeya, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.ZeyaLabelTimer.setText(min_sec_format)
            if self.ZeyaLabelTimer.text() == "05:00":
                ZeyaNotify = win10toast.ToastNotifier()
                ZeyaNotify.show_toast("Через 5 минут зареспавнится босс: ", Zeya[1])
                MyGlobalsVars.aZeya -= 3
            time.sleep(1)
            MyGlobalsVars.aZeya -= 1
        self.ZeyaLabel.show()
        self.ZeyaBar.show()
        self.ZeyaLabelTimer.hide()
        self.ZeyaStart.setEnabled(True)
        self.ZeyaBar.setValue(int(Zeya[2]))
        MyGlobalsVars.aZeya = 0
        if self.ZeyaLabelTimer.text() == "00:01":
            ZeyaNotify = win10toast.ToastNotifier()
            ZeyaNotify.show_toast("Зареспавнился босс: ", Zeya[1])

    def updateLabelZeya(self, value):
        self.ZeyaLabel.setText("Текущее значение: " + str(value))
        Zeya[2] = str(value)

############################Afina#######################################

    def AfinaStarting(self):
        self.AfinaLabel.hide()
        self.AfinaBar.hide()
        self.AfinaLabelTimer.show()
        self.AfinaStart.setEnabled(False)
        MyGlobalsVars.aAfina = int(Afina[2]) * 60
        AfinaStart = threading.Thread(target=self.AfinaTime, args=())
        AfinaStart.start()

    def AfinaStopping(self):
        self.AfinaLabel.show()
        self.AfinaBar.show()
        self.AfinaLabelTimer.hide()
        self.AfinaStart.setEnabled(True)
        self.AfinaBar.setValue(int(Afina[2]))
        MyGlobalsVars.aAfina = 0

    def AfinaTime(self):
        while MyGlobalsVars.aAfina > 0:
            m, s = divmod(MyGlobalsVars.aAfina, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.AfinaLabelTimer.setText(min_sec_format)
            if self.AfinaLabelTimer.text() == "05:00":
                AfinaNotify = win10toast.ToastNotifier()
                AfinaNotify.show_toast("Через 5 минут зареспавнится босс: ", Afina[1])
                MyGlobalsVars.aAfina -= 3
            time.sleep(1)
            MyGlobalsVars.aAfina -= 1
        self.AfinaLabel.show()
        self.AfinaBar.show()
        self.AfinaLabelTimer.hide()
        self.AfinaStart.setEnabled(True)
        self.AfinaBar.setValue(int(Afina[2]))
        MyGlobalsVars.aAfina = 0
        if self.AfinaLabelTimer.text() == "00:01":
            AfinaNotify = win10toast.ToastNotifier()
            AfinaNotify.show_toast("Зареспавнился босс: ", Afina[1])

    def updateLabelAfina(self, value):
        self.AfinaLabel.setText("Текущее значение: " + str(value))
        Afina[2] = str(value)

############################Zeus#######################################

    def ZeusStarting(self):
        self.ZeusLabel.hide()
        self.ZeusBar.hide()
        self.ZeusLabelTimer.show()
        self.ZeusStart.setEnabled(False)
        MyGlobalsVars.aZeus = int(Zeus[2]) * 60
        ZeusStart = threading.Thread(target=self.ZeusTime, args=())
        ZeusStart.start()

    def ZeusStopping(self):
        self.ZeusLabel.show()
        self.ZeusBar.show()
        self.ZeusLabelTimer.hide()
        self.ZeusStart.setEnabled(True)
        self.ZeusBar.setValue(int(Zeus[2]))
        MyGlobalsVars.aZeus = 0

    def ZeusTime(self):
        while MyGlobalsVars.aZeus > 0:
            m, s = divmod(MyGlobalsVars.aZeus, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.ZeusLabelTimer.setText(min_sec_format)
            if self.ZeusLabelTimer.text() == "05:00":
                ZeusNotify = win10toast.ToastNotifier()
                ZeusNotify.show_toast("Через 5 минут зареспавнится босс: ", Zeus[1])
                MyGlobalsVars.aZeus -= 3
            time.sleep(1)
            MyGlobalsVars.aZeus -= 1
        self.ZeusLabel.show()
        self.ZeusBar.show()
        self.ZeusLabelTimer.hide()
        self.ZeusStart.setEnabled(True)
        self.ZeusBar.setValue(int(Zeus[2]))
        MyGlobalsVars.aZeus = 0
        if self.ZeusLabelTimer.text() == "00:01":
            ZeusNotify = win10toast.ToastNotifier()
            ZeusNotify.show_toast("Зареспавнился босс: ", Zeus[1])

    def updateLabelZeus(self, value):
        self.ZeusLabel.setText("Текущее значение: " + str(value))
        Zeus[2] = str(value)

############################Night#######################################

    def NightStarting(self):
        self.NightLabel.hide()
        self.NightBar.hide()
        self.NightLabelTimer.show()
        self.NightStart.setEnabled(False)
        MyGlobalsVars.aNight = int(Night[2]) * 60
        NightStart = threading.Thread(target=self.NightTime, args=())
        NightStart.start()

    def NightStopping(self):
        self.NightLabel.show()
        self.NightBar.show()
        self.NightLabelTimer.hide()
        self.NightStart.setEnabled(True)
        self.NightBar.setValue(int(Night[2]))
        MyGlobalsVars.aNight = 0

    def NightTime(self):
        while MyGlobalsVars.aNight > 0:
            m, s = divmod(MyGlobalsVars.aNight, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.NightLabelTimer.setText(min_sec_format)
            if self.NightLabelTimer.text() == "05:00":
                NightNotify = win10toast.ToastNotifier()
                NightNotify.show_toast("Через 5 минут зареспавнится босс: ", Night[1])
                MyGlobalsVars.aNight -= 3
            time.sleep(1)
            MyGlobalsVars.aNight -= 1
        self.NightLabel.show()
        self.NightBar.show()
        self.NightLabelTimer.hide()
        self.NightStart.setEnabled(True)
        self.NightBar.setValue(int(Night[2]))
        MyGlobalsVars.aNight = 0
        if self.NightLabelTimer.text() == "00:01":
            NightNotify = win10toast.ToastNotifier()
            NightNotify.show_toast("Зареспавнился босс: ", Night[1])

    def updateLabelNight(self, value):
        self.NightLabel.setText("Текущее значение: " + str(value))
        Night[2] = str(value)

############################Poison#######################################

    def PoisonStarting(self):
        self.PoisonLabel.hide()
        self.PoisonBar.hide()
        self.PoisonLabelTimer.show()
        self.PoisonStart.setEnabled(False)
        MyGlobalsVars.aPoison = int(Poison[2]) * 60
        PoisonStart = threading.Thread(target=self.PoisonTime, args=())
        PoisonStart.start()

    def PoisonStopping(self):
        self.PoisonLabel.show()
        self.PoisonBar.show()
        self.PoisonLabelTimer.hide()
        self.PoisonStart.setEnabled(True)
        self.PoisonBar.setValue(int(Poison[2]))
        MyGlobalsVars.aPoison = 0

    def PoisonTime(self):
        while MyGlobalsVars.aPoison > 0:
            m, s = divmod(MyGlobalsVars.aPoison, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.PoisonLabelTimer.setText(min_sec_format)
            if self.PoisonLabelTimer.text() == "05:00":
                PoisonNotify = win10toast.ToastNotifier()
                PoisonNotify.show_toast("Через 5 минут зареспавнится босс: ", Poison[1])
                MyGlobalsVars.aPoison -= 3
            time.sleep(1)
            MyGlobalsVars.aPoison -= 1
        self.PoisonLabel.show()
        self.PoisonBar.show()
        self.PoisonLabelTimer.hide()
        self.PoisonStart.setEnabled(True)
        self.PoisonBar.setValue(int(Poison[2]))
        MyGlobalsVars.aPoison = 0
        if self.PoisonLabelTimer.text() == "00:01":
            PoisonNotify = win10toast.ToastNotifier()
            PoisonNotify.show_toast("Зареспавнился босс: ", Poison[1])

    def updateLabelPoison(self, value):
        self.PoisonLabel.setText("Текущее значение: " + str(value))
        Poison[2] = str(value)

############################Djon#######################################

    def DjonStarting(self):
        self.DjonLabel.hide()
        self.DjonBar.hide()
        self.DjonLabelTimer.show()
        self.DjonStart.setEnabled(False)
        MyGlobalsVars.aDjon = int(Djon[2]) * 60
        DjonStart = threading.Thread(target=self.DjonTime, args=())
        DjonStart.start()

    def DjonStopping(self):
        self.DjonLabel.show()
        self.DjonBar.show()
        self.DjonLabelTimer.hide()
        self.DjonStart.setEnabled(True)
        self.DjonBar.setValue(int(Djon[2]))
        MyGlobalsVars.aDjon = 0

    def DjonTime(self):
        while MyGlobalsVars.aDjon > 0:
            m, s = divmod(MyGlobalsVars.aDjon, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.DjonLabelTimer.setText(min_sec_format)
            if self.DjonLabelTimer.text() == "05:00":
                DjonNotify = win10toast.ToastNotifier()
                DjonNotify.show_toast("Через 5 минут зареспавнится босс: ", Djon[1])
                MyGlobalsVars.aDjon -= 3
            time.sleep(1)
            MyGlobalsVars.aDjon -= 1
        self.DjonLabel.show()
        self.DjonBar.show()
        self.DjonLabelTimer.hide()
        self.DjonStart.setEnabled(True)
        self.DjonBar.setValue(int(Djon[2]))
        MyGlobalsVars.aDjon = 0
        if self.DjonLabelTimer.text() == "00:01":
            DjonNotify = win10toast.ToastNotifier()
            DjonNotify.show_toast("Зареспавнился босс: ", Djon[1])

    def updateLabelDjon(self, value):
        self.DjonLabel.setText("Текущее значение: " + str(value))
        Djon[2] = str(value)

############################Aid#######################################

    def AidStarting(self):
        self.AidLabel.hide()
        self.AidBar.hide()
        self.AidLabelTimer.show()
        self.AidStart.setEnabled(False)
        MyGlobalsVars.aAid = int(Aid[2]) * 60
        AidStart = threading.Thread(target=self.AidTime, args=())
        AidStart.start()

    def AidStopping(self):
        self.AidLabel.show()
        self.AidBar.show()
        self.AidLabelTimer.hide()
        self.AidStart.setEnabled(True)
        self.AidBar.setValue(int(Aid[2]))
        MyGlobalsVars.aAid = 0

    def AidTime(self):
        while MyGlobalsVars.aAid > 0:
            m, s = divmod(MyGlobalsVars.aAid, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.AidLabelTimer.setText(min_sec_format)
            if self.AidLabelTimer.text() == "05:00":
                AidNotify = win10toast.ToastNotifier()
                AidNotify.show_toast("Через 5 минут зареспавнится босс: ", Aid[1])
                MyGlobalsVars.aAid -= 3
            time.sleep(1)
            MyGlobalsVars.aAid -= 1
        self.AidLabel.show()
        self.AidBar.show()
        self.AidLabelTimer.hide()
        self.AidStart.setEnabled(True)
        self.AidBar.setValue(int(Aid[2]))
        MyGlobalsVars.aAid = 0
        if self.AidLabelTimer.text() == "00:01":
            AidNotify = win10toast.ToastNotifier()
            AidNotify.show_toast("Зареспавнился босс: ", Aid[1])

    def updateLabelAid(self, value):
        self.AidLabel.setText("Текущее значение: " + str(value))
        Aid[2] = str(value)

############################Jesus#######################################

    def JesusStarting(self):
        self.JesusLabel.hide()
        self.JesusBar.hide()
        self.JesusLabelTimer.show()
        self.JesusStart.setEnabled(False)
        MyGlobalsVars.aJesus = int(Jesus[2]) * 60
        JesusStart = threading.Thread(target=self.JesusTime, args=())
        JesusStart.start()

    def JesusStopping(self):
        self.JesusLabel.show()
        self.JesusBar.show()
        self.JesusLabelTimer.hide()
        self.JesusStart.setEnabled(True)
        self.JesusBar.setValue(int(Jesus[2]))
        MyGlobalsVars.aJesus = 0

    def JesusTime(self):
        while MyGlobalsVars.aJesus > 0:
            m, s = divmod(MyGlobalsVars.aJesus, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.JesusLabelTimer.setText(min_sec_format)
            if self.JesusLabelTimer.text() == "05:00":
                JesusNotify = win10toast.ToastNotifier()
                JesusNotify.show_toast("Через 5 минут зареспавнится босс: ", Jesus[1])
                MyGlobalsVars.aJesus -= 3
            time.sleep(1)
            MyGlobalsVars.aJesus -= 1
        self.JesusLabel.show()
        self.JesusBar.show()
        self.JesusLabelTimer.hide()
        self.JesusStart.setEnabled(True)
        self.JesusBar.setValue(int(Jesus[2]))
        MyGlobalsVars.aJesus = 0
        if self.JesusLabelTimer.text() == "00:01":
            JesusNotify = win10toast.ToastNotifier()
            JesusNotify.show_toast("Зареспавнился босс: ", Jesus[1])

    def updateLabelJesus(self, value):
        self.JesusLabel.setText("Текущее значение: " + str(value))
        Jesus[2] = str(value)

############################Arkus#######################################

    def ArkusStarting(self):
        self.ArkusLabel.hide()
        self.ArkusBar.hide()
        self.ArkusLabelTimer.show()
        self.ArkusStart.setEnabled(False)
        MyGlobalsVars.aArkus = int(Arkus[2]) * 60
        ArkusStart = threading.Thread(target=self.ArkusTime, args=())
        ArkusStart.start()

    def ArkusStopping(self):
        self.ArkusLabel.show()
        self.ArkusBar.show()
        self.ArkusLabelTimer.hide()
        self.ArkusStart.setEnabled(True)
        self.ArkusBar.setValue(int(Arkus[2]))
        MyGlobalsVars.aArkus = 0

    def ArkusTime(self):
        while MyGlobalsVars.aArkus > 0:
            m, s = divmod(MyGlobalsVars.aArkus, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.ArkusLabelTimer.setText(min_sec_format)
            if self.ArkusLabelTimer.text() == "05:00":
                ArkusNotify = win10toast.ToastNotifier()
                ArkusNotify.show_toast("Через 5 минут зареспавнится босс: ", Arkus[1])
                MyGlobalsVars.aArkus -= 3
            time.sleep(1)
            MyGlobalsVars.aArkus -= 1
        self.ArkusLabel.show()
        self.ArkusBar.show()
        self.ArkusLabelTimer.hide()
        self.ArkusStart.setEnabled(True)
        self.ArkusBar.setValue(int(Arkus[2]))
        MyGlobalsVars.aArkus = 0
        if self.ArkusLabelTimer.text() == "00:01":
            ArkusNotify = win10toast.ToastNotifier()
            ArkusNotify.show_toast("Зареспавнился босс: ", Arkus[1])

    def updateLabelArkus(self, value):
        self.ArkusLabel.setText("Текущее значение: " + str(value))
        Arkus[2] = str(value)

############################Satana#######################################

    def SatanaStarting(self):
        self.SatanaLabel.hide()
        self.SatanaBar.hide()
        self.SatanaLabelTimer.show()
        self.SatanaStart.setEnabled(False)
        MyGlobalsVars.aSatana = int(Satana[2]) * 60
        SatanaStart = threading.Thread(target=self.SatanaTime, args=())
        SatanaStart.start()

    def SatanaStopping(self):
        self.SatanaLabel.show()
        self.SatanaBar.show()
        self.SatanaLabelTimer.hide()
        self.SatanaStart.setEnabled(True)
        self.SatanaBar.setValue(int(Satana[2]))
        MyGlobalsVars.aSatana = 0

    def SatanaTime(self):
        while MyGlobalsVars.aSatana > 0:
            m, s = divmod(MyGlobalsVars.aSatana, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.SatanaLabelTimer.setText(min_sec_format)
            if self.SatanaLabelTimer.text() == "05:00":
                SatanaNotify = win10toast.ToastNotifier()
                SatanaNotify.show_toast("Через 5 минут зареспавнится босс: ", Satana[1])
                MyGlobalsVars.aSatana -= 3
            time.sleep(1)
            MyGlobalsVars.aSatana -= 1
        self.SatanaLabel.show()
        self.SatanaBar.show()
        self.SatanaLabelTimer.hide()
        self.SatanaStart.setEnabled(True)
        self.SatanaBar.setValue(int(Satana[2]))
        MyGlobalsVars.aSatana = 0
        if self.SatanaLabelTimer.text() == "00:01":
            SatanaNotify = win10toast.ToastNotifier()
            SatanaNotify.show_toast("Зареспавнился босс: ", Satana[1])

    def updateLabelSatana(self, value):
        self.SatanaLabel.setText("Текущее значение: " + str(value))
        Satana[2] = str(value)

############################Archangel#######################################

    def ArchangelStarting(self):
        self.ArchangelLabel.hide()
        self.ArchangelBar.hide()
        self.ArchangelLabelTimer.show()
        self.ArchangelStart.setEnabled(False)
        MyGlobalsVars.aArchangel = int(Archangel[2]) * 60
        ArchangelStart = threading.Thread(target=self.ArchangelTime, args=())
        ArchangelStart.start()

    def ArchangelStopping(self):
        self.ArchangelLabel.show()
        self.ArchangelBar.show()
        self.ArchangelLabelTimer.hide()
        self.ArchangelStart.setEnabled(True)
        self.ArchangelBar.setValue(int(Archangel[2]))
        MyGlobalsVars.aArchangel = 0

    def ArchangelTime(self):
        while MyGlobalsVars.aArchangel > 0:
            m, s = divmod(MyGlobalsVars.aArchangel, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.ArchangelLabelTimer.setText(min_sec_format)
            if self.ArchangelLabelTimer.text() == "05:00":
                ArchangelNotify = win10toast.ToastNotifier()
                ArchangelNotify.show_toast("Через 5 минут зареспавнится босс: ", Archangel[1])
                MyGlobalsVars.aArchangel -= 3
            time.sleep(1)
            MyGlobalsVars.aArchangel -= 1
        self.ArchangelLabel.show()
        self.ArchangelBar.show()
        self.ArchangelLabelTimer.hide()
        self.ArchangelStart.setEnabled(True)
        self.ArchangelBar.setValue(int(Archangel[2]))
        MyGlobalsVars.aArchangel = 0
        if self.ArchangelLabelTimer.text() == "00:01":
            ArchangelNotify = win10toast.ToastNotifier()
            ArchangelNotify.show_toast("Зареспавнился босс: ", Archangel[1])

    def updateLabelArchangel(self, value):
        self.ArchangelLabel.setText("Текущее значение: " + str(value))
        Archangel[2] = str(value)

############################King#######################################

    def KingStarting(self):
        self.KingLabel.hide()
        self.KingBar.hide()
        self.KingLabelTimer.show()
        self.KingStart.setEnabled(False)
        MyGlobalsVars.aKing = int(King[2]) * 60
        KingStart = threading.Thread(target=self.KingTime, args=())
        KingStart.start()

    def KingStopping(self):
        self.KingLabel.show()
        self.KingBar.show()
        self.KingLabelTimer.hide()
        self.KingStart.setEnabled(True)
        self.KingBar.setValue(int(King[2]))
        MyGlobalsVars.aKing = 0

    def KingTime(self):
        while MyGlobalsVars.aKing > 0:
            m, s = divmod(MyGlobalsVars.aKing, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.KingLabelTimer.setText(min_sec_format)
            if self.KingLabelTimer.text() == "05:00":
                KingNotify = win10toast.ToastNotifier()
                KingNotify.show_toast("Через 5 минут зареспавнится босс: ", King[1])
                MyGlobalsVars.aKing -= 3
            time.sleep(1)
            MyGlobalsVars.aKing -= 1
        self.KingLabel.show()
        self.KingBar.show()
        self.KingLabelTimer.hide()
        self.KingStart.setEnabled(True)
        self.KingBar.setValue(int(King[2]))
        MyGlobalsVars.aKing = 0
        if self.KingLabelTimer.text() == "00:01":
            KingNotify = win10toast.ToastNotifier()
            KingNotify.show_toast("Зареспавнился босс: ", King[1])

    def updateLabelKing(self, value):
        self.KingLabel.setText("Текущее значение: " + str(value))
        King[2] = str(value)


############################Zevs#######################################

    def ZevsStarting(self):
        self.ZevsLabel.hide()
        self.ZevsBar.hide()
        self.ZevsLabelTimer.show()
        self.ZevsStart.setEnabled(False)
        MyGlobalsVars.aZevs = int(Zevs[2]) * 60
        ZevsStart = threading.Thread(target=self.ZevsTime, args=())
        ZevsStart.start()

    def ZevsStopping(self):
        self.ZevsLabel.show()
        self.ZevsBar.show()
        self.ZevsLabelTimer.hide()
        self.ZevsStart.setEnabled(True)
        self.ZevsBar.setValue(int(Zevs[2]))
        MyGlobalsVars.aZevs = 0

    def ZevsTime(self):
        while MyGlobalsVars.aZevs > 0:
            m, s = divmod(MyGlobalsVars.aZevs, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.ZevsLabelTimer.setText(min_sec_format)
            if self.ZevsLabelTimer.text() == "05:00":
                ZevsNotify = win10toast.ToastNotifier()
                ZevsNotify.show_toast("Через 5 минут зареспавнится босс: ", Zevs[1])
                MyGlobalsVars.aZevs -= 3
            time.sleep(1)
            MyGlobalsVars.aZevs -= 1
        self.ZevsLabel.show()
        self.ZevsBar.show()
        self.ZevsLabelTimer.hide()
        self.ZevsStart.setEnabled(True)
        self.ZevsBar.setValue(int(Zevs[2]))
        MyGlobalsVars.aZevs = 0
        if self.ZevsLabelTimer.text() == "00:01":
            ZevsNotify = win10toast.ToastNotifier()
            ZevsNotify.show_toast("Зареспавнился босс: ", Zevs[1])

    def updateLabelZevs(self, value):
        self.ZevsLabel.setText("Текущее значение: " + str(value))
        Zevs[2] = str(value)

############################Guardian#######################################

    def GuardianStarting(self):
        self.GuardianLabel.hide()
        self.GuardianBar.hide()
        self.GuardianLabelTimer.show()
        self.GuardianStart.setEnabled(False)
        MyGlobalsVars.aGuardian = int(Guardian[2]) * 60
        GuardianStart = threading.Thread(target=self.GuardianTime, args=())
        GuardianStart.start()

    def GuardianStopping(self):
        self.GuardianLabel.show()
        self.GuardianBar.show()
        self.GuardianLabelTimer.hide()
        self.GuardianStart.setEnabled(True)
        self.GuardianBar.setValue(int(Guardian[2]))
        MyGlobalsVars.aGuardian = 0

    def GuardianTime(self):
        while MyGlobalsVars.aGuardian > 0:
            m, s = divmod(MyGlobalsVars.aGuardian, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            self.GuardianLabelTimer.setText(min_sec_format)
            if self.GuardianLabelTimer.text() == "05:00":
                GuardianNotify = win10toast.ToastNotifier()
                GuardianNotify.show_toast("Через 5 минут зареспавнится босс: ", Guardian[1])
                MyGlobalsVars.aGuardian -= 3
            time.sleep(1)
            MyGlobalsVars.aGuardian -= 1
        self.GuardianLabel.show()
        self.GuardianBar.show()
        self.GuardianLabelTimer.hide()
        self.GuardianStart.setEnabled(True)
        self.GuardianBar.setValue(int(Guardian[2]))
        MyGlobalsVars.aGuardian = 0
        if self.GuardianLabelTimer.text() == "00:01":
            GuardianNotify = win10toast.ToastNotifier()
            GuardianNotify.show_toast("Зареспавнился босс: ", Guardian[1])

    def updateLabelGuardian(self, value):
        self.GuardianLabel.setText("Текущее значение: " + str(value))
        Guardian[2] = str(value)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QDir, Qt, QUrl, QSize
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
import sys
from dialog import add_camera



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 531)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.original_mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)## first video
        self.original_mediaPlayer.setObjectName("original_frame")

        videoWidget_orginal_frame = QVideoWidget()

        self.original_mediaPlayer.setVideoOutput(videoWidget_orginal_frame)

        self.verticalLayout.addWidget(videoWidget_orginal_frame)# end of first video


        self.prediction_frame = QMediaPlayer(None, QMediaPlayer.VideoSurface)## second video
        self.prediction_frame.setObjectName("prediction_frame")

        videoWidget_predicted_frame = QVideoWidget()

        self.prediction_frame.setVideoOutput(videoWidget_predicted_frame)

        self.verticalLayout.addWidget(videoWidget_predicted_frame)

        self.verticalLayout.addWidget(videoWidget_predicted_frame)# end of second video

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.detection = QtWidgets.QPushButton(self.centralwidget)
        self.detection.setObjectName("detection")

        self.horizontalLayout.addWidget(self.detection)

        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setObjectName("stop")

        self.horizontalLayout.addWidget(self.stop)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.add_camera = QtWidgets.QPushButton(self.centralwidget)
        self.add_camera.setObjectName("add_camera")
        self.add_camera.clicked.connect(self.add_camera_window)

        self.verticalLayout_2.addWidget(self.add_camera)

        self.choose_camera = QtWidgets.QPushButton(self.centralwidget)
        self.choose_camera.setObjectName("choose_camera")

        self.verticalLayout_2.addWidget(self.choose_camera)

        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setObjectName("exit")
        self.exit.setShortcut('Ctrl+Q')
        self.exit.setStatusTip('Exit application')
        self.exit.clicked.connect(self.exitCall)

        self.verticalLayout_2.addWidget(self.exit)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Intelligence survailance system"))
        self.detection.setText(_translate("MainWindow", "Abnormal detection"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.add_camera.setText(_translate("MainWindow", "Add camera"))
        self.choose_camera.setText(_translate("MainWindow", "Choose \n"" camera"))
        self.exit.setText(_translate("MainWindow", "Exit"))

    def exitCall(self):
        sys.exit(app.exec_())

    def add_camera_window(self):
        #self.w = add_camera()
        #self.w.show()
        #print("heeeelelle")
        #self.MainWindow = QtWidgets.QMainWindow()
        #self.ui = add_camera()
        #self.ui.setupUi(self.MainWindow)
        #self.MainWindow.show()
        #self.MainWindow.close()

        self.Dialog = QtWidgets.QDialog()
        self.ui = add_camera()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.original_mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('/home/mohammad/Desktop/iraq.mp4')))
    ui.original_mediaPlayer.play()

    ui.prediction_frame.setMedia(QMediaContent(QUrl.fromLocalFile('/home/mohammad/Desktop/iraq.mp4')))
    ui.prediction_frame.play()

    sys.exit(app.exec_())

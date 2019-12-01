# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose_camera.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar)


class Ui_choose_camera(QWidget):
    def setupUi(self, choose_camera):
        choose_camera.setObjectName("choose_camera")
        choose_camera.resize(516, 165)
        self.verticalLayout = QtWidgets.QVBoxLayout(choose_camera)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(choose_camera)
        self.label.setMinimumSize(QtCore.QSize(245, 0))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(choose_camera)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.choose_video_path = QtWidgets.QPushButton(choose_camera)
        self.choose_video_path.clicked.connect(self.abrir)
        self.choose_video_path.setEnabled(True)
        self.choose_video_path.setObjectName("choose_video_path")
        self.horizontalLayout.addWidget(self.choose_video_path)
        self.video_path = QtWidgets.QLabel(choose_camera)
        self.video_path.setMaximumSize(QtCore.QSize(300, 21))
        self.video_path.setScaledContents(True)
        self.video_path.setAlignment(QtCore.Qt.AlignCenter)
        self.video_path.setObjectName("video_path")
        self.horizontalLayout.addWidget(self.video_path)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(choose_camera)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(choose_camera)
        self.buttonBox.accepted.connect(choose_camera.accept)
        self.buttonBox.rejected.connect(choose_camera.reject)
        QtCore.QMetaObject.connectSlotsByName(choose_camera)

    def retranslateUi(self, choose_camera):
        _translate = QtCore.QCoreApplication.translate
        choose_camera.setWindowTitle(_translate("choose_camera", "Choose camera"))
        self.label.setText(_translate("choose_camera", "CCTV IP address:"))
        self.lineEdit.setText(_translate("choose_camera", "e.g: rtsp://192.168.1.64/1"))
        self.choose_video_path.setText(_translate("choose_camera", "Choose video path"))
        self.video_path.setText(_translate("choose_camera", "Video path"))

    def abrir(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Selecciona los mediose",
                ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")

        if fileName != '':
            #self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            #self.playButton.setEnabled(True)
            self.video_path.setText(fileName)
            #self.play()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    choose_camera = QtWidgets.QDialog()
    ui = Ui_choose_camera()
    ui.setupUi(choose_camera)
    choose_camera.show()
    sys.exit(app.exec_())

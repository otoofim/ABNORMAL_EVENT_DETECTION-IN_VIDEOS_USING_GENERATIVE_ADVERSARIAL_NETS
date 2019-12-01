# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar)


class Ui_add_camera(QWidget):
    def setupUi(self, add_camera):
        add_camera.setObjectName("add_camera")
        add_camera.resize(574, 432)
        self.verticalLayout = QtWidgets.QVBoxLayout(add_camera)
        self.verticalLayout.setObjectName("verticalLayout")
        self.description = QtWidgets.QTextEdit(add_camera)
        self.description.setEnabled(True)
        self.description.setReadOnly(True)
        self.description.setObjectName("description")
        self.verticalLayout.addWidget(self.description)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.choose_video_path = QtWidgets.QPushButton(add_camera)
        self.choose_video_path.clicked.connect(self.abrir)
        self.choose_video_path.setEnabled(True)
        self.choose_video_path.setObjectName("choose_video_path")
        self.horizontalLayout.addWidget(self.choose_video_path)
        self.video_path = QtWidgets.QLabel(add_camera)

        self.video_path.setMaximumSize(QtCore.QSize(300, 21))
        self.video_path.setScaledContents(True)
        self.video_path.setAlignment(QtCore.Qt.AlignCenter)
        self.video_path.setObjectName("video_path")
        self.horizontalLayout.addWidget(self.video_path)
        self.choose_video_btn = QtWidgets.QPushButton(add_camera)
        self.choose_video_btn.setObjectName("choose_video_btn")
        self.horizontalLayout.addWidget(self.choose_video_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(add_camera)
        self.label.setMinimumSize(QtCore.QSize(181, 27))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.camera_ip_txt_edit = QtWidgets.QLineEdit(add_camera)
        self.camera_ip_txt_edit.setMinimumSize(QtCore.QSize(100, 21))
        self.camera_ip_txt_edit.setAcceptDrops(False)
        self.camera_ip_txt_edit.setMaxLength(32753)
        self.camera_ip_txt_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_ip_txt_edit.setObjectName("camera_ip_txt_edit")
        self.horizontalLayout_2.addWidget(self.camera_ip_txt_edit)

        self.choose_camera_btn = QtWidgets.QPushButton(add_camera)
        #self.choose_camera_btn.clicked.connect(self.abrir)
        self.choose_camera_btn.setMinimumSize(QtCore.QSize(181, 27))
        #self.choose_camera_btn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.choose_camera_btn.setObjectName("choose_camera_btn")
        self.horizontalLayout_2.addWidget(self.choose_camera_btn)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.close_btn = QtWidgets.QDialogButtonBox(add_camera)
        self.close_btn.setOrientation(QtCore.Qt.Horizontal)
        self.close_btn.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.close_btn.setCenterButtons(True)
        self.close_btn.setObjectName("close_btn")
        self.verticalLayout.addWidget(self.close_btn)

        self.retranslateUi(add_camera)
        self.close_btn.accepted.connect(add_camera.accept)
        self.close_btn.rejected.connect(add_camera.reject)
        QtCore.QMetaObject.connectSlotsByName(add_camera)

    def retranslateUi(self, add_camera):
        _translate = QtCore.QCoreApplication.translate
        add_camera.setWindowTitle(_translate("add_camera", "Add camera"))
        self.description.setHtml(_translate("add_camera", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Instruction:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">There are two ways to import a video. First, if you have a video file you can specify the address in the file inspector below. Second, if you have access to the given CCTV IP address, you can determine the address in the IP section. Either way you intend to select to indicate a video file, the following steps is going to be taken:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Choose the given video/camera</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. If you specified a path to a video, at least it should contain enough frames for training</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. Having specified a new camera/video, the training process would begin</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. You can close &quot;Add camera&quot; window but terminal</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5. The process of learning might take up to a few days. It depends on the num of frames provided.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6. </p></body></html>"))
        self.choose_video_path.setText(_translate("add_camera", "Choose video path"))
        self.video_path.setText(_translate("add_camera", "Video path"))
        self.choose_video_btn.setText(_translate("add_camera", "Process"))
        self.label.setText(_translate("add_camera", "CCTV IP address:"))
        self.camera_ip_txt_edit.setText(_translate("add_camera", "e.g: rtsp://192.168.1.64/1"))
        self.choose_camera_btn.setText(_translate("add_camera", "Process"))

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
    add_camera = QtWidgets.QDialog()
    ui = Ui_add_camera()
    ui.setupUi(add_camera)
    add_camera.show()
    sys.exit(app.exec_())

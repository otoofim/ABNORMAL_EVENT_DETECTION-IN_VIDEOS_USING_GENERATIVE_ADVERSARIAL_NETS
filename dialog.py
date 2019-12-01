# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class add_camera(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(574, 432)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")

        self.description = QtWidgets.QTextEdit(Dialog)
        self.description.setEnabled(True)
        self.description.setReadOnly(True)
        self.description.setObjectName("description")
        self.verticalLayout.addWidget(self.description)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.choose_video_path = QtWidgets.QPushButton(Dialog)
        self.choose_video_path.setEnabled(True)
        self.choose_video_path.setObjectName("choose_video_path")
        self.horizontalLayout.addWidget(self.choose_video_path)

        self.video_path = QtWidgets.QLabel(Dialog)
        self.video_path.setMaximumSize(QtCore.QSize(300, 21))
        self.video_path.setScaledContents(True)
        self.video_path.setAlignment(QtCore.Qt.AlignCenter)
        self.video_path.setObjectName("video_path")
        self.horizontalLayout.addWidget(self.video_path)

        self.choose_video_btn = QtWidgets.QPushButton(Dialog)
        self.choose_video_btn.setObjectName("choose_video_btn")
        self.horizontalLayout.addWidget(self.choose_video_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)

        self.camera_path = QtWidgets.QLabel(Dialog)
        self.camera_path.setMaximumSize(QtCore.QSize(181, 27))
        self.camera_path.setScaledContents(True)
        self.camera_path.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.camera_path.setObjectName("camera_path")
        self.horizontalLayout_2.addWidget(self.camera_path)

        self.choose_camera_btn = QtWidgets.QPushButton(Dialog)
        self.choose_camera_btn.setObjectName("choose_camera_btn")
        self.horizontalLayout_2.addWidget(self.choose_camera_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.close_btn = QtWidgets.QDialogButtonBox(Dialog)
        self.close_btn.setOrientation(QtCore.Qt.Horizontal)
        self.close_btn.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.close_btn.setCenterButtons(True)
        self.close_btn.setObjectName("close_btn")
        self.verticalLayout.addWidget(self.close_btn)

        self.retranslateUi(Dialog)
        self.close_btn.accepted.connect(Dialog.accept)
        self.close_btn.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.description.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.choose_video_path.setText(_translate("Dialog", "Choose video path"))
        self.video_path.setText(_translate("Dialog", "Video path"))
        self.choose_video_btn.setText(_translate("Dialog", "Process"))
        self.label.setText(_translate("Dialog", "CCTV IP address:"))
        self.camera_path.setText(_translate("Dialog", "e.g: rtsp://192.168.1.64/1"))
        self.choose_camera_btn.setText(_translate("Dialog", "Process"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = add_camera()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

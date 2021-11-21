from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AlexaUI(object):
    def setupUi(self, AlexaUI):
        AlexaUI.setObjectName("AlexaUI")
        AlexaUI.resize(988, 732)
        self.centralwidget = QtWidgets.QWidget(AlexaUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 1011, 741))
        self.label.setText("SRNoori")
        self.label.setPixmap(QtGui.QPixmap("4.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(900, 670, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(18, 143, 135);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(900, 700, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(18, 143, 135);\n"
"background-color: rgb(145, 0, 2);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -30, 431, 241))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("2.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(500, 20, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(80)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("BACKGROUND:TRANSPARENT;\n"
"border-radius:none;\n"
"color:maroon;\n"
"font-size:20;\n")
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(740, 20, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(80)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("BACKGROUND:TRANSPARENT;\n"
"border-radius:none;\n"
"color:maroon;\n"
"font-size:20;\n")
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 600, 221, 121))
        self.label_3.setText("Shahid")
        self.label_3.setPixmap(QtGui.QPixmap("1.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        AlexaUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(AlexaUI)
        QtCore.QMetaObject.connectSlotsByName(AlexaUI)

    def retranslateUi(self, AlexaUI):
        _translate = QtCore.QCoreApplication.translate
        AlexaUI.setWindowTitle(_translate("AlexaUI", "Alexa~SRNoori"))
        self.pushButton.setText(_translate("AlexaUI", "Start"))
        self.pushButton_2.setText(_translate("AlexaUI", "Exit"))
        self.textBrowser.setHtml(_translate("AlexaUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Myanmar Text\'; font-size:16pt; font-weight:600; font-style:italic;\">\n"
"<p align=\"right\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("AlexaUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Myanmar Text\'; font-size:16pt; font-weight:600; font-style:italic;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AlexaUI = QtWidgets.QMainWindow()
    ui = Ui_AlexaUI()
    ui.setupUi(AlexaUI)
    AlexaUI.show()
    sys.exit(app.exec_())

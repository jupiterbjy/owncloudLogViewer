# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oc_logReader.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 500)
        MainWindow.setAcceptDrops(True)
        MainWindow.setToolTipDuration(-1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.oc_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.oc_listWidget.setGeometry(QtCore.QRect(10, 10, 621, 361))
        self.oc_listWidget.setAcceptDrops(True)
        self.oc_listWidget.setAutoFillBackground(False)
        self.oc_listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.oc_listWidget.setAlternatingRowColors(True)
        self.oc_listWidget.setSelectionRectVisible(True)
        self.oc_listWidget.setObjectName("oc_listWidget")
        self.Debug_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.Debug_textEdit.setGeometry(QtCore.QRect(10, 380, 541, 81))
        self.Debug_textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Debug_textEdit.setReadOnly(True)
        self.Debug_textEdit.setObjectName("Debug_textEdit")
        self.File_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.File_PushButton.setGeometry(QtCore.QRect(560, 380, 71, 23))
        self.File_PushButton.setObjectName("File_PushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Owncloud Log Viewer - Testing"))
        self.File_PushButton.setText(_translate("MainWindow", "File"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

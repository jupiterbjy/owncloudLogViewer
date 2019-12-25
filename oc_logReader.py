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
        MainWindow.resize(809, 500)
        MainWindow.setAcceptDrops(True)
        MainWindow.setToolTipDuration(-1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.oc_treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.oc_treeWidget.setGeometry(QtCore.QRect(10, 10, 791, 261))
        self.oc_treeWidget.setAcceptDrops(True)
        self.oc_treeWidget.setAutoFillBackground(False)
        self.oc_treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.oc_treeWidget.setAlternatingRowColors(True)
        self.oc_treeWidget.setAnimated(False)
        self.oc_treeWidget.setAllColumnsShowFocus(False)
        self.oc_treeWidget.setHeaderHidden(False)
        self.oc_treeWidget.setExpandsOnDoubleClick(True)
        self.oc_treeWidget.setObjectName("oc_treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.oc_treeWidget)
        self.item_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.item_textBrowser.setGeometry(QtCore.QRect(10, 280, 791, 181))
        self.item_textBrowser.setObjectName("item_textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionFile = QtWidgets.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")
        self.menuMenu.addAction(self.actionFile)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Owncloud Log Viewer - Testing"))
        self.oc_treeWidget.setSortingEnabled(True)
        self.oc_treeWidget.headerItem().setText(0, _translate("MainWindow", "Entry"))
        self.oc_treeWidget.headerItem().setText(1, _translate("MainWindow", "Time"))
        self.oc_treeWidget.headerItem().setText(2, _translate("MainWindow", "Level"))
        self.oc_treeWidget.headerItem().setText(3, _translate("MainWindow", "IPv4"))
        self.oc_treeWidget.headerItem().setText(4, _translate("MainWindow", "User"))
        self.oc_treeWidget.headerItem().setText(5, _translate("MainWindow", "App"))
        self.oc_treeWidget.headerItem().setText(6, _translate("MainWindow", "Method"))
        self.oc_treeWidget.headerItem().setText(7, _translate("MainWindow", "Message"))
        __sortingEnabled = self.oc_treeWidget.isSortingEnabled()
        self.oc_treeWidget.setSortingEnabled(False)
        self.oc_treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "1"))
        self.oc_treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "2"))
        self.oc_treeWidget.topLevelItem(0).setText(2, _translate("MainWindow", "3"))
        self.oc_treeWidget.topLevelItem(0).setText(3, _translate("MainWindow", "4"))
        self.oc_treeWidget.topLevelItem(0).setText(4, _translate("MainWindow", "5"))
        self.oc_treeWidget.topLevelItem(0).setText(5, _translate("MainWindow", "6"))
        self.oc_treeWidget.topLevelItem(0).setText(6, _translate("MainWindow", "7"))
        self.oc_treeWidget.topLevelItem(0).setText(7, _translate("MainWindow", "8"))
        self.oc_treeWidget.setSortingEnabled(__sortingEnabled)
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionFile.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

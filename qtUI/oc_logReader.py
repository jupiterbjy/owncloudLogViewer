# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'oc_logReader.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(812, 556)
        MainWindow.setAcceptDrops(True)
        MainWindow.setToolTipDuration(-1)
        self.actionFile = QAction(MainWindow)
        self.actionFile.setObjectName(u"actionFile")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSyntex_Highlighting = QAction(MainWindow)
        self.actionSyntex_Highlighting.setObjectName(u"actionSyntex_Highlighting")
        self.actionSyntex_Highlighting.setCheckable(True)
        self.actionSyntex_Highlighting.setChecked(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.oc_treeWidget = QTreeWidget(self.splitter)
        self.oc_treeWidget.setObjectName(u"oc_treeWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.oc_treeWidget.sizePolicy().hasHeightForWidth())
        self.oc_treeWidget.setSizePolicy(sizePolicy)
        self.oc_treeWidget.setAcceptDrops(True)
        self.oc_treeWidget.setAutoFillBackground(False)
        self.oc_treeWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.oc_treeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.oc_treeWidget.setDragEnabled(False)
        self.oc_treeWidget.setAlternatingRowColors(True)
        self.oc_treeWidget.setSortingEnabled(True)
        self.oc_treeWidget.setAnimated(False)
        self.oc_treeWidget.setAllColumnsShowFocus(False)
        self.oc_treeWidget.setHeaderHidden(False)
        self.oc_treeWidget.setExpandsOnDoubleClick(True)
        self.splitter.addWidget(self.oc_treeWidget)
        self.oc_treeWidget.header().setCascadingSectionResizes(True)
        self.midSectionframe = QFrame(self.splitter)
        self.midSectionframe.setObjectName(u"midSectionframe")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.midSectionframe.sizePolicy().hasHeightForWidth())
        self.midSectionframe.setSizePolicy(sizePolicy1)
        self.midSectionframe.setMinimumSize(QSize(0, 25))
        self.midSectionframe.setMaximumSize(QSize(16777215, 25))
        self.midSectionframe.setAutoFillBackground(False)
        self.midSectionframe.setFrameShape(QFrame.NoFrame)
        self.midSectionframe.setFrameShadow(QFrame.Plain)
        self.midSectionframe.setLineWidth(1)
        self.lvl_textEdit = QTextEdit(self.midSectionframe)
        self.lvl_textEdit.setObjectName(u"lvl_textEdit")
        self.lvl_textEdit.setGeometry(QRect(40, 2, 31, 21))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.lvl_textEdit.sizePolicy().hasHeightForWidth())
        self.lvl_textEdit.setSizePolicy(sizePolicy2)
        self.lvl_textEdit.setMaximumSize(QSize(16777215, 24))
        self.lvl_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lvl_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lvl_textEdit.setReadOnly(True)
        self.level_label = QLabel(self.midSectionframe)
        self.level_label.setObjectName(u"level_label")
        self.level_label.setGeometry(QRect(4, 2, 41, 21))
        self.entry_label = QLabel(self.midSectionframe)
        self.entry_label.setObjectName(u"entry_label")
        self.entry_label.setGeometry(QRect(90, 2, 41, 21))
        self.entry_textEdit = QTextEdit(self.midSectionframe)
        self.entry_textEdit.setObjectName(u"entry_textEdit")
        self.entry_textEdit.setGeometry(QRect(130, 2, 121, 21))
        sizePolicy2.setHeightForWidth(self.entry_textEdit.sizePolicy().hasHeightForWidth())
        self.entry_textEdit.setSizePolicy(sizePolicy2)
        self.entry_textEdit.setMaximumSize(QSize(16777215, 24))
        self.entry_textEdit.setFrameShape(QFrame.StyledPanel)
        self.entry_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.entry_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.entry_textEdit.setReadOnly(True)
        self.dateTimeEdit = QDateTimeEdit(self.midSectionframe)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(310, 2, 141, 21))
        self.dateTimeEdit.setWrapping(False)
        self.dateTimeEdit.setFrame(True)
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setAccelerated(False)
        self.dateTimeEdit.setKeyboardTracking(False)
        self.time_label = QLabel(self.midSectionframe)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setGeometry(QRect(270, 0, 41, 21))
        self.raw_checkBox = QCheckBox(self.midSectionframe)
        self.raw_checkBox.setObjectName(u"raw_checkBox")
        self.raw_checkBox.setGeometry(QRect(470, 2, 51, 21))
        self.splitter.addWidget(self.midSectionframe)
        self.item_textEdit = QTextEdit(self.splitter)
        self.item_textEdit.setObjectName(u"item_textEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.item_textEdit.sizePolicy().hasHeightForWidth())
        self.item_textEdit.setSizePolicy(sizePolicy3)
        self.item_textEdit.setFrameShadow(QFrame.Sunken)
        self.item_textEdit.setLineWidth(1)
        self.item_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.item_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.item_textEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.item_textEdit.setReadOnly(True)
        self.splitter.addWidget(self.item_textEdit)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 812, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setStyleSheet(u"border-top-color: rgb(49, 49, 49);\n"
"gridline-color: rgb(17, 17, 17);\n"
"border-style: outset;")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionFile)
        self.menuMenu.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Owncloud Log Viewer - Testing Builds", None))
        self.actionFile.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSyntex_Highlighting.setText(QCoreApplication.translate("MainWindow", u"Syn. Highlight", None))
        ___qtreewidgetitem = self.oc_treeWidget.headerItem()
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Message", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Method", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"App", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"User", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"IPv4", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Level", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Entry", None));
#if QT_CONFIG(whatsthis)
        self.midSectionframe.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.level_label.setText(QCoreApplication.translate("MainWindow", u"Level", None))
        self.entry_label.setText(QCoreApplication.translate("MainWindow", u"Entry", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.raw_checkBox.setText(QCoreApplication.translate("MainWindow", u"Raw", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi


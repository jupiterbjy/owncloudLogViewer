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
        MainWindow.resize(812, 642)
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
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.oc_treeWidget = QTreeWidget(self.centralwidget)
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
        self.oc_treeWidget.header().setCascadingSectionResizes(True)

        self.verticalLayout.addWidget(self.oc_treeWidget)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalFrame_2 = QFrame(self.centralwidget)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setMinimumSize(QSize(565, 23))
        self.horizontalFrame_2.setMaximumSize(QSize(565, 23))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.level_label = QLabel(self.horizontalFrame_2)
        self.level_label.setObjectName(u"level_label")
        self.level_label.setMinimumSize(QSize(0, 21))

        self.horizontalLayout_3.addWidget(self.level_label)

        self.lvl_textEdit = QTextEdit(self.horizontalFrame_2)
        self.lvl_textEdit.setObjectName(u"lvl_textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.lvl_textEdit.sizePolicy().hasHeightForWidth())
        self.lvl_textEdit.setSizePolicy(sizePolicy1)
        self.lvl_textEdit.setMinimumSize(QSize(0, 21))
        self.lvl_textEdit.setMaximumSize(QSize(30, 24))
        self.lvl_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lvl_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lvl_textEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lvl_textEdit)

        self.entry_label = QLabel(self.horizontalFrame_2)
        self.entry_label.setObjectName(u"entry_label")
        self.entry_label.setMinimumSize(QSize(0, 21))

        self.horizontalLayout_3.addWidget(self.entry_label)

        self.entry_textEdit = QTextEdit(self.horizontalFrame_2)
        self.entry_textEdit.setObjectName(u"entry_textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.entry_textEdit.sizePolicy().hasHeightForWidth())
        self.entry_textEdit.setSizePolicy(sizePolicy2)
        self.entry_textEdit.setMinimumSize(QSize(0, 21))
        self.entry_textEdit.setMaximumSize(QSize(16777215, 24))
        self.entry_textEdit.setFrameShape(QFrame.StyledPanel)
        self.entry_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.entry_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.entry_textEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.entry_textEdit)

        self.time_label = QLabel(self.horizontalFrame_2)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setMinimumSize(QSize(0, 21))

        self.horizontalLayout_3.addWidget(self.time_label)

        self.dateTimeEdit = QDateTimeEdit(self.horizontalFrame_2)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setMinimumSize(QSize(0, 21))
        self.dateTimeEdit.setWrapping(False)
        self.dateTimeEdit.setFrame(True)
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setAccelerated(False)
        self.dateTimeEdit.setKeyboardTracking(False)

        self.horizontalLayout_3.addWidget(self.dateTimeEdit)

        self.raw_checkBox = QCheckBox(self.horizontalFrame_2)
        self.raw_checkBox.setObjectName(u"raw_checkBox")
        self.raw_checkBox.setMinimumSize(QSize(0, 21))

        self.horizontalLayout_3.addWidget(self.raw_checkBox)


        self.horizontalLayout_5.addWidget(self.horizontalFrame_2)

        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(221, 26))
        self.horizontalFrame.setMaximumSize(QSize(221, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.previousButton = QPushButton(self.horizontalFrame)
        self.previousButton.setObjectName(u"previousButton")
        self.previousButton.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_2.addWidget(self.previousButton)

        self.pageLine = QTextEdit(self.horizontalFrame)
        self.pageLine.setObjectName(u"pageLine")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(2)
        sizePolicy3.setHeightForWidth(self.pageLine.sizePolicy().hasHeightForWidth())
        self.pageLine.setSizePolicy(sizePolicy3)
        self.pageLine.setMaximumSize(QSize(75, 24))
        self.pageLine.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pageLine.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pageLine.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.pageLine)

        self.nextButton = QPushButton(self.horizontalFrame)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_2.addWidget(self.nextButton)


        self.horizontalLayout_5.addWidget(self.horizontalFrame)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.item_textEdit = QTextEdit(self.centralwidget)
        self.item_textEdit.setObjectName(u"item_textEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.item_textEdit.sizePolicy().hasHeightForWidth())
        self.item_textEdit.setSizePolicy(sizePolicy4)
        self.item_textEdit.setFrameShadow(QFrame.Sunken)
        self.item_textEdit.setLineWidth(1)
        self.item_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.item_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.item_textEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.item_textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.item_textEdit)

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
        self.level_label.setText(QCoreApplication.translate("MainWindow", u"Level", None))
        self.entry_label.setText(QCoreApplication.translate("MainWindow", u"     Entry", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"     Time", None))
        self.raw_checkBox.setText(QCoreApplication.translate("MainWindow", u"Raw", None))
        self.previousButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi


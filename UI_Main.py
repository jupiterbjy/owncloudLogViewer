import sys
import re
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from oc_logReader import Ui_MainWindow
import fileReader
import OneFilePathDetector as OneFile

# --- References --------------------------------------------------------
# https://github.com/RavenKyu/OpenTutorials_PyQt/
# https://blog.asimation.com/37/
# https://stackoverflow.com/questions/14691525/set-column-width-for-qtreewidget

# TODO: find way to apply conditional formatting on columns
# TODO: find location of core dump in goormIDE
# TODO: create exception in case wrong file was thrown into program.


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Setting Coloum width
        header = self.oc_treeWidget.header()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(False)
        header.setSectionResizeMode(7, QHeaderView.Stretch)
        
        self.oc_treeWidget.sortItems(0, Qt.AscendingOrder)
        self.actionFile.triggered.connect(self.fileButtonClicked)
        self.oc_treeWidget.currentItemChanged.connect(self.treeItemClicked)
        self.oc_treeWidget.itemClicked.connect(self.treeItemClicked)

    def writeConsole(self, text, mode=1):
        if mode:
            self.item_textBrowser.append(str(text))
        else:
            self.item_textBrowser.setPlainText(str(text))
        
    def items(self, itemList):
        self.item = QTreeWidgetItem()
        
        for idx, i in enumerate(itemList):
            self.item.setText(idx, i)
            
        return self.item

    def fileButtonClicked(self):
        f = QFileDialog.getOpenFileName(self)
        self.writeConsole(f[0])
        
        if f[0] != '':
            out = fileReader.lineProcess(f[0])
        
            for i in out:
                item = self.items(i)
                self.oc_treeWidget.invisibleRootItem().addChild(item)
                
    def treeItemClicked(self):
        currentItem = self.oc_treeWidget.selectedItems()
        for item in currentItem:
            txt = re.sub('/n#', '\n#', item.text(7))
            self.writeConsole(txt, mode=0)


def main():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    OneFile.DetectFrozen()
    main()

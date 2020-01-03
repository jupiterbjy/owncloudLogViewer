import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from oc_logReader import Ui_MainWindow
from formatTools import *
import fileReader
import OneFilePathDetector as OneFile

# --- References --------------------------------------------------------
# https://slays.tistory.com/42 <- check this later on day-off
# https://stackoverflow.com/questions/24287111/changing-a-single-strings-color-within-a-qtextedit
# https://github.com/RavenKyu/OpenTutorials_PyQt/
# https://blog.asimation.com/37/
# https://stackoverflow.com/questions/14691525/set-column-width-for-qtreewidget
# https://regexr.com/

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
        self.actionSyntex_Highlighting.toggled.connect(self.highlightToggle)
        self.oc_treeWidget.currentItemChanged.connect(self.treeItemClicked)
        self.oc_treeWidget.itemClicked.connect(self.treeItemClicked)

    def writeConsole(self, text, clear=False):
        if clear:
            self.item_textEdit.setText(str(text))
        else:
            self.item_textEdit.append(str(text))
        
    def fileButtonClicked(self):
        def items(itemList):
            item = QTreeWidgetItem()

            for idx, i in enumerate(itemList):
                item.setText(idx, i)

            return item
        
        f = QFileDialog.getOpenFileName(self)
        self.writeConsole(f[0])
        
        if f[0] != '':
            try:
                out = fileReader.lineProcess(f[0])
            
            except Exception as exp:
                self.writeConsole(exp)
                self.writeConsole(ErrorOut('\nFile Open Failed!\n'))
                self.oc_treeWidget.invisibleRootItem().takeChildren()
            
            else:
                for i in out:
                    item = items(i)
                    self.oc_treeWidget.invisibleRootItem().addChild(item)
                
    def treeItemClicked(self):
        
        currentItem = self.oc_treeWidget.selectedItems()
        
        # only have one item but can't call by index 0. using iteration
        for item in currentItem:
            lvl = lvlColorizer(item.text(2))
            time = item.text(1)
            entry = item.text(0) + ' / ' + str(fileReader.lineCounts)
            
            self.lvl_textEdit.setText(lvl)
            self.entry_textEdit.setText(entry)
            self.msgUpdate(item.text(7))
            
    def msgUpdate(self, msg):
        highlight = self.actionSyntex_Highlighting.isChecked()
        self.writeConsole(messageFormating(msg, highlight), clear=True)
            
    def highlightToggle(self):
        
        currentItem = self.oc_treeWidget.selectedItems()
        for item in currentItem:
            self.msgUpdate(item.text(7))


def main():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    OneFile.DetectFrozen()
    main()

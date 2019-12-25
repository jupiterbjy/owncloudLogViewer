import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from oc_logReader import Ui_MainWindow
import fileReader

# https://github.com/RavenKyu/OpenTutorials_PyQt/
# https://blog.asimation.com/37/

# TODO: find way to apply conditional formatting on columns


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.actionFile.triggered.connect(self.fileButtonClicked)

    def writeConsole(self, text):
        self.item_textBrowser.append(str(text))
        
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


def main():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

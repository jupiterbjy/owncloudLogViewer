import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from oc_logReader import Ui_MainWindow
import fileReader

# https://github.com/RavenKyu/OpenTutorials_PyQt/

class item_Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        pb = QPushButton("Hello")
        layout.addWidget(pb)
        layout.setSizeConstraint(QBoxLayout.SetFixedSize)
        self.setLayout(layout)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.File_PushButton.clicked.connect(self.fileButtonClicked)
        
        item = QListWidgetItem(self.oc_listWidget)
        customItem = item_Form()
        item.setSizeHint(customItem.sizeHint())
        self.oc_listWidget.setItemWidget(item, customItem)
        self.oc_listWidget.addItem(item)
        
    
    def writeConsole(self, text):
        self.Debug_textEdit.append(str(text))
        
    def fileButtonClicked(self):
        f = QFileDialog.getOpenFileName(self)
        self.writeConsole(f[0])
        fileReader
        
def main():
    
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
    
if __name__ == '__main__':
    main()
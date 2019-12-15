import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

from oc_logReader import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.File_PushButton.clicked.connect(self.fileButtonClicked)
    
    def writeConsole(self, text):
        self.Debug_textEdit.append(str(text))
        
    def fileButtonClicked(self):
        f = QFileDialog.getOpenFileName(self)
        
def main():
    
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
    
if __name__ == '__main__':
    main()
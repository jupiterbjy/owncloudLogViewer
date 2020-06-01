import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt

from qtUI.oc_logReader import Ui_MainWindow
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

# TODO: create 'better' exception in case wrong file was thrown into program.
# TODO: create python script to grep all TODO in source codes.
# TODO: subitem by y-m-d => h-m-s order


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Setting Column width
        header = self.oc_treeWidget.header()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(False)
        header.setSectionResizeMode(7, QHeaderView.Stretch)

        self.oc_treeWidget.sortItems(0, Qt.AscendingOrder)

        self.actionFile.triggered.connect(self.fileButtonClicked)
        self.oc_treeWidget.currentItemChanged.connect(self.treeItemClicked)
        self.oc_treeWidget.itemClicked.connect(self.treeItemClicked)
        self.raw_checkBox.toggled.connect(self.highLightToggle)
        self.actionExit.triggered.connect(sys.exit)

        self.statusbar.showMessage("Idle")
        self.fileLineCount = 0

    def writeConsole(self, text, clear=False):
        if clear:
            self.item_textEdit.setText(str(text))
        else:
            self.item_textEdit.append(str(text))

    def writeToUI(self, text):  # abstraction
        self.writeConsole(text)

    @staticmethod
    def fileHandler(file_name):
        try:
            with open(file_name, 'rt'):
                pass
        except IOError:
            return False
        else:
            return True

    def fileToTree(self, file_name):
        def items(lists):
            item_ = QTreeWidgetItem()

            for idx_, i_ in enumerate(lists):
                try:
                    item_.setText(idx_, str(i_))
                except ValueError:
                    item_.setText(idx_, i_[::20])  # it's too long, so str.
                # this str-to-everyone might cause overhead.
                # maybe I need to only apply str to lineProcess's few form items.

            return item_

        self.statusbar.showMessage(f"File {file_name} loaded")

        for form in fileReader.lineProcess_new(file_name):
            item = items(form)
            self.oc_treeWidget.invisibleRootItem().addChild(item)

    def fileButtonClicked(self):
        f = QFileDialog.getOpenFileName()
        if self.fileHandler(f[0]):
            self.fileToTree(f[0])

    def msgUpdate(self, msg):
        if self.raw_checkBox.isChecked():
            self.item_textEdit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
            self.writeConsole(msg, clear=True)
        else:
            self.item_textEdit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
            self.writeConsole(messageFormating(msg), clear=True)

    def treeItemClicked(self):

        current_item = self.oc_treeWidget.selectedItems()

        # only have one item but can't call by index 0. using iteration
        for item in current_item:

            self.statusbar.showMessage(f"Showing row {item.text(0)}")

            lvl = lvlColorizer(item.text(2))
            # time = item.text(1)
            entry = item.text(0) + " / " + str(fileReader.total)

            self.lvl_textEdit.setText(lvl)
            self.entry_textEdit.setText(entry)
            self.msgUpdate(item.text(7))

            self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
            tmp = self.dateTimeEdit.dateTimeFromText(item.text(1))
            self.dateTimeEdit.setDateTime(tmp)

    def highLightToggle(self):

        current_item = self.oc_treeWidget.selectedItems()
        for item in current_item:
            self.msgUpdate(item.text(7))


def main():

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    OneFile.DetectFrozen()
    main()

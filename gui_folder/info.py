from class_folder.DEFINE import *
from gui_folder.gui_duplicate_info import Ui_Form


class Info(QWidget, Ui_Form):
    def __init__(self):
        super(Info, self).__init__()
        self.setupUi(self)
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(DEF_VERSION)
        self.plainTextEdit.appendPlainText(DEF_DATE_EDIT)

    def closeEvent(self, event):
        pass

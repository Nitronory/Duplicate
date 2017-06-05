from class_folder.DEFINE import *
from class_folder.MySignal import MySignal
from gui_folder.gui_duplicate_setting import Ui_Settings


class Setting(QWidget, Ui_Settings):
    def __init__(self):
        super(Setting, self).__init__()
        self.setupUi(self)
        self.signal = MySignal()

    def closeEvent(self, event):
        self.take_data()

    def select_folder(self):
        self.directory = QFileDialog.getExistingDirectory(self, "Seleziona cartella", expanduser("~"),
                                                     QFileDialog.ShowDirsOnly)
        if isdir(self.directory):
            self.le_folder.setText(self.directory)

    def set_default(self, list_p):
        self.le_folder.setText(list_p[DEF_path_dest])
        if list_p[DEF_tollerance]:
            self.cb_tolerance.setChecked(1)
            self.sb_tolerance.setEnabled(1)
            self.sb_tolerance.setValue(list_p[DEF_tollerance])
        else:
            self.cb_tolerance.setChecked(0)
            self.sb_tolerance.setEnabled(0)

        if list_p[DEF_checksum_active]:
            self.cb_checksum.setChecked(1)
            self.button_crc.setEnabled(1)
            self.button_sha256.setEnabled(1)
            if list_p[DEF_checksum_type] == "crc" or list_p[DEF_checksum_type] is None:
                self.button_crc.setChecked(1)
                self.button_sha256.setChecked(0)
            if list_p[DEF_checksum_type] == "sha256":
                self.button_crc.setChecked(0)
                self.button_sha256.setChecked(1)
        else:
            self.cb_checksum.setChecked(0)
            self.button_sha256.setEnabled(0)
            self.button_crc.setEnabled(0)

    def take_data(self):
        t_act = True if self.cb_tolerance.isChecked() else False
        t_num = self.sb_tolerance.value() if t_act else 0
        same_csc_act = True if self.cb_checksum.isChecked() else False
        same_csc_value = "crc" if self.button_crc.isChecked() else "sha256"
        folder = self.le_folder.text()
        to_keep = self.cb_toKeep.currentText()
        self.signal.sig_list.emit([None, folder, t_act, t_num, None, same_csc_act, same_csc_value, to_keep])

    def cb_enable_tollerance(self):
        if not self.cb_tolerance.isChecked():
            self.sb_tolerance.setEnabled(0)
        else:
            self.sb_tolerance.setEnabled(1)

    def cb_enable_checksum(self):
        if not self.cb_checksum.isChecked():
            self.button_crc.setEnabled(0)
            self.button_sha256.setEnabled(0)
        else:
            self.button_crc.setEnabled(1)
            self.button_sha256.setEnabled(1)

            self.button_crc.setChecked(0)
            self.button_sha256.setChecked(1)

    def btn_crc(self):
        self.set_crc()

    def btn_sha256(self):
        self.set_sha256()

    def set_sha256(self):
        self.button_crc.setChecked(0)
        self.button_sha256.setChecked(1)

    def set_crc(self):
        self.button_crc.setChecked(1)
        self.button_sha256.setChecked(0)
from class_folder.DEFINE import *
from class_folder.run_program import find_duplicate
from gui_folder import gui_duplicate as gui
from gui_folder.info import Info
from gui_folder.settings import Setting


class MainDialog(QMainWindow, gui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.obj = None
        self.data_list = []
        self.deafaut_scan_setting()
        self.setting = Setting()
        self.gui_info = Info()
        self.setting.set_default(self.data_list)
        self.apply_setting_to_gui()
        self.setting.signal.sig_list.connect(self.get_data_from_setting)

    def deafaut_scan_setting(self):
        move_folder = join(expanduser("~"), "Documents")
        same_name_act = True
        tolerance_act = True
        tolerance_num = 5
        same_csc_act  = False
        same_csc_type = None
        what_to_keep = "The Newer"
        self.data_list = [None, move_folder, tolerance_act, tolerance_num, same_name_act, same_csc_act, same_csc_type, what_to_keep]

    def clear_gui(self):
        self.le_nfile.clear()
        self.le_nfolder.clear()
        self.le_sameCrc.clear()
        self.le_sizeName.clear()
        self.plainTextEdit.clear()

    def apply_setting_to_gui(self):
        if self.data_list[DEF_samename]:
            self.actionSame_Name.setChecked(1)
        else:
            self.actionSame_Name.setChecked(0)

        if self.data_list[DEF_checksum_active]:
            self.actionSame_CSC.setChecked(1)
        else:
            self.actionSame_CSC.setChecked(0)

    def get_data_from_setting(self, list_p):
        self.data_list[DEF_path_dest] = list_p[DEF_path_dest]
        self.data_list[DEF_tollerance_active] = list_p[DEF_tollerance_active]
        self.data_list[DEF_tollerance] = list_p[DEF_tollerance]
        self.data_list[DEF_checksum_active] = list_p[DEF_checksum_active]
        self.data_list[DEF_checksum_type] = list_p[DEF_checksum_type]
        self.data_list[DEF_what_to_keep] = list_p[DEF_what_to_keep]
        self.apply_setting_to_gui()

    def func_show_info(self):
        self.gui_info.show()

    def func_show_settings(self):
        self.setting.set_default(self.data_list)
        self.setting.show()

    def func_move_files(self):
        self.obj.move()

    def func_load_scan(self):
        pass

    def func_save_scan(self):

        def zipdir(path, ziph):
            print(path)
            for root, dirs, files in os.walk(path):
                for file in files:
                    ziph.write(os.path.join(root, file))

        if self.obj is not None:
            folder_name = "SCAN" + str(self.obj.get_folder())[9:] + ".zip"
            fileName = QFileDialog.getSaveFileName(self, "Save Scan", folder_name, filter="txt (*.zip *.)")[0]
            zipf = zipfile.ZipFile(fileName, 'w', zipfile.ZIP_DEFLATED)
            zipdir(self.obj.get_folder(), zipf)

    def func_list_remove_folder(self):
        for item in self.listWidget.selectedItems():
            self.listWidget.takeItem(self.listWidget.row(item))

    def func_list_clear(self):
        self.listWidget.clear()

    def func_list_add_folder(self):
        directory = QFileDialog.getExistingDirectory(self, "Seleziona cartella", expanduser("~"),
                                                     QFileDialog.ShowDirsOnly)
        if isdir(directory):
            self.listWidget.addItem(directory)

    def func_same_name(self):
        if self.actionSame_Name.isChecked():
            self.data_list[DEF_samename] = True
        else:
            self.data_list[DEF_samename] = False

    def func_same_csc(self):
        if self.actionSame_CSC.isChecked():
            self.data_list[DEF_checksum_active] = True
            self.data_list[DEF_checksum_type] = "crc"
        else:
            self.data_list[DEF_checksum_active] = False
            self.data_list[DEF_checksum_type] = None

    def list_of_folders(self):
        items = []
        for index in range(self.listWidget.count()):
            items.append(self.listWidget.item(index))
        labels = [i.text() for i in items]
        return labels

    def RunProgram(self):
        self.clear_gui()
        paths_to_scan = []
        for path in self.list_of_folders():
            paths_to_scan.append(path)

        self.data_list[DEF_paths_to_scan] = paths_to_scan

        if len(self.data_list[DEF_paths_to_scan]) > 0:
            self.obj = find_duplicate(self.data_list)
            self.obj.signal.sig.connect(self.stampa)
            self.obj.start()

    def stampa(self, text):
        if "PHASE" in text:
            self.plainTextEdit.appendPlainText(text.split(":")[1])

        if "REPORT" in text:
            self.plainTextEdit.appendPlainText(text)

        if "REPORT" in text and "CRC" in text:
            i = text.find(".txt")
            self.le_sameCrc.setText(text[i+9:])

        if "REPORT" in text and "NAME" in text:
            i = text.find(".txt")
            self.le_sizeName.setText(text[i+9:])

        if "ANALIZE" in text:
            self.plainTextEdit.appendPlainText(text[11:])

        if "FOLDERFILE" in text:
            numbs = text[11:]
            folder = numbs.split(";")[0]
            file = numbs.split(";")[1]
            self.le_nfile.setText(str(folder))
            self.le_nfolder.setText(str(file))

        if "NONLOG:" in text:
            if "PROGRESSBAR" in text:
                perc = int(text[7:].split(":")[1])
                self.progressBar.setValue(perc)


def main():
    app = QApplication(sys.argv)
    f = MainDialog()
    f.show()
    app.exec_()


if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './list_gui/duplicate_setting.ui'
#
# Created: Wed May 31 16:48:14 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(600, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        Settings.setMinimumSize(QtCore.QSize(600, 400))
        Settings.setMaximumSize(QtCore.QSize(600, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings.setWindowIcon(icon)
        self.tabWidget = QtGui.QTabWidget(Settings)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 581, 371))
        self.tabWidget.setObjectName("tabWidget")
        self.duplicates = QtGui.QWidget()
        self.duplicates.setObjectName("duplicates")
        self.duplicates_description = QtGui.QPlainTextEdit(self.duplicates)
        self.duplicates_description.setEnabled(True)
        self.duplicates_description.setGeometry(QtCore.QRect(87, 48, 431, 211))
        self.duplicates_description.setFrameShape(QtGui.QFrame.NoFrame)
        self.duplicates_description.setFrameShadow(QtGui.QFrame.Raised)
        self.duplicates_description.setObjectName("duplicates_description")
        self.duplicates_icon = QtGui.QLabel(self.duplicates)
        self.duplicates_icon.setGeometry(QtCore.QRect(27, 50, 41, 41))
        self.duplicates_icon.setText("")
        self.duplicates_icon.setPixmap(QtGui.QPixmap("img/duplicates.png"))
        self.duplicates_icon.setScaledContents(True)
        self.duplicates_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.duplicates_icon.setWordWrap(False)
        self.duplicates_icon.setObjectName("duplicates_icon")
        self.duplicates_title = QtGui.QLabel(self.duplicates)
        self.duplicates_title.setGeometry(QtCore.QRect(27, 20, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.duplicates_title.setFont(font)
        self.duplicates_title.setObjectName("duplicates_title")
        self.cb_toKeep = QtGui.QComboBox(self.duplicates)
        self.cb_toKeep.setGeometry(QtCore.QRect(220, 270, 161, 22))
        self.cb_toKeep.setObjectName("cb_toKeep")
        self.cb_toKeep.addItem("")
        self.cb_toKeep.addItem("")
        self.cb_toKeep.addItem("")
        self.cb_toKeep.addItem("")
        self.cb_toKeep.addItem("")
        self.cb_toKeep.addItem("")
        self.duplicate_label = QtGui.QLabel(self.duplicates)
        self.duplicate_label.setGeometry(QtCore.QRect(120, 270, 61, 16))
        self.duplicate_label.setObjectName("duplicate_label")
        self.tabWidget.addTab(self.duplicates, "")
        self.same_name = QtGui.QWidget()
        self.same_name.setObjectName("same_name")
        self.tolerance_icon = QtGui.QLabel(self.same_name)
        self.tolerance_icon.setGeometry(QtCore.QRect(27, 50, 41, 41))
        self.tolerance_icon.setText("")
        self.tolerance_icon.setPixmap(QtGui.QPixmap("img/tollerance.png"))
        self.tolerance_icon.setScaledContents(True)
        self.tolerance_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.tolerance_icon.setWordWrap(False)
        self.tolerance_icon.setObjectName("tolerance_icon")
        self.tolerance_description = QtGui.QPlainTextEdit(self.same_name)
        self.tolerance_description.setEnabled(True)
        self.tolerance_description.setGeometry(QtCore.QRect(87, 48, 431, 191))
        self.tolerance_description.setFrameShape(QtGui.QFrame.NoFrame)
        self.tolerance_description.setFrameShadow(QtGui.QFrame.Raised)
        self.tolerance_description.setObjectName("tolerance_description")
        self.tolerance_title = QtGui.QLabel(self.same_name)
        self.tolerance_title.setGeometry(QtCore.QRect(27, 20, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.tolerance_title.setFont(font)
        self.tolerance_title.setObjectName("tolerance_title")
        self.cb_tolerance = QtGui.QCheckBox(self.same_name)
        self.cb_tolerance.setGeometry(QtCore.QRect(170, 250, 71, 31))
        self.cb_tolerance.setIconSize(QtCore.QSize(30, 30))
        self.cb_tolerance.setChecked(True)
        self.cb_tolerance.setObjectName("cb_tolerance")
        self.sb_tolerance = QtGui.QSpinBox(self.same_name)
        self.sb_tolerance.setGeometry(QtCore.QRect(257, 254, 51, 22))
        self.sb_tolerance.setMinimum(1)
        self.sb_tolerance.setMaximum(100)
        self.sb_tolerance.setProperty("value", 5)
        self.sb_tolerance.setObjectName("sb_tolerance")
        self.tabWidget.addTab(self.same_name, "")
        self.same_checksum = QtGui.QWidget()
        self.same_checksum.setObjectName("same_checksum")
        self.csc_description = QtGui.QPlainTextEdit(self.same_checksum)
        self.csc_description.setEnabled(True)
        self.csc_description.setGeometry(QtCore.QRect(87, 48, 391, 131))
        self.csc_description.setFrameShape(QtGui.QFrame.NoFrame)
        self.csc_description.setFrameShadow(QtGui.QFrame.Raised)
        self.csc_description.setObjectName("csc_description")
        self.csc_title = QtGui.QLabel(self.same_checksum)
        self.csc_title.setGeometry(QtCore.QRect(27, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.csc_title.setFont(font)
        self.csc_title.setObjectName("csc_title")
        self.csc_icon = QtGui.QLabel(self.same_checksum)
        self.csc_icon.setGeometry(QtCore.QRect(27, 50, 51, 51))
        self.csc_icon.setText("")
        self.csc_icon.setPixmap(QtGui.QPixmap("img/checksum.png"))
        self.csc_icon.setScaledContents(True)
        self.csc_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.csc_icon.setWordWrap(False)
        self.csc_icon.setObjectName("csc_icon")
        self.cb_checksum = QtGui.QCheckBox(self.same_checksum)
        self.cb_checksum.setGeometry(QtCore.QRect(150, 210, 71, 31))
        self.cb_checksum.setIconSize(QtCore.QSize(30, 30))
        self.cb_checksum.setChecked(True)
        self.cb_checksum.setObjectName("cb_checksum")
        self.button_crc = QtGui.QPushButton(self.same_checksum)
        self.button_crc.setGeometry(QtCore.QRect(230, 200, 61, 51))
        self.button_crc.setCheckable(True)
        self.button_crc.setObjectName("button_crc")
        self.button_sha256 = QtGui.QPushButton(self.same_checksum)
        self.button_sha256.setGeometry(QtCore.QRect(300, 200, 61, 51))
        self.button_sha256.setCheckable(True)
        self.button_sha256.setChecked(True)
        self.button_sha256.setObjectName("button_sha256")
        self.tabWidget.addTab(self.same_checksum, "")
        self.move_files = QtGui.QWidget()
        self.move_files.setObjectName("move_files")
        self.mov_description = QtGui.QPlainTextEdit(self.move_files)
        self.mov_description.setEnabled(True)
        self.mov_description.setGeometry(QtCore.QRect(87, 48, 391, 131))
        self.mov_description.setFrameShape(QtGui.QFrame.NoFrame)
        self.mov_description.setFrameShadow(QtGui.QFrame.Raised)
        self.mov_description.setObjectName("mov_description")
        self.mov_icon = QtGui.QLabel(self.move_files)
        self.mov_icon.setGeometry(QtCore.QRect(27, 50, 51, 51))
        self.mov_icon.setText("")
        self.mov_icon.setPixmap(QtGui.QPixmap("img/load.png"))
        self.mov_icon.setScaledContents(True)
        self.mov_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.mov_icon.setWordWrap(False)
        self.mov_icon.setObjectName("mov_icon")
        self.mov_title = QtGui.QLabel(self.move_files)
        self.mov_title.setGeometry(QtCore.QRect(27, 19, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.mov_title.setFont(font)
        self.mov_title.setObjectName("mov_title")
        self.button_selectfolder = QtGui.QPushButton(self.move_files)
        self.button_selectfolder.setGeometry(QtCore.QRect(40, 198, 31, 23))
        self.button_selectfolder.setObjectName("button_selectfolder")
        self.le_folder = QtGui.QLineEdit(self.move_files)
        self.le_folder.setGeometry(QtCore.QRect(80, 200, 401, 20))
        self.le_folder.setReadOnly(True)
        self.le_folder.setObjectName("le_folder")
        self.tabWidget.addTab(self.move_files, "")

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QObject.connect(self.cb_checksum, QtCore.SIGNAL("clicked(bool)"), Settings.cb_enable_checksum)
        QtCore.QObject.connect(self.button_crc, QtCore.SIGNAL("clicked()"), Settings.btn_crc)
        QtCore.QObject.connect(self.button_sha256, QtCore.SIGNAL("clicked()"), Settings.btn_sha256)
        QtCore.QObject.connect(self.button_selectfolder, QtCore.SIGNAL("clicked()"), Settings.select_folder)
        QtCore.QObject.connect(self.cb_tolerance, QtCore.SIGNAL("clicked(bool)"), Settings.cb_enable_tollerance)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QtGui.QApplication.translate("Settings", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.duplicates_description.setPlainText(QtGui.QApplication.translate("Settings", "Duplicates are file with the same name or with the same checksum\n"
"finded in the folder selected.\n"
"\n"
"What file you want to keep when one or more duplicates are found ?\n"
"   the Newer : keep the file with the most recent data of creation\n"
"   the Older   : keep the file with the most older data of creation\n"
"   \n"
"   the file with longer path : longer path from folder selected to file.\n"
"   the file with shoreter path : shorter path from folder selected to file.\n"
"\n"
"   the smaller file : the file with small size\n"
"   the bigger file  : the file with greater size\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.duplicates_title.setText(QtGui.QApplication.translate("Settings", "Duplicates", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_toKeep.setItemText(0, QtGui.QApplication.translate("Settings", "The Newer", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_toKeep.setItemText(1, QtGui.QApplication.translate("Settings", "The Older", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_toKeep.setItemText(2, QtGui.QApplication.translate("Settings", "With Smaller Size", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_toKeep.setItemText(3, QtGui.QApplication.translate("Settings", "With Biggest Size", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_toKeep.setItemText(4, QtGui.QApplication.translate("Settings", "With Longer Path", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_toKeep.setItemText(5, QtGui.QApplication.translate("Settings", "With Shorter Path", None, QtGui.QApplication.UnicodeUTF8))
        self.duplicate_label.setText(QtGui.QApplication.translate("Settings", "File to keep", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.duplicates), QtGui.QApplication.translate("Settings", "Duplicates", None, QtGui.QApplication.UnicodeUTF8))
        self.tolerance_description.setPlainText(QtGui.QApplication.translate("Settings", "Duplicates are file with the same name or with the same checksum\n"
"finded in the folder selected.\n"
"\n"
"What file you want to keep when one or more duplicates are found ?\n"
"   the Newer : keep the file with the most recent data of creation\n"
"   the Older   : keep the file with the most older data of creation\n"
"   \n"
"   the file with longer path : longer path from folder selected to file.\n"
"   the file with shoreter path : shorter path from folder selected to file.\n"
"\n"
"   the smaller file : the file with small size\n"
"   the bigger file  : the file with greater size\n"
"\n"
"     ", None, QtGui.QApplication.UnicodeUTF8))
        self.tolerance_title.setText(QtGui.QApplication.translate("Settings", "Duplicates", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_tolerance.setText(QtGui.QApplication.translate("Settings", "Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.sb_tolerance.setSuffix(QtGui.QApplication.translate("Settings", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.same_name), QtGui.QApplication.translate("Settings", "Same Name", None, QtGui.QApplication.UnicodeUTF8))
        self.csc_description.setPlainText(QtGui.QApplication.translate("Settings", "The checksum method consists of applying the same algoritm to each file readed in binary.\n"
"The result will be an identifying string for the file,\n"
" if you find the result twice you have found a 100% duplicate file.\n"
"\n"
"This method have more accuracy, in order to find duplicate files, but is slower,\n"
"because each file has to be read.", None, QtGui.QApplication.UnicodeUTF8))
        self.csc_title.setText(QtGui.QApplication.translate("Settings", "CheckSum", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_checksum.setText(QtGui.QApplication.translate("Settings", "Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.button_crc.setText(QtGui.QApplication.translate("Settings", "CRC", None, QtGui.QApplication.UnicodeUTF8))
        self.button_sha256.setText(QtGui.QApplication.translate("Settings", "SHA256", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.same_checksum), QtGui.QApplication.translate("Settings", "Same Checksum", None, QtGui.QApplication.UnicodeUTF8))
        self.mov_description.setPlainText(QtGui.QApplication.translate("Settings", "After the scan, many files will be found ( we hope not it is was )\n"
"Move all Duplicate files into a folder, to check it later, to delete all, or for what else...\n"
"\n"
"You can choose to move your files after the scan, or just read the report.", None, QtGui.QApplication.UnicodeUTF8))
        self.mov_title.setText(QtGui.QApplication.translate("Settings", "Moving Duplicate", None, QtGui.QApplication.UnicodeUTF8))
        self.button_selectfolder.setText(QtGui.QApplication.translate("Settings", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.move_files), QtGui.QApplication.translate("Settings", "Move Files", None, QtGui.QApplication.UnicodeUTF8))


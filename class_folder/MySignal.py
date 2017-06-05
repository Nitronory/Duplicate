from class_folder.DEFINE import *

class MySignal(QObject):
    sig = Signal(str)
    sig_list = Signal(list)
    n_file = Signal(int)
    n_folder = Signal(int)

from class_folder.DEFINE import *
from class_folder.Logger import Logger
from class_folder.MySignal import MySignal
from class_folder.move import MoveFiles
from class_folder.phases import phase1_analize_folder, phase2_populate, phase3_result, phase4_report


class find_duplicate(QThread):

    def __init__(self, data, parent=None):
        QThread.__init__(self, parent)

        self.signal = MySignal()
        self.signal.sig.emit("start")
        self.folder = self.create_folder()
        self.log = self.create_log()

        self.crc = data[DEF_checksum_active]
        self.checksum_type = data[DEF_checksum_type]
        self.paths = data[DEF_paths_to_scan]
        self.tollerance = None
        if data[DEF_tollerance_active]:
            self.tollerance = data[DEF_tollerance]

        self.choose_to_keep = data[DEF_what_to_keep]
        self.path_to_move = data[DEF_path_dest]

    def create_folder(self):
        folder = "TEMP " + str(datetime.datetime.now())[0:19].replace(":", ".")
        folder = join("SCAN", folder)
        makedirs(folder)
        return folder

    def create_log(self):
        file_log = join(self.folder, "Report.txt")
        log = Logger(file_log, self.signal )
        return log

    def get_folder(self):
        return self.folder

    def run(self):
        start = datetime.datetime.now()
        self.log.write_log("Program start @ " + str(start))
        self.log.write_log("Create folder " + str(self.folder))
        self.signal.sig.emit("NONLOG:PHASE:PHASE 1/4")
        phase1_analize_folder(self.paths, self.log, self.folder)
        self.signal.sig.emit("NONLOG:PHASE:PHASE 2/4")
        phase2_populate(self.log, self.folder, self.crc, self.checksum_type)
        self.signal.sig.emit("NONLOG:PHASE:PHASE 3/4")
        phase3_result(self.log, self.folder, self.crc, self.tollerance)
        self.signal.sig.emit("NONLOG:PHASE:PHASE 4/4")
        phase4_report(self.log, self.folder)
        end = datetime.datetime.now()
        self.log.write_log("Program end @ " + str(end))

    def move(self):
        MoveFiles(self.log, self.signal, self.folder, self.choose_to_keep, self.path_to_move)

class find_duplicate_from_Saved_file(QThread):
    pass


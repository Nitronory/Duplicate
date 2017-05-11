
from os.path import isdir, isfile, join, getsize, normpath, getmtime, basename
from os import listdir, mkdir
from binascii import crc32
from hashlib import sha256
from classLog import Logger
from classFindDuplicateList import find_duplicate_in_list
import sys
import datetime


class Analize:
    def __init__(self, paths, crc = False):
        self.gran_folder = "TEMP " + str(datetime.datetime.now())[0:20].replace(":", ".")
        mkdir(self.gran_folder)

        report_file = "REPORT.txt"
        path_report_file = join(self.gran_folder, report_file)

        self.log = Logger(path_report_file)
        self.crc = crc
        for path in paths:
            if not isdir(path):
                self.log.write_log("The path to analize is invalid")
                exit(1)

    def run_program(self):
        start = datetime.datetime.now()
        self.log.write_log("Program start @ " + str(start))
        self.log.write_log("Create folder " + str(self.gran_folder))
        self.read_folder()
        self.phase_populate()
        same_name, same_crc = self.phase_analisys()
        self.final_phase(same_crc, same_name)
        end = datetime.datetime.now()
        self.log.write_log("Program end @ " + str(end))
        self.log.write_log("Findend " + str(len(same_name)) + " files with same name")
        if self.crc:
            self.log.write_log("Findend " + str(len(same_crc)) + " files with same crc")
        self.log.write_log("Time elapsed " + str(end-start))

    # -----------------------  #   PHASE READ FOLDER   #  -----------------------  #

    def read_folder(self):
        for path in paths:
            self.log.write_log("read folder " + str(path))
            tmp_list = []
            n_folder, nfile = self.count_file_in_folder(path, tmp_list, 0, 0)
            self.log.write_log("Read folder : " + str(path))
            self.log.write_log("Analized " + str(n_folder) + " folders and " + str(nfile) + " files")
            self.create_tmp_file(path, tmp_list)

    def create_tmp_file(self, path, tmp_list):
        file = "tmp_" + str(path).replace("\\","_").replace(":","") + ".csv"
        path_to_file = join(self.gran_folder, file)
        f = open(path_to_file, "w")
        for element in tmp_list:
            line = element + "\n"
            try:
                f.write(line)
                f.flush()
            except:
                self.log.write_log("Error on this Line " + str(line.replace("\n","")))
        f.close()

    def count_file_in_folder(self, path_passed, tmp_list, i_folder, i_file):
        listed_dir = listdir(path_passed)
        for item in listed_dir:
            item_path = join(path_passed, item)
            if isdir(item_path):
                i_folder += 1
                try:
                    r_folder, r_file = self.count_file_in_folder(item_path, tmp_list, i_folder, i_file)
                    i_file = r_file
                    i_folder = r_folder
                except:
                    self.log.write_log("can't access to the folder : %s " % item_path)
            if isfile(item_path):
                if ".ini" not in item_path:
                    tmp_list.append(item_path)
                    i_file += 1
        return i_folder, i_file

    # -----------------------  #   PHASE POPULATE   #  -----------------------  #

    def phase_populate(self):
        list_temp = listdir(self.gran_folder)
        for file in list_temp:
            self.populate_list_file(file)

    def populate_list_file(self, file_passed):
        name_file = "result_" + file_passed[4:]
        file_result = join(self.gran_folder, name_file)
        f = open(file_result, "w")
        progress = 1

        total = self.count_row(file_passed)

        list_files = []

        if total > 0:
            f3 = open(join(self.gran_folder,file_passed),"r")
            lines = f3.readlines()
            for line in lines:
                file = line.strip("\n")
                if isfile(file):
                    self.printProgressBar(progress, total)
                    ent1 = normpath(file)                          # Path Normalized
                    ent2 = basename(file)                          # File name without Path
                    ent3 = self.calc_algorithm(file) if self.crc else 0     # CRC 0 if skipped
                    ent4 = getsize(file)                           # File Size
                    ent5 = getmtime(file)                          # Time creation / last edit

                    line = str(ent1) + ";" + str(ent2) + ";" + str(ent3) + ";" + str(ent4) + ";" + str(ent5) + ";\n"
                    list_files.append([ent1, ent2, ent3, ent4, ent5])
                    try:
                        f.write(line)
                        f.flush()
                    except:
                        self.log.write_log("Error on this line " + str(line))
                    progress += 1
        f.close()

        return list_files

    def printProgressBar(self, iteration, total, prefix='', suffix='', decimals=1, bar_length=100):
        str_format = "{0:." + str(decimals) + "f}"
        percents = str_format.format(100 * (iteration / float(total)))
        filled_length = int(round(bar_length * iteration / float(total)))
        bar = '█' * filled_length + '-' * (bar_length - filled_length)

        sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
        sys.stdout.flush()

        if iteration == total:
            sys.stdout.write('\n')

    def count_row(self, file):
        with open(join(self.gran_folder,file)) as f:
            return len(f.readlines())

    def calc_algorithm(self, file):
        # return self.calc_crc32(file)
        return self.calc_sha1(file)

    def calc_sha1(self, filename):
        buf = open(filename, 'rb').read()
        hash_object = sha256(buf)
        hex_dig = hash_object.hexdigest()
        return hex_dig

    def calc_crc32(self, filename):
        try:
            buf = open(filename, 'rb').read()
            buf = (crc32(buf) & 0xFFFFFFFF)
            return "%08X" % buf
        except:
            return 0

    #  -----------------------  #   PHASE ANALISYS   #  -----------------------  #

    def phase_analisys(self):
        list_result = self.read_file_result(self.gran_folder)
        same_crc = None
        if self.crc:
            same_crc = self.analize_duplicate_files_same_crc(list_result)
        same_name = self.analize_duplicate_files_same_name(list_result)
        return same_name, same_crc

    def phase_analisys_from_folder(self, folder):
        list_result = self.read_file_result(folder)
        #self.analize_duplicate_files_same_name(list_result)
        self.analize_duplicate_files_same_crc(list_result)

    def read_list_from_file(self, folder, list, file):
        f = open(join(folder, file))
        lines = f.readlines()
        for line in lines:
            list.append(line.replace("\n",""))

    def read_file_result(self, folder):
        big_list = []
        list_result = listdir(folder)
        for file in list_result:
            if file.startswith("result_"):
                self.read_list_from_file(folder, big_list, file)
        return big_list

    def analize_duplicate_files_same_name(self, list_passed):
        tot_to_analize = len(list_passed)
        progress = 0

        from classFindDuplicateList import find_duplicate_in_list
        x = find_duplicate_in_list(list_passed,1)
        return x.get_list()

    def analize_duplicate_files_same_crc(self, list_passed):
        tot_to_analize = len(list_passed)
        progress = 0


        x = find_duplicate_in_list(list_passed,2)
        return x.get_list()

    #  -----------------------  #   PHASE FINAL   #  -----------------------  #

    def final_phase(self, same_crc, same_name):
        if self.crc:
            self.log_same_crc(same_crc)
        self.log_same_name(same_name)

    def log_same_crc(self, dict_passed):
        file = "SAME_CRC.txt"
        path_to_file = join(self.gran_folder, file)
        f = open(path_to_file, "w")

        for k, v in dict_passed.items():
            line = k + " ,"
            for item in v:
                line += "[" + item + "]"
            line += "\n"
            f.write(line)
            f.flush()

    def log_same_name(self, dict_passed):
        file = "SAME_NAME.txt"
        path_to_file = join(self.gran_folder, file)
        f = open(path_to_file, "w")

        for k, v in dict_passed.items():
            line = k + " ,"
            for item in v:
                line += "[" + item + "]"
            line += "\n"
            f.write(line)
            f.flush()


#paths = ["\\\\Mac\\Home\\Desktop\\babbo","\\\\Mac\\Home\\Desktop\\babbo - Copy"]
paths = ["\\\\nas\\Disco1\\marco_files\\Cloud"]
#paths = ["\\\\nas\\Ricordi\\zzRicordi con Data\\2016"]
x = Analize(paths)
x.run_program()
#x.phase_analisys_from_folder("TEMP 2017-05-10 18.08.11")
#x.phase_analisys_from_folder("TEMP 2017-05-10 22.09.32")


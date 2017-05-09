
from os.path import isdir, isfile, join, getsize, normpath, getmtime, splitext, basename, dirname
from os import listdir, mkdir
from binascii import crc32
import sys

import time, datetime

class Analize():
    def __init__(self, paths):

        self.lista_same_crc = []
        self.lista_same_name = []

        for path in paths:
            if not isdir(path):
                print("The path passed is not valid")
                exit(1)
        self.run_program()

    def run_program(self):
        start = datetime.datetime.now()
        self.gran_folder = "TEMP " + str(datetime.datetime.now())[0:20].replace(":",".")
        mkdir(self.gran_folder)
        for path in paths:
            tmp_list = []
            n_folder, nfile = self.count_file_in_folder(path, tmp_list, 0, 0)
            print(path, n_folder,nfile)
            self.create_tmp_file(path, tmp_list)
        self.phase_populate()
        self.phase_analisys()
        self.create_file()
        '''
        stop = datetime.datetime.now()
        delta = stop - start
        print("%d file founded with same name " % len(self.lista_same_name))
        print("%d file founded with same crc " % len(self.lista_same_crc))
        print("Time elapsed : " + str(delta))
        '''

    def phase_analisys(self):
        big_list = []
        list_temp = listdir(self.gran_folder)
        for file in list_temp:
            if file.startswith("result_"):
                self.read_list_from_file(big_list, file)
        self.analize_duplicate_files(big_list)

    def read_list_from_file(self, list, file):
        f = open(join(self.gran_folder, file))
        lines = f.readlines()
        for line in lines:
            list.append(line)

    def create_tmp_file(self, path, tmp_list):
        file = "tmp_" + str(path).replace("\\","_").replace(":","") + ".csv"
        path_to_file = join(self.gran_folder, file)
        f = open(path_to_file, "w")
        for element in tmp_list:
            line = element + "\n"
            f.write(line)
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
                    print("can't access to the folder : %s " % item_path)
            if isfile(item_path):
                tmp_list.append(item_path)
                i_file += 1

                line = item_path + ";\n"
        return i_folder, i_file

    def phase_populate(self):
        list_temp = listdir(self.gran_folder)
        for file in list_temp:
            self.populate_list_file(file, crc=True)

    def count_row(self, file):
        with open(join(self.gran_folder,file)) as f:
            return len(f.readlines())

    def populate_list_file(self, file_passed, crc=False):

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
                    ent3 = self.calc_crc32(file) if crc else 0     # CRC 0 if skipped
                    ent4 = getsize(file)                           # File Size
                    ent5 = getmtime(file)                          # Time creation / last edit

                    line = str(ent1) + ";" + str(ent2) + ";" + str(ent3) + ";" + str(ent4) + ";" + str(ent5) + ";\n"
                    list_files.append([ent1, ent2, ent3, ent4, ent5])
                    f.write(line)
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

    def log_same_crc(self, item):
        self.lista_same_crc.append(item)

    def log_name_crc(self, item):
        self.lista_same_name.append(item)

    def analize_duplicate_files(self, list_passed):
        for item_1 in list_passed:
            for item_2 in list_passed:
                if item_1[1] == item_2[1] and item_1[0] != item_2[0]:
                    if item_1[2] == item_2[2]:
                        self.log_same_crc([item_1[0], item_2[0]])
                    else:
                        self.log_name_crc([item_1[0], item_2[0]])

    def create_file(self):
        name = "Same_CRC.txt"
        file_name = join(self.gran_folder,name)
        f1 = open(file_name,"w")
        for el in self.lista_same_crc:
            line = el[0] + " " + el[1] + "\n"
            f1.write(line)
        f1.close()

        name = "Same_Name.txt"
        file_name = join(self.gran_folder, name)

        f2 = open(file_name,"w")
        for el in self.lista_same_name:
            line = el[0] + " " + el[1] + "\n"
            f2.write(line)
        f2.close()

    def calc_crc32(self, filename):
        try:
            buf = open(filename, 'rb').read()
            buf = (crc32(buf) & 0xFFFFFFFF)
            return "%08X" % buf
        except:
            return 0


paths = ["C:\\Users\MBiondi_Ext\Desktop\YY", "C:\\Users\MBiondi_Ext\Desktop\\fatto - Copia"]
x = Analize(paths)


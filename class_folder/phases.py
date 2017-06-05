from class_folder.DEFINE import *
from class_folder.file_obj import file_obj

class phase1_analize_folder:
    def __init__(self, paths, logger, folder):
        self.gran_folder = folder
        self.log = logger
        for path in paths:
            if not isdir(path):
                self.log.write_log("The path to analize is invalid")
                exit(1)
        self.read_folder(paths)

    def read_folder(self, paths):
        for path in paths:
            self.log.write_log("read folder " + str(path))
            tmp_list = []
            n_folder, n_file = self.read_folder_count_file_in_folder(path, tmp_list, 0, 0)
            self.log.write_log("FOLDERFILE:" + str(n_folder) + ";" + str(n_file))
            self.log.write_log("Read folder : " + str(path))
            self.log.write_log("Analized " + str(n_folder) + " folders and " + str(n_file) + " files")
            self.read_folder_create_tmp_file(path, tmp_list)

    def read_folder_create_tmp_file(self, path, tmp_list):
        file = "tmp_" + str(path).replace("\\", "_").replace("/", "_").replace(":", "") + ".csv"
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

    def read_folder_count_file_in_folder(self, path_passed, tmp_list, i_folder, i_file):
        listed_dir = listdir(path_passed)
        for item in listed_dir:
            item_path = join(path_passed, item)
            if isdir(item_path):
                #self.log.write_log("ANALIZE___:" + str(item_path))
                i_folder += 1
                try:
                    r_folder, r_file = self.read_folder_count_file_in_folder(item_path, tmp_list, i_folder, i_file)
                    i_file = r_file
                    i_folder = r_folder
                except:
                    self.log.write_log("can't access to the folder : %s " % item_path)
            if isfile(item_path):
                if ".ini" not in item_path:
                    # self.log.write_log("ANALIZE:"+str(item_path))
                    tmp_list.append(item_path)
                    i_file += 1
        return i_folder, i_file


class phase2_populate:
    def __init__(self, log, folder, crc=None, checksum_type=None):
        self.gran_folder = folder
        self.crc = crc
        self.checksum_type = checksum_type
        self.log = log
        if self.crc:
            self.log.write_log("Scan to find double file with name and crc")
        else:
            self.log.write_log("Scan to find double file with name")

        self.phase_populate()

    # -----------------------  #   PHASE POPULATE   #  -----------------------  #

    def phase_populate(self):
        list_temp = listdir(self.gran_folder)
        for file in list_temp:
            if "tmp_" in file:
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
                    actual_file = file_obj(normpath(file))
                    if self.checksum_type:
                        actual_file.calc_checksum(self.checksum_type)
                    self.printProgressBar(progress, total)
                    list_files.append(actual_file)
                    try:
                        f.write(actual_file.line_to_print()+"\n")
                        f.flush()
                    except:
                        self.log.write_log("Error on this line " + str(actual_file.line_to_print()))
                    progress += 1
        f.close()
        self.printProgressBar(100, 100)
        return list_files

    def printProgressBar(self, iteration, total, prefix='', suffix='', decimals=1, bar_length=50):
        percents = int(100 * (iteration / total))
        self.log.write_log("NONLOG:PROGRESSBAR:" + str(percents))

    def count_row(self, file):
        with open(join(self.gran_folder,file)) as f:
            return len(f.readlines())


class phase3_result:
    def __init__(self, log, folder, crc, tollerance):
        self.crc = crc
        self.gran_folder = folder
        self.log = log
        self.tollerance = tollerance
        same_name, same_crc = self.phase_analisys()
        if self.tollerance:
            same_name =self.tollerance_func(same_name, self.tollerance)
        self.final_phase(same_crc, same_name)

    def phase_analisys(self):
        list_result = self.read_file_result(self.gran_folder)
        list_same_crc = None
        if self.crc:
            list_same_crc = self.find_list_of_duplicate(list_result, "checksum")
        list_same_name = self.find_list_of_duplicate(list_result, "name")
        return list_same_name, list_same_crc

    def read_file_result(self, folder):
        big_list = []
        list_result = listdir(folder)
        for file in list_result:
            if file.startswith("result_"):
                self.read_list_from_file(folder, big_list, file)
        return big_list

    def read_list_from_file(self, folder, list, file):
        f = open(join(folder, file))
        lines = f.readlines()
        for line in lines:
            file_split = line.split(";")
            obj = file_obj(file_split[DEF_FILE_PATH], file_split[DEF_FILE_CRC], file_split[DEF_FILE_SIZE], file_split[DEF_FILE_DATE],)
            list.append(obj)

    def add_item_to_dict(self, dict, type, item):
        if type == "checksum":
            if item.checksum in dict:
                dict[item.checksum] += [item]
            else:
                dict[item.checksum] = [item]
        if type == "name":
            if item.name in dict:
                dict[item.name] += [item]
            else:
                dict[item.name] = [item]

    def find_list_of_duplicate(self, list, type):

        dict_duplicate = {}

        for item in list:
            if type == "checksum":
                self.add_item_to_dict(dict_duplicate, type, item)
            if type == "name":
                self.add_item_to_dict(dict_duplicate, type, item)

        new_dict = {}
        for k, v in dict_duplicate.items():
            if len(v) > 1:
                new_dict[k] = v
        return new_dict

    def check_tollerance(self, avg_size, size, tollerance):
        delta = int(avg_size * tollerance / 100)
        d_max = int(avg_size + delta)
        d_min = int(avg_size - delta)
        if d_min < int(size) < d_max:
            return True
        else:
            return False

    def tollerance_func(self, dict_p, tollerance):
        list_ret_dics = []
        for k, v in dict_p.items():
            list_to_delete = []
            for item in v:
                if not self.check_tollerance(int(v[0].size), item.size, tollerance):
                    list_to_delete.append(item)

            list_ret_dics.append(self.looking_for_second_file_same_name(list_to_delete, tollerance))

            for item in list_to_delete:
                if type(v) == list:
                    v.remove(item)

        for item in list_ret_dics:
            for sub_item in item:
                dict_p.update(sub_item)

        return dict_p

    def looking_for_second_file_same_name(self, list_p, tollerance):
        ret_list = []
        list_to_compare = list_p[:]
        cont = 2
        for item in list_p:
            sub_dict = {}
            name = item.name + "_" + str(cont)
            sub_dict[name] = [item]
            list_to_compare.remove(item)
            for sub_item in list_to_compare:
                if self.check_tollerance(int(item.size), sub_item.size, tollerance):
                    if item == sub_item:
                        pass
                    else:
                        sub_dict[name] += [sub_item]

            if len(sub_dict[name]) > 1:
                ret_list.append(sub_dict)
            cont += 1
        return ret_list

    def final_phase(self, same_crc, same_name):
        if self.crc:
            path_to_file = join(self.gran_folder, "SAME_CRC.txt")
            self.write_log_same(path_to_file, same_crc)

        path_to_file = join(self.gran_folder, "SAME_NAME.txt")
        self.write_log_same(path_to_file, same_name)

    def write_log_same(self, path_to_file, dict_passed):
        f = open(path_to_file, "w")

        for k, v in dict_passed.items():
            if len(v) > 1:
                line = "{\"" + k + "\" : ["
                for item in v:
                    line += "\"" + item.line_to_print() + "\", "
                line = line[:-2]
                line += "]}\n"
                f.write(line)
                f.flush()


class phase4_report:
    def __init__(self, log, folder, folder_to_scan=None):
        self.gran_folder = folder
        self.folder_to_scan = folder
        if folder_to_scan is not None:
            self.folder_to_scan = folder_to_scan
        self.log = log
        self.read_final_result()

    def converti_dimensione(self, dimensione):
        if dimensione < 1000000:
            ret = str(dimensione / 1000).split(".")[0] + " KB"
        if dimensione < 1000000000 and dimensione > 1000000:
            ret = str(dimensione / 1000000).split(".")[0] + " MB"
        if dimensione < 1000000000000 and dimensione > 1000000000:
            ret = str(dimensione / 1000000000)[:4] + " GB"
        return ret

    def read_dict_from_file(self, file):
        f = open(file, "r")
        lines = f.readlines()
        somma = 0
        for line in lines:
            line_path = line.replace("\\", "/")
            try:
                dict_r2 = eval(line_path)
                for k, v in dict_r2.items():
                        size = int(v[0].split(";")[DEF_FILE_SIZE])
                        somma += size
            except:
                print("error " + line_path)

        string = "REPORT:Totale file doppi : " + str(file) + " --> " + self.converti_dimensione(somma)
        self.log.write_log(string)

    def read_final_result(self):
        list_temp = listdir(self.folder_to_scan)
        for file in list_temp:
            if "SAME_" in file:
                self.read_dict_from_file(join(self.folder_to_scan, file))



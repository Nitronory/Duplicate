from class_folder.DEFINE import *


class MoveFiles:
    def __init__(self, log, signal, folder, what_keep, path_to_move):
        self.log = log
        str_date = "SCAN " + str(datetime.datetime.now())[:19].replace(":", ".")
        self.path_to_move = join(path_to_move, str_date)
        makedirs(abspath(self.path_to_move))
        # self.path_to_move = path_to_move
        self.signal = signal
        self.gran_folder = folder
        self.what_keep = what_keep
        list_same_name, list_same_crc = self.find_files_same()
        self.func_move(list_same_name)
        if list_same_crc:
            self.func_move(list_same_crc)

    def find_files_same(self):
        list_temp = listdir(self.gran_folder)
        list_same_crc = None
        list_same_name = None
        for file in list_temp:
            if "SAME_NAME" in file:
                list_same_name = self.read_files(file)

            if "SAME_CRC" in file:
                list_same_crc = self.read_files(file)

        return list_same_name, list_same_crc

    def read_files(self, file):
        file_path = join(self.gran_folder, file)
        f = open(file_path, "r")
        lines = f.readlines()
        list_of_dict = []
        for line in lines:
            line_path = line.replace("\\", "/")
            try:
                dict_read = eval(line_path)
                list_of_dict.append(dict_read)
            except:
                print("error " + line_path)
        return list_of_dict

    def func_move(self, list_p):
        for dict_in in list_p:
            self.handle_item(dict_in)

    def handle_item(self, item):
        for k, v in item.items():
            to_keep = None
            self.log.write_log("MOVING")
            for item in v:
                pieces = item.split(";")
                if to_keep is None:
                    to_keep = pieces

                if self.what_keep == "The Newer":
                    if pieces[DEF_FILE_DATE] < to_keep[DEF_FILE_DATE]:
                        to_keep = pieces

                if self.what_keep == "The Older":
                    if pieces[DEF_FILE_DATE] > to_keep[DEF_FILE_DATE]:
                        to_keep = pieces

                if self.what_keep == "With Longer Path":
                    if len(pieces[DEF_FILE_PATH]) > len(to_keep[DEF_FILE_PATH]):
                        to_keep = pieces

                if self.what_keep == "With Shorter Path":
                    if len(pieces[DEF_FILE_PATH]) < len(to_keep[DEF_FILE_PATH]):
                        to_keep = pieces

                if self.what_keep == "With Biggest Size":
                    if len(pieces[DEF_FILE_SIZE]) > len(to_keep[DEF_FILE_SIZE]):
                        to_keep = pieces

                if self.what_keep == "With Smaller Size":
                    if len(pieces[DEF_FILE_SIZE]) < len(to_keep[DEF_FILE_SIZE]):
                        to_keep = pieces

            for item in v:
                split_f = item.split(";")
                if split_f != to_keep:
                    self.move_file(split_f[1])

    def rename_file_to_move(self, name, iter):
        if iter == 0:
            return name
        ext = name.split(".")[1]
        len_ext = len(ext) + 1
        new_name = name[:-len_ext] + "(" + str(iter + 1) + ")." + ext
        return new_name

    def move_file(self, orig_file_with_path):
        orig_path, orgi_file_name = split(orig_file_with_path)
        new_file_with_path = join(self.path_to_move, orgi_file_name)

        new_name = None
        cont = 0

        while 1:
            if not isfile(new_file_with_path):
                break
            else:
                new_name = self.rename_file_to_move(orgi_file_name, cont)
                new_file_with_path = join(self.path_to_move, new_name)
            cont += 1

        if new_name is not None:
            try:
                old_path_new_name = join(orig_path, new_name)
                self.log.write_log("RENAME : " + str(orig_file_with_path) + " TO : " + str(old_path_new_name))
                rename(orig_file_with_path, old_path_new_name)
                self.log.write_log("MOVE : " + str(old_path_new_name) + " TO : " + str(new_file_with_path))
                move(old_path_new_name, new_file_with_path)
            except:
                self.log.write_log("ERROR : MOVING " + str(old_path_new_name) + " TO : " + str(new_file_with_path))

        else:
            try:
                self.log.write_log("MOVE : " + str(orig_file_with_path) + " TO : " + str(new_file_with_path))
                move(orig_file_with_path, new_file_with_path)
            except:
                self.log.write_log("ERROR : MOVING " + str(orig_file_with_path) + " TO : " + str(new_file_with_path))

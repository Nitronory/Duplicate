from class_folder.DEFINE import *

class file_obj:
    def __init__(self, path, checksum=None, size=None, date=None):
        self.name = basename(path)
        self.path = path
        self.checksum = checksum
        if size is None:
            self.size = getsize(path)
        else:
            self.size = size

        if date is None:
            self.date = getmtime(path)
        else:
            self.date = date

    def check_name(self, obj):
        if type(obj) is file_obj:
            if obj.name == self.name:
                return True
        return False

    def check_crc(self, obj):
        if type(obj) is file_obj:
            if obj.checksum == self.checksum:
                return True
        return False

    def calc_checksum(self, type_checksum):
        if type_checksum == "sha256":
            self.checksum = self.calc_sha256()
        if type_checksum == "crc":
            self.checksum = self.calc_crc32()
        if type_checksum is None:
            self.checksum = 0

    def calc_sha256(self):
        buf = open(self.path, 'rb').read()
        hash_object = sha256(buf)
        hex_dig = hash_object.hexdigest()
        return hex_dig

    def calc_crc32(self):
        try:
            buf = open(self.path, 'rb').read()
            buf = (crc32(buf) & 0xFFFFFFFF)
            return "%08X" % buf
        except:
            return 0

    def set_size(self, size):
        self.size = int(size)

    def set_crc(self, crc):
        self.size = crc

    def set_date(self, date):
        self.date = date

    def line_to_print(self):
        line = str(self.name) + ";" + str(self.path) + ";" + str(self.checksum) + ";" + str(self.size) + ";" + str(self.date) + ";"
        return line


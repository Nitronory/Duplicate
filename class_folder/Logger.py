class Logger:
    def __init__(self, file, signal):
        self.file = open(file, "w", encoding='latin1', errors='ignore')
        self.signal = signal

    def write_log(self, text):
        line = text + "\n"
        if "NONLOG:" not in line:
            self.file.write(line)
        self.file.flush()
        self.signal.sig.emit(text)

    def __exit__(self):
        self.file.close()



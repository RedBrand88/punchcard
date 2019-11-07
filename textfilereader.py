import os

class txtreader(object):
    path = "~/Documents/timecards"

    def __init__(self, filename):
        self.filename = filename
        self.finalpath = os.path.expanduser(os.path.join(self.path, self.filename))

    def __enter__(self):
        if os.path.exists(self.finalpath):
            self.file = open(self.finalpath, 'r')
            return self.file
        else:
            return None

    def __exit__(self, exception_type, exception_value, traceback):
        self.file.close()
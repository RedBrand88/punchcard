import os

class textfilecreator(object):
    #object created to use with statement
    parentdirectory = "~/Documents"
    directory = "timecards"

    def __init__(self, filename):
        self.filename = filename
        self.path = os.path.expanduser(os.path.join(self.parentdirectory, self.directory))

    def __enter__(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            completepath = os.path.join(self.path, self.filename)
            self.file = open(completepath, 'a+')
            return self.file
        else:
            completepath = os.path.join(self.path, self.filename)
            self.file = open(completepath, 'a+')
            return self.file

    def __exit__(self, exception_type, exception_value, traceback):
        self.file.close()
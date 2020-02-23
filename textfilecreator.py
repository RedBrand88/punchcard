import os

class textfilecreator:
    # object created to use with statement
    # this class creates a file in ~/Documents if it doesn't already exist

    def __init__(self, filename, directory, parentdirectory="~/Documents"):
        self.filename = filename
        self.directory = directory
        self.parentdirectory = parentdirectory
        self.path = os.path.expanduser(os.path.join(self.parentdirectory, self.directory))

    def __enter__(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            completepath = os.path.join(self.path, self.filename)
            self.file = open(completepath, 'a+')
            return self.file
        else:
            completepath = os.path.join(self.path, self.filename)
            self.file = open(completepath, 'a+')
            return self.file

    def __exit__(self, exception_type, exception_value, traceback):
        self.file.close()

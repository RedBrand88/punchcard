import time
from datetime import datetime

class timecard:
    #timecard{"punch in":tuple, "lunch out":tuple, "lunch in":tuple, "punch out":tuple}
    def __init__(self):
        self.timein = self.getCurrentTime()
        self.day = {"punch in":0,"lunch out":0,"lunch in":0,"punch out":0}

    def getCurrentTime(self):
        localtime = time.localtime(time.time())
        return localtime

    def getToday(self):
        today = datetime.now().strftime("%m-%d-%Y")
        return today

    def formatTime(self, timestamp, label):
        timeformated = time.asctime(timestamp)
        line = label + " : " + timeformated + "\n"
        return line

    #possibly change this method unless time tuple is cached
    def getPunchTime(self, key):
        return self.formatTime(self.day[key], key)

    def punch(self):
        if self.day["punch in"] == 0:
            self.day["punch in"] = time.localtime(time.time())
        elif self.day["lunch out"] == 0:
            self.day["lunch out"] = time.localtime(time.time())
        elif self.day["lunch in"] == 0:
            self.day["lunch in"] = time.localtime(time.time())
        elif self.day["punch out"] == 0:
            self.day["punch out"] = time.localtime(time.time())

    def setpunches(self, key, punchvalue):
        self.day[key] = punchvalue

    # def gettotalhours(self):
        #convert strings to min
        #us datetime to find hours worked and return
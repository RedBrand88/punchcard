from time import localtime, time, mktime, asctime
from datetime import datetime

class timecard:
    # timecard{"punch in":tuple, "lunch out":tuple, "lunch in":tuple, "punch out":tuple}
    weekly_total_hours = 0

    # I discovered that everything is an object including mutable default params
    def __init__(self, day=None):
        self.day = day if day is not None else {"punch in":0,"lunch out":0, "lunch in":0, "punch out":0}
        self.timein = self.getCurrentTime()

    # constructor like class method that calls the classes init method
    # this assumes the init method takes a param for day
    @classmethod
    def fromTimeStamp(cls, timestamp):
        day = {"punch in":timestamp, "lunch out":0, "lunch in":0, "punch out":0}
        return cls(day)

    @classmethod
    def fromDateTime(cls, date_time):
        timestamp = date_time.timetuple()
        day = {"punch in":timestamp, "lunch out":0, "lunch in":0, "punch out":0}
        return cls(day)

    @classmethod
    def fromStringDate(cls, string_date):
        timestamp = cls.stringDateToTimeStamp(string_date)
        day = {"punch in":timestamp, "lunch out":0, "lunch in":0, "punch out":0}
        return cls(day)

    @staticmethod
    def stringDateToTimeStamp(string_date, format=None):
        _format = format if format is not None else "%a %b %d %H:%M:%S %Y"
        return datetime.strptime(string_date.rstrip(), _format).timetuple()

    @staticmethod
    def getCurrentTime():
        return localtime(time())

    @staticmethod
    def getToday():
        today = datetime.now().strftime("%m-%d-%Y")
        return today

    @staticmethod
    def formatTime(timestamp, label):
        timeformated = asctime(timestamp)
        line = label + " : " + timeformated + "\n"
        return line

    @staticmethod
    def getTimeDiffInHours(timeEnd, timeBeg):
        timeDiff = timeEnd - timeBeg
        seconds_in_day = 24 * 60 * 60
        min, sec = divmod(timeDiff.days * seconds_in_day + timeDiff.seconds, 60)
        min_to_add = sec / 60
        min += min_to_add
        return min / 60

    @staticmethod
    def structTimeToDateTime(struct):
        return datetime.fromtimestamp(mktime(struct))

    #possibly change this method unless time tuple is cached
    def getPunchTime(self, key):
        return timecard.formatTime(self.day[key], key)

    def punch(self):
        if self.day["punch in"] == 0:
            self.day["punch in"] = timecard.getCurrentTime()
        elif self.day["lunch out"] == 0:
            self.day["lunch out"] = timecard.getCurrentTime()
        elif self.day["lunch in"] == 0:
            self.day["lunch in"] = timecard.getCurrentTime()
        elif self.day["punch out"] == 0:
            self.day["punch out"] = timecard.getCurrentTime()
            timecard.weekly_total_hours += timecard.getTimeDiffInHours(
                timecard.structTimeToDateTime(self.day["punch out"]),
                timecard.structTimeToDateTime(self.day["punch in"]))

    def setpunches(self, key, punchvalue):
        # 'Thu Feb 20 15:06:58 2020\n'
        timestamp = timecard.stringDateToTimeStamp(punchvalue)
        self.day[key] = timestamp

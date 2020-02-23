from timecard import timecard
from textfilecreator import textfilecreator
from textfilereader import txtreader
import os

def main():
    x = timecard()
    directory = "timecards"
    filename = x.getToday() + ".txt"
    timecardpath = os.path.expanduser("~/Documents/timecards/" + filename)
    if os.path.exists(timecardpath):
        #read from file with statement
        line = ""
        punchtoadd = ""
        message = ""
        with txtreader(timecardpath) as readFile:
        #check which punches have been tracked
            for textline in readFile:
                line = textline.split(' : ')
                punch = line[1]
                if "punch in" in line:
                    x.setpunches("punch in", punch)
                    punchtoadd = "lunch out"
                    message = "Have a nice lunch!"
                elif "lunch out" in line:
                    x.setpunches("lunch out", punch)
                    punchtoadd = "lunch in"
                    message = "Welcome back to work!"
                elif "lunch in" in line:
                    x.setpunches("lunch in", punch)
                    punchtoadd = "punch out"
                    message = ""

        if punchtoadd == "":
            punchtoadd = "punch in"

        x.punch()
        if punchtoadd is not "punch out":
            with textfilecreator(timecardpath) as appFile:
                appFile.write(x.getPunchTime(punchtoadd))
        else:
            with textfilecreator(timecardpath) as appFile:
                appFile.write(x.getPunchTime(punchtoadd))
                appFile.write(f"\n\n\nTotal Hours: {x.weekly_total_hours}")
                message = f"You have worked {x.weekly_total_hours} hours today. Drive safe!"

        print(message)
        print("Chunk Chunk")
    else:
        punchtoadd = "punch in"
        x.punch()
        with textfilecreator(filename, directory) as writeFile:
            writeFile.write(x.getPunchTime(punchtoadd))

        print("Welcome to work!")
        print("Chunck Chunck")
        print("Time card punched!")

if __name__ == "__main__":
    main()


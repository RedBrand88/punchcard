from timecard import timecard
from textfilecreator import textfilecreator
from textfilereader import txtreader
import os

def main():
    x = timecard()
    filename = x.getToday() + ".txt"
    timecardpath = os.path.expanduser("~/Documents/timecards/" + filename)
    if os.path.exists(timecardpath):
        #read from file with statement
        line = ""
        punchtoadd = ""
        with txtreader(timecardpath) as readFile:
        #check which punches have been tracked
            for textline in readFile:
                line = textline.split(' : ')
                punch = line[1]
                if "punch in" in line:
                    x.setpunches("punch in", punch)
                    punchtoadd = "lunch out"
                elif "lunch out" in line:
                    x.setpunches("lunch out", punch)
                    punchtoadd = "lunch in"
                elif "lunch in" in line:
                    x.setpunches("lunch in", punch)
                    punchtoadd = "punch out"
        
        if punchtoadd == "":
            punchtoadd = "punch in"

        x.punch()
        with textfilecreator(timecardpath) as appFile:
            appFile.write(x.getPunchTime(punchtoadd))

        print("Chunk Chunk")
    else:
        punchtoadd = "punch in"
        x.punch()
        with textfilecreator(filename) as writeFile:
            writeFile.write(x.getPunchTime(punchtoadd))
        
        print("Welcome to work!")
        print("Chunck Chunck")
        print("Time card punched!")

if __name__ == "__main__":
    main()
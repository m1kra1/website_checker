import os
import subprocess
from datetime import datetime
from tkinter import N
from function import pingURL, fileHandler, userPathCheck
import getpass


#Get current date and time 
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
time = now.strftime("%H:%M:%S")
timeStamp_file = now.strftime("%m-%d-%Y_%H-%M-%S")

print("Mit diesem Programm kannst du eine Website anpingen.")
print("Die Ausgabe wird in einem File auf dem Desktop abgelegt.(Output_DeineURL)")
print("")
urlToCheck = input("Welche URL soll gecheckt werden: ")

#Create User Path to C:/users/username/Desktop/Checker_Result/urlToCheck
userPath = os.path.join(os.path.expandvars("%userprofile%"),"Desktop","checker_result", urlToCheck)
print(userPath)
userPathCheck(userPath)

userFilePath = userPath + "/Output_{}_{}.txt".format(urlToCheck, timeStamp_file)

pingURL(urlToCheck, userFilePath) #function.py - Putting the command line together - Store in File



openFile = input("Möchten Sie die Datei oeffnen? J/N: ").lower()

if openFile == "j":
    fileHandler(userFilePath) #function.py - Check if file open requested - Commandline Path or Quit
else:
    quit()
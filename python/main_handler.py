import os
import subprocess

from requests import patch
from function import pingURL, fileHandler, userPathCheck
import getpass




print("Mit diesem Programm kannst du eine Website anpingen.")
print("Die Ausgabe wird in einem File auf dem Desktop abgelegt.(Output_DeineURL)")
print("")
urlToCheck = input("Welche URL soll gecheckt werden: ")

#Create User Path to Desktop/Checker_Result/
userPath = os.path.join(os.path.expandvars("%userprofile%"),"Desktop","checker_result")
print(userPath)
userPathCheck(userPath)

userFilePath = userPath + "/Output_{}.txt".format(urlToCheck)
pingURL(urlToCheck, userFilePath) #function.py - Putting the command line together - Store in File



openFile = input("Möchten Sie die Datei oeffnen? J/N: ").lower()

if openFile == "j":
    fileHandler(userFilePath) #function.py - Check if file open requested - Commandline Path or Quit
else:
    quit()
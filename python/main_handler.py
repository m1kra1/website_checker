
from os import system
import subprocess
from function import pingURL
from function import fileHandler

print("Mit diesem Programm kannst du eine Website anpingen.")
print("Die Ausgabe wird in einem File auf dem Desktop abgelegt.(Output_DeineURL)")
print("")
urlToCheck = input("Welche URL soll gecheckt werden: ")

pingURL(urlToCheck) #function.py - Putting the command line together - Store in File

openFile = input("Möchten Sie die Datei oeffnen? J/N: ").lower()

if openFile == "j":
    fileHandler(urlToCheck) #function.py - Check if file open requested - Commandline Path or Quit
else:
    quit()
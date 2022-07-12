import os


def userPathCheck(userPath):
    #Check if dir exists
    checkDir = os.path.isdir(userPath)
    #If not exiting - create dir
    if checkDir == False:
        os.mkdir(userPath)
    else:
        return()

def pingURL(urlToCheck, userFilePath):
    
    #Get userFilePath and create Command for ping. Execute Command Line
    commandUrlToCheck = "ping "+ urlToCheck + " > {}".format(userFilePath)
    print(commandUrlToCheck)
    os.system(commandUrlToCheck)
    
    
def fileHandler(userFilePath):
        os.system(userFilePath)
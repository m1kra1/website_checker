import os

def pingURL(urlToCheck):
    commandUrlToCheck = "ping "+ urlToCheck + " > C:/Users/MikeLaptop/Desktop/Output_{}.txt".format(urlToCheck)
    print(commandUrlToCheck)
    os.system(commandUrlToCheck)
    
def fileHandler(urlToCheck):
        openFilePath = "C:/Users/MikeLaptop/Desktop/Output_{}.txt".format(urlToCheck)
        os.system(openFilePath)
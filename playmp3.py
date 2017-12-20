from playsound import playsound
import os

#peek function is use to play mp3 made from text
def speek(path):
    playsound(path)
    a=removefile(path)
    print(a)
#remove file funtion is use to delete the file after our proc compile

def removefile(path):
    os.remove(path)
    b="file is deleted"
    return b

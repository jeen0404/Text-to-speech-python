from gtts import gTTS
from playsound import playsound
import playmp3

#here you can add wellcome sound
'''
wellcome=""
playsound(wellcome)
'''


#this function is use to take input from user
def entertext():
    text=str(input("enter the text"))
    return text

#this is our main function it convert string into mp3 file
def prosess(name):
    a=name   #it,s value of we passed from while loop
    path=str(a+'.mp3')#here we add to string and .mp3 extention
    print(path)
    text=entertext()#here we call entertext function and take input from user
    t=str("")#here we define empty string 

    if(text==t):        #here we check user text is empty or not if condition is true we call again entertext function
        print("enter ext first")
        entertext()
    else:               #if user is write some text then we convert it into voice or mp3 usein gtts here
        tts = gTTS(text=text, lang='en')
        tts.save(path)
        playmp3.speek(path) #here we call the function of other file name is playmp3 where it play and delete
		
#we defaine a and convert into string because if we use only one name then the gtts will give us error so we change the name of mp3 every time
a=0
while 1 :#we use while loop because we can't open file every time
    a=a+1
    b=str(a)
    prosess(b)#were the value of a passed to prosess function

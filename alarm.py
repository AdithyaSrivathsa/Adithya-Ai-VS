from time import time
import pyttsx3
import datetime
import os 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("alarm.txt", "rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("alarm.txt", "r+")
deletetime .truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("tony", "")
    timenow = timeset.replace("set an alarm", "")
    timenow = timeset.replace(" and ", ":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%I:%M:%S")
        if currenttime == Alarmtime:
            speak("Time's Up!")
            os.startfile("alarm.mp3")
        elif currenttime + "00:00:30" == Alarmtime:
            exit()
ring(time)

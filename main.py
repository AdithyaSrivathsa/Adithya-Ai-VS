import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import speech_recognition
import requests
import pyautogui
import os
from bs4 import BeautifulSoup
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 4
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-us')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
#def commands...........................................................................................................................
def alarm(query):
    timehere = open("alarm.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def searchGoogle(query):
    import wikipedia as googleScrap
    speak("This is what I found")
    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query, 1)
        speak(result)

    except:
        speak("Did not find anything about that, sorry")


def searchYoutube(query):
    web = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("Done, Sir")


def searchWikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    speak("According to wikipedia...")
    print(results)
    speak(results)

running = True
# Starting...............................................................................................................
if __name__ == "__main__":
    while running:
        query = takeCommand().lower()
        if "dumb" in query:
            hour = int(datetime.datetime.now().hour)
            if 0 <= hour <= 12:
                speak("Yes sir?")
            elif 12 < hour <= 18:
                speak("Yes sir?")

            else:
                speak("Yes sir?")

            query = takeCommand().lower()
            if "go to sleep" in query:
                speak("Ok, See you, Remember if you need anything just say, wake up")
                breakpoint

            elif "shutdown" in query:
                os._exit(0)
    #websearch commands...........................................................................................
            elif "wikipedia" in query:
                speak("Searching from wikipedia....")
                query = query.replace("tony", "")
                query = query.replace("search wikipedia", "")
                query = query.replace("wikipedia", "")
                searchWikipedia(query)

            elif "youtube" in query:
                speak("This is what I found for your search!")
                query = query.replace("tony", "")
                query = query.replace("youtube search", "")
                query = query.replace("youtube", "")
                searchYoutube(query)
            
            elif "google" in query:
                query = query.replace("tony", "")
                query = query.replace("google search", "")
                query = query.replace("google", "")
                searchGoogle(query)

            elif "opencanvas" in query:
                query = query.replace("tony", "")
                query = query.replace("google search", "")
                query = query.replace("google", "")
                speak("Opening Canvas")
                webbrowser.open("https://pccsk12.instructure.com/?login_success=1")
                speak("Done Sir")

            elif "temperature" in query:
                speak("Checking temperature")
                location = "location"
                search = "temperature"
                url = f"https://www.google.com/search?q={location} + {search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_ = "BNeawe").text
                speak(f"current{search} is {temp}")

            elif "weather" in query:
                speak("Checking weather")
                location = "location"
                search = "temperature"
                url = f"https://www.google.com/search?q={location} + {search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_ = "BNeawe").text
                speak(f"current{search} is {temp}")
    #time......................................................................................................................................................
            elif "time" in query:
                currenttime = datetime.datetime.now().strftime("%I:%M:%S")  
                speak(f"The current time is {currenttime}")

            elif "set an alarm" in query:
                print("input time example:- 10:10:10")
                speak("Set the time")
                currenttime = datetime.datetime.now().strftime("%I:%M:%S")
                print("The current time is", currenttime)
                a = input("Please set the time:- ")
                alarm(a)
                speak("Done sir")
    #audio controls...............................................................................................................................
            elif "pause" in query:
                pyautogui.click(1805, 1058, duration = 1)
                pyautogui.click(1729, 381, duration = 1)
                speak("paused")

            elif "play" in query:
                pyautogui.click(1805, 1058, duration = 1)
                pyautogui.click(1729, 381, duration = 1)
                speak("playing")

            elif "volume down" in query:
                pyautogui.press("volumedown")

            elif "volume up" in query:
                pyautogui.press("volumeup")
    #apps....................................................................................................................................                
            elif "play music" in query:
                speak("Launching sir")
                pyautogui.hotkey("ctrl", "esc")
                sleep(0.5)
                pyautogui.hotkey("y")
                sleep(0.5)
                pyautogui.hotkey("enter")
                sleep(6)
                pyautogui.rightClick(326, 330, duration = 1)
                sleep(0.5)
                pyautogui.click(422, 363, duration = 1)

            elif "launch fortnite" in query:
                speak("Launching sir")
                pyautogui.hotkey("ctrl", "esc")
                sleep(0.5)
                pyautogui.hotkey("e")
                sleep(0.5)
                pyautogui.hotkey("enter")
                sleep(12)
                pyautogui.click(420, 542, duration = 1)

            elif "open whatsapp" in query:
                speak("Launching sir")
                pyautogui.hotkey("ctrl", "esc")
                sleep(0.5)
                pyautogui.typewrite("whatsapp")
                sleep(0.5)
                pyautogui.hotkey("enter")

            elif "call mom" in query:
                speak("Calling mom")
                pyautogui.hotkey("ctrl", "esc")
                sleep(0.5)
                pyautogui.typewrite("whatsapp")
                sleep(0.5)
                pyautogui.hotkey("enter")
                sleep(9)
                pyautogui.click(194, 109, duration = 1)
                sleep(0.5)
                pyautogui.typewrite("Amma")
                sleep(0.5)
                pyautogui.click(205, 243, duration = 1)
                sleep(0.5)
                pyautogui.click(1768, 60, duration = 1)

            elif "call dad" in query:
                speak("Calling dad")
                pyautogui.hotkey("ctrl", "esc")
                sleep(0.5)
                pyautogui.typewrite("whatsapp")
                sleep(0.5)
                pyautogui.hotkey("enter")
                sleep(9)
                pyautogui.click(194, 109, duration = 1)
                sleep(0.5)
                pyautogui.typewrite("Appa")
                sleep(0.5)
                pyautogui.click(205, 243, duration = 1)
                sleep(0.5)
                pyautogui.click(1768, 60, duration = 1)

            elif "call grandma" in query:
                speak("Calling grandma")
                pyautogui.hotkey("ctrl", "esc")
                sleep(0.5)
                pyautogui.typewrite("whatsapp")
                sleep(0.5)
                pyautogui.hotkey("enter")
                sleep(9)
                pyautogui.click(194, 109, duration = 1)
                sleep(0.5)
                pyautogui.typewrite("Veena Ajji")
                sleep(0.5)
                pyautogui.click(205, 243, duration = 1)
                sleep(0.5)
                pyautogui.click(1768, 60, duration = 1)

            elif "call sister" in query:
                speak("Calling sister")
                pyautogui.hotkey("ctrl", "esc")
                sleep(0.5)
                pyautogui.typewrite("whatsapp")
                sleep(0.5)
                pyautogui.hotkey("enter")
                sleep(9)
                pyautogui.click(194, 109, duration = 1)
                sleep(0.5)
                pyautogui.typewrite("Sis(BTS Obsessed)")
                sleep(0.5)
                pyautogui.click(205, 243, duration = 1)
                sleep(0.5)
                pyautogui.click(1768, 60, duration = 1)

            elif "brave" in query:
                speak("Launching sir")
                pyautogui.hotkey("ctrl", "esc")
                sleep(0.5)
                pyautogui.typewrite("brave")
                sleep(0.5)
                pyautogui.hotkey("enter")

            elif "mail" in query:
                speak("Launching sir")
                pyautogui.hotkey("ctrl", "esc")
                sleep(0.5)
                pyautogui.typewrite("mail")
                sleep(0.5)
                pyautogui.hotkey("enter")

            elif "control panel" in query:
                speak("Launching sir")
                pyautogui.hotkey("ctrl", "esc")
                sleep(0.5)
                pyautogui.typewrite("control panel")
                sleep(0.5)
                pyautogui.hotkey("enter")    

            elif "file explorer" in query:
                speak("Launching sir")
                pyautogui.hotkey("ctrl", "esc")
                sleep(0.5)
                pyautogui.typewrite("file explorer")
                sleep(0.5)
                pyautogui.hotkey("enter")

            elif "skype" in query:
                speak("Launching sir")
                pyautogui.hotkey("ctrl", "esc")
                sleep(0.5)
                pyautogui.typewrite("skype")
                sleep(0.5)
                pyautogui.hotkey("enter")
            
            elif "close application" in query:
                speak("Closing Sir")
                pyautogui.hotkey("alt", "f4")

                
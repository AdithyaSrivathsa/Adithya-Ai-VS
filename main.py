import datetime
from socket import SocketType
from timeit import repeat
import wikipedia
import pywhatkit
import webbrowser
import speech_recognition as sr
import requests
import pyautogui
import os
from bs4 import BeautifulSoup
from time import sleep
from gtts import gTTS
from time import ctime
import keyboard
import json
from threading import Event

def speak(audioString):
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
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
    
def news():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=1f7f17e1e6434b0b8731210961274768",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=1f7f17e1e6434b0b8731210961274768",
            "health" : "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=1f7f17e1e6434b0b8731210961274768",
            "science" :"https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=1f7f17e1e6434b0b8731210961274768",
            "sports" :"https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=1f7f17e1e6434b0b8731210961274768",
            "technology" :"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=1f7f17e1e6434b0b8731210961274768"
}

        
    content = None
    url = None
    speak("Which field news do you want, [business], [health], [technology], [sports], [entertainment] or [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("News found!")
            break
        else:
            url = True
    if url is True:
        print("News not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("This is the news for today")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"For more info visit: {news_url}")
    stop_run = Event()
    keyboard.on_press_key('esc', callback=lambda _: stop_run.set())
    while not stop_run.is_set():
        news()
        
def searchGoogle(query):
    import wikipedia as googlescrap
    speak("This is what I found")   
    try:
        pywhatkit.search(query)
        result = googlescrap.summary(query, 1)
        speak(result)

    except:
        speak("No speakable output")


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
        if "friday" in query:
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
                pyautogui.click(1237, 13, duration = 1)
                pyautogui.click(1376, 362, duration = 1)
                speak("paused")

            elif "play" in query:
                pyautogui.click(1237, 13, duration = 1)
                pyautogui.click(1376, 362, duration = 1)
                speak("playing")

            elif "volume down" in query:
                pyautogui.keyDown("volumedown")

            elif "volume up" in query:
                pyautogui.keyDown("volumeup")
    #apps....................................................................................................................................                
            elif "play music" in query:
                speak("Launching sir")
                pyautogui.click(1207, 14, duration = 1.5)
                sleep(0.5)
                pyautogui.typewrite("youtube music")
                sleep(0.5)
                pyautogui.hotkey("enter")
                sleep(6)
                pyautogui.rightClick(326, 330, duration = 1)
                sleep(0.5)
                pyautogui.click(422, 363, duration = 1)

            elif "launch fortnite" in query:
                speak("Launching sir")
                pyautogui.click(1207, 14, duration = 1.5)
                sleep(0.5)
                pyautogui.typewrite("nvidia")
                sleep(0.5)
                pyautogui.hotkey("enter")

            elif "text" in query:
                speak("Who do you want to text")
                a = input("Who do you want to text: ")
                speak("Ok, which app do you want to use?")
                b = takeCommand()
                speak("What is your message?")
                c = takeCommand()
                speak(f"Ok, texting {a}")
                pyautogui.click(1207, 14, duration = 1.5)
                sleep(0.5)
                pyautogui.typewrite(b)
                sleep(1.5)
                pyautogui.hotkey("enter")
                sleep(7)
                pyautogui.click(214, 125, duration = 1)
                sleep(0.5)
                pyautogui.typewrite(a)
                sleep(0.5)
                if b == "whatsapp":
                    pyautogui.click(154, 205, duration = 1)
                    sleep(0.5)
                    pyautogui.click(727, 759, duration = 1)
                    pyautogui.typewrite(c)
                    sleep(0.5)
                    pyautogui.hotkey("enter")
                else:
                    pyautogui.click(223, 323, duration = 1)
                    sleep(0.5)
                    pyautogui.click(784, 775, duration = 1)
                    pyautogui.typewrite(c)
                    sleep(0.5)
                    pyautogui.hotkey("enter")
            
            elif "open whatsapp" in query:
                speak("Launching sir")
                pyautogui.click(1207, 14, duration = 1.5)
                sleep(0.5)
                pyautogui.typewrite("whatsapp")
                sleep(0.5)
                pyautogui.hotkey("enter")

            elif "call mom" in query:
                speak("Calling mom")
                pyautogui.click(1207, 14, duration = 1.5)
                sleep(0.5)
                pyautogui.typewrite("whatsapp")
                sleep(0.5)
                pyautogui.hotkey("enter")
                sleep(9)
                pyautogui.click(333, 109, duration = 1)
                sleep(0.5)
                pyautogui.typewrite("Amma")
                sleep(0.5)
                pyautogui.click(154, 215, duration = 1)
                sleep(0.5)
                pyautogui.click(1283, 54, duration = 1)

            elif "call dad" in query:
                speak("Calling dad")
                pyautogui.click(1207, 14, duration = 1.5)
                sleep(0.5)
                pyautogui.typewrite("whatsapp")
                sleep(0.5)
                pyautogui.hotkey("enter")
                sleep(9)
                pyautogui.click(333, 109, duration = 1)
                sleep(0.5)
                pyautogui.typewrite("Appa")
                sleep(0.5)
                pyautogui.click(154, 215, duration = 1)
                sleep(0.5)
                pyautogui.click(1283, 54, duration = 1)

            elif "call grandma" in query:
                speak("Calling grandma")
                pyautogui.click(1207, 14, duration = 1.5)
                sleep(0.5)
                pyautogui.typewrite("whatsapp")
                sleep(0.5)
                pyautogui.hotkey("enter")
                sleep(9)
                pyautogui.click(333, 109, duration = 1)
                sleep(0.5)
                pyautogui.typewrite("Veena Ajji")
                sleep(0.5)
                pyautogui.click(154, 215, duration = 1)
                sleep(0.5)
                pyautogui.click(1283, 54, duration = 1)

            elif "call sister" in query:
                speak("Calling sister")
                pyautogui.click(1207, 14, duration = 1.5)
                sleep(0.5)
                pyautogui.keyUp("command")
                sleep(0.5)
                pyautogui.keyUp("spacebar")
                sleep(0.5)
                pyautogui.typewrite("whatsapp")
                sleep(0.5)
                pyautogui.hotkey("enter")
                sleep(9)
                pyautogui.click(333, 109, duration = 1)
                sleep(0.5)
                pyautogui.typewrite("Sis(BTS Obsessed)")
                sleep(0.5)
                pyautogui.click(154, 215, duration = 1)
                sleep(0.5)
                pyautogui.click(1283, 54, duration = 1)

            elif "brave" in query:
                speak("Launching sir")
                pyautogui.click(1207, 14, duration = 1.5)
                sleep(0.5)
                pyautogui.typewrite("brave")
                sleep(0.5)
                pyautogui.hotkey("enter")

            elif "mail" in query:
                speak("Launching sir")
                pyautogui.click(1207, 14, duration = 1.5)
                sleep(0.5)
                pyautogui.typewrite("mail")
                sleep(0.5)
                pyautogui.hotkey("enter")

            elif "settings" in query:
                speak("Launching sir")
                pyautogui.click(1207, 14, duration = 1.5)
                sleep(0.5)
                pyautogui.typewrite("system preferences")
                sleep(0.5)
                pyautogui.hotkey("enter")    

            elif "file explorer" in query:
                speak("Launching sir")
                pyautogui.click(1207, 14, duration = 1.5)
                sleep(0.5)
                pyautogui.typewrite("file explorer")
                sleep(0.5)
                pyautogui.hotkey("enter")

            elif "open skype" in query:
                speak("Launching sir")
                pyautogui.click(1207, 14, duration = 1.5)
                sleep(0.5)
                pyautogui.typewrite("skype")
                sleep(0.5)
                pyautogui.hotkey("enter")
            
            elif "close application" in query:
                speak("Closing Sir")
                pyautogui.hotkey("option", "command", "esc")
                
            elif "spam" in query:
                speak("Who do you want to spam")
                a = input("Who do y ou want to spam: ")
                speak("Ok, which app do you want to use?")
                b = takeCommand()
                speak(f"Ok, spamming {a}")
                pyautogui.click(1207, 14, duration = 1.5)
                sleep(2)
                pyautogui.typewrite(b)
                sleep(2)
                pyautogui.hotkey("enter")
                sleep(7)
                pyautogui.click(214, 125, duration = 1)
                sleep(0.5)
                pyautogui.typewrite(a)
                sleep(0.5)
                pyautogui.click(223, 323, duration = 1)
                sleep(0.5)
                pyautogui.click(784, 775, duration = 1)
                sleep(0.5)
                pyautogui.typewrite(a)
                sleep(0.5)
                pyautogui.hotkey("enter")
                speak("spamming sir")
                i = 1
                while i <= 100:
                    pyautogui.typewrite("l bozo + ratio")
                    pyautogui.hotkey("enter")
                    i += 1
                i = False
                
            elif "news" in query:
                news()
                
            elif keyboard.is_pressed('q'):
                print('You Pressed the q Key!')
                breakpoint

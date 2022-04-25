import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)

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
        speak("Say that again")
        return "None"
    return query

query = takeCommand().lower()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#add..............................................................................................................................................................................
if "play music" in query:
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

elif "close application" in query:
    speak("Closing Sir")
    pyautogui.hotkey("alt", "f4")

elif "pc lock" in query:
    speak("Lcoking sir")
    pyautogui.hotkey("ctrl", "alt", "del")

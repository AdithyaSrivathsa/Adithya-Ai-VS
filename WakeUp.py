import pyttsx3
import datetime
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        speech_recognition.Recognizer().adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-is')
        print(f"You said:{query}\n")

    except Exception as e:
        return "None"
    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour <= 12:
                speak("Good Morning sir how may I help you today?")
            elif hour > 12 and hour <= 18:
                speak("Good Afternoon sir how may I help you today?")

            else:
                speak("Good Evening sir how may I help you today")

        while True:
            query = takeCommand().lower()
            if "go to sleep jarvis" in query:
                speak("Ok, See you, Remember if you need anything just? say, wake up jarvis")

            elif "thank you" in query:
                speak("You are welcome sir")

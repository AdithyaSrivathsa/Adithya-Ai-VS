import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#websearch def................................................................................................
def searchGoogle(query):
    import wikipedia as googleScrap
    speak("This is what I found")
    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query, 1)
        speak(result)   

    except:
        speak("No speakable output, sorry")


def searchYoutube(query):
    web = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("Done Sir")


def searchWikipedia(query):
    results = wikipedia.summary(query,sentences=2)
    speak("According to wikipedia..")
    print(results)
    speak(results)

   #el 
    if "wikipedia" in query:
                speak("Searching from wikipedia....")
                query = query.replace("jarvis", "")
                query = query.replace("search wikipedia", "")
                query = query.replace("wikipedia", "")
                searchWikipedia(query)

    #el 
    elif "youtube" in query:
                speak("This is what I found for your search!")
                query = query.replace("jarvis", "")
                query = query.replace("youtube search", "")
                query = query.replace("youtube", "")
                searchYoutube(query)
                
    #el         
    elif "google" in query:
                query = query.replace("jarvis", "")
                query = query.replace("google search", "")
                query = query.replace("google", "")
                searchGoogle(query)

    elif "opencanvas" in query:
                query = query.replace("tony", "")
                query = query.replace("google search", "")
                query = query.replace("google", "")
                webbrowser.open("https://pccsk12.instructure.com/?login_success=1")
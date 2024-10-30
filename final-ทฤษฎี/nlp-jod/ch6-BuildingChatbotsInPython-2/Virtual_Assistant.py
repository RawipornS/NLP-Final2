import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

def assistant(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Set the assistant voice (female)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def greeting():
    assistant("Hello, I am JAVIS. How about you Tony Stark")


def core_code():
    greeting()

def audioinput():
    # This function takes audio input from the user
    aud = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening and processing...')
        aud.pause_threshold = 0.7
        audio = aud.listen(source)
        
        try:
            print("Understanding...")
            # Recognizing speech using Google Web Speech API
            phrase = aud.recognize_google(audio, language='en-us')
            print("You said: ", phrase)
            return phrase
        except Exception as exp:
            print(exp)
            print("Can you please repeat that")
            return "None"

def theDay():
    # This function is for the day
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {
        1: 'Monday', 2: 'Tuesday',
        3: 'Wednesday', 4: 'Thursday',
        5: 'Friday', 6: 'Saturday',
        7: 'Sunday'
    }
    if day in Day_dict.keys():
        weekday = Day_dict[day]
        print(weekday)
        assistant("It's " + weekday)

def theTime():
    # This function is for time
    time = str(datetime.datetime.now())
    hour = time[11:13]
    minute = time[14:16]
    assistant("The time right now is " + hour + " hours and " + minute + " minutes")

core_code()

while True:
    phrase = audioinput().lower()
    print(phrase)
    if "what is your name" in phrase:
        assistant("I am Jarvis, your assistant Tony.")
        continue

    elif "iron man" in phrase:
        assistant("Ok Tony Stark , Confirmed use of mark 49 armor ")
        continue

    elif "bye" in phrase:
        assistant("Exiting. Have a Good Day Ironman")
        exit()

    elif "what day is it" in phrase:
        theDay()
        continue

    elif "what time is it" in phrase:
        theTime()
        continue

    elif "open google" in phrase:
        assistant("Opening Google")
        webbrowser.open("https://www.google.com")
        continue

    elif "open youtube" in phrase:
        assistant("What do you want to search on YouTube?")
        search_phrase = audioinput()
        
        if search_phrase != "None":
            assistant(f"Searching YouTube for {search_phrase}")
            search_query = search_phrase.replace(" ", "+")  # แทนที่ช่องว่างด้วย + เพื่อใช้ใน URL
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
        else:
            assistant("I didn't catch that, please try again.")
        continue

    elif "wiki" in phrase:
        assistant("Checking Wikipedia")
        phrase = phrase.replace("wiki ", "")
        result = wikipedia.summary(phrase, sentences=4)
        assistant("As per Wikipedia: " + result)
        continue

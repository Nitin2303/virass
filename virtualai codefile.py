import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki

listener = sr.Recognizer()
speaker = pyttsx3.init()
"""" RATE """
rate = speaker.getProperty("rate")
speaker.setProperty("rate",150)
"""VOICE"""
voices = speaker.getProperty("voices")
speaker.setProperty("voice",voices[1].id) #index value 0 for male voice

def speak(text):
    speaker.say("yes boss"+text)

    speaker.runAndWait()
def speak__exp(text):
    speaker.say(text)
    speaker.runAndWait()

virass = "siri"
speak__exp("i am your "+virass+"tell me boss")
def commander():
    command =""
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.upper()
            if virass in command:
                command = command.replace(virass+" "," ")
                print(command)
                speak(command)

    except:
        print("check your mic bro!")
    return command
while True:
    us_command = commander()
    
    if "bye" in us_command:
        print("good bye and take care boss")
        break
    elif "time" in us_command:
        current_time = dt.datetime.now().strftime("%I:%M %p")
        speak(current_time)
        print(current_time)
    elif "play" in us_command:
        us_command = us_command.replace("play", " ")
        print("playing" + us_command)
        speak("playing" + us_command)
        pk.playonyt(us_command)
    elif "search for" in us_command or "google" in us_command:
        us_command = us_command.replace("search for ", " ")
        us_command = us_command.replace("google", " ")
        speak("searching for" + us_command)
        pk.search(us_command)
    elif "who is " in us_command:
        us_command = us_command.replace("who is", " ")
        info = wiki.summary(us_command, 2)
        print(info)
        speak(info)
    elif "who are you" in us_command:
        speak__exp("i am your" + virass + "boss")

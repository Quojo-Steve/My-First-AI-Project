from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

# speech engine initialization
engine =  pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #0 = male voice, 1 = female voice
activationWord = 'computer'

def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print("Listening for command...")

    with sr.Microphone() as source2:
        listener.adjust_for_ambient_noise(source2, duration=0.2)
        # listener.pause_threshold = 2
        input_speech = listener.listen(source2)

    try:
        print("Recognizing speech")
        query = listener.recognize_google(input_speech)
        print(f"The input speech was {query}")
    except Exception as ex:
        print("I did not quite catch that")
        speak("I did not quite catch that")
        print(ex)
        return None
    return query

# main loop
if __name__ == '__main__':
    speak("All systems running")

    while True:
        # parse all input as a list
        query = parseCommand()

        if query is not None:
            query = query.lower().split()

            if query and query[0] == activationWord:
                query.pop(0)

                # list commands
                if query and query[0] == "say":
                    if 'hello' in query:
                        speak("Greetings, father")
                    else:
                        query.pop(0)  # remove say
                        speech = ' '.join(query)
                        speak(speech)
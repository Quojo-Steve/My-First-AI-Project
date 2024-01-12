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

#configuring chrome as the default browser
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def search_wikipedia(query = ""):
    search_result = wikipedia.search(query)
    if not search_result:
        print("No wikipedia result")
        return "No result received" 
    try:
        wikiPage = wikipedia.page(search_result[0])
    except wikipedia.DisambiguationError as err:
        wikiPage = wikipedia.page(err.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    return wikiSummary

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

                # navigation to web commands
                if query and query[0] == 'go' and query[1] == 'to':
                    speak("Opening...")
                    query = ' '.join(query[2:])
                    webbrowser.get('chrome').open_new(query)

                # wikipedia commands
                if query and query[0] == 'wikipedia':
                    query = ' '.join(query[1:])
                    speak("Querying wikipedia")
                    speak(search_wikipedia(query))
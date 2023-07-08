import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import calendar
import webbrowser
import pyautogui 
#method to access recognize the commands by user
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def user_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source,timeout=10)
            command = listener.recognize_google(voice)
            command = command.lower()
            
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
                talk(command)
                return command
    except Exception as e:
        print(e)
def tellDay():
    day = datetime.date.today()
    talk(calendar.day_name[day.weekday()])
def run_alexa():
    while(True):
        command = user_command()
        if(command!=None):
            if 'play' in command:
                song = command.replace('play', '')
                talk('playing' + song)
                pywhatkit.playonyt(song)
            elif 'today' in command:
                tellDay()
                continue    
            elif 'what' in command:
                content = command.replace('what', '')
                talk('playing' + content)
                pywhatkit.playonyt(content)
            elif 'time' in command:
                info = datetime.datetime.now().strftime('%I:%M %p')
                print(info)
                talk('Current time is '+ info)
            elif 'from wikipedia' in command:
                person = command.replace('who is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            elif 'hello google' in command:
                talk('Opening Google chrome...')
                webbrowser.open('www.google.com')
                continue
            elif 'on web' in command:
                pywhatkit.search(command)
                talk('Searchig result in google...')
                continue
            elif 'open amazon' in command:
                talk('Opening amazon site...')
                webbrowser.open('www.amazon.com')
                continue
            elif 'open facebook' in command:
                talk('Opening Facebook site....')
                webbrowser.open('www.facebook.com')
                continue
            elif 'open Twitter' in command:
                talk('Opening Twitter site....')
                webbrowser.open('www.twitter.com')
                continue
            elif 'open whatsapp' in command:
                talk('opening whatsapp site...')
                webbrowser.open('www.whatsapp.com')
                continue
            elif 'open flipcart' in command:
                talk('opening flipcart site...')
                webbrowser.open('flipcart.com')
                continue
            elif 'on amazon' in command:
                command=command.replace('on amazon','')
                print('Searchig result in amazon for '+command)
                talk('Searchig result in amazon for '+command)
                command=command.replace(' ','+')
                command='https://www.amazon.com/s?k='+command
                webbrowser.open(command)
                continue
            elif 'developer' in command:
                talk('Yes i am an develper')
            elif 'hii' in command:
                talk('Hello krishna how are you')
            elif 'love' in command:
                talk('I to love you')
            elif 'joke' in command:
                talk(pyjokes.get_jokes())
            elif 'how are you' in command:
                talk('I am fine,how are you')
            elif 'drink' in command:
                talk('No i cant drink')
            elif 'where' in command:
                talk('I am in MIiC COLLEGE')
            elif 'future' in command:
                talk('i want to became a fullstack developer')
            elif 'who are' in command:
                talk('I am alexa')
                print('Alexa.....')
                
        else:
            print("Voice NOt Recognized")
run_alexa()

    


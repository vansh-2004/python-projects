import pyttsx3#for speech output
import speech_recognition as s#for speech input
import datetime#for telling time
import wikipedia
import webbrowser
import os#to open application or file
import smtplib#to send e-mails
#[
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#] for getting and setting a voice
#[
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#] to make programmme say a string (defined on variable audio)
#[
def wishMe():
    speak("hello sir!")
#] greets the programmer / operater
#[
def ask():
    speak("what can I do for you?")
#]

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = s.Recognizer()
    with s.Microphone() as source:
        print("Listening...")
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("unable to recoginize the command")
        speak("Say that again please...")  
        return "None"
    return query
def takeCommand1():
    #It takes microphone input from the user and returns string output

    r = s.Recognizer()
    with s.Microphone() as source:
        
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try:
            
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
          
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
def pause():
    programpause=input("press <edith> to continue...")
l=0

if __name__ == "__main__":
    wishMe()
    ask()
    while l==0:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            cp = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(cp)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("to whom do you want to send the mail?")
                to = takeCommand()    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
        elif 'open code blocks' in query:
            cp = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            os.startfile(cp)
        elif 'open firefox' in query:
            cp = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        l=1
    while l==1:
        query = takeCommand1().lower()
        if 'friday' in query:
            l=0
            speak("yes sir")
            while l==0:
                query = takeCommand().lower()
                if 'search' and 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("search","")
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'open stack overflow' in query:
                    webbrowser.open("stackoverflow.com")   


                elif 'play music' in query:
                    music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

                elif 'open vs code' in query:
                    cp = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(cp)

                elif 'send email' in query:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        speak("to whom do you want to send the mail?")
                        to = takeCommand()    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry sir. I am not able to send this email")
                elif 'how are you' in query:
                    speak("I'm awesome sir")
                l=1


from tkinter import *       # GUI
import tkinter as tk
from tkinter import Tk      # for User Interface
# from PIL import Image, ImageTk
import pyttsx3              # for audio like sapi5
import datetime             # for current time
import pyjokes              # for jokes pip install pyjokes
# import random
import operator             # for calculation
import speech_recognition as src    # importing for voice recognizing
import wikipedia            # for searching
import webbrowser           # to open browser
import os
import pywhatkit            # for playing any videos & song on youtube
from pywikihow import search_wikihow        # for how to do task

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 185)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """ This wishMe function will works before running run maya button or works before opening Assistant Maya GUI"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Boss")

    elif 12 <= hour < 18:
        speak("Good Afternoon Boss")

    else:
        speak("Good Evening Boss!")

    speak("This is mayaa appointed as your Assistant")


def takecommand():
    """ It takes microphone  input from the user and returns string output"""
    r = src.Recognizer()
    with src.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Sorry, Can You repeat this please")
        query = None
        return query
    return query


# noinspection PyUnresolvedReferences

class Widget:
    def __init__(self):
        root = Tk()
        root = root
        root.title('Dashboard')
        root.geometry('555x735+400+0')

        self.compText = StringVar()
        self.userText = StringVar()

        #------TextShowcase------#
        self.userText.set("Press 'Run Maya' For Command")

        userFrame = LabelFrame(root, text="User Command", font=('times new roman', 10, 'bold'))
        userFrame.pack(fill='both', expand='yes')

        #-------INSIDE FRAME COMMAND WILL BE SHOWN AFTER COMMAND TAKEN FROM USER----------#
        left = Message(userFrame, textvariable=self.userText, bg='#3B3B98', fg='white')
        left.config(font=("Century Gothic", 22, 'bold'))
        left.pack(fill='both', expand='yes')

        compFrame = LabelFrame(root, text="Assistant Maya", font=('Times New Roman', 10, 'bold'))
        compFrame.pack(fill='both', expand="yes")

        left2 = Message(compFrame, textvariable=self.compText, bg='#3B3B98', fg='white')
        left2.config(font=("Century Gothic", 12, 'bold'))
        left2.pack(fill='both', expand='yes')

        self.compText.set('Hello, I am Maya a Assistant appointed for task Performing like Playing Songs, Videos,\
                          Opening browser,Opening Youtube etc. Assistant Maya is Developed By Rohit Kumar Sah')

        #------Button for Activating Maya------#
        '''You Can Command by pressing Run Maya button for each task'''
        btn = Button(root, text='Run Maya', font=('Arial', 20), bg="orange", fg='white', command=self.clicked) \
            .pack(fill='x', expand='no')

        #------------Button for closing---------------#
        btn2 = Button(root, text='Close', font=('Arial', 20), bg='orange', fg='white', command=root.destroy) \
            .pack(fill='x', expand='no')

        root.mainloop()

    #------ Run Maya Button function for further task like open,time,calculate,play, or search on wikipedia------#
    def clicked(self):
        # wishMe()
        query = takecommand()
        self.userText.set('listening....')
        self.userText.set(query)

        if query != None:
            query = query.lower()

            # ------It will open youtube after taking command from user-------#
            if 'youtube' in query:
                speak('opening youtube')
                webbrowser.open("youtube.com")

            # User can search on wikipedia by giving command like According to wikipedia#
            elif 'wikipedia' in query:
                speak('Searching...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to wikipedia")
                speak(results)

            #-To Search like how to cook... or how to use... first user have to say "activate" and
            # will speak up  How to do mode is activated and take input from user if user input recognized clearly
            # AIMaya will speak up some output-#
            elif "activate" in query:
                speak(" How To Do Mode is Activated")
                how = takecommand()
                max_result = 1
                how_to = search_wikihow(how, max_result)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)

            # User can search on wikipedia by giving command like According to wikipedia or who is#
            elif 'who is' in query:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to wikipedia")
                speak(results)

            elif 'define' in query:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)


            #----Command open facebook & it will open facebook------#
            elif 'facebook' in query:
                speak('opening facebook')
                webbrowser.open("facebook.com")

            elif 'how are you' in query:
                speak("I am Fine Sir Thank You for Asking")

            elif "tell me your name" in query:
                speak("My name is Mayaa")

            #-importing pyjokes will perform some random jokes -#
            elif 'joke' in query:
                listen = (pyjokes.get_joke())
                speak(listen)
                print(listen)

            elif 'How are you' in query:
                speak('I am Fine, Thank You so much for asking')

            #-for video playlist from local disk -#
            elif 'video' in query:
                music_dir = 'D:\\Playlist'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            #-for playing task on youtube like songs-#
            elif 'play' in query:
                song = query.replace('play', '')
                mood = ('playing' + song)
                pywhatkit.playonyt(song)
                speak(mood)

            #-to activate calculator just say open calculator-#
            elif 'open calculator' in query:
                try:
                    r = src.Recognizer()
                    with src.Microphone() as source:
                        speak("Okay, What you want to calculate")
                        print("Listening...")
                        r.pause_threshold = 1
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    my_string = r.recognize_google(audio)
                    print(my_string)

                    def get_operator_fn(op):
                        return {
                            '+': operator.add,  # plus
                            '-': operator.sub,  # minus
                            '*': operator.mul,  # multiplied by
                            '/': operator.__truediv__,  # divided
                        }[op]

                    def eval_binary_expr(op1, oper, op2):  # 6 plus 3
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)

                    speak("Your Result is")
                    speak(eval_binary_expr(*(my_string.split())))
                except:
                    speak('Sorry, I am not able to recall the calculation task. Please try again')

            #-for current time -#
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The Current time is {strTime}")

            #
            elif 'thank you' in query:
                speak("My Pleasure")

            #-it will open google search for searching-#
            elif 'google' in query:
                webbrowser.open("google.com")

            elif 'softwarica' in query or 'software Rika' in query or 'software QA' in query:
                speak('I know, Softwarica is a college of IT and e-Commerce in kathmandu nepal,\
                      Softwarica is collaborated with Coventry University which is located in UK')

            #--Opening Campus 4.0 with this given two query --#
            elif 'Campus 4.0' in query or 'campus' in query:
                speak('Opening')
                webbrowser.open('https://campus.softwarica.edu.np/')

            #--For opening google map--#
            elif 'map' in query or 'google map' in query:
                speak('opening')
                webbrowser.open('https://www.google.com/maps')



# if __name__ == "__main__":
#     # speak("Initializing")
#     wishMe()
#     widget = Widget()

import pywhatkit
import serial
import pyttsx3
import webbrowser
import pyaudio
import speech_recognition as sr
import os
import pyautogui
import datetime
import smtplib
from bs4 import BeautifulSoup
import requests
import urllib.request
import numpy as np
import time
from playsound import playsound
import serial
import cv2
from PIL import Image
import pywhatkit as kt
from datetime import datetime
from datetime import date
import holidays

today = date.today()
var1 = input('please enter your city name : ')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0  Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

x = datetime.now()
jarvis = pyttsx3.init()


class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = "MP4"

movie = Movie_MP4(r"C:\Users\PRACHEE\Downloads\WhatsApp Video 2022-05-20 at 2.03.28 PM.mp4")


movie.play()
time.sleep(17)
os.system("taskkill /im WhatsApp Video 2022-05-20 at 2.03.28 PM.mp4 /f")
now = datetime.now()

dt1 = datetime.now()
current_time = now.strftime("%H:%M")
from datetime import date
date = datetime.today()
location1 = var1
city = location1
city = city + " weather"
city = city.replace(" ", "+")
res = requests.get(
     f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
    headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
location = soup.select('#wob_loc')[0].getText().strip()
time = soup.select('#wob_dts')[0].getText().strip()
info = soup.select('#wob_dc')[0].getText().strip()
weather = soup.select('#wob_tm')[0].getText().strip()
weekday = dt1.strftime('%A')

jarvis.say('hi sir. the date is {}, it is {} {}, the weather is {}, and the temperature is {} °Celcius'.format(today,weekday,current_time,info,weather))
jarvis.runAndWait()
print('jarvis : hi sir. the date is {} it is {} {}. the weather is {}. and the temperature is {} °Celcius'.format(today,weekday,current_time,info,weather))
class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = "MP4"


r = sr.Recognizer()
y = list(x.timetuple())

if y[3] > 12 and y[3] < 16:
    #/.greet good afternoon
    jarvis.say('good afternoon sir')
    jarvis.runAndWait()
    print('jarvis : good afternoon sir')

elif y[3] < 10:
    #/.greet good morning
    jarvis.say('good morning sir')
    jarvis.runAndWait()
    print('jarvis : good morning sir')

elif y[3] >= 16:
    #/.greet good evening
    jarvis.say('good evening sir')
    jarvis.runAndWait()
    print('jarvis : good evening sir')




def Load_GUI():
    from bs4 import BeautifulSoup
    import requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    from PyQt5 import QtCore, QtGui, QtWidgets
    from datetime import date
    date = date.today()
    date1 = str(date)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    class Ui_MainWindow(object):

        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(1121, 724)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(-170, 10, 1391, 781))
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap("C:/Users/PRACHEE/Downloads/jarvis_image.png"))
            self.label.setScaledContents(True)
            self.label.setObjectName("label")
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(900, 540, 75, 23))
            font = QtGui.QFont()
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(75)
            self.pushButton.setFont(font)
            self.pushButton.setStyleSheet("color: rgb(85, 170, 0);")
            self.pushButton.setObjectName("pushButton")
            self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_2.setGeometry(QtCore.QRect(990, 540, 75, 23))
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.pushButton_2.setFont(font)
            self.pushButton_2.setStyleSheet("color: rgb(255, 0, 0);")
            self.pushButton_2.setObjectName("pushButton_2")
            self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
            self.textBrowser.setGeometry(QtCore.QRect(410, 0, 256, 61))
            self.textBrowser.setStyleSheet("background:transparent\n"
                                           "color:white"
                                           "")

            self.textBrowser.setObjectName("textBrowser")
            self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
            self.textBrowser_2.setGeometry(QtCore.QRect(660, 0, 256, 61))
            self.textBrowser_2.setStyleSheet("background:transparent\n"
                                             "color:white"

                                             "")
            city = "vapi"
            city = city + " weather"
            city = city.replace(" ", "+")
            res = requests.get(
                f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
                headers=headers)

            soup = BeautifulSoup(res.text, 'html.parser')
            location = soup.select('#wob_loc')[0].getText().strip()
            time = soup.select('#wob_dts')[0].getText().strip()
            info = soup.select('#wob_dc')[0].getText().strip()
            weather = soup.select('#wob_tm')[0].getText().strip()

            city = var1
            city = city + " weather"
            holidays_india = holidays.India()

            self.textBrowser_2.setText('''current location : {}
        date : {}
        Current weather : {}
        Current time : {}
        Current holiday : {} '''.format(var1, date1, info,current_time,holidays_india.get(date)))

            self.textBrowser_2.setObjectName("textBrowser_2")
            self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
            self.textEdit.setGeometry(QtCore.QRect(780, 530, 111, 21))
            self.textEdit.setObjectName("textEdit")
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 21))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.pushButton.setText(_translate("MainWindow", "Run"))
            self.pushButton_2.setText(_translate("MainWindow", "terminate"))

    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())





while (1):


    try:

        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.2)

            audio2 = r.listen(source2)

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText)
            command = MyText
            date = date.today()



        if MyText == 'who are you':
            print('you : {}'.format(MyText))
            jarvis.say("i am jarvis i am made by professor Neil bhurke")
            jarvis.runAndWait()
            print('jarvis : i am jarvis i am made by professor Neil bhurke')




        elif MyText == 'what is your favourite food':
            print('you : {}'.format(MyText))
            jarvis.say("i like to eat pizza")
            jarvis.runAndWait()
            print('jarvis : i like to eat pizza')

        elif command == 'who is your favourite superhero':
            print('you : {}'.format(command))
            jarvis.say("iron man")
            jarvis.runAndWait()
            print('jarvis : iron man')

        elif command == 'sing a song for me':
            print('you : {}'.format(command))
            jarvis.say(
                "when in public wear a mask just a teeny weeny task it helps keep us safe and sound health care all around on your mouth and on your nose good to cover both of those")
            jarvis.runAndWait()
            print(
                'jarvis : when in public wear a mask just a teeny weeny task it helps keep us safe and sound health care all around on your mouth and on your nose good to cover both of those')

        elif command == 'who invented the letter 0':
            print('you : {}'.format(command))
            jarvis.say("Aryabhatt invented letter zero")
            jarvis.runAndWait()
            print('jarvis : Aryabhatt invented letter zero')

        elif command == 'what is a figure with 6 7 8 9 10 sides called':
            print('you : {}'.format(command))
            jarvis.say("Hexagon, Heptagon, Octagon, Nonagon, Decagon respectively")
            jarvis.runAndWait()
            print('jarvis : Hexagon, Heptagon, Octagon, Nonagon, Decagon respectively')

        elif command == 'in which country did the chess originate':
            print('you : {}'.format(command))
            jarvis.say("Chess was originated in the country India")
            jarvis.runAndWait()
            print('jarvis : Chess was originated in the country India')

        elif command == 'how many degrees are there in a circle':
            print('you : {}'.format(command))
            jarvis.say("360 degrees")
            jarvis.runAndWait()
            print('jarvis : 360 degrees')

        elif command == 'who is known as human computer':
            print('you : {}'.format(command))
            jarvis.say("shakuntala devi was know as human computer")
            jarvis.runAndWait()
            print('jarvis : shakuntala devi was known as human computer')

        elif command == 'how many seconds are there in an hour':
            print('you : {}'.format(command))
            jarvis.say("3600 seconds")
            jarvis.runAndWait()
            print('jarvis : 3600 seconds')

        elif command == 'what is the full form of bodmas':
            print('you : {}'.format(command))
            jarvis.say("Bracket Of Division Multiplication Addition Subtraction")
            jarvis.runAndWait()
            print('jarvis : Bracket Of Division Multiplication Addition Subtraction')

        elif command == 'which is the first computer in the world':
            print('you : {}'.format(command))
            jarvis.say("ENIAC computing system was the first computer in the world")
            jarvis.runAndWait()
            print('jarvis : ENIAC computing system was the first computer in the world')

        elif command == 'what is the full form of wi-fi':
            print('you : {}'.format(command))
            jarvis.say("wireless fidelity is full form of welifi")
            jarvis.runAndWait()
            print('jarvis : wireless fidelity is full form of welifi')

        elif command == 'who is the father of vaccination':
            print('you : {}'.format(command))
            jarvis.say("edward jenner is the father of vaccination")
            jarvis.runAndWait()
            print('jarvis : edward jenner is the father of vaccination')

        elif command == 'i am fine':
            print('you : {}'.format(command))
            jarvis.say("thats awosome!")
            jarvis.runAndWait()
            print('jarvis : thats awosome!')

        elif command == 'how are you so intelligent':
            print('you : {}'.format(command))
            jarvis.say("i am intelligent beacause of professor neil bhurke")
            jarvis.runAndWait()
            print('jarvis : i am intelligent beacause of professor neil bhurke')

        elif command == 'open google':
            print('you : {}'.format(command))
            jarvis.say('opening google')
            jarvis.runAndWait()
            print('opening google')
            webbrowser.open('https://www.google.com/')

        elif command == 'open python web page':
            jarvis.say("opening python web page")
            jarvis.runAndWait()
            webbrowser.open('https://www.python.org/')

        elif command == 'open arduino web page':
            jarvis.say("opening arduino web page")
            jarvis.runAndWait()
            webbrowser.open('https://www.arduino.cc/')

        elif command == 'open youtube':
            jarvis.say("opening youtube")
            jarvis.runAndWait()
            webbrowser.open('https://www.youtube.com/')

        elif command == 'open instructable':
            jarvis.say("opening instructables")
            jarvis.runAndWait()
            webbrowser.open('https://www.instructables.com/')

        elif command == 'ok jarvis you can quit':
            print('you : {}'.format(command))
            jarvis.say("ok sir,thanks for using me")
            jarvis.runAndWait()
            print('jarvis : ok sir, thanks for using me')
            break

        elif command == 'who is neil armstrong':
            print('you : {}'.format(command))
            jarvis.say(
                "Neil Armstrong was a NASA astronaut most famous for being the first person to walk on the moon, on July 20, 1969. Armstrong also flew on NASA's Gemini 8 mission in 1966. He retired from NASA in 1971 and remained active in the aerospace community, although he chose to keep mostly out of the public spotlight.")
            jarvis.runAndWait()
            print(
                'jarvis : Neil Armstrong was a NASA astronaut most famous for being the first person to walk on the moon, on July 20, 1969. Armstrong also flew on NASAs Gemini 8 mission in 1966. He retired from NASA in 1971 and remained active in the aerospace community, although he chose to keep mostly out of the public spotlight')

        elif command == 'close the browser':
            jarvis.say("closing browser")
            jarvis.runAndWait()
            os.system("taskkill /im chrome.exe /f")
            jarvis.say('successfully terminated chrome.exe')
            jarvis.runAndWait()

        elif command == 'send email':
            print('you : {}'.format(command))
            password = 'Jarvis@2022'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('jarvis.bot.neil@gmail.com', password)
            jarvis.say('sending email to girija')
            jarvis.runAndWait()
            jarvis.say('please tell what i should send to girija');
            jarvis.runAndWait()
            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.listen(source2)

                MyText1 = r.recognize_google(audio2)
                MyText1 = MyText1.lower()
                print(MyText1)
                command1 = MyText1
            server.sendmail('girijabhurke@gmail.com',
                            'languagesolutionscoaching@gmail.com',
                            command1)
            jarvis.say('succesfully sent email girija');
            jarvis.runAndWait();


        elif command == 'send email':
            print('you : {}'.format(command))

            password = 'Jarvis@2022'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            var3 = 'jarvis.bot.neil@gmail.com'
            server.starttls()
            server.login(var3, password)
            jarvis.say('sending email')
            jarvis.runAndWait()
            jarvis.say('please tell what i should send');
            jarvis.runAndWait()
            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.listen(source2)

                MyText2 = r.recognize_google(audio2)
                MyText2 = MyText2.lower()
                print(MyText2)
                command2 = MyText2
                var4 =  input('please enter the email ID from which you want to recieve the email : ')
            server.sendmail(var3,
                            var4,
                            command2)
            jarvis.say('succesfully sent email');
            jarvis.runAndWait();



        elif command == 'play music':
            print('you : {}'.format(command))
            jarvis.say('sir what should i play?')
            jarvis.runAndWait()
            print('jarvis : what should i play?')
            if command == 'play by your choice':
                print('you : {}'.format(command))
                jarvis.say('ok sir')
                jarvis.runAndWait()
                print('jarvis : ok sir')
                webbrowser.open('https://youtu.be/dQw4w9WgXcQ')

            elif command == 'play believer':
                print('you : {}'.format(command))
                jarvis.say('playing believer')
                jarvis.runAndWait()
                print('jarvis : playing believer')
                webbrowser.open('https://www.youtube.com/watch?v=W0DM5lcj6mw')
            elif command == 'play endurance theme song':
                print('you : {}'.format(command))
                jarvis.say('playing endurance theme song on youtube')
                jarvis.runAndWait()
                print('jarvis : playing endurance theme song on youtube')
                webbrowser.open('https://www.youtube.com/watch?v=Kd8MQX3lZoE')

            elif command == 'play my favourite song':
                print('you {}'.format(command));
                jarvis.say('ok sir searching Bella ciao on youtube');
                jarvis.runAndWait();
                jarvis.say('found Bella ciao on youtube');
                jarvis.runAndWait();
                webbrowser.open('https://youtu.be/dQw4w9WgXcQ');



        elif command == 'what is the weather today':
            print('you : {}'.format(command))
            jarvis.say('sir please tell what location i should show the whether')
            jarvis.runAndWait()
            print('sir please tell what location i should show the whether')
            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.listen(source2)

                MyText1 = r.recognize_google(audio2)
                MyText1 = MyText1.lower()
                print(MyText1)
                command1 = MyText1
            city = command1
            city = city + " weather"
            city = city.replace(" ", "+")
            res = requests.get(
                f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
                headers=headers)
            print("Searching...\n")
            jarvis.say('searching........')
            jarvis.runAndWait()
            soup = BeautifulSoup(res.text, 'html.parser')
            location = soup.select('#wob_loc')[0].getText().strip()
            time = soup.select('#wob_dts')[0].getText()
            info = soup.select('#wob_dc')[0].getText().strip()
            weather = soup.select('#wob_tm')[0].getText().strip()
            print(location)
            jarvis.say('your location is' + location)
            jarvis.runAndWait()
            print(current_time)
            jarvis.say('current time is ' + current_time)
            jarvis.runAndWait()
            print(info)
            jarvis.say('the weather is' + info)
            jarvis.runAndWait()
            print(weather + "°C")
            jarvis.say('and temperature is ' + weather + '°Celcius')
            jarvis.runAndWait()
            print("Have a Nice Day!")
            jarvis.say('have a nice day!')
            jarvis.runAndWait()

        elif command == 'turn volume up':
            print('you : {}'.format(command))
            pyautogui.press('volumeup')

        elif command == 'turn volume down':
            print('you : {}'.format(command))
            pyautogui.press('volumedown')

        elif command == 'turn volume mute':
            print('you : {}'.format(command))
            pyautogui.press('volumemute')

        elif command == 'show me the stock market of top 15 companies in the world':
            print('you : {}'.format(command))
            jarvis.say('loading stock market')
            jarvis.runAndWait()
            print('jarvis : loading stock market.........')
            webbrowser.open('https://www.moneycontrol.com/stocks/marketinfo/marketcap/bse/index.html')

        elif command == 'ok jarvis you can sleep now':
            print('you : {}'.format(command))
            jarvis.say('ok sir ,have a nice day ahead!')
            jarvis.runAndWait()
            break

        elif command == 'turn on':
            jarvis.say('sure,sir')
            jarvis.runAndWait()
            i="on"
            serialcomm1 = serial.Serial('COM49', 9600)
            serialcomm1.timeout = 1
            serialcomm1.write(i.encode())
            time.sleep(0.5)
            print(serialcomm1.readline().decode('ascii'))
            serialcomm1.close()




        elif command == 'turn off':

            jarvis.say('sure,sir')
            jarvis.runAndWait()
            i = 'off'
            serialcomm = serial.Serial('COM49', 9600)
            serialcomm.timeout = 1
            serialcomm.write(i.encode())
            time.sleep(0.5)
            print(serialcomm.readline().decode('ascii'))
            serialcomm.close()

        elif command == 'get daily news':
            def speak(str):
                from win32com.client import Dispatch
                speak = Dispatch('SAPI.SpVoice')
                speak.Speak(str)

            import requests
            from bs4 import BeautifulSoup
            import pyttsx3
            url = 'https://www.bbc.com/news'
            response = requests.get(url)
            bot = pyttsx3.init()
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('h3')
            for x in headlines:
                 speak(x.text.strip())
                 print(x.text.strip())

        elif command == 'show me the files of my latest project':
            print('you : {}'.format(command))
            im = Image.open(r"E:\jarvisgui\carproject.png")
            im.show()
            jarvis.say('this, is the car project. this project is about wireless data transmission or IOT, and fingerprint identification in a car, you can also see the GPS latitude and longitude, or google maps, via you sms in your mobile. you can see the C++ code files in a minute,thank you sir, and have a great day ahead')
            jarvis.runAndWait()
            import os
            os.startfile(r"E://jarvisgui/car_project.txt")

        elif command == 'search on google':
            jarvis.say('ok sir using json_-python library to search the web, please tell what should i search on google')
            jarvis.runAndWait()
            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.listen(source2)

                MyText1 = r.recognize_google(audio2)
                MyText1 = MyText1.lower()
                print(MyText1)
                command1 = MyText1
                target = command1
            kt.search(target)



        elif command == 'pause':
            jarvis.say('ok sir on pause mode you acn unpause bu saying unpause')
            jarvis.runAndWait()
            while(1):
                with sr.Microphone() as source2:
                    r.adjust_for_ambient_noise(source2, duration=0.2)

                    audio2 = r.listen(source2)

                    MyText1 = r.recognize_google(audio2)
                    MyText1 = MyText1.lower()
                    print(MyText1)
                    command1 = MyText1
                    if command1 == 'unpause':
                        break



        elif command == 'start my meeting':
            dt = datetime.now()
            if dt.isoweekday() == 1 or 2 or 3:

                webbrowser.open('https://meet.google.com/nrh-jgwz-gys')

                jarvis.say('ok sir, you are ready to join the meeting, best of luck for today sir!')
                jarvis.runAndWait()

            elif dt.isoweekday() == 5 or 6 or 7:

                webbrowser.open('https://meet.google.com/dga-cfbt-fgu')

                jarvis.say('ok sir, you are ready to join the meeting, best of luck for today sir!')
                jarvis.runAndWait()

        elif command == 'play while i wait':

            from playsound import playsound


            jarvis.say('loading hangman')
            jarvis.runAndWait()
            print('loading hangman......')
            import random


            def hangman():

                word = random.choice(
                    ["ironman", "hulk", "thor", "captainamerica", "clint", "loki", "avengers", "nick", "phil", "maria"])
                validLetters = 'abcdefghijklmnopqrstuvwxyz'
                turns = 10
                guessmade = ''

                while len(word) > 0:
                    main = ""
                    missed = 0

                    for letter in word:
                        if letter in guessmade:
                            main = main + letter
                        else:
                            main = main + "_" + " "
                    if main == word:
                        print(main)
                        print("You win!")
                        break

                    print("Guess the word:", main)
                    guess = input()

                    if guess in validLetters:
                        guessmade = guessmade + guess
                    else:
                        print("Enter a valid character")
                        guess = input()

                    if guess not in word:
                        turns = turns - 1
                        if turns == 9:
                            print("9 turns left")
                            print("  --------  ")
                        if turns == 8:
                            print("8 turns left")
                            print("  --------  ")
                            print("     O      ")
                        if turns == 7:
                            print("7 turns left")
                            print("  --------  ")
                            print("     O      ")
                            print("     |      ")
                        if turns == 6:
                            print("6 turns left")
                            print("  --------  ")
                            print("     O      ")
                            print("     |      ")
                            print("    /       ")
                        if turns == 5:
                            print("5 turns left")
                            print("  --------  ")
                            print("     O      ")
                            print("     |      ")
                            print("    / \     ")
                        if turns == 4:
                            print("4 turns left")
                            print("  --------  ")
                            print("   \ O      ")
                            print("     |      ")
                            print("    / \     ")
                        if turns == 3:
                            print("3 turns left")
                            print("  --------  ")
                            print("   \ O /    ")
                            print("     |      ")
                            print("    / \     ")
                        if turns == 2:
                            print("2 turns left")
                            print("  --------  ")
                            print("   \ O /|   ")
                            print("     |      ")
                            print("    / \     ")
                        if turns == 1:
                            print("1 turns left")
                            print("Last breaths counting, Take care!")
                            print("  --------  ")
                            print("   \ O_|/   ")
                            print("     |      ")
                            print("    / \     ")
                        if turns == 0:
                            print("You loose")
                            print("You let a kind man die")
                            print("  --------  ")
                            print("     O_|    ")
                            print("    /|\      ")
                            print("    / \     ")
                            break


            name = input("Enter your name")
            print("Welcome", name)
            print("-------------------")
            print("try to guess the word in less than 10 attempts")
            hangman()
            print()

        elif command == 'what is python':
            jarvis.say('''Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, 
                       as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages,
                        which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed, For more details please visit the following website''')
            jarvis.runAndWait()
            print('''Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, 
                       as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages,
                        which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed, For more details please visit the following website''')
            time.sleep(1)
            print('https://www.python.org/doc/essays/blurb/')


        elif command == 'load python browser':
            print('you : {}'.format(command))
            jarvis.say('ok sir. launching python browser')
            jarvis.runAndWait()
            print('jarvis : ok sir. launching python browser')
            from PyQt5.QtWidgets import *
            import sys
            from PyQt5.QtWebEngineWidgets import *
            from PyQt5.QtCore import *


            class MainWindow(QMainWindow):
                def __init__(self):
                    super(MainWindow, self).__init__()
                    self.browser = QWebEngineView()
                    self.browser.setUrl(QUrl('http://google.com'))
                    self.setCentralWidget(self.browser)
                    self.showMaximized()

                    navbar = QToolBar()
                    self.addToolBar(navbar)
                    back_btn = QAction('Back', self)
                    back_btn.triggered.connect(self.browser.back)
                    navbar.addAction(back_btn)

                    forward_btn = QAction('Forward', self)
                    forward_btn.triggered.connect(self.browser.forward)
                    navbar.addAction(forward_btn)

                    reload_btn = QAction('reload', self)
                    reload_btn.triggered.connect(self.browser.reload)
                    navbar.addAction(reload_btn)

                    home_btn = QAction('home', self)
                    reload_btn.triggered.connect(self.navigate_home)
                    navbar.addAction(home_btn)

                def navigate_home(self):
                    self.browser.setUrl(QUrl('http://google.com'))


            app = QApplication(sys.argv)
            QApplication.setApplicationName('Python Browser')
            window = MainWindow()
            app.exec_()


    except sr.RequestError as e:
        jarvis.say("Could not request results  {0}".format(e))
        jarvis.runAndWait()
        print('Could not request results {0}'.format(e))
        jarvis.say('critical system error system failed to respond. please wait till we reconnect you to jarvis.pys server. jarvis will be with you in a few minutes!');
        jarvis.runAndWait()
        print('critical system error system failed to respond. please wait till we reconnect you to jarvis.pys server. jarvis will be with you in a few minutes!');




    except sr.UnknownValueError:
        print('jarvis : unknown value error connection timed out while taking query from user')


    except SyntaxError:
        jarvis.say("something went wrong auto reload in 3.2.1")
        jarvis.runAndwait()
        print('jarvis : something went wrong auto reload in 3, 2, 1.')

    except TypeError:
        jarvis.say("something went wrong auto reload in 3.2.1")
        jarvis.runAndwait()
        print('jarvis : something went wrong auto reload in 3, 2, 1.')

    except IndentationError:
        jarvis.say("something went wrong auto reload in 3.2.1")
        jarvis.runAndwait()
        print('jarvis : something went wrong auto reload in 3, 2, 1.')

    except pywhatkit.core.exceptions.InternetException:
        jarvis.say('No Internet')
        jarvis.runAndWait()
        print('jarvis : No Internet')

    except:
        jarvis.say("something went wrong auto reload in 3.2.1")
        jarvis.runAndWait()
        print('jarvis : something went wrong auto reload in 3, 2, 1.')


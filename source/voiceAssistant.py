from datetime import date, datetime
from bs4.element import TemplateString
from bs4 import BeautifulSoup
from unidecode import unidecode
import speech_recognition
import pyttsx3
import wikipedia
import requests
import os
import subprocess

robotEar = speech_recognition.Recognizer()													# robotEar: bien nhan am thanh
robotMouth = pyttsx3.init()																	# robotMoutth: bien phat am thanh
robotBrain = ""																				# robotBrain: bien nhan noi dung phan hoi lai

def getWeather(str):
	place = str.split("weather")[1]
	search = f"temperature{place}"
	url = f"https://www.google.com/search?q={search}"
	r = requests.get(url)
	data = BeautifulSoup(r.text, "html.parser")
	temp = data.find("div",class_="BNeawe").text
	return temp

def getNews():
	#import what we need
	from requests_html import HTMLSession
	session = HTMLSession()
	#use session to get the page
	r = session.get('https://news.google.com/topstories?hl=vi&gl=VN&ceid=VN%3Avi')
	#render the html, sleep=1 to give it a second to finish before moving on. scrolldown= how many times to page down on the browser, to get more results. 5 was a good number here
	r.html.render(sleep=1, scrolldown=0)
	#find all the articles by using inspect element and create blank list
	articles = r.html.find('article')
	newslist = []
	#loop through each article to find the title and link. try and except as repeated articles from other sources have different h tags.
	for item in articles:
	    try:
	        newsitem = item.find('h3', first=True)
	        title = newsitem.text
	        link = newsitem.absolute_links
	        newsarticle = {
	            'title': unidecode(title),
	            'link': link 
	        }
	        newslist.append(unidecode(title))
	    except:
	       pass
	#print the length of the list
	for i in range(5):
	    print(newslist[i], end = '\n')

def openApp(name):								#hàm tìm đường dẫn và mở app
	appPath = ""
	for root, dirs, files in os.walk("C:\\"):
		if name in files:
			appPath = os.path.join(root, name)
	if(appPath):
		subprocess.call(appPath)
	else:
		global robotBrain
		robotBrain = "App not found"
while True:
	with speech_recognition.Microphone() as mic:		
		robotEar.adjust_for_ambient_noise(mic)
		print("robot: i'm listening")
		#audio = robotEar.listen(mic)
		audio = robotEar.record(mic, duration=5)
		
	try:
		you = robotEar.recognize_google(audio)
	except:
		you = ""
	you = you.lower()								#lowercase input để dễ so sánh 
	print("You: ", you)
	if you == "":
		robotBrain = "Sorry, please say again"
	elif "can you hear me" in you:
		robotBrain = "Yes, very clearly"
	elif "hello" in you:
		robotBrain = "Hi, Master"
	elif "who are you" in you:
		robotBrain = "I am Corona, your assistant"
	elif "girlfriend" in you:
		robotBrain = "not yet, may be soon"
	elif "today" in you:
		today = date.today()
		robotBrain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robotBrain = now.strftime("%H hours %M minutes %S seconds")
	elif "open" in you:
		if "notepad" in you:
			openApp("notepad.exe")
		elif "excel" in you:
			openApp("EXCEL.EXE")
		elif "powerpoint" in you:
			openApp("POWERPNT.EXE")
		elif "word" in you:
			openApp("WINWORD.EXE")
		elif "calculator" in you:
			openApp("calc.exe")
		elif "microsoft" in you and "edge" in you:
			openApp("msedge.exe")
		elif "chrome" in you:
			openApp("chrome.exe")
	elif "weather" in you:
		robotBrain = "The weather is: " + getWeather(you)
	elif "news" in you:
		robotBrain = "Here's you news"
		getNews()
	elif "bye" in you:
		robotBrain = "Good bye, Toan"
		voices = robotMouth.getProperty('voices')  
		robotMouth.setProperty('voice', voices[1].id)  
	
		robotMouth.say(robotBrain)
		robotMouth.runAndWait()
		break
	#elif "what is" or "what are" or "who are" or "who is" in you:
	else:
		try:
			robotBrain = wikipedia.summary(you, sentences = 2)
		except:
			robotBrain = "Can't find " + you
	#else:
	#	robotBrain = "Don't give up, do your best and the rest will come"
	
	print("RobotBrain: " + robotBrain)

	voices = robotMouth.getProperty('voices')  
	robotMouth.setProperty('voice', voices[1].id)  
	
	robotMouth.say(robotBrain)
	robotMouth.runAndWait()

 
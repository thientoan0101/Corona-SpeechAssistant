from datetime import date, datetime
import speech_recognition
import pyttsx3
import wikipedia
import os

robotEar = speech_recognition.Recognizer()													# robotEar: bien nhan am thanh
robotMouth = pyttsx3.init()																	# robotMoutth: bien phat am thanh
robotBrain = ""																				# robotBrain: bien nhan noi dung phan hoi lai

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
	elif "notepad" and "open" in you:
		os.system("notepad")
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

 
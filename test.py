#  University of Engineeering and Management, Jaipur
#  Department of Computer Science and Engineering , Artifical Intelligence and Machine Learning , Batch 2023-2027 
# editable link: https://prod.liveshare.vsengsaas.visualstudio.com/join?70F345567DC0DBE79AC4724D7594D1E7390C

import speech_recognition as sr 
import random     
import pyttsx3                 
import webbrowser                
import serial                    
import pywhatkit                  

robot_name = 'nova'

hi_words_u = ['hi', 'hello', 'namaskar']
bye_words_u = ['bye', 'tata', 'alvida']
hi_words = ['hi there', 'hello there', 'whats up boss']
bye_words = ['bye bye', 'cya' , 'sayonara']
r_u_there = ['are you there', 'you there']
jokes = ['What do kids play when their mom is using the phone? Bored games','Why are snails slow? Because they are carrying a house on their back','What’s the smartest insect? A spelling bee!','What does a storm cloud wear under his raincoat? Thunderwear','What is fast, loud and crunchy? A rocket chip','How does the ocean say hi? It waves!','What do you call a couple of chimpanzees sharing an Amazon account? PRIME-mates','Why did the teddy bear say no to dessert? Because she was stuffed']

engine = pyttsx3.init()                   
voices = engine.getProperty('voices')     
engine.setProperty('voice', voices[0].id)  
engine.setProperty('rate', 150)          

listener = sr.Recognizer()

def listen():
	try:
		with sr.Microphone() as source:                         # Microphone Access
			print("<<=TALK=>>")
			voice = listener.listen(source)                     # Microphone Listener
			command = listener.recognize_google(voice).lower()  # Google API
			command = command.lower()                          
			print(command)

			if (command.split(' ')[0] == robot_name):
				print("<<=REPLYING=>>")
				process(command)                 # call process funtion to take action
	except:
		pass

def process(words):
	print(words) 
	word_list = words.split(' ')[1:] 

	if word_list[0] == 'play':
		talk("Okay boss, playing")
		extension = ' '.join(word_list[1:])                   
		pywhatkit.playonyt(extension)          
		return

	elif word_list[0] == 'search':
		talk("Okay boss, searching")
		extension = ' '.join(word_list[1:])
		pywhatkit.search(extension)
		return

	elif word_list[0] == 'help':
		talk("Messaging emergency contacts about your situation")
		pywhatkit.sendwhatmsg_instantly("+91234567890", "This is an automated message by Nova,Subhranil has requested emergency help as soon as possible", 15, True, 4)

	# elif word_list[0] == 'details':
	# 	port.write(b'u')
	# 	port.write(b'i')
	# 	port.write(b'i')
	# 	talk("Hello I'm Nova, your energetic and helpful companion, designed by the brilliant minds of Team Sankalp! Im just 1 day old, but dont let my age fool you, i have got all the skills to keep things exciting and fun")
	# 	port.write(b'i')
	# 	port.write(b'u')
	# 	port.write(b'i')
	# 	port.write(b'h')
	# 	port.write(b'l')
	# 	talk("Here is what i can do. Say a friendly hi and wave you off with a bye. Help you out with searches when you're curious. Crack jokes that will make you giggle. Play some tunes to brighten your day. Open up applications and assist with tasks. Oh, and if you are looking for action, I can punch, smash, and throw an uppercut. You think i m not energetic enough, i can even do exercise. ")

	if word_list[0] == 'introduce':
		talk("Hello, I am Nova your personal companion bot, Here to assist you with your daily desktop duties")

	elif word_list[0] == 'joke':
		talk('Okay boss, here is a joke to enlighten your mood')
		talk(random.choice(jokes))
  
	# elif word_list[0] == 'love':
	# 	talk('I cant process love, but i do love you , sparkle')
	# 	port.write(b'l')
  
	elif word_list[0] == 'exercise':
		talk('Who took my dumbells')
  
	if (word_list[0] == 'get') and (word_list[1] == 'info'):
		talk("Okay, I am right on it")
		extension = ' '.join(word_list[2:])                   
		inf = pywhatkit.info(extension)
		talk(inf)                                              # Result       
		return

	elif word_list[0] == 'open':
		talk("Opening, sir")
		url = f"http://{''.join(word_list[1:])}"
		webbrowser.open(url)
		return

	for word in word_list:
		if word in hi_words_u:
			talk(random.choice(hi_words))

		elif word in bye_words_u:
			talk(random.choice(bye_words))


def talk(sentence):
	engine.say(sentence)
	engine.runAndWait()

while True:
    listen()
	

import pyttsx3

pyttsx3.speak("i will speak this text")

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id) #try 0,1,2,3___
engine.say("I changed my voice")
engine.runAndWait()

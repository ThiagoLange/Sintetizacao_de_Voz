import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 120)
engine.setProperty("volume", 1.)
engine.setProperty("voice", "brazil")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

frase = input("Digite a frase a ser falada:\n")
engine.say(frase)

engine.runAndWait()


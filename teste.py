import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 120)
engine.setProperty("volume", 1.)
engine.setProperty("voice", "brazil")
engine.say("Gabriel e Leticia vai estudar")

engine.runAndWait()
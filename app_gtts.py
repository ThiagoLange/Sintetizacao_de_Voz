from gtts import gTTS
from playsound import playsound
tts = gTTS('Leticia apura no banho', lang='pt-br')
tts.save('ola.mp3')
playsound('ola.mp3')
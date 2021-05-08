from gtts import gTTS
import os                          #ar= العربية 
tts = gTTS(text='مرحبا ', lang='ar')# en= english
tts.save("/sdcard/naciri.mp3")
os.system("/sdcard/naciri.mp3")
#god.mp3 # sdcard سوف يكون في 
#يمكن لك تغير إسم 

import random
from audioplayer import AudioPlayer
import os
import time
import _thread

CORRECT_ANSWERS_THRESHOLD = 3

math_solved = False
sound = AudioPlayer('./alarm.mp3')

def play_alarm():
    sound.play(loop=True, block=True)


os.system('vcgencmd display_power 1')
try:
    _thread.start_new_thread(play_alarm, ())
except:
    print("Thread Error")

correct_answers = 0
while correct_answers is not CORRECT_ANSWERS_THRESHOLD:
    problem = ""
    problem += str(random.randint(0, 15))
    problem += " + "
    problem += str(random.randint(-15, 15))
    answer = int(eval(problem))
    choice = int(input(problem + " = "))
    if choice is answer:
        correct_answers += 1

print('Bomb successfully diffused')
sound.stop()
os.system('vcgencmd display_power 0')

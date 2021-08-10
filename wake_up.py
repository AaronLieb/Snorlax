import playsound
import random
import os
import time
import _thread

CORRECT_ANSWERS_THRESHOLD = 3

math_solved = False

def play_alarm():
    while not math_solved:
        playsound.playsound('./alarm.mp3', True)


os.system('vcgencmd display_power 1')
try:
    _thread.start_new_thread(play_alarm, ())
except:
    print("Thread Error")

correct_answers = 0
while correct_answers is not CORRECT_ANSWERS_THRESHOLD - 1:
    problem = ""
    problem += str(random.randint(0, 15))
    problem += " + "
    problem += str(random.randint(-15, 15))
    answer = int(eval(problem))
    choice = int(input(problem + " = "))
    if choice is answer:
        correct_answers += 1

print('Bomb successfully diffused')
os.system('vcgencmd display_power 0')

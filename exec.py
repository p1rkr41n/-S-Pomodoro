from Set.SetCircle import Circle
from Set.SetLongBreak import LongRelax
from Set.SetShortBreak import ShortRelax
from Set.SetPomodoro import Pomodoro
import os
import time
import msvcrt
from playsound import playsound

class pomodoro:
    def __init__(self, time, short, long, round, option):
        self.time = Pomodoro(time)
        self.short = ShortRelax(short)
        self.long = LongRelax(long)
        self.round = Circle(round)
    def run(self):
        print("Wait 1s before Start")
        time.sleep(1)
        print(self.time)
        i=1
        try:
            while True:
                print("Starting pomodoro "+ str(i))
                print("In pomo: "+ str(self.time))
                time.sleep(self.time)
                playsound("ring.mp3")
                if i%self.round==0:
                    print("Long Relax " + str(self.long))
                    time.sleep(self.long)
                    playsound("ohno.wav")
                else:
                    print("Short Relax "+ str(self.short))
                    time.sleep(self.short)
                    playsound("ring.mp3")
                i+=1
        except :
            exit()

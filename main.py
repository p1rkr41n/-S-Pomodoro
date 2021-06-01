from time import process_time, sleep
from PyQt5.QtCore import pyqtRemoveInputHook
from exec import pomodoro as pomodoro
import gui3
import gui31
from threading import Thread
import os
import psutil
import sys

def worker1():
    gui3.run()
    #sys.exit(gui3)
def worker2():
    #pomodoro(25,5,25,4)
    gui31.run1()
def worker3():
    with open("setting.txt", "r+") as setter:
        getset = setter.readlines()
        valuer=[]
        for line in getset:
            valuer.insert(len(valuer), int(line.rstrip("\n")))
    pomodoro(valuer[0], valuer[1], valuer[2], valuer[3], valuer[4]).run()
if __name__ == "__main__":
    #print("buscu")
    worker1()
    #worker2()
    t2 =Thread(target = worker2)
    t3 =Thread(target = worker3)
    t2.start()
    t3.start()
    #Kill all process
    while True:
        sleep(1)
        if (t2.is_alive()== False):
            psutil.Process(os.getpid()).kill()
            break
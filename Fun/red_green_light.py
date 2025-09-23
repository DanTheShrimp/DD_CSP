#DD Period 7 For Fun :D

import time
import random
import sys
import keyboard
import threading

def placeholder():
    example = 0

def doll():
    towards = [
        "/----\\",
        "|*__*|",
        "\\____/"
    ]
    away = [
        "/----\\",
        "|    |",
        "\\____/"
    ]
    for item in towards:
        print(item)
    print("Green light in 3")
    time.sleep(3)
    for item in away:
        print(item)
    facing_away = True
    print("PRESS E TO RUN")
    while True:
        if keyboard.is_pressed("e"):
            advanced_player = 0
            advanced_player = advanced_player+1
            break
    print("Red light in 1")
    time.sleep(1)
    for item in towards:
        print(item)
    facing_away = False
    time_sleep = 5
    print(f"Green light in 5")
    timer = threading.Timer(5.0, )
    timer.start()
    while True:
        if keyboard.is_pressed('e'):
            print("You died!")
            sys.exit()
        else:
            timer.join()
            break
    for item in away:
        print(item)
    facing_away = True
    print("PRESS E TO RUN")
    e = input("").strip().upper()
    if e == "E":
        advanced_player = advanced_player+1
    for item in towards:
        print(item)
    random_time = random.randint(1, 5)
    print(f"Green light in {random_time}")
    time.sleep(random_time)
    for item in away:
        print(item)
    facing_away = True
    print("PRESS E TO RUN")
    e = input("").strip().upper()
    if e == "E":
        advanced_player = advanced_player+1
    if advanced_player >= 3:
        print("You win!")
        sys.exit()
    else:
        doll()
doll()

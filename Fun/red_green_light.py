#DD Period 7 For Fun :D

import time
import random
import sys
import keyboard

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
        if keyboard.is_pressed('e'):
            advanced_player = 0
            advanced_player = advanced_player+1
    print("Red light in 1")
    time.sleep(1)
    for item in towards:
        print(item)
    facing_away = False
    time_sleep = 5
    print(f"Green light in 5")
    def see_if_die(true):
        if true == False:
            random_time = 5
            while random_time > 0:
                it_is_red = input("").strip().upper()
                time.sleep(1)
                random_time = random_time-1
                if random_time == 0:
                    it_is_red = "G"
        if it_is_red == "E":
            died = True
        else:
            died = False
        return died
    if_died = see_if_die(False)
    if if_died == True:
        print("You died")
        sys.exit()
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
    if see_if_die(False) == True:
        print("You died")
        sys.exit()
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

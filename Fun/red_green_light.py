#DD Period 7 For Fun :D

import time
import random
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
    time.sleep(3)
    sleep = random.randint(5, 10)
    facing = 1
    for item in away:
        print(item)
doll()

import random
import sys
import time

def coin():
    coinanswer=random.randint(1,2)
    if coinanswer==1:
        coinanswer=str("heads")
    elif coinanswer==2:
        coinanswer=str("tails")
    else:
        print("Something went wrong.")
    time.sleep(1)
    print(f"The answer is {coinanswer}.")

def die():
    while True:
        sidesofdie=int(input("How many sides do you want on the die?\n"))
        if sidesofdie<=3:
            print("Choose a number higher than 3.")
        else:
            break
    dieanswer=random.randint(1,sidesofdie)
    print(f"The answer is {dieanswer}.")

def menu():
    menu=[
    "Coin Flip",
    "Numbered Die",
    "Random Card"
    ]
    cointranslated="placeholder"
    for item in menu:
        print(item)
        time.sleep(1)
    ques1=str(input("Which of the options above would you like to use?\n"))
    if "coin" in ques1:
        coin()
    elif "die" in ques1 or "dice" in ques1:
        die()

menu()
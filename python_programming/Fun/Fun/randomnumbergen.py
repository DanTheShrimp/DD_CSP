import random
import sys
import time

def menu():
    menu=[
        "Coin Flip",
        "Numbered Die",
        "Random Card"
    ]
    for item in menu:
        print(item)
        time.sleep(1)
    ques1=input("Which of the options above would you like to use?").strip
    if "coin" in ques1:
        coinanswer=random.randint(1,2)
        if coinanswer==1:
            coinanswer="heads"
        elif coinanswer==2:
            coinanswer="tails"
    time.sleep(1)
    print(f"The answer is {coinanswer}.")
    return 0

menu=[
    "Coin Flip",
    "Numbered Die",
    "Random Card"
]
cointranslated="placeholder"
for item in menu:
    print(item)
    time.sleep(1)
ques1=input("Which of the options above would you like to use?\n").strip
if ques1=="coin":
    coinanswer=random.randint(1,2)
if coinanswer==1:
    cointranslated='heads'
elif coinanswer==2:
    cointranslated='tails'
time.sleep(1)
print(f"The answer is {cointranslated}.")
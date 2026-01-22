import random
import time

def coin():
    coinanswer=random.randint(1,2)
    if coinanswer==1:
        coinanswer=str("heads")
    elif coinanswer==2:
        coinanswer=str("tails")
    else:
        print("Something went wrong.")
    print("Flipping...")
    time.sleep(1)
    print(f"The side is {coinanswer}.")

def die():
    loopthing=0
    while True:
        while True:
            try:
                loopthing=0
                sidesofdie=int(input("How many sides do you want on the die?\n"))
            except ValueError:
                print("Put in a non-decimal number.")
                time.sleep(0.5)
                loopthing=1
            if loopthing==0:
                break
        if sidesofdie<=3:
            print("Choose a number higher than 3.")
        else:
            break
    time.sleep(0.5)
    print("Rolling...")
    dieanswer=random.randint(1,sidesofdie)
    time.sleep(1)
    print(f"The number is {dieanswer}.")

def card():
    cardlist=["Ace of Spades","Two of Spades","Three of Spades","Four of Spades","Five of Spades","Six of Spades","Seven of Spades","Eight of Spades","Nine of Spades","Ten of Spades","Jack of Spades","Queen of Spades","King of Spades","Ace of Clubs","Two of Clubs","Three of Clubs","Four of Clubs","Five of Clubs","Six of Clubs","Seven of Clubs","Eight of Clubs","Nine of Clubs","Ten of Clubs","Jack of Clubs","Queen of Clubs","King of Clubs","Ace of Diamonds","Two of Diamonds","Three of Diamonds","Four of Diamonds","Five of Diamonds","Six of Diamonds","Seven of Diamonds","Eight of Diamonds","Nine of Diamonds","Ten of Diamonds","Jack of Diamonds","Queen of Diamonds","King of Diamonds","Ace of Hearts","Two of Hearts","Three of Hearts","Four of Hearts","Five of Hearts","Six of Hearts","Seven of Hearts","Eight of Hearts","Nine of Hearts","Ten of Hearts","Jack of Hearts","Queen of Hearts","King of Hearts","Joker","Joker"]
    print("Drawing a random card...")
    cardanswer=random.randint(1,54)
    time.sleep(1)
    print(f"The card is {cardlist[cardanswer]}.")

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
    while True:
        ques1=str(input("Which of the options above would you like to use?\n"))
        if "coin" in ques1:
            coin()
            break
        elif "die" in ques1 or "dice" in ques1:
            die()
            break
        elif "card" in ques1:
            card()
            break
        else:
            print("Choose a valid option.")
            time.sleep(0.5)

menu()
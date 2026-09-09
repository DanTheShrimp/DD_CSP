#Daniel Delong, Dice Roller
import time,random

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

def dice_roll(): #rolling a die
    typer("Which dice do you want to roll? Your options are D4, D6, D8, D10, D12, and D20.")

    while True: #we want to be able to loop this part just in case they don't input an answer we want
        diceroll_answer=input("").lower()
        time.sleep(0.75)

        #seeing if there is a 4, 6, 8, 10, 12, or 20 in their answer
        if "4" in diceroll_answer:
            diceroll_answer=4
            break
        elif "6" in diceroll_answer:
            diceroll_answer=6
            break
        elif "8" in diceroll_answer:
            diceroll_answer=8
            break
        elif "10" in diceroll_answer:
            diceroll_answer=10
            break
        elif "12" in diceroll_answer:
            diceroll_answer=12
            break
        elif "20" in diceroll_answer:
            diceroll_answer=20
            break
        else: #if there isn't then we loop and ask them to put in another answer
            typer("Please choose one of the options.")
            continue
    
    typer("How many of that dice do you want to roll?")

    while True:
        try:
            number_of_dice=int(input("")) #getting their input, making sure it is an integer
        except:
            typer("Please input a number.")
        else:
            break
    time.sleep(0.75)
    typer("Rolling the dice.")
    time.sleep(0.25)
    typer("...")
    time.sleep(0.25)
    typer("...")
    time.sleep(0.25)
    typer("...")
    time.sleep(1)
    #this rolls the dice one at a time, printing it immediately after it rolls the dice
    while number_of_dice>0:
        rolled_dice=random.randint(1,diceroll_answer)
        typer(f"The rolled number is {rolled_dice}.") #printing the answer
        number_of_dice-=1
        time.sleep(0.25)

dice_roll()
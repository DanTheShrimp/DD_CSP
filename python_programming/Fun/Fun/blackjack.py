import sys,time,random
#Make random number gen never pick the face down card, but before everything make the game pick a card, remove it, and set the face down as that card
cards=[
    " _____ \n"
    "|\\   /|\n"
    "| \\ / |\n"
    "|  &  |\n"
    "| / \\ |\n"
    "|/___\\|\n",

    " _____ \n"
    "|A .  |\n"
    "| /.\\ |\n"
    "|(_._)|\n"
    "|  |  |\n"
    "|____V|\n",

    " _____ \n"
    "|2    |\n"
    "|  ^  |\n"
    "|     |\n"
    "|  ^  |\n"
    "|____Z|\n",

    " _____ \n"
    "|3    |\n"
    "| ^ ^ |\n"
    "|     |\n"
    "|  ^  |\n"
    "|____E|\n",

    " _____ \n"
    "|4    |\n"
    "| ^ ^ |\n"
    "|     |\n"
    "| ^ ^ |\n"
    "|____h|\n",

    " _____ \n"
    "|5    |\n"
    "| ^ ^ |\n"
    "|  ^  |\n"
    "| ^ ^ |\n"
    "|____S|\n",

    " _____ \n"
    "|6    |\n"
    "| ^ ^ |\n"
    "| ^ ^ |\n"
    "| ^ ^ |\n"
    "|____9|\n",

    " _____ \n"
    "|7    |\n"
    "| ^ ^ |\n"
    "|^ ^ ^|\n"
    "| ^ ^ |\n"
    "|____L|\n",

    " _____ \n"
    "|8    |\n"
    "|^ ^ ^|\n"
    "| ^ ^ |\n"
    "|^ ^ ^|\n"
    "|____8|\n",

    " _____ \n"
    "|9    |\n"
    "|^ ^ ^|\n"
    "|^ ^ ^|\n"
    "|^ ^ ^|\n"
    "|____6|\n",

    " _____ \n"
    "|10 ^ |\n"
    "|^ ^ ^|\n"
    "|^ ^ ^|\n"
    "|^ ^ ^|\n"
    "|___0I|\n",

    " _____ \n"
    "|J  ww|\n"
    "| ^ {)|\n"
    "|(.)% |\n"
    "| | % |\n"
    "|__%%[|\n",
]

def menu():
    print("Welcome to Blackjack.")
    time.sleep(1)
    print(f"{cards[11]}")

menu()
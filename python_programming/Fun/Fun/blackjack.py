import sys,time,random
#Make random number gen never pick the face down card, but before everything make the game pick a card, remove it, and set the face down as that card
def typer(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01) 
    print()
deck=[
    [" _____ ",
    "|\\   /|",
    "| \\ / |",
    "|  &  |",
    "| / \\ |",
    "|/___\\|"],

    [" _____ ",
    "|A .  |",
    "| /.\\ |",
    "|(_._)|",
    "|  |  |",
    "|____V|"],

    [" _____ ",
    "|2    |",
    "|  ^  |",
    "|     |",
    "|  ^  |",
    "|____Z|"],

    [" _____ ",
    "|3    |",
    "| ^ ^ |",
    "|     |",
    "|  ^  |",
    "|____E|"],

    [" _____ ",
    "|4    |",
    "| ^ ^ |",
    "|     |",
    "| ^ ^ |",
    "|____h|"],

    [" _____ ",
    "|5    |",
    "| ^ ^ |",
    "|  ^  |",
    "| ^ ^ |",
    "|____S|"],

    [" _____ ",
    "|6    |",
    "| ^ ^ |",
    "| ^ ^ |",
    "| ^ ^ |",
    "|____9|"],

    [" _____ ",
    "|7    |",
    "| ^ ^ |",
    "|^ ^ ^|",
    "| ^ ^ |",
    "|____L|"],

    [" _____ ",
    "|8    |",
    "|^ ^ ^|",
    "| ^ ^ |",
    "|^ ^ ^|",
    "|____8|"],

    [" _____ ",
    "|9    |",
    "|^ ^ ^|",
    "|^ ^ ^|",
    "|^ ^ ^|",
    "|____6|"],

    [" _____ ",
    "|10 ^ |",
    "|^ ^ ^|",
    "|^ ^ ^|",
    "|^ ^ ^|",
    "|___0I|"],

    [" _____ ",
    "|J  ww|",
    "| ^ {)|",
    "|(.)% |",
    "| | % |",
    "|__%%[|"],

    [" _____ ",
    "|Q  ww|",
    "| ^ {(|",
    "|(.)%%|",
    "| |%%%|",
    "|_%%%O|"],

    [" _____ ",
    "|K  WW|",
    "| ^ {)|",
    "|(.)%%|",
    "| |%%%|",
    "|_%%%>|"],

    [" _____ ",
    "|A _  |",
    "| ( ) |",
    "|(_'_)|",
    "|  |  |",
    "|____V|"],

    [" _____ ",
    "|2    |",
    "|  &  |",
    "|     |",
    "|  &  |",
    "|____Z|"],

    [" _____ ",
    "|3    |",
    "| & & |",
    "|     |",
    "|  &  |",
    "|____E|"],

    [" _____ ",
    "|4    |",
    "| & & |",
    "|     |",
    "| & & |",
    "|____h|"],

    [" _____ ",
    "|5    |",
    "| & & |",
    "|  &  |",
    "| & & |",
    "|____S|"],

    [" _____ ",
    "|6    |",
    "| & & |",
    "| & & |",
    "| & & |",
    "|____9|"],

    [" _____ ",
    "|7    |",
    "| & & |",
    "|& & &|",
    "| & & |",
    "|____L|"],

    [" _____ ",
    "|8    |",
    "|& & &|",
    "| & & |",
    "|& & &|",
    "|____8|"],

    [" _____ ",
    "|9    |",
    "|& & &|",
    "|& & &|",
    "|& & &|",
    "|____6|"],

    [" _____ ",
    "|10 & |",
    "|& & &|",
    "|& & &|",
    "|& & &|",
    "|___0I|"],

    [" _____ ",
    "|J  ww|",
    "| o {)|",
    "|o o% |",
    "| | % |",
    "|__%%[|"],

    [" _____ ",
    "|Q  ww|",
    "| o {(|",
    "|o o%%|",
    "| |%%%|",
    "|_%%%O|"],

    [" _____ ",
    "|K  WW|",
    "| o {)|",
    "|o o%%|",
    "| |%%%|",
    "|_%%%>|"],

    [" _____ ",
    "|A_ _ |",
    "|( v )|",
    "| \\ / |",
    "|  .  |",
    "|____V|"],

    [" _____ ",
    "|2    |",
    "|  v  |",
    "|     |",
    "|  v  |",
    "|____Z|"],

    [" _____ ",
    "|3    |",
    "| v v |",
    "|     |",
    "|  v  |",
    "|____E|"],

    [" _____ ",
    "|4    |",
    "| v v |",
    "|     |",
    "| v v |",
    "|____h|"],

    [" _____ ",
    "|5    |",
    "| v v |",
    "|  v  |",
    "| v v |",
    "|____S|"],

    [" _____ ",
    "|6    |",
    "| v v |",
    "| v v |",
    "| v v |",
    "|____9|"],

    [" _____ ",
    "|7    |",
    "| v v |",
    "|v v v|",
    "| v v |",
    "|____L|"],

    [" _____ ",
    "|8    |",
    "|v v v|",
    "| v v |",
    "|v v v|",
    "|____8|"],

    [" _____ ",
    "|9    |",
    "|v v v|",
    "|v v v|",
    "|v v v|",
    "|____6|"],

    [" _____ ",
    "|10 v |",
    "|v v v|",
    "|v v v|",
    "|v v v|",
    "|___0I|"],

    [" _____ ",
    "|J  ww|",
    "|   {)|",
    "|(v)% |",
    "| v % |",
    "|__%%[|"],

    [" _____ ",
    "|Q  ww|",
    "|   {(|",
    "|(v)%%|",
    "| v%%%|",
    "|_%%%O|"],

    [" _____ ",
    "|K  WW|",
    "|   {)|",
    "|(v)%%|",
    "| v%%%|",
    "|_%%%>|"],

    [" _____ ",
    "|A ^  |",
    "| / \\ |",
    "| \\ / |",
    "|  v  |",
    "|____V|"],

    [" _____ ",
    "|2    |",
    "|  o  |",
    "|     |",
    "|  o  |",
    "|____Z|"],

    [" _____ ",
    "|3    |",
    "| o o |",
    "|     |",
    "|  o  |",
    "|____E|"],

    [" _____ ",
    "|4    |",
    "| o o |",
    "|     |",
    "| o o |",
    "|____h|"],

    [" _____ ",
    "|5    |",
    "| o o |",
    "|  o  |",
    "| o o |",
    "|____S|"],

    [" _____ ",
    "|6    |",
    "| o o |",
    "| o o |",
    "| o o |",
    "|____9|"],

    [" _____ ",
    "|7    |",
    "| o o |",
    "|o o o|",
    "| o o |",
    "|____L|"],

    [" _____ ",
    "|8    |",
    "|o o o|",
    "| o o |",
    "|o o o|",
    "|____8|"],

    [" _____ ",
    "|9    |",
    "|o o o|",
    "|o o o|",
    "|o o o|",
    "|____6|"],

    [" _____ ",
    "|10 o |",
    "|o o o|",
    "|o o o|",
    "|o o o|",
    "|___0I|"],

    [" _____ ",
    "|J  ww|",
    "| /\\{)|",
    "| \\/% |",
    "|   % |",
    "|__%%[|"],

    [" _____ ",
    "|Q  ww|",
    "| /\\{(|",
    "| \\/%%|",
    "|  %%%|",
    "|_%%%O|"],

    [" _____ ",
    "|K  WW|",
    "| /\\{)|",
    "| \\/%%|",
    "|  %%%|",
    "|_%%%>|"],
]
blank=[
    "       ",
    "       ",
    "       ",
    "       ",
    "       ",
    "       "
]
house_hand=[]
player_hand=[]
unknown_card=random.randint(1,52)
house_hand.append(deck[unknown_card])
del deck[unknown_card]
if "A" in house_hand[0][1]:
    uc_value="A"
elif "J" in house_hand[0][1] or "Q" in house_hand[0][1] or "K" in house_hand[0][1]:
    uc_value=10
elif "2" in house_hand[0][1]:
    uc_value=2
elif "3" in house_hand[0][1]:
    uc_value=3
elif "4" in house_hand[0][1]:
    uc_value=4
elif "5" in house_hand[0][1]:
    uc_value=5
elif "6" in house_hand[0][1]:
    uc_value=6
elif "7" in house_hand[0][1]:
    uc_value=7
elif "8" in house_hand[0][1]:
    uc_value=8
elif "9" in house_hand[0][1]:
    uc_value=9
elif "10" in house_hand[0][1]:
    uc_value=10

player_card0=random.randint(1,51)
player_card0=2
player_hand.append(deck[player_card0])
del deck[player_card0]
if "A" in player_hand[0][1]:
    pc0_value="A"
elif "J" in player_hand[0][1] or "Q" in player_hand[0][1] or "K" in player_hand[0][1]:
    pc0_value=10
elif "2" in player_hand[0][1]:
    pc0_value=2
elif "3" in player_hand[0][1]:
    pc0_value=3
elif "4" in player_hand[0][1]:
    pc0_value=4
elif "5" in player_hand[0][1]:
    pc0_value=5
elif "6" in player_hand[0][1]:
    pc0_value=6
elif "7" in player_hand[0][1]:
    pc0_value=7
elif "8" in player_hand[0][1]:
    pc0_value=8
elif "9" in player_hand[0][1]:
    pc0_value=9
elif "10" in player_hand[0][1]:
    pc0_value=10

house_card0=random.randint(1,50)
house_hand.append(deck[house_card0])
del deck[house_card0]
if "A" in house_hand[1][1]:
    hc0_value="A"
elif "J" in house_hand[1][1] or "Q" in house_hand[1][1] or "K" in house_hand[1][1]:
    hc0_value=10
elif "2" in house_hand[1][1]:
    hc0_value=2
elif "3" in house_hand[1][1]:
    hc0_value=3
elif "4" in house_hand[1][1]:
    hc0_value=4
elif "5" in house_hand[1][1]:
    hc0_value=5
elif "6" in house_hand[1][1]:
    hc0_value=6
elif "7" in house_hand[1][1]:
    hc0_value=7
elif "8" in house_hand[1][1]:
    hc0_value=8
elif "9" in house_hand[1][1]:
    hc0_value=9
elif "10" in house_hand[1][1]:
    hc0_value=10

player_card1=random.randint(1,49)
player_card1=14
player_hand.append(deck[player_card1])
del deck[player_card1]
if "A" in player_hand[1][1]:
    pc1_value="A"
elif "J" in player_hand[1][1] or "Q" in player_hand[1][1] or "K" in player_hand[1][1]:
    pc1_value=10
elif "2" in player_hand[1][1]:
    pc1_value=2
elif "3" in player_hand[1][1]:
    pc1_value=3
elif "4" in player_hand[1][1]:
    pc1_value=4
elif "5" in player_hand[1][1]:
    pc1_value=5
elif "6" in player_hand[1][1]:
    pc1_value=6
elif "7" in player_hand[1][1]:
    pc1_value=7
elif "8" in player_hand[1][1]:
    pc1_value=8
elif "9" in player_hand[1][1]:
    pc1_value=9
elif "10" in player_hand[1][1]:
    pc1_value=10

def player_part():
    split_able="no"
    if pc0_value=="A" and pc1_value=="A":
        typer(f"Your total card value is 2 or 12.")
    elif pc0_value=="A":
        if pc1_value+11==21:
            typer("Blackjack! You win.")
            sys.exit()
        else:
            typer(f"Your total card value is {pc1_value+1} or {pc1_value+11}")
    elif pc1_value=="A":
        if pc0_value+11==21:
            typer("Blackjack! You win.")
            sys.exit()
        else:
            typer(f"Your total card value is {pc0_value+1} or {pc0_value+11}")
    else:
        typer(f"Your total card value is {pc0_value+pc1_value}")
    if pc0_value==pc1_value:
        split_able="yes"
    while True:
        if split_able=="yes":
            will_split=input("You are able to split because you're card values are equal. Do you want to split?\n")
            if "yes" in will_split:
                typer("Hitting on both.")
                typer("House's cards: Your cards:")
                time.sleep(0.5)
                player_card2=random.randint(1,48)
                player_hand.append(deck[player_card2])
                del deck[player_card2]
                if "A" in player_hand[2][1]:
                    pc2_value="A"
                elif "J" in player_hand[2][1] or "Q" in player_hand[2][1] or "K" in player_hand[2][1]:
                    pc2_value=10
                elif "2" in player_hand[2][1]:
                    pc2_value=2
                elif "3" in player_hand[2][1]:
                    pc2_value=3
                elif "4" in player_hand[2][1]:
                    pc2_value=4
                elif "5" in player_hand[2][1]:
                    pc2_value=5
                elif "6" in player_hand[2][1]:
                    pc2_value=6
                elif "7" in player_hand[2][1]:
                    pc2_value=7
                elif "8" in player_hand[2][1]:
                    pc2_value=8
                elif "9" in player_hand[2][1]:
                    pc2_value=9
                elif "10" in player_hand[2][1]:
                    pc2_value=10

                player_card3=random.randint(1,47)
                player_hand.append(deck[player_card3])
                del deck[player_card3]
                if "A" in player_hand[3][1]:
                    pc3_value="A"
                elif "J" in player_hand[3][1] or "Q" in player_hand[3][1] or "K" in player_hand[3][1]:
                    pc3_value=10
                elif "2" in player_hand[3][1]:
                    pc3_value=2
                elif "3" in player_hand[3][1]:
                    pc3_value=3
                elif "4" in player_hand[3][1]:
                    pc3_value=4
                elif "5" in player_hand[3][1]:
                    pc3_value=5
                elif "6" in player_hand[3][1]:
                    pc3_value=6
                elif "7" in player_hand[3][1]:
                    pc3_value=7
                elif "8" in player_hand[3][1]:
                    pc3_value=8
                elif "9" in player_hand[3][1]:
                    pc3_value=9
                elif "10" in player_hand[3][1]:
                    pc3_value=10
                printer_helper=0
                for item in deck[0]:
                    print(f" {item}        {player_hand[0][printer_helper]}   {player_hand[1][printer_helper]}")
                    printer_helper+=1
                printer_helper=0
                for item in blank:
                    print(f" {item}        {player_hand[2][printer_helper]}   {player_hand[3][printer_helper]}")
                    printer_helper+=1
                if pc0_value=="A" and pc2_value=="A":
                    typer(f"Your total card value for pair one is 2 or 12.")
                elif pc2_value=="A":
                    if pc0_value+11==21:
                        typer("Blackjack! That pair is now locked.")
                        pair1_locked="yes"
                    else:
                        typer(f"Your total card value for pair one is {pc0_value+1} or {pc0_value+11}.")
                        pair1_locked="no"
                elif pc0_value=="A":
                    if pc2_value+11==21:
                        typer("Blackjack! That pair is now locked.")
                        pair1_locked="yes"
                    else:
                        typer(f"Your total card value for pair one is {pc2_value+1} or {pc2_value+11}.")
                        pair1_locked="no"
                elif pc1_value=="A" and pc3_value=="A":
                    typer(f"Your total card value for pair two is 2 or 12.")
                elif pc3_value=="A":
                    if pc1_value+11==21:
                        typer("Blackjack! That pair is now locked.")
                        pair2_locked="yes"
                    else:
                        typer(f"Your total card value is {pc1_value+1} or {pc1_value+11}.")
                        pair2_locked="no"
                elif pc1_value=="A":
                    if pc3_value+11==21:
                        typer("Blackjack! That pair is now locked.")
                        pair2_locked="yes"
                    else:
                        typer(f"Your total card value is {pc3_value+1} or {pc3_value+11}.")
                        pair2_locked="no"
                else:
                    typer(f"Your total card value for pair one is {pc0_value+pc2_value}.")
                    typer(f"Your total card value for pair two is {pc1_value+pc3_value}.")
        break

def menu():
    typer("Welcome to Blackjack.")
    time.sleep(0.75)
    typer("Here are the rules:")
    time.sleep(0.5)
    typer("1: You will be given 2 cards, hitting means you get another card; standing means you stop. The House will have 2 cards, but one will be hidden.")
    time.sleep(0.25)
    typer("2: Number cards are their own number in value.")
    time.sleep(0.25)
    typer("3: Aces are worth 1 or 11, Face cards are worth 10.")
    time.sleep(0.25)
    typer("4: Always assume the House has a 10 hidden.")
    time.sleep(0.25)
    typer("5: Do not go over 21, or you bust and lose.")
    time.sleep(1)

    typer("House's cards: Your cards:")
    time.sleep(0.5)
    printer_helper=0
    for item in deck[0]:
        print(f" {item}        {player_hand[0][printer_helper]}")
        printer_helper=printer_helper+1
    printer_helper=0
    for item in house_hand[0]:
        print(f" {item}        {player_hand[1][printer_helper]}")
        printer_helper=printer_helper+1
    player_part()

menu()
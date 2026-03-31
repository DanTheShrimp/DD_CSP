import sys, time, random
#SEVEN CARD CHARLIE!!!
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

house_hand=[]
player_hand=[
    ["       ",
    "       ",
    "       ",
    "       ",
    "       ",
    "       "]
]
player_value_history=[]
house_value_history=[]
current_player_value=0
current_house_value=0

def typer(text):
    for char in text:
        print(char, end="")
        time.sleep(0.01)
    print()

def house_valuefinder(card):
    decklen=len(deck)
    chosenh_card=random.randint(1,decklen-1)
    house_hand.append(deck[chosenh_card])
    del deck[chosenh_card]
    if "A" in house_hand[card][1]:
        hc_value=1
    elif "J" in house_hand[card][1] or "Q" in house_hand[card][1] or "K" in house_hand[card][1]:
        hc_value=10
    elif "2" in house_hand[card][1]:
        hc_value=2
    elif "3" in house_hand[card][1]:
        hc_value=3
    elif "4" in house_hand[card][1]:
        hc_value=4
    elif "5" in house_hand[card][1]:
        hc_value=5
    elif "6" in house_hand[card][1]:
        hc_value=6
    elif "7" in house_hand[card][1]:
        hc_value=7
    elif "8" in house_hand[card][1]:
        hc_value=8
    elif "9" in house_hand[card][1]:
        hc_value=9
    elif "10" in house_hand[card][1]:
        hc_value=10
    return hc_value

def player_valuefinder(card):
    decklen=len(deck)
    chosenp_card=random.randint(1,decklen-1)
    player_hand.append(deck[chosenp_card])
    del deck[chosenp_card]
    if "A" in player_hand[card][1]:
        hp_value=1
    elif "J" in player_hand[card][1] or "Q" in player_hand[card][1] or "K" in player_hand[card][1]:
        hp_value=10
    elif "2" in player_hand[card][1]:
        hp_value=2
    elif "3" in player_hand[card][1]:
        hp_value=3
    elif "4" in player_hand[card][1]:
        hp_value=4
    elif "5" in player_hand[card][1]:
        hp_value=5
    elif "6" in player_hand[card][1]:
        hp_value=6
    elif "7" in player_hand[card][1]:
        hp_value=7
    elif "8" in player_hand[card][1]:
        hp_value=8
    elif "9" in player_hand[card][1]:
        hp_value=9
    elif "10" in player_hand[card][1]:
        hp_value=10
    return hp_value

def custom_printer(hidden):
    printer_helper=0
    def seven_card_charlieplayer():
        try:        
            print(player_hand[1][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(player_hand[2][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(player_hand[3][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(player_hand[4][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(player_hand[5][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(player_hand[6][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(player_hand[7][printer_helper])
        except IndexError:
            print(player_hand[0][0])

    def seven_card_charliehouse(hidden):
        if hidden=="yes":
            try:        
                print(deck[0][printer_helper], end=" ")
            except IndexError:
                print(player_hand[0][0], end=" ")
        if hidden=="no":
            try:        
                print(house_hand[0][printer_helper], end=" ")
            except IndexError:
                print(player_hand[0][0], end=" ")
        try:
            print(house_hand[1][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(house_hand[2][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(house_hand[3][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(house_hand[4][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(house_hand[5][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(house_hand[6][printer_helper])
        except IndexError:
            print(player_hand[0][0])
    typer("House cards:")
    time.sleep(0.5)
    for item in player_hand[0]:
        if hidden=="yes":
            try:
                seven_card_charliehouse("yes")
                printer_helper+=1
            except IndexError:
                print(item)
        if hidden=="no":
            try:
                seven_card_charliehouse("no")
                printer_helper+=1
            except IndexError:
                print(item)
    printer_helper=0
    typer("Your cards:")
    time.sleep(0.5)
    for item in player_hand[0]:
        try:
            seven_card_charlieplayer()
            printer_helper+=1
        except IndexError:
            print(item)

pcard_1=player_valuefinder(1)
hcard_1=house_valuefinder(0)

pcard_2=player_valuefinder(2)
hcard_2=house_valuefinder(1)

def win(who):
    won=[
    "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|             You win!              |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
    ]
    lost=[
    "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|             You lost!             |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
    ]
    if who=="p":
        for item in won:
            print(item)
        sys.exit()
    elif who=="h":
        for item in lost:
            print(item)
        sys.exit()

def win_checker_forstart(first_num, second_num):
    win=0
    if first_num==1 and second_num==10:
        win=1
    elif first_num==10 and second_num==1:
        win=1
    return win

def total_value_calculator(first_num, second_num, who):
    lost=0
    if first_num+second_num>21:
        lost=1
    else:
        total=first_num+second_num
        who.append(total)
    return lost

if win_checker_forstart(pcard_1, pcard_2)==1:
    win("p")
elif win_checker_forstart(hcard_1, hcard_2)==1:
    win("h")

def player_value_calculator(firstnum, secondnum):
    current_player_value=firstnum+secondnum
    player_value_history.append(current_player_value)
    return current_player_value

def value_printer(who):
    if who=="p":
        typer("Your current total card value is: ")
        time.sleep(0.25)
        typer(str(current_player_value))
    elif who=="h":
        typer("The house's total card value is: ")
        time.sleep(0.25)
        typer(str(current_house_value))

typer("Welcome to Blackjack.")
time.sleep(0.5)
typer("Here are the rules of this game:")
time.sleep(0.5)
typer("1. The goal is to get as close to 21 without going over. If you start with an Ace and another card worth 10, you win instantly.")
time.sleep(0.75)
typer("2. Face cards are worth 10, and Aces are worth 1. Number cards are worth themselves.")
time.sleep(0.75)
typer("3. If you reach 7 cards without going over 21, you automatically win. This rule is called Seven Card Charlie, and it also affects the house.")
time.sleep(0.75)
typer("4. During your turn, you can hit or stand. Hitting means you want another card, and standing means you stop.")
time.sleep(0.75)
typer("5. The house will continuously hit until they reach 17 or any number higher than 17.")
time.sleep(1.5)
typer("Let's begin.")
time.sleep(0.5)
custom_printer("yes")
current_player_value=player_value_calculator(pcard_1,pcard_2)
value_printer("p")

def player_turn(player_value_helper):
    def hit_stand_sequence():
        while True:
            time.sleep(0.75)
            typer("Do you want to hit or stand?")
            try:
                hit_or_stand=input(str(""))
            except ValueError:
                time.sleep(0)

            if "hit" in hit_or_stand and "stand" in hit_or_stand:
                time.sleep(0)
            else:
                if "hit" in hit_or_stand:
                    hit_or_stand="hit"
                    break
                elif "stand" in hit_or_stand:
                    hit_or_stand="stand"
                    break
        return hit_or_stand
    answer=hit_stand_sequence()
    if answer=="hit":
        next_pcard=player_valuefinder(player_value_helper)
        custom_printer("yes")
        player_value_calculator(player_value_history[player_value_helper-3],next_pcard)
        current_player_value=player_value_history[player_value_helper-2]
        typer("Your current total card value is: ")
        time.sleep(0.25)
        typer(str(current_player_value))

player_turn(3)
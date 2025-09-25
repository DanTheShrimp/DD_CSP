#DD Period 7 Build a Game monster designs

import time
import sys
import random
goblin = [
"/|___|\\",
"|o\\ /o|",
"\\__^__/"
]
goblin_hurt = [
"/|___|\\",
"|>\\ /o|",
"\\__^__/"
]
goblin_dead = [
"/|___|\\",
"|/x x\\|",
"\\__o__/"
]
bandit = [
"/*****\\",
"|o\\`/o|",
"\\__w__/"
]
bandit_hurt = [
"/*****\\",
"|>\\`/o|",
"\\__w__/"
]
bandit_dead = [
"/*****\\",
"|/x`x\\|",
"\\__o__/"
]
boss = [
"   /\\   ",
" _/ii\\_ ",
" /0``0\\ ",
" | ~~ |",
" ######",
"  #### ",
"   ##  "
]
boss_hurt = [
"   /\\   ",
" _/ii\\_ ",
" />``0\\ ",
" | ~~ |",
" ######",
"  #### ",
"   ##  "
]
boss_dead = [
"   /\\   ",
" _/ii\\_ ",
" /x``x\\ ",
" | ~~ |",
" ######",
"  #### ",
"   ##  "
]

def goblin_encounter():
    time.sleep(2)
    print("Oh no! A goblin has appeared and is ready to attack!")
    for item in goblin:
        print(item)
    time.sleep(2)
    while True:
        e = input("Press E to roll initiative. ").strip().upper()
        if e == "E":
            player_initiative = random.randint(1,20)
            break
    enemy_initiative = random.randint(1,20)
    if enemy_initiative > player_initiative:
        print(f"Your initiative, {player_initiative}, is lower than the goblin's initiative. The goblin will go first.")
        who_first = "Goblin"
    elif enemy_initiative < player_initiative:
        print(f"Your initiative, {player_initiative}, is higher than the goblin's initiative. You will go first.")
        who_first = "Player"
    elif enemy_initiative == player_initiative:
        print(f"Your initiative, {player_initiative}, is the same as the goblin's initiative. You will go first.")
        who_first = "Player"
    if who_first == "Goblin":
        print("The goblin leaps foward and swings their crude sword at you. You attempt to dodge and fail. Your current health is 10.")
        current_hp = 10
    elif who_first == "Player":
        while True:
            weapon_choosing = input("What weapon would you like to use? You have a shortsword and shortbow in your inventory. ").strip().capitalize()
            if weapon_choosing == "Shortbow":
                weapon_choice = "shortbow"
                break
            elif weapon_choosing == "Shortsword":
                weapon_choice = "sword"
                break
        print(f"You have chosen the {weapon_choice}.")
        if weapon_choice == "shortbow":
            damage = {random.randint(1,6)+1}
            print(f"You loosed an arrow from your {weapon_choice}, dealing {damage} damage.")
            for item in goblin_hurt:
                print(item)
            goblin_hp = 10-damage

goblin_encounter()
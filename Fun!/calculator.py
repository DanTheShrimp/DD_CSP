#DD Period 7 for fun :D

import random
import sys

random_number = random.randint(1, 10)
if random_number == 7:
    print("RAAAAARRGGHHHH!!!!!!!!")
    sys.exit()

first_number = int(input("What is the first number?\n"))
middle_thing = input("What is the operation? (+,-,/, *, or **)\n")
last_number = int(input("What is the last number?\n"))

if middle_thing == "+":
    print(first_number+last_number)

elif middle_thing == "-":
    print(first_number-last_number)

elif middle_thing == "/":
    print(first_number/last_number)

elif middle_thing == "*":
    print(first_number*last_number)

elif middle_thing == "**":
    print(first_number**last_number)

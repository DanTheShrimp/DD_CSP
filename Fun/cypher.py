#Daniel DeLong, Cypher
import sys,time,random

"""letter=input("Give me a letter: ")
letter=letter[0].lower()
number_value=ord(letter)
number_value+=2
new_letter=chr(number_value)
print(f"Your new letter is {new_letter}.")"""

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")
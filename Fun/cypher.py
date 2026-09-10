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

typer("Input a sentence for me, make it as long as you want.")
sentence=input("")
changed_sentence=[]

loop_helper=0
change_it_by=random.randint(1,50)
while True:
    try:
        chosen_letter=sentence[loop_helper]
        letter_value=ord(chosen_letter)
        letter_value+=change_it_by
        changed_sentence.append(chr(letter_value))
    except:
        break
    else:
        loop_helper+=1

time.sleep(0.75)
full_sentence="".join(changed_sentence)
typer(f"The sentence was shifted up one ascii character {change_it_by} times.")
time.sleep(1)
typer("Your new sentence is:\n")
time.sleep(1)
typer(full_sentence)
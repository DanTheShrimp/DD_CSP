#Daniel DeLong, Idiot Proof
import time

def typer(text):
    for char in text:
        print(char,end="")
        time.sleep(0.05)
    print("")

while True:
    typer("What is your first name?")
    first_name=input("").strip().title() #get their input, strip it of trailing white space, and make the first letter of every word capital
    time.sleep(0.75)
    typer("And what is your last name?")
    last_name=input("").strip().title()
    time.sleep(0.75)
    while True:
        try:
            typer("Please input your phone number, no dashes.")
            phone_number=int(input("")) #get their input, and make sure it's an integer
        except:
            time.sleep(0)
        else:
            phone_number=list(str(phone_number)) #turn the player's input into a string and then into a list
            if len(phone_number)==10: #if the new list is exactly 10 items long
                first_phone_part="".join(phone_number[0:3]) #set the first phone part to the 1st through 3rd numbers
                second_phone_part="".join(phone_number[3:6]) #set the second phone part to the 4th through 6th numbers
                third_phone_part="".join(phone_number[6:10]) #set the third phone part to the 7th through 10th numbers
                full_phone_number=first_phone_part+"-"+second_phone_part+"-"+third_phone_part #concatinate everything with dashes inbetween
                break
    time.sleep(0.75)
    while True:
        try:
            typer("Now please put in your gpa.")
            gpa=float(input("")) #get their input, and make sure it's a float, or decimal number
        except:
            time.sleep(0)
        else:
            break
    time.sleep(0.75)
    typer(f"Hello, {first_name+" "+last_name}. Just to confirm, your phone number is {full_phone_number}, and your GPA is {round(gpa,1)}?") #concatinate the first and last name, type the full phone number, and round their gpa input to the first decimal place
    is_it_correct=input("")
    time.sleep(1)
    if "ye" in is_it_correct or "yu" in is_it_correct: #we do "ye" and "ya" just in case if they say yep, yup, yessir, yeppity, etc
        typer("Great, we'll add it to our databases so we can sell your personal information to the highest bidder.")
        break #break the loop, so basically end the program
    else:
        continue #loop
#Daniel DeLong, Idiot Proof
import time


name=input("What is your name: ").title().strip()
while True:
    try:
        phone_number=int(input("Please input your phone number, no dashes: "))
    except:
        time.sleep(0)
    else:
        phone_number=str(phone_number)
        phone_number=list(phone_number)
        if len(phone_number)==10:
            first_phone_part="".join(phone_number[0:3])
            second_phone_part="".join(phone_number[3:6])
            third_phone_part="".join(phone_number[6:10])
            full_phone_number=first_phone_part+"-"+second_phone_part+"-"+third_phone_part
            break
while True:
    try:
        gpa=float(input("Now please put in your gpa: "))
    except:
        time.sleep(0)
    else:
        break

print(f"Hello, {name}. Just to confirm, your phone number is {full_phone_number}, and your GPA is {round(gpa,1)}")
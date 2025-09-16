#DD Period 7 Financial Calculator, but updated!

import sys #this is going to be used later on
print("Hello! I am your personal financial calculator. Please type in all of the information I require.")

def get_stuff(request):
    if request == "income":
        result = float(input("How much do you make each month?\n"))

    elif request == "rent" or "transportation":
        result = float(input(f"How much does your {request} cost?\n"))

    elif request == "utilities" or "groceries":
        result = float(input(f"How much do your {request} cost?\n"))

    return result

income = get_stuff("income")
rent = get_stuff("rent")
utilities = get_stuff("utilities")
groceries = get_stuff("groceries")
transportation = get_stuff("transportation")

savings = income*0.1
income_left_after_savings = income*0.9

income_left = income_left_after_savings-(rent+utilities+groceries+transportation)
total_expenses = rent+utilities+groceries+transportation

if income_left_after_savings < total_expenses:
    print("I am unable to help you. Your finances are in ruins.")
    end = 1

elif income_left_after_savings > total_expenses:
    end = 0

if end == 1:
    sys.exit() #this is so we can stop the program from continuing if they are spending more than they earn

if total_expenses == 0:
    print("You must be lying! I refuse to help you.")
    sys.exit() #fool proofing. no lying allowed...

def percentage(type):
    if type == "total":
        result2 = round((total_expenses/income_left_after_savings)*100, 2)

    elif type == "rent":
        result2 = round((rent/income)*100 ,2)

    elif type == "utilities":
        result2 = round((utilities/income)*100, 2)

    elif type == "groceries":
        result2 = round((groceries/income)*100, 2)

    elif type == "transportation":
        result2 = round((transportation/income)*100, 2)

    return result2

if percentage("total") == 50:
    print(f"Nice job, or not. You are spending {percentage("total")}% of your monthly income on expenses.")

elif percentage("total") < 50:
    print(f"Also, you are spending {percentage("total")}% of your monthly income on expenses. Nice job! That isn't that much!")

elif percentage("total") > 50:
    print(f"You need to get help. Your monthly expenses are", str(percentage("total")), + "% of your monthly income.")

print("Here is a more detailed analysis!")
print("You are spending ", round((rent/income_left_after_savings)*100, 2) + "% of your monthly earnings on rent.")
print("You are spending ", round((utilities/income_left_after_savings)*100, 2) + "% of your monthly earnings on utilities.")
print("You are spending ", round((groceries/income_left_after_savings)*100, 2) + "% of your monthly earnings on groceries.")
print("You are spending ", round((transportation/income_left_after_savings)*100, 2) + "% of your monthly earnings on transportation.")

print("You will be saving $", round(savings, 2), "every month!")
print("That means you will be saving $", round(savings*12, 2), "each year!")
print("You will have $", round(income_left, 2), "after all of your expenses.")
print("And you will have $", round(income_left*12, 2), "to spend each year." )

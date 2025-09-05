#DD Period 7 Financial Calculator

print("Hello! I am your personal financial calculator. Please type in all of the information I require.")

income = float(input("How much do you make each month?\n"))
rent = float(input("How much does your rent cost?\n"))
utilities = float(input("How much do your utilities cost?\n"))
groceries = float(input("How much do your groceries cost?\n"))
transportation = float(input("How much does your transportation cost?\n"))

savings = income*0.1
income_left_after_savings = income*0.9

income_left = income_left_after_savings-(rent+utilities+groceries+transportation)

print("You will be saving $", savings, "Every month!")
print("You will have $", income_left, "after all of your expenses.")
print("That means you will be saving")
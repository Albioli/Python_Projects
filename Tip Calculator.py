print("Welcome to the tip calculator")

print("- - -")

total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

amount = float(total_bill / people) * ((100 + tip) / 100)

final_amount = round(amount, 2)

print(f"Each person should pay: ${final_amount}")

final_tip = round(final_amount - (final_amount / ((100 + tip) / 100)), 2)

print(f"The tip that everyone will have to pay is: ${final_tip}")
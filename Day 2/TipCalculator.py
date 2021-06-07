# Original Code
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

# Solution
total_amount = bill*(1 + float(tip)/100)
amount_per_person = round(total_amount/float(people),2)
print(f"Each person should pay: {amount_per_person}")
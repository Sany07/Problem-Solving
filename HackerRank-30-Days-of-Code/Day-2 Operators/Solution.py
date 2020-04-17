meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

pr = 100
tip = meal_cost * tip_percent / pr
tax = meal_cost * tax_percent / pr
total = meal_cost + tip + tax

print("The total meal cost is " + str(round(total)) + " dollars.")

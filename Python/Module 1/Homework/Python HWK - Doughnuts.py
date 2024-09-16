# AUTHOR:Stone Leiker
# COURSE:ANLY 615

# PROGRAM:PY HW2 Problem (Cost of Dounts)

# PURPOSE: Cost of Donuts - A doughnut shop charges $1.00 per doughnut for orders of less than 1/2 dozen and $0.75 per doughnut for orders of a half-dozen or more. Write a program thatrequests the number of doughnuts ordered and displays the total cost. 
# INPUT: Request the number of doughnuts orders
# Request the number of doughnuts ordered by Aggie students
num_doughnuts = int(input("Howdy! Welcome to Aggies Business Doughnuts! How many would you like to order? Don't be shy now, if you're thinking of ordering 100 doughnuts, we won't judge! In fact, we'll probably high-five you. Enter!"))

# Process - Determine the cost per doughnut based on the number ordered
if num_doughnuts < 6:
    cost_per_doughnut = 1.00
else:
    cost_per_doughnut = 0.75

# Calculate the total cost
total_cost = num_doughnuts * cost_per_doughnut

# OUTPUT
print(f"Thank you for supporting Aggies Business! Because you're awesome, enjoy a 25% discount on your next order. You're welcome! Your total is: ${total_cost:.2f}")

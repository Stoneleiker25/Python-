# AUTHOR:Stone Leiker
# COURSE:ANLY 615

# PROGRAM:PY HW2, Problem 6 (Weight Conversions)

# PURPOSE:Write a program that displays a pound (lb) to kilogram (kg) weight conversion table. Entries in the table should range from 100 to 300 pounds in increments of 10 pounds. Note: the formula kg = lb / 2.2046 converts pounds to kilograms. 

# INPUT: Convert from Pounds (lbs) to Kilogram (kg)
start_pounds = 100 # Starting value in pounds 
end_pounds = 300   # Ending value in pounds
increment = 10     # Increment value in pounds


# PROCESS: Calcacute and generate the conversion table from the range 100 to 300 pounds
def pounds_to_kilograms(pounds):
    return pounds / 2.2046

# OUPUT: The program will print each weights in pounds along with its equivalent in kilograms.
print("Pounds  Kilograms")
print("----------------")

for pounds in range (100, 301, 10):
    kilograms = pounds_to_kilograms(pounds)
    print(f"{pounds}     {kilograms:.2f}")

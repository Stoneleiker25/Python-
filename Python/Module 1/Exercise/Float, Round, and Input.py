#!/usr?bin/ env python3

#Display a title
print("The Miles Per Gallon program")
print()

# Input is from the User and Int is no demical
miles_driven = float(input("Enter miles driven:\t\t"))
gallon_used = float(input("Enter gallons of gas used:\t"))
print()

#calcualte and round miles per gallon
mpg = miles_driven / gallon_used
mpg = round(mpg, 2)

#display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print()
print("Bye!")

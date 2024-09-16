# AUTHOR:Stone Leiker
# COURSE:ANLY 615

# PROGRAM: PY HW3 Problem (Squared Age as Year)

# PURPOSE: A person born in 1980 can claim "I will be x years old in the year x squared." Write a program to calculate how old a person born in 1980 will be when the value of their age (x) squared is equal to the year they are x years old on their birthday.

def calculate_age_for_squared_year(born_year):
    """Calculate the age where age squared equals the year."""
    
    age = 1
    while True:
        current_year = born_year + age
        if age ** 2 == current_year:
            return age, current_year
        age += 1

def main():
    #INPUT: The year the person was born
    born_year = 1980

    #PRCOESS: Calculate the age and year where age squared equals that year 
    age, current_year = calculate_age_for_squared_year(born_year)
    
    #OUPUT: The result
    print(f"A person born in {born_year} will be {age} years old in the year {current_year}, when their age squared equals that year.")

if __name__ == "__main__":
    main()


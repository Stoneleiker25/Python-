# AUTHOR:Stone Leiker
# COURSE:ANLY 615

# PROGRAM: PY HW3 Problem 6 (Employee Raise)

# PURPOSE: Write a program that asks an employee to enter their current annual salary, first name, and last name. Calculate the employee's salary for next year. Employees who earn less than $50,000 will receive a 5% raise, while those who earn $50,000 or more will receive a raise of $2,500 plus 2% of the amount over $50,000. Use the main module to control the program flow. Write a function to display the program overview, collect the inputs, calculate the raise, and display the old salary, the amount of the raise, the effective raise rate (i.e., raise / old salary), and the new salary for the employee.  
    
def employee_data(): # develop the employee data
    current_salary = int(input("Enter the employee's current salary: "))
    first_name = input("Enter the employee's first name: ")
    last_name = input("Enter the employee's last name: ")
    return first_name, last_name, current_salary

#PROCESS: Calcuate salary with raise rate for a new salary into 2025.
def calculate_raise(current_salary):
    if current_salary < 50000:
        raise_amount = current_salary * 0.05
    else:
        raise_amount = 2500 + (current_salary - 50000) * 0.02

    new_salary = current_salary + raise_amount
    raise_rate = raise_amount / current_salary
    return raise_amount, raise_rate, new_salary

#OUPUT: The result plan of 2025

def results(first_name, last_name, current_salary, raise_amount, raise_rate, new_salary):
    print(f"Employee Name: {first_name} {last_name}")
    print(f"Old Salary: ${current_salary:.2f}")
    print(f"Raise Amount: ${raise_amount:.2f}")
    print(f"Raise Rate: {raise_rate:.2%}")
    print(f"New Salary: ${round(new_salary):,}")

# Overview of the salary program
def overview():
    print("This program calculates the raise for an employee based on their current salary.")

# Final Report
def main():
    "The Overview Program"
    overview()
    first_name, last_name, current_salary = employee_data()
    raise_amount, raise_rate, new_salary = calculate_raise(current_salary)
    results(first_name, last_name, current_salary, raise_amount, raise_rate, new_salary)

if __name__ == "__main__":
    main()
    

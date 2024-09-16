# AUTHOR:Stone Leiker
# COURSE:ANLY 615

# PROGRAM: PY HW5 Problem (String Manipulation)

# PURPOSE: Write a program that asks the user to enter a word or phrase and then displays the word or phrase with all occurrences of the letter "r" removed. Example: "Park the car in Harvard Yard" becomes "Pak the ca in Havad Yad."
def remove_letter_r(text):
    """ Remove all 'r' from the letter. """
    return text.replace('r', '').replace('R', '')

def get_user_input():
    while True:
        user_input = input("Enter a word: ").strip()
        if user_input:
            return user_input
        print("Please enter a non-empty string.")
def main_remove_letter_r():
    """
    Main function to run the program.
    """

    # INPUT: Enter a word 
    user_input = get_user_input()

    # PROCESS: Remove 'r' 
    result = remove_letter_r(user_input)

    # OUTPUT: Display the modified text
    print("Modified text", result)

if __name__ == "__main__":
    main_remove_letter_r()


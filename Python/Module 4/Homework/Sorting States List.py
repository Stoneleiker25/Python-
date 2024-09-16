# AUTHOR:Stone Leiker
# COURSE:ANLY 615

# PROGRAM: PY HW5 Problem (Storing States List)

# PURPOSE: Sorting States List - The data file "States.txt Download States.txt" contains the 50 US states in order they joined the union with one state per line. Write a program to read the file contents into a list. Then sort the list based on the number of consonants contained in the state name in ascending order. HINT: You will need to write a function to count the number of consonants in a word.
# Function to count the number of consants in a word (state name)
def count_consonants(state_name):
    vowels = 'aeiouAEIOU'
    consonants = 0
    for char in state_name:
        if char.isalpha() and char not in vowels:
            consonants += 1
    return consonants

def main():
    # INPUT: Read the file states list
    try:
        with open('C:\\Users\\leiker-s\\Desktop\\ANLY 615\\Python\\Module 4\\States.txt', 'r') as file:
            states = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Error: The file was not found.")
        return
    
    # PROCESS: Sort states the list on the number
    states_sorted = sorted(states, key=count_consonants)
    
    #OUPUT: Display the sorted states list
    print("States sorted by the number of consonants in acending order:")
    for state in states_sorted:
        print(state)

if __name__ == "__main__":
    main()



# AUTHOR:Stone Leiker
# COURSE:ANLY 615

# PROGRAM: PY HW4 Problem (Crayon Colors)

#PURPOSE:Crayon Colors - The file "Colors.txt Download Colors.txt" contains the names of 123 crayon colors with one color per line. Write a program that asks the user to enter a letter of the alphabet and then displays all the colors that start with that letter. Write three separate functions: one to get the user input, one to read the colors.txt file into a list, one to build a list with the colors that start with the letter, and one to display the output. 

#INITIZATION
file_path = r'C:\Users\leiker-s\Desktop\ANLY 615\Python\Module 3\colors.txt'

#INPUT: Read the file
def get_user_input():
    letter = input("Enter a letter of the alphabet: ").lower()
    return letter


#PROCESS: read the colors from the file and fitler them
def read_color_file(file_path):
        with open(file_path, 'r') as file:
                colors = file.read().splitlines()
        return colors

def filter_colors(colors, letter):
    filtered_colors = [color for color in colors if color.lower().startswith(letter)]
    return filtered_colors

#OUTPUT: Display the filtered colors 
def display_colors(filtered_colors):
    if filtered_colors:
        print("Colors that start with the letter:")
        for color in filtered_colors:
            print(color)

    else:
        print("No colors found that start with that letter")
        
# Main function to run the program
def main():
    letter = get_user_input()
    colors = read_color_file(file_path)
    filtered_colors = filter_colors(colors, letter)
    display_colors(filtered_colors)

if __name__== "__main__":
    main()

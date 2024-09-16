# AUTHOR:Stone Leiker
# COURSE:ANLY 615

# PROGRAM: PY HW4 Problem (Rose Bowl)

#PURPOSE: Rose Bowl - The Rosebowl.txt Download Rosebowl.txtdata set contains the names of the teams that won the Rose Bowl from 1902 (Michigan on the first line) to 2020 (Oregon on the last line). Write a program that reads the file and counts the number of Rose Bowl wins for each team (university). Create a new comma-delimited file that includes the team and the number of times the team won the Rose Bowl for each team. Display a list to the user of all teams that have won more than four Rose Bowls. 

#Initialization
import csv
from collections import Counter

#INPUT - Read the file and get teams' data
def read_rosebowl(filename):
    with open(filename, 'r') as file:
        teams = file.read().splitlines()
    return teams
        

#PROCESS: Count the number of Rose Bowl for each team
def win_team_count(teams):
    return Counter(teams)

# Write the results to a new CSV file
def write_wins_csv(wins, output_filename):
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Team', 'Wins'])
        for team, win_count in wins.items():
            writer.writerow([team, win_count])
                          
 # OUTPUT: Display teams with more than 4 wins                         
def display_teams_more_than_4wins(wins):
    print("Teams with more than 4 wins:")
    for team, win_count in wins.items():
        if win_count > 4:
            print(f"{team}: {win_count} wins")


def main():
    filename = r'C:\Users\leiker-s\Desktop\ANLY 615\Python\Module 3\Rosebowl.txt'
    output_filename = 'Rosebowl_Wins.csv'

    teams = read_rosebowl(filename)

    teams_wins = win_team_count(teams)
    write_wins_csv(teams_wins, output_filename)

    display_teams_more_than_4wins(teams_wins)

if __name__ == "__main__":
    main()

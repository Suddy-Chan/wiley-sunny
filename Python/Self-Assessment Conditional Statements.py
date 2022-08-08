'''
Self-Assessment: Conditional Statements

Name: Ho Yeung Chan (Sunny)
Date: 8 Aug 2022
'''
last_name = input("What's your last name? ")
start = last_name[0].capitalize() # get the first letter and capitalize it
team = ""
if start == "A" or start == "B" or start == "C" or start == "D":
    team = "Red Dragons"
elif start == "E" or start == "F" or start == "G" or start == "H":
    team = "Dark Wizards"
elif start == "I" or start == "J" or start == "K" or  start == "L":
    team = "Moving Castles"
elif start == "M" or start == "N" or start == "O" or start == "P":
    team = "Golden Snitches"
elif start == "Q" or start == "R" or start == "S" or start == "T":
    team = "Night Guards"
else:
    team = "Black Holes"
print(f"Aha! You're on the team {team}!")
print("Good luck in the games!")

# Activity 1
# Write a program that asks the user how much money they have in their wallet. 
# The program should output "You're rich!" if the user inputs $20 or more and "You're broke!" if the input is less than $20.
money = float(input("Enter how much money your have in wallet: "))
if money >= 20:
    print("You're rich!")
else:
    print("You're broke!")

# Activity 2
# version 1 - use if
cat = input("Do you own any cats? (Type Yes/No) ")
dog = input("Do you own any dogs? (Type Yes/No) ")

if cat == "Yes" and dog == "Yes":
    print("You must really love pets!")
elif cat == "No" or dog == "No":
    print("Maybe you need more pets.")

# Activity 2
# version 2 - use if-else
cat = input("Do you own any cats? (Type Yes/No) ")
dog = input("Do you own any dogs? (Type Yes/No) ")

if cat == "Yes" and dog == "Yes":
    print("You must really love pets!")
else:
    print("Maybe you need more pets.")

# Activity 3
print("This program will ask you 3 Yes/No questions on Geography.")
print("Type Yes/No only.")

score = 0
ans = input("Q1: Toronto is the capital of Canada. ")
if ans == "Yes":
    print("Wrong. Capital of Cananda is Ottawa.")
else:
    print("Correct!")
    score += 1
    
ans = input("Q2: China has only 1 time zone. ")
if ans == "Yes":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
ans = input("Q3: Canada is the largest country in the world. ")
if ans == "Yes":
    print("Wrong. The largest country is Russia.")
else:
    print("Correct!")
    score += 1
print("Your final score is", score)

# Activity 4
season = input("What season is it? Type fall/autumn, winter, spring, or summer. ")
# change to lower case
season = season.lower()

if season == "fall" or season == "autumn":
    print("I bet the leaves are pretty there!")
elif season == "winter":
    print("I hope you're ready for snow!")
elif season == "spring":
    print("I can smell the flowers!")
elif season == "summer":
    print("Make sure your AC is working!")
else:
    print("I don't recognize that season.")

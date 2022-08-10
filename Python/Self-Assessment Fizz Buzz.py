# Name: Ho Yeung Chan (Sunny)    Date: 10 Aug 2022
# Ask the user for a number.
num = int(input("How many fizzing and buzzing units do you need in your life? "))
replaced = 0 # number of int replace by words
count = 0
# Continue counting until the number of integers replaced with "fizz," "buzz," or "fizz buzz" reaches the input number.
while replaced < num:
    if count%3 != 0 and count%5 != 0 or count == 0:
        print(count)
    elif count%3 == 0 and count%5 != 0:
        print("fizz")
        replaced += 1
    elif count%5 == 0 and count%3 != 0:
        print("buzz")
        replaced += 1
    else:
        print("fizz buzz")
        replaced += 1
    count += 1
print("TRADITION!!")

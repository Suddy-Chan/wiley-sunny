# Activity 1
# Given the list fruit_list, write a script that iterates through the list and prints each item on a separate line.

fruit_list = ["apple", "banana", "cherry", "gooseberry",
"kumquat", "orange", "pineapple"]
 
# your code here
for i in fruit_list:
    print(i)

# Activity 2
# Write a Python script that asks the user for a string and displays the characters of the string to the user, 
# with each character on a new line.

string = input("Enter a string: ")
for i in string:
    print(i)

# Activity 3
# Write a Python script that computes the length of a string without using the len() function.
string = "Hello"
length = 0

for i in string:
    length += 1
print("Length of the string is", length)

# Activity 4
# Create a program that starts with a list of strings, identifies all the strings with more than two characters, 
# stores the results in another list, and displays the new list.
string = ["Hello", "Sunny", "a", "bb", "ccc"]
new_string = []
for i in string:
    if len(i) > 2:
        new_string.append(i)
print(new_string)

# Activity 5
# Write two scripts, each of which displays all numbers divisible by 50 between 100 and 1000 (inclusive).

#Use the range function with for in one script.
#Use while without range in the other script.
#Both scripts should have identical outputs.

# script 1: range
# your code here
for i in range(100,1001):
    if i%50 == 0:
        print(i)
        
# script 2: while
# your code here
i = 100
while i <=1000:
    if i%50 == 0:
        print(i)
    i += 1

# Activity 6
# Create a script that computes the sum of all numbers between 0 and 100.
sum_num = 0
for i in range(0,101):
    sum_num += i
print("Sum of all numbers betwwen 0 and 100 is", sum_num)

# Activity 7
#　Create a script that computes the factorial of any given number.
num = 5
fac = 1
for i in range(1,num+1):
    fac *= i
print("Factorial of", num, "is", fac)

# Activity 8
# Starting with the defined fruit_list in the code block below, update the script to perform the following tasks.
fruit_list = ["apple", "banana", "cherry", "gooseberry",
"kumquat", "orange", "pineapple"]
 
# your code here
# Prompt the user to enter the name of a fruit.
fruit = input("Enter a fruit name (type quit to exit): ")
# The script should repeat itself until the user enters a stop word at the prompt.
while fruit != "quit":
    # If the fruit is in fruit_list, display an appropriate message to the user and tell the user its index value in the list
    if fruit in fruit_list:
        print(fruit, "is in the list with index", fruit_list.index(fruit))
        fruit = input("Enter a fruit name (type quit to exit): ")
    # If the fruit is not in fruit_list, display an appropriate message to the user and prompt them to try again.
    if fruit not in fruit_list and fruit != "quit":
        print(fruit, "is not in the list")
        fruit = input("Enter a fruit again (type quit to exit): ")

# Activity 9
# Create a script that asks the user for a variable number of values and displays the sum of those values to the user. 
# The program should prompt the user for values until the user enters the word "quit" (uppercase or lowercase), 
# display the values used in the calculation, and then display the total of those values.
num_list = []

# ask for the first number
num = input("Enter a number (type quit to exit): ")
if num != "quit" and num != "Quit":
    num = int(num)
    num_list.append(num)
else:
    num = num.lower()

# ask for other numbers if input is not quit
while num != "quit":
    num = input("Enter another number (type quit to exit): ")
    if num != "quit" and num != "Quit":
        num = int(num)
        num_list.append(num)
    else:
        num = num.lower()

# calculate the sum, display the values and sum
sum_num = 0
for i in num_list:
    sum_num += i
print("The values you entered:", num_list)
print("Sum of them:", sum_num)
    

# Activity 10
# Write a script that asks the user for an integer value and then displays the multiplication table 
# of that input number from 1 through the integer squared.
num = int(input("Enter an integer: "))
for i in range(1,num**2+1):
    print(i, "x", num, "=", i*num)

# Activity 11
# Create a script that identifies all prime numbers between 0 and 100

for i in range(0,101):
    prime = False
    for j in range(2,i+1):
        if i%j == 0:
            break
        prime = True
    if prime == True:
        print(i, "is a prime number.")

# Activity 12
# Write a script that calculates the greatest common denominator between two numbers.
a = 80
b = 200
factor_a = []
factor_b = []
for i in range(1,a+1):
    if a%i == 0:
        factor_a.append(i)
for j in range(1,b+1):
    if b%j == 0:
        factor_b.append(j)

for i in factor_a:
    for j in factor_b:
        if i == j:
            gcd = i
print("Greatest common denominator of", a, "and", b, "is", gcd)

# Activity 13
# Write a Python script that computes the frequency of each digit in a given integer.
freq = dict()
num = "193845445"
for i in num:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i in freq.keys():
    if freq[i] == 1:
        print(i, "occurs", freq[i], "time")
    else:
        print(i, "occurs", freq[i], "times")

# Activity 14
# Write a script that calculates the lowest common multiple of two given integers.
a = 10
b = 20
multiple_a = []
multiple_b = []
for i in range(a,a*b+1):
    if i%a == 0:
        multiple_a.append(i)
for j in range(b,a*b+1):
    if j%b == 0:
        multiple_b.append(j)

for i in multiple_a:
    for j in multiple_b:
        if i == j:
            lcm = i
        break
print("Lowest common multiple of", a, "and", b, "is", lcm)

# Activity 15
# Write a Python script that determines if an input number can be expressed as the sum of two prime numbers.
num = int(input("Enter a number: "))
for a in range(1,num+1):
    b = num - a
    prime_a = False
    prime_b = False
    for i in range(2,a+1):
        if a%i == 0:
            break
        prime_a = True # a is prime
    for j in range(2,b+1):
        if b%j == 0:
            break
        prime_b = True # b is prime
    if prime_a == True and prime_b == True:
        break
if prime_a == True and prime_b == True:
    print(num, "can be expressed as sum of two prime numbers.")
else:
    print(num, "cannot be expressed as sum of two prime numbers.")

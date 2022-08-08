# Activity 1
# Prompt the user for an integer and store the value in a variable.
num = input("Enter an integer: ")

# Display the data type of the variable that holds the entered data.
print("Data type of the integer you entered:",type(num))

#Convert the value to an integer type and store the converted value in a new variable.
num = int(num)

#Display the value and type of the new variable in a single sentence. (For example, "The value is 8 with type integer.")
print(f"The value is {num} with type {type(num)}")

#Run the program and enter a float value at the prompt. What is its value in the last step?
#ValueError: invalid literal for int() with base 10: '1.5'

# Activity 2
# do not change the order in which the numbers and operators appear in the next line
result = (5 + 3) ** 2 * 9
 
print(result) # the output should be 576

# Activity 3
# Create a computer program that prompts the user for a float number and returns the integer portion of the floating number.
num = input("Enter a float number")
num = int(float(num))
print("Integer portion is:", num)

# Activity 4
# Write a computer program that calculates and displays the current value of a deposit for a given initial deposit, 
# interest rate, how many times interest is calculated per year, and the number of years since the initial deposit.

print("V -- value")
print("P -- initial deposit")
print("r -- interest rate as a fraction (eg 0.05)")
print("n -- the number of times per year interest is calculated")
print("t -- the number of years since the initial deposit")

P = float(input("Enter P: "))
r = float(input("Enter r: "))
n = int(input("Enter n: "))
t = int(input("Enter t: "))

V = P * (1 + r/n) ** (n * t)
print("Current value V:", V)
print("Interest rate r:", r)
print("How many times interest is calculated per year n:", n)
print("Number of years since the initial deposit t:", t)

# Activity 5
# Write a computer program that prompts the user for a principal amount, 
# the rate of interest, and the number of days for a loan and then calculates and 
# returns the simple interest for the life of the loan. Use the formula:
# interest = principal * rate * days / 365

P = float(input("Enter the principal amount: "))
r = float(input("Enter the interest rate: "))
n = int(input("Enter a number of days for loan: "))
I = P * r * n / 365
print("Simple interest:", I)

# Activity 6
# Create a computer program that displays three statements that evaluate to True and 
# three statements that evaluate to False.

# True
a = 1
b = 2
print(a < b)

# False
a = 10
b = 11
print(a == b)

# Activity 7
num = int(input("Enter a number: "))

print("You entered", num)
# the boolean of the number entered
print("The boolean of your number is", bool(num))
# the binary equivalent of the number entered
print("The binary equivalent of your number is", bin(num))
# the square root of the number entered to 3 dp
print("The square root of your number is", round(num ** (1/2),3))

# Activity 8
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))
e = int(input("Enter the fifth number: "))

product = a*b*c*d*e
sum_five = a+b+c+d+e
avg = sum_five / 5

print("Product:", product)
print("Sum:", sum_five)
print("Average:", avg)

# Activity 9
address = "12 New Street"
print("The full address is",address)
print("The building or house number is",address[0:2])
print("The street name is",address[3:])

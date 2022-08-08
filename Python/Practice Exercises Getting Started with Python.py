# Activity 4
# Create a computer program that prompts the user for a purchase total 
# and a sales tax rate and then returns the total price of the sale.

total = float(input("Enter purchase total: "))
rate = float(input("Enter sales tax rate: "))

price = total * (1 + rate)
print("Total price is", price)

# Activity 6
# Write out the following program and run it using 4 as the first value and 10 as the second value.
first = input("Input a number: ")
second = input("Input another number: ")

if first > second:
    print(first + " is greater than " + second)
elif first < second:
    print(second + " is greater than " + first)
else:
    print("They are the same number!")
    
# problem: the conditional if is comparing strings but not integers
# solution: use int() to convert them to integers
first = input("Input a number: ")
second = input("Input another number: ")

if int(first) > int(second):
    print(first + " is greater than " + second)
elif int(first) < int(second):
    print(second + " is greater than " + first)
else:
    print("They are the same number!")
    
# Activity 11
name = input("Enter your first and last name: (e.g. Robert Taylor) ")
address = input("Enter your complete street address: (e.g. 25 Main Street) ")
city = input("Enter your city, state, and zip: (e.g. Paterson NJ 07501) ")
phone = input("Enter your 10-digit phone number: (e.g., 201-857-5309) ")

print("Your name is", name)
print("Your address is", address)
print("Your city, state and zip are", city)
print("Your phone number is", phone)

change = input("Enter which item you want to change: (name, address, city or phone) ")
if change == "name":
    name = input("Enter your new name: ")
elif change == "address":
    address = input("Enter your new address: ")
elif change == "city":
    city = input("Enter your new city, state and zip: ")
else:
    phone = input("Enter your new phone number: ")

print("Your name is", name)
print("Your address is", address)
print("Your city, state and zip are", city)
print("Your phone number is", phone)

# Activity 12
# Write a program that allows a user to create a new Contact, 
# including a first and last name, complete street address, city, state, zip, phone number, and email address.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
address = input("Enter your complete street address: (e.g. 25 Main Street) ")
city = input("Enter your city, state, and zip: (e.g. Paterson NJ 07501) ")
phone = input("Enter your 10-digit phone number: (e.g., 201-857-5309) ")
email = input("Enter your email address: ")

print("Your name is", first_name, last_name)
print("Your address is", address)
print("Your city, state and zip are", city)
print("Your phone number is", phone)
print("Your email address is", email)

# Activity 13

# Prompt the user for complete Contact details for a new contact.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
address = input("Enter your complete street address: (e.g. 25 Main Street) ")
city = input("Enter your city, state, and zip: (e.g. Paterson NJ 07501) ")
phone = input("Enter your 10-digit phone number: (e.g., 201-857-5309) ")
email = input("Enter your email address: ")

# Displays the Contact details entered by the user.
print("Your name is", first_name, last_name)
print("Your address is", address)
print("Your city, state and zip are", city)
print("Your phone number is", phone)
print("Your email address is", email)

# Prompts the user to select a value to change.
change = input("Enter which item you want to change: (first name, last name, address, city, phone or email) ")

# Updates the selected value with a new input value.
if change == "first name":
    first_name = input("Enter your new first name: ")
elif change == "last name":
    last_name = input("Enter your new last name: ")
elif change == "address":
    address = input("Enter your new address: ")
elif change == "city":
    city = input("Enter your new city, state and zip: ")
elif change == "phone":
    phone = input("Enter your new phone number: ")
else:
    email = input("Enter your new email address: ")
    
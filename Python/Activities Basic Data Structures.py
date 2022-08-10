# Activity 1
# Prompt the user to answer a series of 3-5 questions about themselves (such as their name, their age, 
# their birthday, or where they live) and save the answers in a list. Display the results to the user.
name = input("What is your name? ")
age = input("How old are you? ")
city = input("Which city do you live in? ")
hobby = input("What is your hobby? ")
ans = [name, age, city, hobby]
print("About you:", ans)

# Activity 2
# Present the user with an existing list of items (such as the list created in the previous activity) 
# and prompt the user for 2-4 more items to add to the list. Update the list with the new items and display the updated list.
print("About you:", ans)
birth = input("What's your birthday? ")
school = input("What is your collage? ")
siblings = input("How many siblings do you have? ")
ans.extend([birth, school, siblings])
print("About you:", ans)

# Activity 3
# Present the user with a list of 7-9 items (such as the list created in the previous activities) 
# and prompt them to enter one item to delete from the list. Delete the named item from the list and display the updated list.
mylist = ["A","B","c", "D", "e", "F", "G", "H"]
print(mylist)
item = input("Enter an item from the list to delete: ")
mylist.remove(item)
print(mylist)

# Activity 4
# Present the user with a list of 7-9 items (such as the list created in the previous activities) 
# and prompt them to select one item from the list to update, along with the new value for that item. 
# Change the item's value and display the new list to the user.
mylist = ["A","B","c", "D", "e", "F", "G", "H"]
print(mylist)
index= int(input("Enter an item's index from the list to update: "))
item = input("Enter the new value for that item: ")
mylist[index] = item
print("Updated list:", mylist)

# Activity 5
# Create four tuples:

# One tuple with a person's first name and last name
name = ("Sunny", "Chan")
# A second tuple with the person's current profession
profession = ("Trainee",)
# A third tuple with the person's current address
address = ("Ma On Shan, Hong Kong",)
# A fourth tuple with the person's previous address
prev_address = ("Sha Tin, Hong Kong",)
# Combine all tuples into a new, single tuple that contains all items from the original tuples.
combine = name + profession + address + prev_address

# Activity 6
# Using the final tuple from the previous activity, write a program that performs the following steps:

# Display the tuple to the user.
print(combine)
# Prompt the user to enter a value that should be changed.
index = int(input("Enter a item's index in the tuple to change: "))
# Prompt the user to enter the updated value for that item.
item = input("Enter the new value for that item: ")
# Update the value and display the updated tuple to the user.
combine[index] = item
print(combine)

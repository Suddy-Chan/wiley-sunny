# Name: Ho Yeung Chan (Sunny)    Date: 10 Aug 2022

# Define a set with at least five elements.
myset = {10,7,3,13,27,5}
original_set = {10,7,3,13,27,5}
print("Original set:", myset)

# Ask the user for a value.
num = int(input("Enter a value: "))
# Ask the user for an operation ("add" or "remove").
option = input("Enter an operation (add or remove, or quit to exit): ").lower()

while option != "quit":
    if option == "remove":
        # If the value exists in the set, remove the value from the set and display the updated set to the user.
        if num in myset:
            myset.remove(num)
            print(myset)
        # If the value does not exist in the set, display a user-friendly error message.
        else:
            print(num, "does not exist in set.")
        num = int(input("Enter a value: "))
        option = input("Enter an operation (add or remove, or quit to exit): ").lower()
    if option == "add":
        # If the value exists in the set, display a user-friendly error message.
        if num in myset:
            print(num, "already exist in the set.")
        # If the value does not exist in the set, add the value to the set and display the updated set to the user.
        else:
            myset.add(num)
            print(myset)
        num = int(input("Enter a value: "))
        option = input("Enter an operation (add or remove, or quit to exit): ").lower()

# the original set, the final version of the updated set
print("Orignal set:", original_set)
print("Updated set:", myset)

# the difference between the two sets.
print("Removed items:", original_set - myset)
print("Added items:", myset - original_set)

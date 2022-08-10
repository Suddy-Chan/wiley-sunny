# Activity 1
# Create a program that sums all the values in a dictionary and displays them.
dict1 = {"hello":4,"world":4,"I":1,"am":2,"Martha":3}
sum_value = 0
for i in dict1.values():
    sum_value += i
print("Sum of values:", sum_value)

# Activity 2
# Write a program that displays the maximum and minimum values in a dictionary. 
# You may use the same dictionary you used in the previous activity or create a new one.
dict1 = {"hello":4,"world":4,"I":1,"am":2,"Martha":3}
maximum = -10000
minimum = 10000
for i in dict1.values():
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
print("Maximum value is", maximum)
print("Minimum value is", minimum)

# Activity 3
# Write a program that returns the sum of the integer elements in a set.
set1 = {10,20,18,6,3}
sum_num = 0
for i in set1:
    sum_num += i
print("Sum of integers:", sum_num)

# Activity 4
# Write a program that computes and displays the maximum and the minimum values in a set.
set1 = {10,20,18,6,3}
maximum = -10000
minimum = 10000
for i in set1:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
print("Maximum value is", maximum)
print("Minimum value is", minimum)

# Activity 5
# Given the following dictionary storage, complete the following tasks:
storage = {
    "cupboard" : ["spices", "flour", "sugar"],
    "drawer" : ["fork", "knife", "spoon"],
    "fridge" : ["butter", "milk", "cheese"],
    "emergency jar" : 150
}
# Add a key named "freezer".
storage["freezer"] = ""
# Set the value of "freezer" to be a list containing the items "ice cubes", "ice cream", and "pepperoni pizza".
storage["freezer"] = ["ice cubes", "ice cream", "pepperoni pizza"]
# Sort the items in the cupboard using sort.
storage["cupboard"].sort()
# Add "cream" to the fridge.
storage["fridge"].append("cream")
# Remove "sugar" from the cupboard.
storage["cupboard"].remove("sugar")
# Subtract $25 from the emergency jar.
storage["emergency jar"] -= 25

print(storage)

# Activity 6
# Create a new dictionary named shopping_list and add the following items to the dictionary:
shopping_list = {
    "milk" : 4,
    "butter" : 2,
    "crackers" : 1.5,
    "rice" : 2.25,
    "spaghetti" : 1.75,
    "dish soap": 3.25
}
# Loop through each item in the list and print out each key with its price. 
for i in shopping_list:
    print(i)
    print("price:", shopping_list[i])
#Next, calculate how much it will cost if you purchase all the items on the list.

#Use a variable named total_cost to store the calculated value.
total_cost = 0
#Loop through the dictionary and add the price of each item to the total cost.
for i in shopping_list:
    total_cost += shopping_list[i]
#After looping through the dictionary, print out the total cost in a message that is meaningful to the user.
print("Total cost of all items is", total_cost)

# Activity 7
# Create two dictionaries: price and quantity.
# The price dictionary should be the same as the shopping_list dictionary in the previous activity:
price = {
    "milk" : 4,
    "butter" : 2,
    "crackers" : 1.5,
    "rice" : 2.25,
    "spaghetti" : 1.75,
    "dish soap": 3.25
}
# The quantity dictionary should have the same keys, 
# but with values that represent the number of items to purchase rather than the price:
quantity = {
    "milk" : 1,
    "butter" : 1,
    "crackers" : 3,
    "rice" : 2,
    "spaghetti" : 5,
    "dish soap": 1
}
# Write a script that loops through both dictionaries to calculate the total cost 
# if we purchase the indicated quantity of each item in the dictionaries.
total_cost = 0
for i in price:
    total_cost += price[i] * quantity[i]
print("Total cost is", total_cost)

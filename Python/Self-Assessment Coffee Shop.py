'''
Self-Assessment: Basic Python Data Types

Name: Ho Yeung Chan (Sunny)
Date: 8 Aug 2022
'''

# Ask the user what size cup they want, choosing between small, medium, and large.
size = input("Do you want small, medium, or large? ")

# Ask the user what kind of coffee they want, choosing between brewed, espresso, and cold brew.
kind = input("Do you want brewed, espresso, or cold press? ")

# Ask the user what flavoring they want, if any. Choices include hazelnut, vanilla, and caramel.
flavor_yes = input("Do you want a flavored syrup? (Yes or No) ")
if flavor_yes == "Yes":
    flavor = input("Do you want hazelnut, vanilla, or caramel? ")
else:
    flavor = "none"

size = size.lower()
kind = kind.lower()
flavor = flavor.lower()

# Calculate the price of the cup
cost = 0
if size == "small":
    cost += 2
elif size == "medium":
    cost += 3
else:
    cost += 4
    
if kind == "brewed":
    cost += 0
elif kind == "espresso":
    cost += 0.5
else:
    cost += 1
    
if flavor == "none":
    cost += 0
else:
    cost += 0.5
    
# Display a statement that summarizes what the user ordered.
print(f"You asked for a {size} cup of {kind} coffee with {flavor} syrup.")

# Display the total cost of the cup of coffee as well as the cost with a 15% tip
print("Your cup of coffee costs", cost)
print("The price with a tip is", round(cost * 1.15, 2))

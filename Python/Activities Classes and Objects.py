# Activity 1
# For this activity, choose another Noun of your choice to create a class.
class Country:
    # Include at least three attributes that are common to most (if not all) instances of the Noun
    name = ""
    area = 0.0
    population = 0

# Activity 2
# Use the Noun class you created in the previous activity to create at least four different objects. 
# Print out all attributes for each object.
fr = Country()
fr.name = "France"
fr.area = 543940.00
fr.population = 67390000
print(fr.name, "has", fr.population, "people", "with area", fr.area, "square kilometers.")

uk = Country()
uk.name = "United Kingdom"
uk.area = 243610.00
uk.population = 67220000
print(uk.name, "has", uk.population, "people", "with area", uk.area, "square kilometers.")

sg = Country()
sg.name = "Singapore"
sg.area = 728.00
sg.population = 5680000
print(sg.name, "has", sg.population, "people", "with area", sg.area, "square kilometers.")

usa = Country()
usa.name = "United States of America"
usa.area = 9834000.00
usa.population = 336997624
print(usa.name, "has", usa.population, "people", "with area", usa.area, "square kilometers.")

# Activity 3
# Create an __init__ method for your Noun class. Include at least four of the attributes 
# you originally defined in the new method.
class Country:
    name = ""
    area = 0.0
    population = 0
    density = 0.0
    def __init__(self,name,area,population):
        self.name = name
        self.area = area
        self.population = population
        self.density = 0.0
    # Activity 4
    # Create a method for your Noun class.
    def calculate_density(self):
        self.density = self.population / self.area

# Activity 5
# Create a separate class that is logically related to your original Noun class, 
# based on the example that a Person can have one or more Addresses.
class City:
    name = ""
    population = 0
    def __init__(self,name,population):
        self.name = name
        self.population = population
    def display(self):
        print(self.name, "has", self.population, "people.")

# Create at least one Noun object that includes a list of objects from the associated class. 
class Country:
    name = ""
    area = 0.0
    population = 0
    density = 0.0
    def __init__(self,name,area,population,cities):
        self.name = name
        self.area = area
        self.population = population
        self.density = 0.0
        self.cities = cities
    def calculate_density(self):
        self.density = self.population / self.area
    def display(self):
        print(self.name, "has the following cities:")
        for city in self.cities:
            city.display()

ny = City("New York", 8380000)
la = City("Los Angeles", 3970000)
sf = City("San Francisco", 870000)
cities = list()
cities.append(ny)
cities.append(la)
cities.append(sf)
usa = Country("United States of America", 9834000.00, 336997624, cities)

# Display the Noun with the related objects.
usa.display()

# Activity 0
# Before beginning, create a class Noun to use as the starting point for the activities in this section. 
class Country:
    name = ""
    area = 0.0
    population = 0
    def __init__(self,name,area,population):
        self.name = name
        self.area = area
        self.population = population
    def display(self):
        print(self.name, "has", self.population, "people", "with area", self.area, "square kilometers.")

# Activity 1
# Use inheritance to create another class that will inherit from the Noun class.
class City(Country):
    pass

# Create two objects using the new class
sf = City("San Francisco", 121, 870000)
ny = City("New York", 783.8, 8380000)

# display each object's information using the display method.
sf.display()
ny.display()

# Activity 2
# Add at least two attributes to the new class created in the previous activity. 
# These attributes should be different from the attributes in the original Noun class and specific to the new class.
class City(Country):
    mayor = ""
    area_code = ""
    def __init__(self,mayor,area_code):
        self.mayor = mayor
        self.area_code = area_code
    def display(self):
        print("The mayor is", self.mayor, "and the area code is", self.area_code)
        
# create at least two new objects based on the inherited class
sf = City("London Breed", "415/628")
ny = City("Eric Adams", "212/646/332" )
# display them with the class attributes.
sf.display()
ny.display()

# Activity 3
# Create a second and a third class that inherit from the Noun class you started with.
# Include at least three class-specific attributes for each class.
# For each of the new classes, override the __init__ and display methods to display the new attributes.
class State(Country):
    abbrev = ""
    capital = ""
    elevation = 0
    
    def __init__(self,abbrev,capital,elevation):
        self.abbrev = abbrev
        self.capital = capital
        self.elevation = elevation
        
    def display(self):
        print(self.abbrev,": capital is", self.capital, "and elevation is", self.elevation)
        
class County(Country):
    chair = ""
    time_zone = ""
    high_elevation = 0
    
    def __init__(self,chair,time_zone,high_elevation):
        self.chair = chair
        self.time_zone = time_zone
        self.high_elevation = high_elevation
        
    def display(self):
        print("Its chair is", self.chair, "and its highest elevation is", self.high_elevation)
        print("Its time zone is", self.time_zone)

# Create at least two new objects based on the inherited class
ca = State("CA", "Sacramento", 880)
fl = State("FL", "Tallahassee", 30)
cook = County("Toni R. Preckwinkle", "UTC−6", 290)
miami = County("Daniella Levine Cava", "UTC−5", 22)
# display them with the class attributes
ca.display()
fl.display()
cook.display()
miami.display()

# Activity 4
# Using the three inherited classes you have already created, 
# use the __init__ method of the Noun class to set the values of the original attributes defined in the Noun class.
class City(Country):
    mayor = ""
    area_code = ""
    def __init__(self,name,area,population,mayor,area_code):
        Country.__init__(self,name,area,population)
        self.name = name
        self.mayor = mayor
        self.area_code = area_code
    def display(self):
        print(self.name, "has", self.population, "people", "with area", self.area, "square kilometers.")
        print("The mayor is", self.mayor, "and the area code is", self.area_code)
        
class State(Country):
    abbrev = ""
    capital = ""
    elevation = 0
    
    def __init__(self,name,area,population,abbrev,capital,elevation):
        Country.__init__(self,name,area,population)
        self.abbrev = abbrev
        self.capital = capital
        self.elevation = elevation
        
    def display(self):
        print(self.name, self.abbrev, "has", self.population, "people", "with area", self.area, "square kilometers.")
        print("Its capital is", self.capital, "and its elevation is", self.elevation)
        
class County(Country):
    chair = ""
    time_zone = ""
    high_elevation = 0
    
    def __init__(self,name,area,population,chair,time_zone,high_elevation):
        Country.__init__(self,name,area,population)
        self.chair = chair
        self.time_zone = time_zone
        self.high_elevation = high_elevation
        
    def display(self):
        print(self.name, "has", self.population, "people", "with area", self.area, "square kilometers.")
        print("Its chair is", self.chair, "and its highest elevation is", self.high_elevation)
        print("Its time zone is", self.time_zone)

# Create two objects for each of the three inherited classes and display all attributes,
# including attributes from the original Noun class.
sf = City("San Francisco", 121, 870000, "London Breed", "415/628")
ny = City("New York", 783.8, 8380000, "Eric Adams", "212/646/332" )
ca = State("California", 423970, 39185605, "CA", "Sacramento", 880)
fl = State("Florida", 170312, 21538187, "FL", "Tallahassee", 30)
cook = County("Cook", 4230, 5275541, "Toni R. Preckwinkle", "UTC−6", 290)
miami = County("Miami-Dade", 6297, 2701767, "Daniella Levine Cava", "UTC−5", 22)

sf.display()
ny.display()
ca.display()
fl.display()
cook.display()
miami.display()

#Activity 5
#Create a class that inherits from your initial inherited class. Include at least one attribute specific to this class.
class Neighborhood(City):
    zip_code = ""
    def __init__(self,name,area,population,mayor,area_code,zip_code):
        City.__init__(self,name,area,population,mayor,area_code)
        self.zip_code = zip_code
    def display(self):
        print(self.name, "has", self.population, "people", "with area", self.area, "square kilometers.")
        print("The mayor is", self.mayor, "and the area code is", self.area_code)
        print("Its ZIP code is", self.zip_code)
    
#Create two objects based on this class and display all attributes for each object.
alamo = Neighborhood("Alamo Square", 1.20, 5617, "Dean Preston", "415/628", "94115")
jtown = Neighborhood("Japantown", 0.09, 1397,"Dean Preston", "415/628", "94115")
alamo.display()
jtown.display()

# Activity 6
# Create another class that inherits from the class created for the previous activity. 
# For the new class, create at least one class-specific attribute and one object based on the class.
class Building(Neighborhood):
    height = 0.0
    def __init__(self,name,area,population,mayor,area_code,zip_code,height):
        Neighborhood.__init__(self,name,area,population,mayor,area_code,zip_code)
        self.height = height
    def display(self):
        print(self.name, "has", self.population, "people", "with area", self.area, "square kilometers.")
        print("The mayor is", self.mayor, "and the area code is", self.area_code)
        print("Its ZIP code is", self.zip_code)
        print("Its height is", self.height)

transamerica = Building("Transamerica Pyramid", 1.20, 5617, "Dean Preston", "415/628", "94115", 853)
print(isinstance(transamerica,Neighborhood))

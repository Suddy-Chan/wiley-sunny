'''
Self-Assessment: Basic Python Data Types

Name: Ho Yeung Chan (Sunny)
Date: 8 Aug 2022
'''
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
city = input("Enter the city you live: ")
hourly_wage = int(input("Enter your hourly wage: "))
work_hour = int(input("Enter your number of working hours pre week: "))

# capitalize the first letter for name and city
first_name = first_name.capitalize()
last_name = last_name.capitalize()
city = city.capitalize()

week_wage = hourly_wage * work_hour
monthly_wage = week_wage * 4
yearly_wage = monthly_wage * 12

print(f"Hi,{first_name}, {last_name}!,How are you?")
print(f"I hope the weather is nice in {city}.")
print(f"Based on the information you provided, you earn {week_wage} dollars per week, approximately {monthly_wage} dollars per month, and {yearly_wage} dollars per year.")

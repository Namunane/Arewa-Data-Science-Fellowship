# 'Day 2: 30 Days of python programming
first_name = 'Enock'
last_name = 'Namunane'
full_name = 'Enock Namunane'
City = 'Johannesburg'
Age = 24
Year = 2025
is_married = "Yes"
is_true = 'Yes'
is_light_on ='No'
# Declaring multiple variables in one line
Name, Age, Country, City = 'Enock', 23, 'Kenya', 'Nairobi'
Variables = [first_name, last_name, full_name, City, Age, Year, is_married, is_true, is_light_on, Name, Age, Country, City]
for x in Variables:
    print(f"{x}: {type(x)}")
Lenghth_of_firstname = print(len(first_name))
Lenghth_of_lastname = print(len(last_name))
if len(first_name) > len(last_name):
    print('The length of the first name is greater than the length of the last name')
elif len(first_name) < len(last_name):
        print('The length of the last name is greater than the length of the first name')
else:
        print('The length of the first name is equal to the length of the last name')
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
results = [total, diff, product, division, remainder, exp, floor_division]
for x in results:
    print(x)


# Area of a circle
radius_in_metres = 30
area_of_circle = 3.142 * radius_in_metres ** 2
circum = 2 * 3.142 * radius_in_metres
results = [area_of_circle, circum]
for x in results:
    print(x)
radius = int(input('Enter the radius of the circle in metres: '))
area_of_circle = 3.142 * radius ** 2
circum = 2 * 3.142 * radius
result = [area_of_circle, circum]
for x in result :
     print(x)
first_name = str(input('Enter your first name: '))
last_name = str(input('Enter your last name: '))
country = str(input('Enter your country: '))
age = int(input('Enter your age: '))
Biodata = [first_name, last_name, country, age]
help('')
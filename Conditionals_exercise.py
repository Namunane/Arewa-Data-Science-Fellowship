## Exercise Level 1
Age = int(input("Enter your age: "))
Missing_age = 18 - Age
if Age >= 18:
    print("You are old enough to learn to drive")
else:
    print(f"You need {Missing_age} more to learn to drive")


My_age = 30
Your_age = int(input("Enter your age: "))
if My_age > Your_age:
    age_difference = My_age - Your_age
    if age_difference == 1:
        print(f"I am {age_difference} year older than you")
    else:
        print(f"I am {age_difference} years older than you")
elif My_age < Your_age:
    age_difference = Your_age - My_age
    if age_difference == 1:
        print(f"You are {age_difference} year older than me")
    else:
        print(f"You are {age_difference} years older than me")
else:
    print("We are the same age")


a = int(input("Enter number a: "))
b = int(input("Enter number b :"))
if a >b :
    print(f"{a} is greater thab {b}")
elif a <b :
    print(f"{a} is less than {b}")
else :
    print(f"{a} is equal to {b}")


## Exercise Level 2
score = int(input("Enter your score: "))
if 80 <=score >= 100:
    grade = "A"
    print(f"Your grade is {grade}")
elif 70 <= score >= 79:
    grade = "B"
    print(f"Your grade is {grade}")
elif 60 <= score >= 69 :
    grade = "C"
    print(f"Your grade is {grade}")
elif 50 <= score >= 59:
    grade = "D"
    print(f"Your grade is {grade}")
else :
    grade = "F"
    print(f"Your grade is {grade}")


Summer = ["June, July, August"]
Winter =["December, January, February"]
Spring =["March, April, May"]
Autumn =["September, October, November"]
Month = input("Enter the month: ")
if Month in Summer:
    print("It is Summer!")
elif Month in Spring:
    print("It is Spring!")
elif Month in Winter:
    print("It is Winter!")
elif Month in Autumn:
    print("It is Autumn!")
else:
    print("Invalid month")


fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ")
if fruit in fruits:
    print(f"{fruit} already exist in the list")
else:
    fruits.append(fruit)
    print(fruits)




## Exercise Level 3
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(f"The middle skill is: {skills[middle_index]}")

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print(f"Has Python skill: {has_python}")

# Determine the person's title based on their skills
if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif set(skills) >= {'Node', 'Python', 'MongoDB'}:
        print('He is a backend developer')
    elif set(skills) >= {'React', 'Node', 'MongoDB'}:
        print('He is a fullstack developer')
    else:
        print('unknown title')

# If the person is married and if he lives in Finland, print the information in the following format:
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
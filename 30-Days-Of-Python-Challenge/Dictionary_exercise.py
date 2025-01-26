## Exercise 
Dog = {
    'name': 'Jack',
    'color': 'brown',
    'breed': 'Beagle',
    'legs': 4,
    'age': 4,
        }   

student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis', 'Data Science'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

student_length = len(student)
skills = student['skills']
student['skills'].append('Machine Learning')
student['skills'].append('Deep Learning')
student_keys = list(student.keys()) # getting student keys as a list
student_values = list(student.values()) # getting student values as a list
student_items = list(student.items())
print(student_items)
del student['address']
del Dog
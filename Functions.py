# EXERCISE MODULE 9
# LEVEL ONE
def add_two_numbers(a,b):
    return a + b

def area_of_circle(r):
    return 3.14 * r**2

def convert_celsius_to_fahrenheit(C):
    return (C*9/5) + 32

def check_season(month):
    month = month.lower()  # Convert the input month to lowercase
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return 'Invalid month'

def solve_quadratic_eqn


def print_list(List):
    for x in List:
        print(x)

def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

def add_item(lst, item):
    lst.append(item)
    return lst

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

def sum_of_numbers(n):
    return sum(range(n + 1))

def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

## LEVEL TWO
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n + 1 - evens
    return f"The number of evens are {evens}. The number of odds are {odds}."

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_empty(param):
    return not bool(param)

import statistics

def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def calculate_mode(lst):
    return statistics.mode(lst)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    variance = calculate_variance(lst)
    return variance ** 0.5

## LIST COMPRESHENSION EXERCISE
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print(negative_and_zero)  

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist in list_of_lists for inner_list in sublist for num in inner_list]
print(flattened_list) 

tuples_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuples_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dict = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]
print(countries_dict)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [' '.join(name) for sublist in names for name in sublist]
print(concatenated_names)


# Lambda function to calculate the slope
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None

# Lambda function to calculate the y-intercept
y_intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1 if slope(x1, y1, x2, y2) is not None else None


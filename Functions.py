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

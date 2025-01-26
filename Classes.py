class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def total_income(self):
        return sum(income['amount'] for income in self.incomes)

    def total_expense(self):
        return sum(expense['amount'] for expense in self.expenses)

    def account_info(self):
        return {
            'Firstname': self.firstname,
            'Lastname': self.lastname,
            'Total Income': self.total_income(),
            'Total Expense': self.total_expense(),
            'Account Balance': self.account_balance()
        }

    def add_income(self, description, amount):
        self.incomes.append({'description': description, 'amount': amount})

    def add_expense(self, description, amount):
        self.expenses.append({'description': description, 'amount': amount})

    def account_balance(self):
        return self.total_income() - self.total_expense()


import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        data_count = Counter(self.data)
        mode_data = data_count.most_common(1)[0]
        return {'mode': mode_data[0], 'count': mode_data[1]}

    def var(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / self.count()

    def std(self):
        return math.sqrt(self.var())

    def freq_dist(self):
        data_count = Counter(self.data)
        total_count = self.count()
        return [(count / total_count * 100, value) for value, count in data_count.items()]

    def describe(self):
        return {
            'Count': self.count(),
            'Sum': self.sum(),
            'Min': self.min(),
            'Max': self.max(),
            'Range': self.range(),
            'Mean': self.mean(),
            'Median': self.median(),
            'Mode': self.mode(),
            'Variance': self.var(),
            'Standard Deviation': self.std(),
            'Frequency Distribution': self.freq_dist()
        }


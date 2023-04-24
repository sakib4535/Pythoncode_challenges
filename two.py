""" loc and iloc are used to access specific rows of a pandas DataFrame or Series,
but they are not applicable to a list of dictionaries. Instead, you can use slicing
and indexing with the [] operator to access specific elements or subsets of the list.
"""

students = [
    {'name': 'Alice', 'age': 20, 'gender': 'female', 'grade': 95},
    {'name': 'Bob', 'age': 18, 'gender': 'male', 'grade': 80},
    {'name': 'Charlie', 'age': 19, 'gender': 'male', 'grade': 85},
    {'name': 'David', 'age': 21, 'gender': 'male', 'grade': 75},
    {'name': 'Emma', 'age': 20, 'gender': 'female', 'grade': 90},
    {'name': 'Frank', 'age': 19, 'gender': 'male', 'grade': 70},
    {'name': 'Gina', 'age': 18, 'gender': 'female', 'grade': 88},
    {'name': 'Henry', 'age': 22, 'gender': 'male', 'grade': 82},
    {'name': 'Ivy', 'age': 20, 'gender': 'female', 'grade': 92},
    {'name': 'Jack', 'age': 19, 'gender': 'male', 'grade': 78}
]

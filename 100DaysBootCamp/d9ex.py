
# Day 9.1
from distutils.ccompiler import new_compiler


student_score = {
    "Harry": 81,
    "Ron": 78,
    "Draco": 74,
    "Neville": 62,
    "Hermion": 99,
}
"""
    Write a program that converts their scores to grades.By the end of your program, you should have a new dictionary called student_grades that should contain
    student names for key and their grades for values. The final version of the student_grades dictionary will be checked.
    This is the scoring criteria:

    Scores 91-100: Grade = "Outstanding"

    Scores 81-90: Grade="Exceeds Expectation"

    Scores 71-80: Grade = "Acceptable"

    Score 70 or lower: Grade="Fail"
"""
# TODO-1: Create an empty dictionary called student_grades

# TODO-2: Write your code below to add the grades to student grades

# Proposed solution


def convert_score(scores):
    student_grades = {}
    for key in scores:
        if 91 <= scores[key] <= 100:
            student_grades[key] = "Outstanding"
        elif 81 <= scores[key] <= 90:
            student_grades[key] = "Exceeds Expectation"
        elif 71 <= scores[key] <= 80:
            student_grades[key] = "Acceptable"
        elif 0 <= scores[key] <= 70:
            student_grades[key] = "Fail"
    return student_grades


# print(convert_score(student_score))

#############    Nesting  #####################
capital = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a line in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in a dictionary

travel_logs = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in a list
visit_log = [
    {"country": "France",
     "cities": ["Paris", "Lille", "Dijon"],
     "visits":12,
     },
    {
        "country": "Germany",
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
        "visits":5,
    },
]


# Coding challenge exe: Dictionary in a list
"""
    You're going to write a program that adds to a visit_log. You can see a visit_log which is a list that contains 2 Dictionaries.

    Write a fucntion that will work with the following line of code 
    add_new_country("Russia",2, ["Moscow", "Saint Petersburg"] )
"""


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities"] = cities_visited
    new_country["visits"] = times_visited
    visit_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(visit_log)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])

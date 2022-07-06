import random
"""
new_dict = {new_key:new_value for item in list} 
new_dict1 = {new_key:new_value for (key, value) in dict.items()}
new_dict1 = {new_key:new_value for (key, value) in dict.items() if test}
"""

names = ["Alex", "Beth", "Caroline", "Dave", 'Eleanor', 'Freddie']
student_scores = {student:random.randint(1,100) for student in names }
#print(student_scores)

passed_students ={student:score for (student, score) in student_scores.items() if score >70}
print(passed_students)
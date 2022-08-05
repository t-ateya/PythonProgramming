student = {"name":"Jose", "school":'Computing', "grades":(66, 77, 88)}

def average_grade(data:dict):
    grades = data['grades']
    return sum(grades)/len(grades)


def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student["grades"])
        count += len(student['grades'])
    
    return total/count

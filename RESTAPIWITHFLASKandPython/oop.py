class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades)/len(self.grades)


student1 = Student("Bob", (90, 90, 93, 78, 90))
student2 = Student("Rolf", (90, 90, 93, 78, 100))
print(student1.average_grade())
print(student2.average_grade())
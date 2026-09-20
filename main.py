# Author: Saksham
# Village: Basahra Uprhar, Shankargarh, Prayagraj
# Project: Student Record System

students = []

def add_student(name, roll):
    students.append({"name": name, "roll": roll})
    print(f"Student {name} added")

add_student("Saksham", 1)
add_student("Amit", 2)

print(students)

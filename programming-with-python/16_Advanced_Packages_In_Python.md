"""
===========================================================
                PACKAGES IN PYTHON
===========================================================

A package in Python is a collection of modules organized
in directories.

Think of it like:
    Package  → Folder
    Module   → Python file (.py)

===========================================================

Example Structure:

school_package/
│
├── __init__.py
├── student.py
├── teacher.py
└── fees.py

===========================================================
"""


# =========================================================
# 1. CREATING MODULES (SIMULATED IN SINGLE FILE)
# =========================================================

# student.py (module)
def add_student(name, age):
    return {"name": name, "age": age}


def get_student():
    return "Returning student data"


# teacher.py (module)
def add_teacher(name, subject):
    return {"name": name, "subject": subject}


# fees.py (module)
def calculate_fee(amount):
    return amount + (amount * 0.18)


# =========================================================
# 2. SIMULATING PACKAGE USAGE
# =========================================================
print("\n========== PACKAGE USAGE SIMULATION ==========")

student = add_student("Rahul", 20)
teacher = add_teacher("Mr. Sharma", "Python")

print("Student:", student)
print("Teacher:", teacher)


# =========================================================
# 3. IMPORT STYLE EXPLANATION (THEORY DEMO)
# =========================================================

print("\n========== IMPORT TYPES ==========")

print("""
1. import module
   → import student

2. from module import function
   → from student import add_student

3. import module as alias
   → import student as st

4. from package import module
   → from school_package import student
""")


# =========================================================
# 4. REAL-WORLD PACKAGE EXAMPLE STRUCTURE
# =========================================================

print("\n========== REAL WORLD PACKAGES ==========")

print("""
Popular Python Packages:

1. numpy       → Numerical computing
2. pandas      → Data analysis
3. matplotlib  → Data visualization
4. requests    → API calls / HTTP requests
5. flask       → Web development
6. django      → Full-stack web framework
7. tensorflow  → Machine learning
""")


# =========================================================
# 5. USING BUILT-IN PACKAGE EXAMPLE
# =========================================================

import math
import random

print("\n========== BUILT-IN PACKAGE EXAMPLE ==========")

print("Square Root:", math.sqrt(64))
print("Random Number:", random.randint(1, 100))


# =========================================================
# 6. CUSTOM PACKAGE STYLE DESIGN (REAL PROJECT IDEA)
# =========================================================

print("\n========== SCHOOL MANAGEMENT PACKAGE ==========")


class StudentModule:
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"Student Name: {self.name}"


class TeacherModule:
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"Teacher Name: {self.name}"


student_obj = StudentModule("Rahul")
teacher_obj = TeacherModule("Mr. Kumar")

print(student_obj.display())
print(teacher_obj.display())


# =========================================================
# 7. PACKAGE BENEFITS
# =========================================================

print("\n========== BENEFITS OF PACKAGES ==========")

print("""
✔ Code reusability
✔ Better organization
✔ Easy maintenance
✔ Scalability for large projects
✔ Team collaboration support
""")


# =========================================================
# END OF PROGRAM
# =========================================================
print("\nPackages concept demonstrated successfully.")
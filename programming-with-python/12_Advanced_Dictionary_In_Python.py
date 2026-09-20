# =========================================================
# STUDENT DATABASE
# =========================================================
# Dictionary storing multiple students.
# Each student ID acts as a unique key.
# The value is another dictionary containing student details.
# =========================================================

students = {
    101: {
        "name": "Rahul Kumar",
        "age": 20,
        "course": "Computer Science",
        "marks": {
            "Python": 95,
            "Java": 88,
            "Database": 91
        },
        "city": "Hyderabad"
    },

    102: {
        "name": "Priya Sharma",
        "age": 21,
        "course": "Electronics",
        "marks": {
            "Python": 85,
            "Java": 80,
            "Database": 89
        },
        "city": "Bangalore"
    }
}


# =========================================================
# FUNCTION: DISPLAY ALL STUDENTS
# =========================================================
def display_students():
    """
    Displays all student records.
    """

    print("\n========== STUDENT RECORDS ==========")

    for student_id, details in students.items():

        print(f"\nStudent ID : {student_id}")
        print(f"Name       : {details['name']}")
        print(f"Age        : {details['age']}")
        print(f"Course     : {details['course']}")
        print(f"City       : {details['city']}")

        print("Marks:")

        # Nested dictionary iteration
        for subject, mark in details['marks'].items():
            print(f"   {subject} : {mark}")


# =========================================================
# FUNCTION: ADD NEW STUDENT
# =========================================================
def add_student(student_id, name, age, course, city):
    """
    Adds a new student to the dictionary.
    """

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": {},
        "city": city
    }

    print(f"\nStudent '{name}' added successfully.")


# =========================================================
# FUNCTION: ADD MARKS
# =========================================================
def add_marks(student_id, subject, mark):
    """
    Adds subject marks for a student.
    """

    if student_id in students:

        students[student_id]["marks"][subject] = mark

        print(f"Added {subject} marks for student ID {student_id}")

    else:
        print("Student ID not found.")


# =========================================================
# FUNCTION: SEARCH STUDENT
# =========================================================
def search_student(student_id):
    """
    Searches for a student using student ID.
    """

    if student_id in students:

        student = students[student_id]

        print("\n========== STUDENT FOUND ==========")
        print("Name   :", student['name'])
        print("Age    :", student['age'])
        print("Course :", student['course'])
        print("City   :", student['city'])

    else:
        print("Student not found.")


# =========================================================
# FUNCTION: UPDATE STUDENT CITY
# =========================================================
def update_city(student_id, new_city):
    """
    Updates the city of a student.
    """

    if student_id in students:

        old_city = students[student_id]['city']

        students[student_id]['city'] = new_city

        print(f"\nCity updated from {old_city} to {new_city}")

    else:
        print("Student ID not found.")


# =========================================================
# FUNCTION: DELETE STUDENT
# =========================================================
def delete_student(student_id):
    """
    Deletes a student record from dictionary.
    """

    if student_id in students:

        deleted_student = students.pop(student_id)

        print(f"\nDeleted student: {deleted_student['name']}")

    else:
        print("Student ID not found.")


# =========================================================
# FUNCTION: CALCULATE AVERAGE MARKS
# =========================================================
def calculate_average(student_id):
    """
    Calculates average marks of a student.
    """

    if student_id in students:

        marks = students[student_id]["marks"]

        if len(marks) > 0:

            total = sum(marks.values())

            average = total / len(marks)

            print(f"\nAverage Marks: {average:.2f}")

        else:
            print("No marks available.")

    else:
        print("Student ID not found.")


# =========================================================
# MAIN PROGRAM EXECUTION
# =========================================================

# Display existing students
display_students()


# Add new student
add_student(
    student_id=103,
    name="Arjun Reddy",
    age=22,
    course="Mechanical Engineering",
    city="Chennai"
)


# Add marks to new student
add_marks(103, "Python", 90)
add_marks(103, "Java", 87)
add_marks(103, "Database", 93)


# Search student
search_student(103)


# Update city
update_city(103, "Visakhapatnam")


# Calculate average marks
calculate_average(103)


# Delete student
delete_student(102)


# Display final student records
display_students()


# =========================================================
# END OF PROGRAM
# =========================================================
print("\nProgram executed successfully.")

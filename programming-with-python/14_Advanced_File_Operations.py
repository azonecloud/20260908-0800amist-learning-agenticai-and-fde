"""
===========================================================
            ADVANCED FILE OPERATIONS IN PYTHON
===========================================================

Author  : Python Learning Example
Purpose : Demonstrate advanced real-world file handling

Topics Covered:
    1. Writing files
    2. Reading files
    3. Appending files
    4. Using with statement
    5. Reading line by line
    6. File existence checking
    7. Exception handling
    8. CSV file handling
    9. JSON file handling
   10. Binary file operations
   11. File copying
   12. File renaming
   13. File deletion
   14. Directory operations
   15. Real-world logging system

===========================================================
"""


# =========================================================
# IMPORT REQUIRED MODULES
# =========================================================
import os
import json
import csv
import shutil
from datetime import datetime


# =========================================================
# 1. WRITING TO A FILE
# =========================================================
print("\n========== WRITING TO FILE ==========")

with open("students.txt", "w") as file:

    file.write("Rahul Kumar\n")
    file.write("Priya Sharma\n")
    file.write("Arjun Reddy\n")

print("Data written successfully.")


# =========================================================
# 2. READING FROM A FILE
# =========================================================
print("\n========== READING FILE ==========")

with open("students.txt", "r") as file:

    content = file.read()

print(content)


# =========================================================
# 3. APPENDING TO A FILE
# =========================================================
print("\n========== APPENDING DATA ==========")

with open("students.txt", "a") as file:

    file.write("Sneha Verma\n")

print("New student appended.")


# =========================================================
# 4. READING FILE LINE BY LINE
# =========================================================
print("\n========== READING LINE BY LINE ==========")

with open("students.txt", "r") as file:

    for line in file:
        print(line.strip())


# =========================================================
# 5. CHECKING FILE EXISTENCE
# =========================================================
print("\n========== FILE EXISTENCE CHECK ==========")

filename = "students.txt"

if os.path.exists(filename):
    print(f"{filename} exists.")
else:
    print(f"{filename} does not exist.")


# =========================================================
# 6. EXCEPTION HANDLING IN FILE OPERATIONS
# =========================================================
print("\n========== EXCEPTION HANDLING ==========")

try:

    with open("unknown.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File not found.")

except Exception as error:
    print("Unexpected Error:", error)


# =========================================================
# 7. CSV FILE HANDLING
# =========================================================
print("\n========== CSV FILE HANDLING ==========")

students_data = [
    ["ID", "Name", "Course"],
    [101, "Rahul", "Python"],
    [102, "Priya", "Data Science"],
    [103, "Arjun", "Machine Learning"]
]

# Writing CSV file
with open("students.csv", "w", newline="") as csv_file:

    writer = csv.writer(csv_file)

    writer.writerows(students_data)

print("CSV file created successfully.")

# Reading CSV file
with open("students.csv", "r") as csv_file:

    reader = csv.reader(csv_file)

    for row in reader:
        print(row)


# =========================================================
# 8. JSON FILE HANDLING
# =========================================================
print("\n========== JSON FILE HANDLING ==========")

student_json = {
    "id": 101,
    "name": "Rahul Kumar",
    "course": "Python",
    "marks": 95
}

# Writing JSON file
with open("student.json", "w") as json_file:

    json.dump(student_json, json_file, indent=4)

print("JSON file written successfully.")

# Reading JSON file
with open("student.json", "r") as json_file:

    data = json.load(json_file)

print(data)


# =========================================================
# 9. BINARY FILE OPERATIONS
# =========================================================
print("\n========== BINARY FILE OPERATIONS ==========")

binary_data = bytes([10, 20, 30, 40, 50])

# Writing binary file
with open("binary_file.bin", "wb") as binary_file:

    binary_file.write(binary_data)

print("Binary file written.")

# Reading binary file
with open("binary_file.bin", "rb") as binary_file:

    content = binary_file.read()

print("Binary Data:", content)


# =========================================================
# 10. FILE COPYING
# =========================================================
print("\n========== FILE COPYING ==========")

shutil.copy("students.txt", "students_backup.txt")

print("File copied successfully.")


# =========================================================
# 11. FILE RENAMING
# =========================================================
print("\n========== FILE RENAMING ==========")

if os.path.exists("students_backup.txt"):

    os.rename("students_backup.txt", "backup_students.txt")

    print("File renamed successfully.")


# =========================================================
# 12. FILE DELETION
# =========================================================
print("\n========== FILE DELETION ==========")

temp_file = "temp.txt"

with open(temp_file, "w") as file:
    file.write("Temporary file")

if os.path.exists(temp_file):

    os.remove(temp_file)

    print("Temporary file deleted.")


# =========================================================
# 13. DIRECTORY OPERATIONS
# =========================================================
print("\n========== DIRECTORY OPERATIONS ==========")

directory_name = "StudentData"

# Create directory
if not os.path.exists(directory_name):

    os.mkdir(directory_name)

    print("Directory created.")

# List files and folders
print("\nFiles and Directories:")
print(os.listdir())


# =========================================================
# 14. REAL-WORLD LOGGING SYSTEM
# =========================================================
print("\n========== LOGGING SYSTEM ==========")

log_message = f"User logged in at {datetime.now()}\n"

with open("application.log", "a") as log_file:

    log_file.write(log_message)

print("Log entry added.")


# =========================================================
# 15. READING LARGE FILES EFFICIENTLY
# =========================================================
print("\n========== LARGE FILE READING ==========")

with open("students.txt", "r") as file:

    while True:

        chunk = file.read(10)

        if not chunk:
            break

        print(chunk)


# =========================================================
# 16. FILE POINTER OPERATIONS
# =========================================================
print("\n========== FILE POINTER OPERATIONS ==========")

with open("students.txt", "r") as file:

    print("First 5 characters:", file.read(5))

    print("Current Position:", file.tell())

    file.seek(0)

    print("After seek():", file.read(5))


# =========================================================
# 17. SAFE FILE HANDLING FUNCTION
# =========================================================
print("\n========== SAFE FILE READER ==========")

def read_file_safely(filename):

    """
    Reads a file safely using exception handling.
    """

    try:

        with open(filename, "r") as file:

            return file.read()

    except FileNotFoundError:
        return "File does not exist."

    except Exception as error:
        return f"Error: {error}"


print(read_file_safely("students.txt"))


# =========================================================
# END OF PROGRAM
# =========================================================
print("\nAdvanced file operations completed successfully.")
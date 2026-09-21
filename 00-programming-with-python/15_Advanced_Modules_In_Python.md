"""
===========================================================
              ADVANCED MODULES IN PYTHON
===========================================================

A module in Python is a file containing Python code
(variables, functions, classes).

This program demonstrates commonly used ADVANCED modules:

1. os          → Operating system operations
2. sys         → System-specific parameters
3. math        → Mathematical operations
4. random      → Random number generation
5. datetime    → Date and time handling
6. time        → Time-related functions
7. collections → Advanced data structures
8. itertools   → Iteration tools
9. statistics  → Statistical calculations
10. re         → Regular expressions

===========================================================
"""

# =========================================================
# 1. OS MODULE (OPERATING SYSTEM)
# =========================================================
import os

print("\n========== OS MODULE ==========")

print("Current Directory:", os.getcwd())

# List files in directory
print("Files:", os.listdir())


# =========================================================
# 2. SYS MODULE (SYSTEM INFORMATION)
# =========================================================
import sys

print("\n========== SYS MODULE ==========")

print("Python Version:", sys.version)
print("Platform:", sys.platform)


# =========================================================
# 3. MATH MODULE
# =========================================================
import math

print("\n========== MATH MODULE ==========")

print("Square Root of 144:", math.sqrt(144))
print("Factorial of 5:", math.factorial(5))
print("Value of Pi:", math.pi)


# =========================================================
# 4. RANDOM MODULE
# =========================================================
import random

print("\n========== RANDOM MODULE ==========")

print("Random Number (1-10):", random.randint(1, 10))

students = ["Rahul", "Priya", "Arjun", "Sneha"]
print("Random Student:", random.choice(students))


# =========================================================
# 5. DATETIME MODULE
# =========================================================
from datetime import datetime

print("\n========== DATETIME MODULE ==========")

now = datetime.now()
print("Current Date & Time:", now)
print("Year:", now.year)
print("Month:", now.month)


# =========================================================
# 6. TIME MODULE
# =========================================================
import time

print("\n========== TIME MODULE ==========")

print("Starting process...")
time.sleep(1)
print("1 second delay completed")


# =========================================================
# 7. COLLECTIONS MODULE
# =========================================================
from collections import Counter, defaultdict, deque

print("\n========== COLLECTIONS MODULE ==========")

# Counter example
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = Counter(data)
print("Counter:", count)

# defaultdict example
dd = defaultdict(int)
dd["a"] += 1
print("DefaultDict:", dd)

# deque example
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print("Deque:", dq)


# =========================================================
# 8. ITERTOOLS MODULE
# =========================================================
import itertools

print("\n========== ITERTOOLS MODULE ==========")

# combinations
items = ["A", "B", "C"]
print("Combinations:", list(itertools.combinations(items, 2)))

# permutations
print("Permutations:", list(itertools.permutations(items, 2)))


# =========================================================
# 9. STATISTICS MODULE
# =========================================================
import statistics

print("\n========== STATISTICS MODULE ==========")

marks = [80, 85, 90, 95, 100]

print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))
print("Standard Deviation:", statistics.stdev(marks))


# =========================================================
# 10. REGEX MODULE (re)
# =========================================================
import re

print("\n========== REGEX MODULE ==========")

text = "My email is python@example.com"

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

match = re.search(pattern, text)

if match:
    print("Email Found:", match.group())


# =========================================================
# 11. PRACTICAL REAL-WORLD MINI PROJECT
# =========================================================
print("\n========== MINI PROJECT ==========")

# Generate random student marks and calculate average
students = {
    "Rahul": [random.randint(60, 100) for _ in range(5)],
    "Priya": [random.randint(60, 100) for _ in range(5)],
    "Arjun": [random.randint(60, 100) for _ in range(5)]
}

for name, marks in students.items():

    avg = statistics.mean(marks)

    print(f"{name} Marks: {marks}")
    print(f"{name} Average: {avg:.2f}\n")


# =========================================================
# 12. TIME-BASED LOGGING EXAMPLE
# =========================================================
print("\n========== LOGGING WITH TIME ==========")

log = f"System executed at {datetime.now()}\n"

with open("system_log.txt", "a") as file:
    file.write(log)

print("Log saved.")


# =========================================================
# END OF PROGRAM
# =========================================================
print("\nAll advanced modules demonstrated successfully.")
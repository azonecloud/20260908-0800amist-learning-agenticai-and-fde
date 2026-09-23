"""==========================================================
        REAL-WORLD EXAMPLES OF IF STATEMENTS
              AND WHILE LOOPS IN PYTHON
===========================================================

This program demonstrates how IF statements and WHILE loops
are used in real-world applications such as:

1. ATM Machine
2. Login Authentication System
3. Online Shopping Discount System
4. Traffic Signal Monitoring
5. Hospital Patient Check System
6. Mobile Battery Monitoring
7. Password Retry System
8. Banking Balance Checker

===========================================================
"""


# =========================================================
# 1. ATM WITHDRAWAL SYSTEM
# =========================================================
print("\n========== ATM WITHDRAWAL SYSTEM ==========")

balance = 5000
withdraw_amount = 2000

if withdraw_amount <= balance:
    balance -= withdraw_amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")


# =========================================================
# 2. LOGIN AUTHENTICATION SYSTEM
# =========================================================
print("\n========== LOGIN AUTHENTICATION ==========")

username = "admin"
password = "12345"

entered_username = "admin"
entered_password = "12345"

if entered_username == username:

    if entered_password == password:
        print("Login Successful")
    else:
        print("Wrong Password")

else:
    print("Invalid Username")


# =========================================================
# 3. ONLINE SHOPPING DISCOUNT SYSTEM
# =========================================================
print("\n========== ONLINE SHOPPING ==========")

cart_total = 4500

if cart_total >= 5000:
    discount = 20
elif cart_total >= 3000:
    discount = 10
else:
    discount = 5

print("Cart Total:", cart_total)
print("Discount Applied:", discount, "%")


# =========================================================
# 4. TRAFFIC SIGNAL SYSTEM
# =========================================================
print("\n========== TRAFFIC SIGNAL ==========")

signal = "RED"

if signal == "RED":
    print("STOP")
elif signal == "YELLOW":
    print("GET READY")
elif signal == "GREEN":
    print("GO")
else:
    print("Invalid Signal")


# =========================================================
# 5. HOSPITAL TEMPERATURE CHECK
# =========================================================
print("\n========== HOSPITAL TEMPERATURE CHECK ==========")

body_temperature = 102

if body_temperature > 100:
    print("Patient has fever")
else:
    print("Temperature is normal")


# =========================================================
# 6. MOBILE BATTERY MONITORING SYSTEM
# =========================================================
print("\n========== MOBILE BATTERY MONITOR ==========")

battery = 100

while battery > 0:

    print("Battery Level:", battery, "%")

    battery -= 20

print("Phone switched off")


# =========================================================
# 7. PASSWORD RETRY SYSTEM
# =========================================================
print("\n========== PASSWORD RETRY SYSTEM ==========")

correct_password = "python123"

attempts = 0
max_attempts = 3

while attempts < max_attempts:

    entered_password = "python123"

    if entered_password == correct_password:
        print("Access Granted")
        break

    else:
        print("Wrong Password")

    attempts += 1

else:
    print("Maximum attempts exceeded")


# =========================================================
# 8. BANK ACCOUNT BALANCE CHECKER
# =========================================================
print("\n========== BANK BALANCE CHECKER ==========")

account_balance = 10000

while account_balance > 0:

    withdraw = 2500

    if withdraw <= account_balance:
        account_balance -= withdraw
        print("Withdrawn:", withdraw)
        print("Remaining Balance:", account_balance)

    else:
        print("Not enough balance")
        break


# =========================================================
# 9. FACTORY MACHINE MONITORING
# =========================================================
print("\n========== FACTORY MACHINE MONITOR ==========")

machine_temperature = 70

while machine_temperature <= 100:

    print("Machine Temperature:", machine_temperature)

    if machine_temperature >= 90:
        print("WARNING: High Temperature")

    machine_temperature += 10

print("Machine Shutdown")


# =========================================================
# 10. STUDENT ATTENDANCE SYSTEM
# =========================================================
print("\n========== STUDENT ATTENDANCE SYSTEM ==========")

attendance_percentage = 82

if attendance_percentage >= 75:
    print("Eligible for Exams")
else:
    print("Not Eligible for Exams")


# =========================================================
# 11. E-COMMERCE ORDER TRACKING
# =========================================================
print("\n========== ORDER TRACKING ==========")

order_status = "Shipped"

if order_status == "Processing":
    print("Your order is being prepared")
elif order_status == "Shipped":
    print("Your order is on the way")
elif order_status == "Delivered":
    print("Order delivered successfully")
else:
    print("Unknown status")


# =========================================================
# 12. SIMPLE COUNTDOWN TIMER
# =========================================================
print("\n========== COUNTDOWN TIMER ==========")

timer = 5

while timer > 0:
    print("Time Left:", timer)
    timer -= 1

print("Time's up!")


# =========================================================
# END OF PROGRAM
# =========================================================
print("\nAll real-world examples executed successfully.")

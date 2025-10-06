# Problem: Teacher must count students first!
num_students = int(input("How many students? "))
total = 0

for i in range(num_students):
    grade = float(input("Enter grade: "))
    total += grade

average = total / num_students
print(f"Average: {average}")

# Complete sentinel pattern - all three parts labeled
grade = float(input("Enter grade (-1 to stop): "))  # Part 1: Prime input

while grade != -1:  # Part 2: Condition
    print(f"You entered: {grade}")
    grade = float(input("Enter grade (-1 to stop): "))  # Part 3: Update input

print("Done entering grades!")


grade = float(input("Enter grade (-1 to stop): "))

while grade != -1:
    print(f"You entered: {grade}")
    # Forgot to ask for next grade

# Infinite loop
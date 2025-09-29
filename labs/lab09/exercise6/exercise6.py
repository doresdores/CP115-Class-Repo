position = input()
overtime_hours = int(input())
is_weekend = input()

# TODO: Your code here
base_rates = {
    "Manager": 30,
    "Supervisor": 20,
    "Staff": 15,
    "Intern": 8
}

base_rate = base_rates.get(position, 0)

if overtime_hours <= 8:
    overtime_pay = overtime_hours * base_rate * 1.5
else:
    overtime_pay = (8 * base_rate * 1.5) + ((overtime_hours - 8) * base_rate * 2.0)


if is_weekend == "yes":
    overtime_pay += overtime_hours * 5

print(round(overtime_pay, 2))


print(overtime_pay)
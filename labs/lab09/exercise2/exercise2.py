employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
if tax_status == "single":
    if total_income >= 5000:
        tax_rate = 0.22
    else:
        tax_rate = 0.18
elif tax_status == "married":
    if total_income >= 6000:
        tax_rate = 0.20
    else:
        tax_rate = 0.15
elif tax_status == "head":
    if total_income >= 5500:
        tax_rate = 0.25
    else:
        tax_rate = 0.19


print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
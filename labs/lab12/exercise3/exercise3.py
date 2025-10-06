age_input = input()

# TODO: Your code here
total_age = 0
age_count = 0
while age_input != "done":
    age = int(age_input)
    total_age += age
    age_count += 1
    age_input = input()


if age_count == 0:
    average_age =0
else:
    average_age = total_age / age_count


print(age_count)
print(total_age)
print(f"{average_age:.2f}")



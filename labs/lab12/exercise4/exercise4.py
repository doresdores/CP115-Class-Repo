score_input = input()

# TODO: Your code here
passing_count =0
failing_count =0
score_count = 0

while score_input != "end":
    score_count += 1  
    score = int(score_input) 
    score_input = input()
    if score >= 60 :
        passing_count += 1
    else:
        failing_count += 1


if (passing_count == 0) :
    pass_rate = 0
else:
    pass_rate = (passing_count / score_count) * 100

print(passing_count)
print(failing_count)
print(f"{pass_rate:.2f}")

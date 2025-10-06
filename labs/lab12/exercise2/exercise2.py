score = float(input())

# TODO: Your code here
score_count = 0
total_score = 0

while not (score <0 or score >100) :
    score_count +=1
    total_score += score
    score = float(input())

if total_score == 0:
    average_score= 0
else:
    average_score = total_score / score_count

print(score_count)
print(total_score)
print(f"{average_score:.2f}")

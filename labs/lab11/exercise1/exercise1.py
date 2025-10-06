num_rounds = int(input())
# TODO: Your code here
total_score = 0
rounds_processed = 0

for num in range(num_rounds):
    round_score = int(input())
    if round_score > 100:
        round_score += int(0.2 * round_score)  
    total_score += round_score
    rounds_processed += 1

print(f"{total_score:.1f}")
print(rounds_processed)




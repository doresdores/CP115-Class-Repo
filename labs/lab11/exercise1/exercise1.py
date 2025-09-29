num_rounds = int(input())
# TODO: Your code here
# Use input() inside the loop to get each round's score

total_score = 0
rounds_processed = 0

for _ in range(num_rounds):
    round_score = int(input())  # integer input only
    if round_score > 100:
        round_score += int(0.2 * round_score)  # 20% bonus rounded down
    total_score += round_score
    rounds_processed += 1

print(f"{total_score:.1f}")
print(rounds_processed)




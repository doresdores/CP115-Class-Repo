target_points = int(input("targer point:"))

# TODO: Your code here
# Use input() inside the while loop to get points each round
point = int(input())
while point != target_points:
    
    level += step
    step += 1  # Increase step each time

print(total_points)
print(rounds_played)
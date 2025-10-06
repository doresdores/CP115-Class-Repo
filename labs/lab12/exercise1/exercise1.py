price = float(input())

# TODO: Your code here
total_cost = 0
item_count = 0
while price > -1:  
    item_count += 1
    total_cost += price
    price = float(input()) 

print(item_count)
print(f"{total_cost:.2f}")

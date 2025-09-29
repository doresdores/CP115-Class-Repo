age = int(input())
accident_count = int(input())

# Your code here
if age > 50 :
    base_premium = 2000
elif age >= 25 :
    base_premium = 1800
else:
    base_premium = 2400

if accident_count >= 3:
    accident_penalty =600
    final_premium = base_premium - accident_penalty

elif accident_count >= 1:
    accident_penalty = 300
    final_premium = base_premium - accident_penalty

else :
    discount_amount = 0.1 * base_premium
    final_premium = base_premium + discount_amount
    print('NO PENALTY')




print(base_premium)
print(final_premium)
print(discount_amount)
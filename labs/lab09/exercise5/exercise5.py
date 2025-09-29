main_course = input()
drink = input()
dessert = input()
customer_age = int(input())

# TODO: Your code here
main_course_prices = {
    "Chicken": 10,
    "Beef": 12,
    "Fish": 11
}

drink_prices = {
    "Soft Drink": 2,
    "Coffee": 3
}

dessert_prices = {
    "Ice Cream": 4,
    "Cake": 5
}


main_price = main_course_prices.get(main_course, 0)
drink_price = drink_prices.get(drink, 0)
dessert_price = dessert_prices.get(dessert, 0)


food_cost = main_price + drink_price + dessert_price
service_charge = 0.10 * food_cost
total_with_service = food_cost + service_charge


if customer_age > 60:
    discount = 0.15 * total_with_service
elif customer_age < 18:
    discount = 0.10 * total_with_service
else:
    discount = 0


final_bill = total_with_service - discount
print(f"{final_bill:.2f}")
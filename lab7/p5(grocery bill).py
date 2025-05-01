grocery_prices = {
    "apple": 160.0,
    "banana": 50.0,
    "milk": 80.0,
    "bread": 40.0,
    "eggs": 120.0
}

grocery_quantity = {
    "apple": 3,
    "banana": 6,
    "milk": 1,
    "bread": 2,
    "eggs": 1
}

total_bill = 0

for item in grocery_prices:
    if item in grocery_quantity:
        total_bill += grocery_prices[item] * grocery_quantity[item]

print("Total Bill: ₹", total_bill)
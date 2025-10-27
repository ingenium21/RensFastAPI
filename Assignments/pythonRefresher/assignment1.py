"""
- You have $50 
- you buy an item that is $15
- with a tax of 3%
- print how much money you have left
"""

current_money = 50
item_price = 15
tax_rate = 0.03

total_cost = item_price * (1 + tax_rate)
remaining_money = current_money - total_cost
print("Money left: $", round(remaining_money, 2))

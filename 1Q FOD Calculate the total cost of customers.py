item_prices = [2.5, 1.0, 3.75]  
quantities = [3, 5, 2]  
discount_rate = 10 
tax_rate = 8 

total_cost_before_discount = sum(price * quantity for price, quantity in zip(item_prices, quantities))

discounted_cost = total_cost_before_discount * (1 - discount_rate / 100)

total_cost_after_tax = discounted_cost * (1 + tax_rate / 100)

print("Total Cost: $", round(total_cost_after_tax, 2))

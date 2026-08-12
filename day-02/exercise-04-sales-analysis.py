"""
Exercise: Sales List Analysis
Student: Ayush Rayamajhi
Day: 2
"""

monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

# 1. Highest to lowest
sorted_sales = sorted(monthly_sales, reverse=True)

# 2. Sales above 100000
high_sales = [amount for amount in monthly_sales if amount > 100000]

# 3. Add 13% tax
sales_with_tax = [amount * 1.13 for amount in monthly_sales]

# 4. Total sales
total_sales = sum(monthly_sales)

# 5. Average sales
average_sales = total_sales / len(monthly_sales)

print("Highest to lowest:", sorted_sales)
print("Sales above NPR 100000:", high_sales)
print("Sales with 13% tax:", sales_with_tax)
print(f"Total sales: NPR {total_sales:.2f}")
print(f"Average sales: NPR {average_sales:.2f}")
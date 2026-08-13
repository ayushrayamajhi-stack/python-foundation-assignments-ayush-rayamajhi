"""
Exercise: Inventory Value from CSV
Student: Ayush Rayamajhi
Day: 4
"""

import csv


def total_inventory_value(path):
    total = 0.0

    with open(path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            price = float(row["price"])
            quantity = int(row["quantity"])

            total += price * quantity

    return round(total, 2)


# Test
print(total_inventory_value("products.csv"))
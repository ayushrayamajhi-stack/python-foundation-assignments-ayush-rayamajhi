"""
Exercise: Nested Order Summary
Student: Ayush Rayamajhi
Day: 2
"""

orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

# 1. Print every order ID and customer
print("Order customers:")

for order_id, order in orders.items():
    print(f"{order_id}: {order['customer']}")

# 2. Print only completed orders
print("\nCompleted orders:")

for order_id, order in orders.items():
    if order["status"] == "Completed":
        print(f"{order_id}: {order['customer']} - NPR {order['amount']}")

# 3. Calculate total amount of completed orders
completed_total = sum(
    order["amount"]
    for order in orders.values()
    if order["status"] == "Completed"
)

# 4. Count pending orders
pending_count = sum(
    1
    for order in orders.values()
    if order["status"] == "Pending"
)

print(f"\nTotal completed amount: NPR {completed_total}")
print(f"Pending orders: {pending_count}")

# 5. Add a new order
orders["ORD-004"] = {
    "customer": "Sagar",
    "amount": 4200,
    "status": "Completed"
}

print("\nNew order added:")
print(f"ORD-004: {orders['ORD-004']['customer']} - NPR {orders['ORD-004']['amount']}")
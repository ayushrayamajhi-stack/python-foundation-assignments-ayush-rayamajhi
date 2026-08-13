"""
Exercise: Simple Interest Calculator
Student: Ayush Rayamajhi
Day: 3
"""

# Function with default arguments
def calculate_simple_interest(principal, rate=5, time=1):
    interest = (principal * rate * time) / 100
    return interest


# Test cases
print(calculate_simple_interest(1000, 10, 2))
print(calculate_simple_interest(1000))
print(calculate_simple_interest(2000, time=3))
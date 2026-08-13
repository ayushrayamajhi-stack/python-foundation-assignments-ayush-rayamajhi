"""
Exercise: Analyze Numbers
Student: Ayush Rayamajhi
Day: 3
"""

def analyze_numbers(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    total = sum(numbers)
    descending = sorted(numbers, reverse=True)

    return smallest, largest, total, descending


# Test the function
smallest, largest, total, desc = analyze_numbers([4, 9, 1, 7, 3])

print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
print(f"Total: {total}")
print(f"Descending: {desc}")
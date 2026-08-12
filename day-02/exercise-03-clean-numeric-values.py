"""
Exercise: Clean Numeric Values
Student: Ayush Rayamajhi
Day: 2
"""

raw_values = [100, None, 250, "invalid", 300, None, 450]

valid_values = []

for value in raw_values:
    if not isinstance(value, int):
        continue

    valid_values.append(value)

print("Valid values:", valid_values)

valid_values_comprehension = [
    value for value in raw_values
    if isinstance(value, int)
]

print("Using comprehension:", valid_values_comprehension)
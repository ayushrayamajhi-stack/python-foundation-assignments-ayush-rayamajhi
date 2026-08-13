"""
Exercise: Class Average
Student: Ayush Rayamajhi
Day: 3
"""

# Accept any number of scores using *args
def class_average(*scores):
    if not scores:
        return 0

    return round(sum(scores) / len(scores), 2)


# Test cases
print(class_average(80, 90, 70))
print(class_average(55, 60, 65, 70, 75))
print(class_average())
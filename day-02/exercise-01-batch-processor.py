"""
Exercise: Batch Processor
Student: Ayush Rayamajhi
Day: 2
"""

for batch_number in range(1, 11):
    print(f"Processing batch {batch_number}")

    if batch_number % 3 == 0:
        print("Checkpoint reached")
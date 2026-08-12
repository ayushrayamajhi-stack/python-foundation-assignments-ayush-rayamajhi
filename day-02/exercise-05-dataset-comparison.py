"""
Exercise: Dataset Comparison
Student: Ayush Rayamajhi
Day: 2
"""

dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

# All unique dataset names
all_datasets = dataset_a | dataset_b

# Found in both
common_datasets = dataset_a & dataset_b

# Only in dataset A
only_a = dataset_a - dataset_b

# Only in dataset B
only_b = dataset_b - dataset_a

print("All unique datasets:", all_datasets)
print("Datasets in both:", common_datasets)
print("Only in dataset A:", only_a)
print("Only in dataset B:", only_b)
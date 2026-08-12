"""
Exercise: File Validator
Student: Ayush Rayamajhi
Day: 1
"""

# Get file name from user
file_name = input("Enter a file name: ").strip().lower()

# Supported extensions
allowed_extensions = (".csv", ".json", ".parquet")

# Validate file
if file_name.endswith(allowed_extensions):
    print(f"Valid file: {file_name}")
else:
    print("Invalid file type.")
    print("Accepted formats: .csv, .json, .parquet")
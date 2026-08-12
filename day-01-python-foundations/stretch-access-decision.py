"""
Exercise: Dataset Access Decision
Student: Ayush Rayamajhi
Day: 1
"""

# Input values
user_role = "analyst"
is_active = True
requested_dataset = "sales_data"

# Access rules
allowed_roles = ["analyst", "scientist", "engineer"]
restricted_datasets = ["salary_data", "personal_data"]

# Access decision
if not is_active:
    print("Access denied because the user is inactive.")
elif user_role not in allowed_roles:
    print("Access denied because the role is not allowed.")
elif requested_dataset in restricted_datasets:
    print("Access denied because the dataset is restricted.")
else:
    print("Access granted.")
    
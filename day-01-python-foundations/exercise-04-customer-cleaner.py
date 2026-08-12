"""
Exercise: Customer Record Cleaner
Student: Ayush Rayamajhi
Day: 1
"""

# Raw data
raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

# Clean data
name = raw_name.strip().title()
city = raw_city.strip().title()
age = int(raw_age.strip())
email = raw_email.strip().lower()

# Ternary expression
status = "Adult" if age >= 18 else "Minor"

# Output
print(f"Name: {name}")
print(f"City: {city}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Status: {status}")
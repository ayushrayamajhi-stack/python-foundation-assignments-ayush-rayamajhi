"""
Exercise: Pipeline Health Status
Student: Ayush Rayamajhi
Day: 1
"""

# Input values
rows_loaded = 9800
rows_failed = 200
runtime_minutes = 18

# Calculations
total_rows = rows_loaded + rows_failed
failure_rate = (rows_failed / total_rows) * 100

# Determine pipeline status
if failure_rate <= 2 and runtime_minutes <= 20:
    status = "Healthy"
elif failure_rate <= 5:
    status = "Warning"
else:
    status = "Critical"

# Output
print(f"Rows loaded: {rows_loaded}")
print(f"Rows failed: {rows_failed}")
print(f"Failure rate: {failure_rate:.2f}%")
print(f"Runtime: {runtime_minutes} minutes")
print(f"Pipeline status: {status}")
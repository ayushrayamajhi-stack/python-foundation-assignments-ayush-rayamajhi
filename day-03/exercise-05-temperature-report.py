"""
Exercise: Temperature Report
Student: Ayush Rayamajhi
Day: 3
"""

import random
import datetime
import temperature_utils


# Generate 5 random Celsius temperatures between 15 and 40
celsius_temperatures = [
    random.randint(15, 40)
    for _ in range(5)
]


# Convert Celsius temperatures to Fahrenheit
fahrenheit_temperatures = [
    temperature_utils.celsius_to_fahrenheit(celsius)
    for celsius in celsius_temperatures
]


# Get today's date
today = datetime.datetime.now()
date_string = today.strftime("%d-%m-%Y")


# Display the report
print(f"Temperature Report — {date_string}")
print(f"Celsius:    {celsius_temperatures}")
print(f"Fahrenheit: {fahrenheit_temperatures}")
print(f"Module version: {temperature_utils.MODULE_VERSION}")
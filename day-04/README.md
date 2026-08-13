# Day 4: File Handling, Error Handling & Logging

## Topics Covered

- File handling
- Reading and writing text files
- `with open()`
- CSV files
- `csv.DictReader`
- JSON files
- `json.load()`
- `json.dump()`
- Data type conversion
- List comprehensions
- Exception handling
- Custom exceptions
- `try`
- `except`
- `else`
- `finally`
- `raise`
- Logging
- `logging.getLogger()`
- `FileHandler`
- Data validation
- Basic data-processing pipelines

## Exercises

1. Line and Word Counter
2. Inventory Value from CSV
3. Filtering a JSON Library Catalog
4. Custom Exception for User Registration
5. Order Processing Pipeline with Logging

## How to Run

Run each Python file using:

```bash
python3 exercise-01-line-word-counter.py
python3 exercise-02-inventory-value.py
python3 exercise-03-library-catalog.py
python3 exercise-04-user-registration.py
python3 exercise-05-order-pipeline.py
```
Make sure the required input files are in the same directory when running the exercises.

## What I Learned

This day focused on working with files, handling errors, validating data, and creating a simple data-processing pipeline.

I learned how to read and write files using with open() and how to work with CSV files using csv.DictReader. I also practiced converting CSV values from strings into integers and floats before performing calculations.

I learned how to work with JSON files using json.load() and json.dump() and how to filter data before saving the processed results.

I also learned how Python handles exceptions using try, except, else, and finally. I practiced creating a custom exception using a class that inherits from Exception and using raise to trigger it when invalid data is provided.

Finally, I learned the basics of Python logging and used a logger with a FileHandler to record successful and failed records while processing an order dataset.

## Challenges Faced

The most challenging exercise was the order-processing pipeline because it combined several concepts into one program.

I had to handle invalid data, negative values, file errors, logging, JSON output, and valid and invalid record counts at the same time.

Understanding custom exceptions and the difference between handling an exception and deliberately raising one was also challenging.

I solved these problems by breaking the program into smaller steps and testing each part individually before combining everything into the complete pipeline.
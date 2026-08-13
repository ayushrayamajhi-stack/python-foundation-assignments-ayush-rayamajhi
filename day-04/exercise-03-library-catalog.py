"""
Exercise: Filtering a JSON Library Catalog
Student: Ayush Rayamajhi
Day: 4
"""

import json


def available_books_after(json_path, year, output_path):
    with open(json_path, "r") as file:
        books = json.load(file)

    titles = [
        book["title"]
        for book in books
        if book["available"] and book["year"] > year
    ]

    with open(output_path, "w") as file:
        json.dump(titles, file, indent=2)

    return titles


# Test
result = available_books_after(
    "library.json",
    2015,
    "available_books.json"
)

print(result)
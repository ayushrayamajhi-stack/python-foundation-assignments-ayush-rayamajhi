"""
Exercise: Line and Word Counter
Student: Ayush Rayamajhi
Day: 4
"""

def line_word_counter(path):
    with open(path, "r") as file:
        lines = file.readlines()

    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)

    return num_lines, num_words


# Test
print(line_word_counter("diary.txt"))
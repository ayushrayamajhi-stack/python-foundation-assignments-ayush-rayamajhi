"""
Exercise: Student Score Dictionary
Student: Ayush Rayamajhi
Day: 2
"""

student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}

# 1. Print every student and score
print("Student scores:")

for student, score in student_scores.items():
    print(f"{student}: {score}")

# 2. Passing students
passing_students = {
    student: score
    for student, score in student_scores.items()
    if score >= 60
}

# 3. Highest scoring student
highest_student = max(student_scores, key=student_scores.get)
highest_score = student_scores[highest_student]

# 4. Average score
average_score = sum(student_scores.values()) / len(student_scores)

print("\nPassing students:")
for student, score in passing_students.items():
    print(f"{student}: {score}")

print(f"\nHighest scorer: {highest_student} ({highest_score})")
print(f"Average score: {average_score:.2f}")
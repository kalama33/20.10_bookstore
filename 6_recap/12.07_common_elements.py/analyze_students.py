students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 92]},
    {"name": "Bob", "age": 21, "grades": [80, 88, 94]},
    {"name": "Charlie", "age": 19, "grades": [90, 95, 98]},
    {"name": "David", "age": 20, "grades": [75, 82, 87]}
]


def analyze_students(students):
    for student in students:
        grades = student["grades"]
        average_grade = sum(grades) / len(grades)
        student["average_grade"] = average_grade

    oldest_student = max(students, key=lambda x: x["age"])
    youngest_student = min(students, key=lambda x: x["age"])
    oldest_name = [student for students in students]
    
    # oldest_youngest = (oldest_student["name"], youngest_student["name"])

    age_student_counts = {}
    for student in students:
        age = student["age"]
        if age in age_student_counts:
            age_student_counts[age].append(student["name"])
        else:
            age_student_counts[age] = [student["name"]]

    return oldest_youngest, age_student_counts


result = analyze_students(students)
oldest_youngest = result[0]
age_student_counts = result[1]

print("Oldest and youngest students:", oldest_youngest)
print("Student counts by age:", age_student_counts)
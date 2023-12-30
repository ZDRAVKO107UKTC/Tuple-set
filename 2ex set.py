students_count = int(input())
grades_dict = {}

for _ in range(students_count):
    name, grade = input().split()
    grade = float(grade)

    if name not in grades_dict:
        grades_dict[name] = []

    grades_dict[name].append(grade)

for student, grades in grades_dict.items():
    average_grade = sum(grades) / len(grades)
    formatted_grades = ' '.join(f"{grade:.2f}" for grade in grades)
    print(f"{student} -> {formatted_grades} (avg: {average_grade:.2f})")

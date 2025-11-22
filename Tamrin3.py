# لیست دانشجویان  دیکشنری‌ها
students_list = [
    {
        "student_id": 1,
        "name": "علی",
        "grades": [18, 19, 20]
    },
    {
        "student_id": 2,
        "name": "زهرا",
        "grades": [15, 14, 16.5]
    }
]


def calculate_student_gpa(student):
    grades = student["grades"]
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


for student in students_list:
    gpa = calculate_student_gpa(student)
    print(f"معدل {student['name']} : {gpa:.2f}")  
  

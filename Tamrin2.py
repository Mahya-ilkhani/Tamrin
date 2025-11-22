def get_positive_int(message):
    value = int(input(message))
    while value <= 0:
        print("لطفاً یک عدد صحیح بزرگ‌تر از صفر وارد کنید.")
        value = int(input(message))
    return value


def get_grade(message):
    grade = float(input(message))
    return grade


def evaluate_average(avg):
    if avg >= 17:
        return "عالی"
    elif avg >= 12:
        return "قبول"
    else:
        return "مشروط"


def main():
    print("برنامهٔ محاسبهٔ معدل ساده")
    course_count = get_positive_int("تعداد درس‌ها را وارد کنید: ")

    grades = []
    for i in range(1, course_count + 1):
        g = get_grade(f"نمرهٔ درس {i} را وارد کنید: ")
        grades.append(g)

    avg = sum(grades) / len(grades)
    status = evaluate_average(avg)

    print("\n--- نتیجه ---")
    print(f"نمرات وارد شده: {grades}")
    print(f"میانگین: {avg:.2f}")
    print(f"وضعیت: {status}")


if __name__ == "__main__":
    main()

#include <iostream>
using namespace std;

int get_positive_int(const string& message) {
    int value;
    cout << message;
    cin >> value;

    while (value <= 0) {
        cout << "لطفاً یک عدد صحیح بزرگ‌تر از صفر وارد کنید: ";
        cin >> value;
    }
    return value;
}

float get_grade(const string& message) {
    float grade;
    cout << message;
    cin >> grade;
    return grade;
}

string evaluate_average(float avg) {
    if (avg >= 17)
        return "عالی";
    else if (avg >= 12)
        return "قبول";
    else
        return "مشروط";
}

int main() {
    cout << "برنامهٔ محاسبهٔ معدل ساده" << endl;

    int course_count = get_positive_int("تعداد درس‌ها را وارد کنید: ");

    
    float* grades = new float[course_count];

    for (int i = 0; i < course_count; i++) {
        grades[i] = get_grade("نمرهٔ درس " + to_string(i + 1) + " را وارد کنید: ");
    }

    float sum = 0;
    for (int i = 0; i < course_count; i++) {
        sum += grades[i];
    }

    float avg = sum / course_count;
    string status = evaluate_average(avg);

    cout << "\n--- نتیجه ---\n";
    cout << "نمرات وارد شده: ";
    for (int i = 0; i < course_count; i++) {
        cout << grades[i] << " ";
    }

    cout << "\nمیانگین: " << avg;
    cout << "\nوضعیت: " << status << endl;

    
    delete[] grades;

    return 0;
}

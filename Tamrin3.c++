

#include <iostream>
#include <string>

using namespace std;

struct Student {
    int student_id;
    string name;
    float grades[3];
    int grade_count;
    
    
    float calculate_gpa() {
        if (grade_count == 0) return 0;
        float sum = 0;
        for (int i = 0; i < grade_count; i++) {
            sum += grades[i];
        }
        return sum / grade_count;
    }
};

int main() {
    
    Student students[2] = {
        {1, "علی", {18, 19, 20}, 3},
        {2, "زهرا", {15, 14, 16.5}, 3}
    };
    
  
    for (int i = 0; i < 2; i++) {
        float gpa = students[i].calculate_gpa();
        cout << "معدل " << students[i].name << " : " << gpa << endl;
    }
    
    return 0;
}
 

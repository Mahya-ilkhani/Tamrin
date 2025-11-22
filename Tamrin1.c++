#include <iostream>
#include <string>
using namespace std;

int main() {
    string name;
    int birth_year;
    int current_year = 2025; 

    cout << "Please enter your name: ";
    getline(cin, name);

    cout << "Please enter your year of birth: ";
    cin >> birth_year;

    int age = current_year - birth_year;

    cout << "Hello, " << name << "! You are approximately " << age << " years old." << endl;

    return 0;
}

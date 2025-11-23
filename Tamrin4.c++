#include <iostream>
#include <string>
using namespace std;

class Book {
private:
    string title;  
    string author;   
    double price;    

public:
  
    Book(string t, string a, double p) {
        title = t;
        author = a;
        price = p;
    }

  
    void display_details() const {
        cout << "عنوان کتاب: " << title << endl;
        cout << "نویسنده: " << author << endl;
        cout << "قیمت: " << price << " تومان" << endl;
        cout << "-----------------------------" << endl;
    }

  
    void apply_discount(double percent) {
        price = price - (price * percent / 100.0);
    }
};

int main() {
  
    Book book1("دنیای سوفی", "یوستین گوردر", 200000);
    Book book2("مسخ", "کافکا", 150000);

  
    cout << "اطلاعات اولیه کتاب‌ها:" << endl;
    book1.display_details();
    book2.display_details();

    // اعمال تخفیف
    book1.apply_discount(10);  // 10 درصد
    book2.apply_discount(15);  // 15 درصد

  
    cout << "\nاطلاعات پس از اعمال تخفیف:" << endl;
    book1.display_details();
    book2.display_details();

    return 0;
}

#include <iostream>
#include <string>
using namespace std;


class Vehicle {
protected:
    string brand;
    int year;

public:
    Vehicle(const string& brand, int year)
        : brand(brand), year(year) {}

    virtual void display_info() const {
        cout << "Brand: " << brand << endl;
        cout << "Year: " << year << endl;
    }

    
    virtual ~Vehicle() = default;
};


class Car : public Vehicle {
private:
    int num_doors;

public:
    Car(const string& brand, int year, int num_doors)
        : Vehicle(brand, year), num_doors(num_doors) {}

    void display_info() const override {
        Vehicle::display_info();
        cout << "Number of doors: " << num_doors << endl;
    }
};


class Motorcycle : public Vehicle {
private:
    bool has_sidecar;

public:
    Motorcycle(const string& brand, int year, bool has_sidecar)
        : Vehicle(brand, year), has_sidecar(has_sidecar) {}

    void display_info() const override {
        Vehicle::display_info();
        cout << "Has sidecar: " 
             << (has_sidecar ? "Yes" : "No") 
             << endl;
    }
};

int main() {
    Vehicle v("GenericBrand", 2010);
    cout << "=== Vehicle ===" << endl;
    v.display_info();

    cout << "\n=== Car ===" << endl;
    Car c("Toyota", 2022, 4);
    c.display_info();

    cout << "\n=== Motorcycle ===" << endl;
    Motorcycle m("Harley", 2018, false);
    m.display_info();

    return 0;
}

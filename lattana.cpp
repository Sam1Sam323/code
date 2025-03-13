#include <iostream>
#include <iomanip> // Ð? d?nh d?ng GPA khi in
using namespace std;

class Student {
private:
    string name;
    string id;
    double gpa;

public:
    // Constructor
    Student(string name, string id, double gpa) {
        this->name = name;
        this->id = id;
        setGPA(gpa); // Ki?m tra GPA h?p l?
    }

    // Getter methods
    string getName() const {
        return name;
    }

    string getId() const {
        return id;
    }

    double getGPA() const {
        return gpa;
    }

    // Setter methods
    void setName(string name) {
        this->name = name;
    }

    void setId(string id) {
        this->id = id;
    }

    void setGPA(double gpa) {
        if (gpa >= 0.0 && gpa <= 4.0) { // Ki?m tra h?p l? c?a GPA (gi? s? thang di?m 4.0)
            this->gpa = gpa;
        } else {
            cout << "L?i: GPA ph?i n?m trong kho?ng t? 0.0 d?n 4.0.\n";
            this->gpa = 0.0; // M?c d?nh n?u giá tr? không h?p l?
        }
    }

    // Phuong th?c hi?n th? thông tin sinh viên
    void displayInfo() const {
        cout << "Student Name: " << name << endl;
        cout << "Student ID: " << id << endl;
        cout << "GPA: " << fixed << setprecision(2) << gpa << endl;
    }
};

// Hàm main d? ki?m tra
int main() {
    // T?o m?t d?i tu?ng Student
    Student student("LATTANA", "24D116022", 3.75);
    student.displayInfo();

    // Thay d?i thông tin sinh viên
    cout << "\nC?p nh?t GPA:\n";
    student.setGPA(3.9);
    student.displayInfo();

    return 0;
}


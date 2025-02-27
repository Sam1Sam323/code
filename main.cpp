#include <iostream>
#include <string>

class Person {
private:
    std::string name;
    int age;
    std::string address;

public:
    // Constructor
    Person(std::string name, int age, std::string address) {
        this->name = name;
        this->age = age;
        this->address = address;
    }

    // Getters
    std::string getName() const {
        return name;
    }

    int getAge() const {
        return age;
    }

    std::string getAddress() const {
        return address;
    }

    // Setters
    void setName(std::string name) {
        this->name = name;
    }

    void setAge(int age) {
        if (age >= 0) {
            this->age = age;
        }
    }

    void setAddress(std::string address) {
        this->address = address;
    }

    // Method to display person information
    void displayInfo() const {
        std::cout << "Ho va ten: " << name << std::endl;
        std::cout << "Tuoi: " << age << std::endl;
        std::cout << "Dia chi: " << address << std::endl;
    }
};

int main() {
    // Create a person object
    Person person1("LATTANA", 19, "Xaysomboun");
    
    // Display person information
    person1.displayInfo();
    
    // Update some information
    person1.setAge(19);
    person1.setAddress("Xaysomboun City");
    
    std::cout << "\nAfter updating:" << std::endl;
    person1.displayInfo();
    
    return 0;
} 
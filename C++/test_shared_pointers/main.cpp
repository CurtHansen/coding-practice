#include <string>
#include <iostream>
#include <utility>
#include <vector>
#include <memory>
#include <map>

class Pet{
    friend class Person;
private:
    std::string name;
    std::string type;
public:
    Pet(std::string n,std::string t): name(std::move(n)), type(std::move(t)) {};
    friend std::ostream& operator<< (std::ostream& out, const Pet& pet){
        out << pet.name << "/" << pet.type;
        return out;
    }
};

class Person{
private:
    int age;
    std::string name;
    std::shared_ptr<Pet> pet;
public:
    Person(int a, std::string n): age(a), name(std::move(n)) {};
    Person(int a, std::string n, std::shared_ptr<Pet> p): age(a), name(std::move(n)), pet(std::move(p)) {};
    ~Person()= default;
    void print_name(){std::cout << "My name is: " << name << "." << std::endl;};
    void print_pet(){
        if(pet) { // If we don't check this, we get a memory error if the pet has not been set (i.e., is null).
            std::cout << " My pet is " << *pet << "." << std::endl;
        } else {
            std::cout << " I have no pet." << std::endl;
        }
    };
};

int main() {
    std::vector<std::shared_ptr<Pet>> pets;
    pets.emplace_back(std::make_shared<Pet>("Pluto","dog"));
    pets.emplace_back(std::make_shared<Pet>("Tweety","bird"));
    pets.emplace_back(std::make_shared<Pet>("Felix","cat"));
    pets.emplace_back(std::make_shared<Pet>("Sammy","serpent"));

    std::vector<std::shared_ptr<Person>> people;
    people.emplace_back(std::make_shared<Person>(30,"Bob"));
    people.emplace_back(std::make_shared<Person>(35,"John",pets[0]));
    people.emplace_back(std::make_shared<Person>(40,"Jane",pets[2]));

    for (auto person: people){
        person->print_name();
        person->print_pet();
    }
    return 0;
}
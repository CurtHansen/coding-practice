//
// Created by Curt Hansen on 2024.12.10.
//
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
    Person(int a, std::string n, std::shared_ptr<Pet> p): age(a), name(std::move(n)), pet(std::move(p)) {};
    ~Person()= default;
    void print_name(){std::cout << "My name is: " << name << std::endl;};
    void print_pet(){std::cout << " My pet is " << *pet << std::endl;};
};

typedef std::map<std::shared_ptr<Pet>,float> MapPetScore;


int main(){
    std::vector<Person> people;
    int num_people = 100;
    people.reserve(num_people);

    std::vector<std::shared_ptr<Pet>> pets;
    pets.emplace_back(std::make_shared<Pet>("Pluto","dog"));
    pets.emplace_back(std::make_shared<Pet>("Tweety","bird"));
    pets.emplace_back(std::make_shared<Pet>("Felix","cat"));
    pets.emplace_back(std::make_shared<Pet>("Sammy","serpent"));

    for(int i=0;i<num_people;i++) {
        std::shared_ptr<Pet> ptr_pet = pets[i%4];
        people.emplace_back(10, "Mr."+std::to_string(i),ptr_pet);
        people.back().print_name();
        people.back().print_pet();
    }
    std::cout << people.size() << std::endl;
    return 0;

}
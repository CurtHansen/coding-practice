#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <unordered_set>
#include "template.hpp"



class Animal {
    protected:
        int numlegs;
        bool warmblooded;
    public:
        Animal(){};
        virtual void makenoise()=0;
};

class Insect: private Animal {
    private:
        int numwings;
        int numantennae;
    public:
        Insect(int numwing, int numantenna){
            numlegs = 6;
            warmblooded = false;
            numwings = numwing;
            numantennae = numantenna;
        }
        void makenoise() override {std::cout << "Bzzz" << std::endl;}
        void selfdescribe() {std::cout << "I am an inssect" << std::endl;};
};

void recur_set(int,int,std::unordered_set<int>);


int main(){

    // Test classes.
    Insect bee(4, 2);
    bee.makenoise();
    bee.selfdescribe();

    //////
    std::cout << std::endl;
    std::map<std::string, int> mymap;
    std::map<std::string, int>::iterator it;
    mymap["Curt"] = strlen("Curt");
    mymap["Hansen"] = strlen("Hansen");
    std::string something = "Bob";
    mymap[something] = something.size();
    it = mymap.begin();

    while (it != mymap.end()){
        std::cout << "Name " << it->first << " has number of chars equal to " << it->second << std::endl;
        it++;
    }

    std::string attempt;
    attempt = "Curt";
    it = mymap.find(attempt);
    if (it != mymap.end()){
        std::cout << "Attempt " << attempt << " found with value " << it->second << std::endl;
    } else {
        std::cout << "Attempt " << attempt << " not found." << std::endl;
    }
    attempt = "Joe";
    it = mymap.find(attempt);
    if (it != mymap.end()){
        std::cout << "Attempt " << attempt << " found with value " << it->second << std::endl;
    } else {
        std::cout << "Attempt " << attempt << " not found." << std::endl;
    }

    ///////
    std::cout << std::endl;
    std::string mystring = "CurtHansen";
    int n = mystring.size();
    std::cout << mystring.substr(n-4,1) + mystring.substr(7,2) << std::endl;
    mystring = mystring.substr(0, 3) + mystring.substr(5);
    std::cout << "mystring is now " << mystring << std::endl;

    ///////
    std::cout << std::endl;
    std::queue<int> myqueue;
    myqueue.push(5);
    myqueue.push(50);
    myqueue.push(56);
    myqueue.push(100);
    myqueue.push(500);
    myqueue.push(1012);

    n = 0;
    while (!myqueue.empty()) {
        n = myqueue.front();
        myqueue.pop();
        std::cout << n << std::endl;
    }

    ///////
    std::cout << std::endl;
    struct Person{
        int age=0;
        std::string name;
    };
    Person dad;
    dad.age = 10; dad.name = "Bob";

    struct Person* ptr;
    ptr = &dad;

    std::cout << "Dad's age is " << ptr->age << " and name is " << ptr->name << "." << std::endl;

    //////
    int z, x=1, y= 3;
    z = addtwo<int>(x,y);
    std::cout << x << " plus " << y << " is " << z << std::endl;

    //////
    std::unordered_set<int> myset;
    recur_set(0,5,myset);

    return 0;

}

void recur_set(int level, int maxlevel, std::unordered_set<int> myset){

    if (level == maxlevel) {return;}

    myset.insert(level);
    std::cout << "Contents of set at level " << level << " before recursive call: ";
    for (auto elem: myset) {std::cout << " " << elem;}
    std::cout << std::endl;

    recur_set(level+1, maxlevel, myset);

    std::cout << "Contents of set at level " << level << " after recursive call: ";
    for (auto elem: myset) {std::cout << " " << elem;}
    std::cout << std::endl;

}
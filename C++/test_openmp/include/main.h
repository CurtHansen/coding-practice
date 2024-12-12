//
// Created by Curt Hansen on 2/22/23.
//

#ifndef TEST_OPENMP_MAIN_H
#define TEST_OPENMP_MAIN_H
#include <vector>

class MyClass {
public:
    MyClass();
private:
    int a;
    int b;
    int c;
};

int main(int, char**);
std::vector<MyClass*> do_something(int, const std::string&);

#endif //TEST_OPENMP_MAIN_H

#include <iostream>
#include <omp.h>

#include "main.h"
#include <unistd.h>
#include <fstream>
#include <sstream>
#include <iomanip>

int main(int argc, char** argv) {

    int idx, start_num=1, end_num=std::stoi(argv[1]);
    std::string directory = "/Users/curthansen/Documents/Coding/CodeExamples/temp";
    #pragma omp parallel for default(none) \
            shared(start_num, end_num,directory) \
	        private(idx)
    for (idx = start_num; idx <= end_num; idx++) {
        do_something(idx,directory);
    }
    return 0;
}

std::vector<MyClass*> do_something(int idx, const std::string& directory){

    std::vector<MyClass*> myvector;
    return myvector;

    /*
    int total = 0;
    for (int i=0;i<1000;i++){
        total = total + i;
    }
    std::ostringstream ss;
    ss << std::setw( 4 ) << std::setfill( '0' ) << idx;
    std::ofstream log;
    log.open(directory+"/iteration"+ss.str()+".log");
    log << "Contents from iteration "+std::to_string(idx)+": blah" << std::endl;
    log.close();
    */

}

MyClass::MyClass() {
    a = 1;
    b = 1;
    c = 1;
}

cmake_minimum_required(VERSION 3.26)
project(test_vector)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(test_vector
        test_vector.cpp)

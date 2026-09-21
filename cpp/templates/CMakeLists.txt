cmake_minimum_required(VERSION 3.17)
project(Test)

set(CMAKE_CXX_STANDARD 20)
include_directories(src)

add_executable(Test src/main.cpp src/template.hpp)

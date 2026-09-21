cmake_minimum_required(VERSION 3.26)
project(test_distributions)

set(CMAKE_CXX_STANDARD 17)
include_directories(/opt/homebrew/include)

add_executable(test_distributions main.cpp)

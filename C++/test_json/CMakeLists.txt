cmake_minimum_required(VERSION 3.26)
project(TestJSON)

set(CMAKE_CXX_STANDARD 17)
include_directories(/opt/homebrew/include)
add_executable(TestJSON test_json.cpp
        test_json.h
)

# Basics
cmake_minimum_required(VERSION 3.23)
set(PROJECT_NAME test_openmp)
project(${PROJECT_NAME} VERSION 1.0 DESCRIPTION "Test functionality of openmp on Mac.")
set(CMAKE_CXX_STANDARD 14)
set(TARGET_NAME ${PROJECT_NAME})

# Libraries.
find_package(Armadillo REQUIRED)
# find_package(Boost COMPONENTS timer REQUIRED)


# Set source files and directories.
set(SOURCE_FILES src/main.cpp)
include_directories(include  ${ARMADILLO_INCLUDE_DIRS})

# Compile and link.
add_executable(${TARGET_NAME} ${SOURCE_FILES})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fopenmp")
set_target_properties(${TARGET_NAME} PROPERTIES VERSION ${PROJECT_VERSION})
target_link_libraries(${TARGET_NAME} ${ARMADILLO_LIBRARIES} )

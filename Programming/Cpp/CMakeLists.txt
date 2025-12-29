cmake_minimum_required(VERSION 3.15)
project(CppReview VERSION 1.0.0)
set(CMAKE_CXX_STANDARD 20)

add_subdirectory(./Polymorphism)
add_subdirectory(./SmartPointers)

add_executable(main main.cpp)
target_link_libraries(main PUBLIC Polymorphism)
target_link_libraries(main PUBLIC SmartPointers)

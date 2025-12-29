cmake_minimum_required(VERSION 3.15)
project(Polymorphism VERSION 1.0.0)
set(CMAKE_CXX_STANDARD 20)

include_directories(.)
add_library(Polymorphism Polymorphism.cpp Base.cpp
        DerivedPublicLa.h
        DerivedPublicLb.h
        DerivedPublicLa.cpp
        DerivedPublicLb.cpp)
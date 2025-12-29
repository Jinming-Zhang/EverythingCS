cmake_minimum_required(VERSION 3.15)
project(SmartPointers)

add_library(SmartPointers SmartPointers.h SmartPointers.cpp
        UniquePointerDemo.h
        UniquePointerDemo.cpp
        SampleClass.cpp
        SampleClass.h)
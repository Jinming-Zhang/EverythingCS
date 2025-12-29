//
// Created by wolfy on 2/17/2025.
//
#include <memory>
#include "UniquePointerDemo.h"
#include "SampleClass.h"

void func(std::unique_ptr<SampleClass> ptr) {
}

void UniquePointerDemo::PassPtrAsFunctionParam() {

  std::unique_ptr<SampleClass> pt1{std::make_unique<SampleClass>()};
}

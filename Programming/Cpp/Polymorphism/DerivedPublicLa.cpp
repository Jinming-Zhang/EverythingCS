//
// Created by wolfy on 2/17/2025.
//

#include <iostream>
#include "DerivedPublicLa.h"

void DerivedPublicLa::BaseFun1Virtual() {
  std::cout << "DerivedLa BaseFun1Virtual called\n";
}

DerivedPublicLa::DerivedPublicLa() {
  std::cout << "DerivedPublicLa Constructor called\n";
}

DerivedPublicLa::~DerivedPublicLa() {
  std::cout << "DerivedPublicLa Destructor called\n";
}

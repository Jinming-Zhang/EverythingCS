//
// Created by wolfy on 2/17/2025.
//

#include <iostream>
#include "Base.h"

Base::Base() {
  std::cout << "Base Constructor called\n";
}

Base::~Base() {
  std::cout << "Base Destructor called\n";
}

void Base::BaseFun1Virtual() {
  std::cout << "BaseFun1Virtual called\n";
}

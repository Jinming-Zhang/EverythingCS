//
// Created by wolfy on 2/17/2025.
//

#include <iostream>
#include "Polymorphism.h"
#include "Base.h"
#include "DerivedPublicLa.h"
#include "DerivedPublicLb.h"

void Polymorphism::RunDemo() {
  std::cout << "Polymorphism\n";
  Base b1{};
  DerivedPublicLa dla{};
  dla.BaseFun1Virtual();

  DerivedPublicLb lb(1.0, 2);
//  DerivedPublicLb lb2{1.0, 2}; // compiler error
}

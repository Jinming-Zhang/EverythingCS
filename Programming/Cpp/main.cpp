//
// Created by wolfy on 2/17/2025.
//
#include "Polymorphism/Polymorphism.h"
#include "SmartPointers/SmartPointers.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <functional>
#include <unordered_map>

int main(int argc, char **argv) {
//  Polymorphism p{};
//  p.RunDemo();
//  SmartPointers sp{};
//  sp.RunDemo();
  std::vector<int> intlst{1, 2, 2, 3, 4, 1, 2, 6};
  std::for_each(intlst.begin(), intlst.end(),
                [](int e) { std::cout << e << ", "; });
  std::vector<int>::iterator miniPtr = std::min_element(intlst.begin(),
                                                        intlst.end());
  std::cout << "min number: " << *miniPtr << std::endl;
  std::reverse(intlst.begin(), intlst.end());
  std::for_each(intlst.begin(), intlst.end(),
                [](int e) { std::cout << e << ", "; });
  std::vector<int>::iterator findRes = std::find(intlst.begin(), intlst.end(),
                                                 3);
  if (findRes != intlst.end()) {
    std::cout << "Find result: " << *findRes << std::endl;
  } else {
    std::cout << "Element not found." << std::endl;
  }

  findRes = std::find(intlst.begin(), intlst.end(),
                      100);
  if (findRes != intlst.end()) {
    std::cout << "Find result: " << *findRes << std::endl;
  } else {
    std::cout << "Element not found." << std::endl;
  }

  findRes = std::find_if(intlst.begin(), intlst.end(),
                         [](int &e) {
                             if (e + 1 == 7) {
                               e++;
                               return true;
                             }
                             return false;
                         });
  if (findRes != intlst.end()) {
    std::cout << "Find result: " << *findRes << std::endl;
  } else {
    std::cout << "Element not found." << std::endl;
  }


  std::function<bool(int)> pred = [](int e) {
      if (e % 3 == 0) {
        return true;
      }
      return false;
  };

  findRes = std::find_if(intlst.begin(), intlst.end(), pred);
  if (findRes != intlst.end()) {
    std::cout << "Find result: " << *findRes << std::endl;
  } else {
    std::cout << "Element not found." << std::endl;
  }
  std::unordered_map<int, int> elemCount{};
  elemCount.insert(std::make_pair<int, int>(2, 1));

  return 0;
}

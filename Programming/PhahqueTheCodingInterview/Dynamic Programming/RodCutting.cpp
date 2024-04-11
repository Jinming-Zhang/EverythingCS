#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include "../utils/Timer.h"

std::map<int, int> rodPrices = {
    {1, 1},
    {2, 5},
    {3, 8},
    {4, 9},
    {5, 10},
    {6, 17},
    {7, 17},
    {8, 20},
    {9, 24},
    {10, 30},
    {11, 31},
    {12, 32},
    {13, 35},
    {14, 39},
    {15, 44},
    {16, 47},
    {17, 49},
    {18, 52},
    {19, 54},
    {20, 58},
    {21, 60},
    {22, 62},
    {23, 65},
    {24, 69},
    {25, 74},
    {26, 77},
    {27, 89},
    {28, 82},
    {29, 84},
    {30, 98},
    {31, 100},
    {32, 102},
    {33, 105},
    {34, 109},
    {35, 114},
    {36, 117},
    {37, 119},
    {38, 122},
    {39, 124},
    {40, 128},
};

/// @brief return the revenue of optimal cut of a rod of length n
/// @param p
/// @param n
/// @return
int CutRodSlow(std::map<int, int> &priceMap, int n)
{
  if (n == 0)
  {
    return 0;
  }
  if (n > priceMap.size())
  {
    return CutRodSlow(priceMap, priceMap.size()) + CutRodSlow(priceMap, n - priceMap.size());
  }

  int res{-1};
  for (int i{1}; i <= n; ++i)
  {
    int total{0};
    int rest = CutRodSlow(priceMap, n - i);
    total = priceMap[i] + rest;
    res = std::max(total, res);
  }
  return res;
}

int main(int argc, char const *argv[])
{
  Timer t;
  std::cout << rodPrices.size() << std::endl;
  std::cout << CutRodSlow(rodPrices, 40) << std::endl;
  std::cout << t.elapsed() << std::endl;
  return 0;
}

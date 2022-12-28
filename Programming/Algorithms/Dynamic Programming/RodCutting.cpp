#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>

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
};

/// @brief return the revenue of optimal cut of a rod of length n
/// @param p
/// @param n
/// @return
int CutRodSlow(std::map<int, int> priceMap, int n)
{
  if (n == 0)
  {
    return 0;
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
  std::cout << rodPrices.size() << std::endl;
  std::cout << CutRodSlow(rodPrices, 1) << std::endl;
  std::cout << CutRodSlow(rodPrices, 2) << std::endl;
  std::cout << CutRodSlow(rodPrices, 3) << std::endl;
  std::cout << CutRodSlow(rodPrices, 4) << std::endl;
  std::cout << CutRodSlow(rodPrices, 5) << std::endl;
  std::cout << CutRodSlow(rodPrices, 6) << std::endl;
  return 0;
}

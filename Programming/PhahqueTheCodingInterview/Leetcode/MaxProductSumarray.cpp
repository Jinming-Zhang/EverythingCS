#include <iostream>
#include <vector>

void printA(const std::vector<std::vector<int>> &A)
{
  int n{A.size()};
  for (int r{0}; r < n; ++r)
  {
    for (int c{0}; c < n; ++c)
    {
      auto v{A[r][c]};
      std::cout << A[r][c] << " ";
    }
    std::cout << std::endl;
  }
}

int maxProduct(std::vector<int> &nums)
{
  int n{(int)nums.size()};
  int max{nums[0]};

  for (int i{0}; i < n; ++i)
  {
    if (nums[i] > max)
    {
      max = nums[i];
    }
    std::vector<int> products(n);
    products[i] = nums[i];

    for (int j{i + 1}; j < n; ++j)
    {
      int prod{nums[j] * products[j - 1]};
      products[j] = prod;
      if (prod > max)
      {
        max = prod;
      }
    }
  }
  return max;
}

int maxProductOmg(std::vector<int> &nums)
{
  int n{nums.size()};
  int maxAtI{nums[0]};

  std::vector<std::vector<int>> A(n);
  for (int r{0}; r < n; ++r)
  {
    for (int c{0}; c < n; ++c)
    {
      A[r].push_back(-99999);
    }
  }
  printA(A);
  A[0][0] = nums[0];
  for (int i{0}; i < n; ++i)
  {
    for (int j{0}; j < i; ++j)
    {
      // maxAtI
    }
  }
  return n;
}

int main(int argc, char const *argv[])
{
  std::vector<int> t1{2, 3, -2, 4};
  std::vector<int> t2{-2, 0, -1};
  std::vector<int> t3{0, 2};
  std::cout << maxProduct(t1) << std::endl;
  std::cout << maxProduct(t2) << std::endl;
  std::cout << maxProduct(t3) << std::endl;
  return 0;
}

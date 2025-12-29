#include <iostream>
#include <vector>

std::vector<int> searchRange(std::vector<int> &nums, int target)
{
  std::vector<int> res{-1, -1};
  if (nums.size() == 0)
  {
    return res;
  }
  int left{0};
  int right{(int)nums.size()};
  int mid{left + (right - left) / 2};
  while (nums[mid] != target)
  {
    if (mid == left)
    {
      return res;
    }
    if (nums[mid] > target)
    {
      right = mid;
    }
    else
    {
      left = mid;
    }
    mid = left + (right - left) / 2;
  }
  left = mid;
  right = mid;
  while (left > 0 && nums[left - 1] == target)
  {
    --left;
  }
  while (right < (nums.size() - 1) && nums[right + 1] == target)
  {
    ++right;
  }
  res[0] = left;
  res[1] = right;
  return res;
}

void printV(std::vector<int> v)
{
  for (auto i : v)
  {
    std::cout << i << " ";
  }
  std::cout << std::endl;
}

int main(int argc, char const *argv[])
{
  std::vector<int> t1{5, 7, 7, 8, 8, 10};
  int tar1{8};
  std::vector<int> t2{5, 7, 7, 8, 8, 10};
  int tar2{6};
  std::vector<int> t3{5, 7, 7, 8, 8, 10};
  int tar3{0};

  printV(searchRange(t1, tar1));
  printV(searchRange(t2, tar2));
  printV(searchRange(t3, tar3));
  return 0;
}

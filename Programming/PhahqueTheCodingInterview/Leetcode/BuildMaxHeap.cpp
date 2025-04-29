#include <iostream>
#include <vector>

template <typename T>
std::vector<T> BuildMaxHeap(std::vector<T> &v, int rootInd = 0)
{
  int lastNoneLeafInd{std::floor(v.size() / 2.0)};
  for (int i{v.size()}; i >= lastNoneLeafInd && i >= rootInd; --i)
  {
    int parentIndex{std::floor(v.size() / 2.0)};
    int leftChildIndex{2 * parentIndex + 1};
    int rightChildIndex{2 * parentIndex + 2};

    if (parentIndex < rightChildIndex)
    {
      int tmp = v[parentIndex];
      v[parentIndex] = v[rightChildIndex];
      v[rightChildIndex] = tmp;
      // build heap on v[rightChildIndex]
    }

    else if (parentIndex < leftChildIndex)
    {
      int tmp = v[parentIndex];
      v[parentIndex] = v[leftChildIndex];
      v[leftChildIndex] = tmp;
      // build heap on v[leftChildIndex]
    }
  }
}

template <typename T>
void printVector(const std::vector<T> &v)
{
  for (auto i : v)
  {
    std::cout << i << " ";
  }
  std::cout << std::endl;
}

int main(int argc, char const *argv[])
{
  std::vector<int> t1{4, 1, 3, 2, 16, 9, 10, 14, 8, 7};

  return 0;
}

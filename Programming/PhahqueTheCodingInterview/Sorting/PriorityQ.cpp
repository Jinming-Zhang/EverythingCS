#include <iostream>
#include <vector>
#include <math.h>

template <typename T>
class MaxHeap
{
private:
  std::vector<T> heap{};
  // left child of i: 2i
  // right child of i: 2i+1
  // parent of i: floor(i/2)
  void MaxHeapify(int startIndex, int lastIndex)
  {
    startIndex << 2;
    int leftChild{startIndex + 1};
    int rightChild{startIndex + 2};
    int maxIndex{startIndex};
    if (leftChild <= lastIndex && heap[leftChild] > heap[maxIndex])
    {
      maxIndex = leftChild;
    }
    if (rightChild <= lastIndex && heap[rightChild] > heap[maxIndex])
    {
      maxIndex = rightChild;
    }

    if (maxIndex != startIndex)
    {
      std::swap(heap[startIndex], heap[maxIndex]);
      MaxHeapify(maxIndex, lastIndex);
    }
  }

  void BuildMaxHeap(int lastIndex)
  {
    int cap{static_cast<int>((lastIndex + 1) / 2)};
    for (int i{cap}; i >= 0; --i)
    {
      MaxHeapify(i, lastIndex);
    }
  }

public:
  MaxHeap() {}
  // operations
  void Insert(T obj)
  {
    heap.push_back(obj);
    BuildMaxHeap(heap.size() - 1);
  }
  void Pop()
  {
  }
  void HeapSort()
  {
    int index{static_cast<int>(heap.size() - 1)};
    while (index > 0)
    {
      std::swap(heap[0], heap[index]);
      --index;
      MaxHeapify(0, index);
    }
  }
  void Print()
  {
    for (T elmt : heap)
    {
      std::cout << elmt << ", ";
    }
    std::cout << std::endl;
  }
};

int main(int argc, char const *argv[])
{
  MaxHeap<int> q{};
  q.Insert(8);
  q.Insert(2);
  q.Insert(5);
  q.Insert(1);
  q.Insert(9);
  q.Insert(6);
  q.Insert(7);
  q.Insert(4);
  q.Insert(3);
  q.Print();
  q.HeapSort();
  q.Print();
  return 0;
}

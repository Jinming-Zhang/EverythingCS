#include <iostream>
#include <vector>
#include <math.h>

template <typename T>
class PriorityQ
{
private:
  std::vector<T> queue{};
  // left child of i: 2i
  // right child of i: 2i+1
  // parent of i: floor(i/2)
  void HeapifySingle(int index = 0)
  {
    int leftChild{2 * index};
    int rightChild{2 * index + 1};
    int minIndex{index};
    if (leftChild < queue.size() && queue[leftChild] < queue[minIndex])
    {
      minIndex = leftChild;
    }
    if (rightChild < queue.size() && queue[rightChild] < queue[minIndex])
    {
      minIndex = rightChild;
    }
    if (minIndex != index)
    {
      std::swap(queue[index], queue[minIndex]);
      HeapifySingle(minIndex);
    }
  }
  void HeapifyAll()
  {
    int cap{static_cast<int>(queue.size() / 2)};
    for (int i{cap}; i >= 0; --i)
    {
      HeapifySingle(i);
    }
  }

public:
  PriorityQ() {}
  // operations
  void Push(T obj)
  {
    queue.push_back(obj);
    HeapifyAll();
  }
  void Pop()
  {
  }
  void Print()
  {
    for (T elmt : queue)
    {
      std::cout << elmt << ", ";
    }
    std::cout << std::endl;
  }
};

int main(int argc, char const *argv[])
{
  PriorityQ<int> q{};
  q.Push(8);
  q.Push(2);
  q.Push(5);
  q.Push(1);
  q.Push(9);
  q.Push(6);
  q.Push(7);
  q.Push(4);
  q.Push(3);
  q.Print();
  return 0;
}

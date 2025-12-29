#include <iostream>
#include <vector>
using namespace std;

vector<int> heapify(vector<int> arr)
{
  for (int i{0}; i < arr.size() / 2; ++i)
  {
    int root{arr[i]};
    if (2 * i < arr.size())
    {
      if (root < arr[2 * i])
      {
        arr[i] = arr[2 * i];
        arr[2 * i] = root;
      }
    }

    if (2 * i + 1 < arr.size())
    {
    }
  }
}

void printV(const vector<int> &arr)
{
  for (int i{0}; i < arr.size(); ++i)
  {
    cout << i << " ";
  }
  cout << endl;
}

int main(int argc, char const *argv[])
{
  vector<int> input{5, 2, 1, 7, 6, 3, 4};
  return 0;
}

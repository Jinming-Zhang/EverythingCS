#include <iostream>
#include <vector>
#include <queue>
#include <math.h>

using namespace std;

int minCostConnectPoints(vector<vector<int>> &points)
{
  if (points.size() == 0)
  {
    return 0;
  }

  int totalCost{0};
  vector<int> keys(points.size(), 99999999);
  vector<bool> included(points.size(), false);
  int setCount{0};

  keys[0] = 0;
  while (setCount != points.size())
  {
    // find vertex with minimum key value
    int tarIndex{0};
    int curMin{99999999};
    for (int i{0}; i < keys.size(); ++i)
    {
      if (!included[i] && keys[i] < curMin)
      {
        curMin = keys[i];
        tarIndex = i;
      }
    }

    totalCost += curMin;
    included[tarIndex] = true;
    ++setCount;

    // check all neighbours
    vector<int> p1{points[tarIndex]};
    for (int i{0}; i < points.size(); ++i)
    {
      if (i != tarIndex)
      {
        vector<int> p2{points[i]};
        int dst{abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])};
        if (dst < keys[i])
        {
          keys[i] = dst;
        }
      }
    }
  }
  return totalCost;
}

int main(int argc, char const *argv[])
{
  vector<vector<int>> t1{{0, 0}, {2, 2}, {3, 10}, {5, 2}, {7, 0}};

  vector<vector<int>> t2{
      {3, 12}, {-2, 5}, {-4, 1}};

  cout << minCostConnectPoints(t1) << endl;
  cout << minCostConnectPoints(t2) << endl;
  return 0;
}

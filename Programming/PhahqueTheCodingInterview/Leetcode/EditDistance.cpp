#include <iostream>
#include <vector>
using namespace std;

double minDistance(string word1, string word2)
{
  double replaceCost{1.5};
  double insertCost{1};
  double deleteCost{0.5};

  int colNo = word1.size() + 1;
  int rowNo = word2.size() + 1;
  double *dpTable = new double[rowNo * colNo];

  // initialize base cases
  for (int col{0}; col < colNo; ++col)
  {
    dpTable[col] = col;
  }
  for (int row{0}; row < rowNo; ++row)
  {
    int rowIndex = row * colNo;
    dpTable[rowIndex] = row;
  }

  // build dp table
  for (int row{1}; row < rowNo; ++row)
  {
    for (int col{1}; col < colNo; ++col)
    {
      int index = col + row * colNo;
      int topIndex = col + (row - 1) * colNo;
      int leftIndex = (col - 1) + (row)*colNo;
      int topLeftIndex = (col - 1) + (row - 1) * colNo;
      // case: same letter
      if (word1[col - 1] == word2[row - 1])
      {
        dpTable[index] = dpTable[topLeftIndex];
      }
      // case: different letter
      else
      {
        // insertion cost
        double iCost = insertCost + dpTable[topIndex];
        // deletion cost
        double dCost = deleteCost + dpTable[leftIndex];
        // replace cost
        double rCost = replaceCost + dpTable[topLeftIndex];
        double minCost = min(min(iCost, dCost), rCost);
        dpTable[index] = minCost;
      }
    }
  }
  return dpTable[rowNo * colNo - 1];

  delete[] dpTable;
}

int main(int argc, char const *argv[])
{
  string word1 = "DENVER";
  string word2 = "NERVED";
  cout << minDistance(word1, word2) << endl;
  word1 = "intention";
  word2 = "execution";
  cout << minDistance(word1, word2) << endl;
  return 0;
}

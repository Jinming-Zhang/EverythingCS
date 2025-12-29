#include <iostream>

bool isValidInput(char *input, int size);

int main(int argc, char **argv)
{
  using std::cin;
  using std::cout;
  using std::endl;

  cout << "Enter a valid code, or \"all\" to guess all combinations." << endl;

  char code[4]{};
  cin.getline(code, std::size(code));
  return 0;
}

bool isValidInput(char *input, int size)
{
  char validChars[6]{'A', 'B', 'C', 'D', 'E', 'F'};
  if (size == 3)
  {
    return input == "all";
  }
  if (size == 4)
  {
    for (int i{0}; i < size; ++i)
    {
      for (int j{0}; j < size; ++j)
      {
        if (i != j && input[i] == input[j])
        {
          return false;
        }
      }
    }
  }
}

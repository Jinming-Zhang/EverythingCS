#include <iostream>

int commonStringLength(std::string text1, std::string text2)
{
  if (text1.size() <= 0 || text2.size() <= 0)
  {
    return 0;
  }

  if (text1.size() == 1 && text2.size() == 1)
  {
    if (text1[0] == text2[0])
    {
      return 1;
    }
    else
    {
      return 0;
    }
  }

  if (text1[0] == text2[0])
  {
    return 1 + commonStringLength(text1.substr(1), text2.substr(1));
  }
  int first = commonStringLength(text1, text2.substr(1));
  int second = commonStringLength(text1.substr(1), text2);
  int third = commonStringLength(text1.substr(1), text2.substr(1));
  return std::max(std::max(first, second), third);
}

int commonStringLengthNoRecur(std::string text1, std::string text2)
{
  int text1Ind{0};
  int text2Ind{0};
  while (text1Ind < text1.size() && text2Ind < text2.size())
  {
  }
  if (text1[0] == text2[0])
  {
    return 1 + commonStringLength(text1.substr(1), text2.substr(1));
  }
  int first = commonStringLength(text1, text2.substr(1));
  int second = commonStringLength(text1.substr(1), text2);
  int third = commonStringLength(text1.substr(1), text2.substr(1));
  return std::max(std::max(first, second), third);
}

int main(int argc, char const *argv[])
{
  std::string text1{"abcdefg"};
  std::string text2{"bdegkill"};
  std::cout << text1.substr(2, 3) << std::endl;
  int res{commonStringLength(text1, text2)};
  std::cout << "f";
  // std::cout << std::to_string(res) << std::endl;

  return 0;
}

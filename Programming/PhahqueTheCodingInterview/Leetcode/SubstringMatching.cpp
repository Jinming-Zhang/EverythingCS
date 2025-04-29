#include <iostream>
#include <vector>
#include <set>

std::vector<std::string> stringMatching(std::vector<std::string> &words)
{
  std::set<std::string> res{};
  for (size_t i{0}; i < words.size(); ++i)
  {
    for (size_t j{0}; j < words.size(); ++j)
    {
      if (i != j && words[j].find(words[i]) != std::string::npos)
      {
        res.insert(words[i]);
      }
    }
  }
  return std::vector<std::string>(res.begin(), res.end());
}

int main(int argc, char const *argv[])
{
  std::vector<std::string> t1{"mass", "as", "hero", "superhero"};
  std::vector<std::string> t2{"leetcode", "et", "code"};

  auto r1{stringMatching(t1)};
  std::cout << "Result 1\n";
  for (auto s : r1)
  {
    std::cout << s << " ";
  }
  std::cout << std::endl;

  auto r2{stringMatching(t2)};
  std::cout << "Result 2\n";
  for (auto s : r2)
  {
    std::cout << s << " ";
  }
  std::cout << std::endl;

  return 0;
}

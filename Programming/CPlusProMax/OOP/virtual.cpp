#include <iostream>
class Base
{
public:
  virtual int add(int a, int b)
  {
    return a + b;
  }
};

class Derived : public Base
{
public:
  virtual int add(int a, int b) override
  {
    return a - b;
  }
  void print()
  {
    std::cout << "Derived print\n";
  }
};

int main(int argc, char const *argv[])
{
  Derived d{};
  Base *baseRef{&d};
  Base baseCopy{d};

  Base *basePtr = new Derived();

  std::cout << "Base reference add: " << baseRef->add(1, 4) << "\n";
  std::cout << "Base copy add: " << baseCopy.add(1, 4) << "\n";
  std::cout << "Derived add: " << d.add(1, 4) << "\n";
  std::cout << "Base pointer add: " << basePtr->add(1, 4) << "\n";
  std::cout << "Downcast base pointer to derived pointer: ";
  dynamic_cast<Derived *>(basePtr)->print();

  return 0;
}

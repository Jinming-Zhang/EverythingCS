# Class Templates
Class means `Struct`, `Class`, `Union`, and `Array`.

Similar with [[Template Functions]], class templates solves the situation where the same data structure is needed for multiple different types.

# Define a class template
Begin with `template parameter declaration`, then define the class as normal except use template parameters defined before in place of where a real type that is needed later.

```cpp
template <typename T>
struct Pair
{
    T first{};
    T second{};
};

int main()
{
    Pair<int> p1{ 5, 6 };        // instantiates Pair<int> and creates object p1
    std::cout << p1.first << ' ' << p1.second << '\n';

    Pair<double> p2{ 1.2, 3.4 }; // instantiates Pair<double> and creates object p2
    std::cout << p2.first << ' ' << p2.second << '\n';

    Pair<double> p3{ 7.8, 9.0 }; // creates object p3 using prior definition for Pair<double>
    std::cout << p3.first << ' ' << p3.second << '\n';

    return 0;
}
```

# Template Instantiation
When a class template is encountered, the compiler will instantiate the class with the provided type parameter if it hasn't been instantiated before.

# Using class templates in multiple files
Same as [[Template Functions]], class templates are exempt from one-definition rule, so they can be defined in header files and be distributed to different cpp files without issue.
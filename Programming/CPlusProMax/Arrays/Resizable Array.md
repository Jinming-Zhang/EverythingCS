## std::array
A fix-sized array that won't decay to pointer when passed into a function as parameter.
```cpp
std::array<int, 5> myArray;
myArray = { 0, 1, 2, 3, 4 }; // okay
myArray = { 9, 8, 7 }; // okay, elements 3 and 4 are set to zero!
myArray = { 0, 1, 2, 3, 4, 5 }; // not allowed, too many elements in initializer list!
// does boundary checking
myArray.at(1);
// No boundary checking
myArray[2];
// return 5
myArray.size();
```

> 	Always pass `std::array` by reference or `const` reference

Since each different type and length of the array is considered a different type, we can use template functions for array operations.
```cpp
template <typename T, std::size_t size> // parameterize the element type and size
void printArray(const std::array<T, size>& myArray)
{
    for (auto element : myArray)
        std::cout << element << ' ';
    std::cout << '\n';
}
```

## std::vector
A c++ implementation of dynamically allocated array.
Similar as `std::array`, but has  `resize()` and additional functions to adjust the size of the array.

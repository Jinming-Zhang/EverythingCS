# sizeof
`sizeof()` operator returns the total size in **bytes** that the given array takes.
```cpp
int array[]{ 1, 1, 2, 3, 5, 8, 13, 21 };
    std::cout << sizeof(array) << '\n'; // will print the size of the array multiplied by the size of an int
```
# std::size()
`std::size()` from `<iterator>` returns the number of elements in the given array.
> It doesn't work with fixed sized array passed inside a function.
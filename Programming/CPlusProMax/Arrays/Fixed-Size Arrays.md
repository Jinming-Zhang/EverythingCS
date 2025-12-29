
# Fixed Array
Array of fixed length, the length of the array in initialization must be a **compile-time** constant.

Valid:
```cpp
// using a literal constant
int numberOfLessonsPerDay[7]{}; // Ok

// using a constexpr symbolic constant
constexpr int daysPerWeek{ 7 };
int numberOfLessonsPerDay[daysPerWeek]{}; // Ok
```

Not valid:
```cpp
const int daysPerWeek{ temp }; // the value of daysPerWeek isn't known until runtime, so this is a runtime constant, not a compile-time constant!
int numberOfLessonsPerDay[daysPerWeek]{}; // Not ok
```

### Fixed Array Initialization
use  initializer list to initialize a fixed array:
```cpp
int prime[5]{ 2, 3, 5, 7, 11 }; // use initializer list to initialize the fixed array
```
If there are few initializers in the array than the size, the remaining elements will be **zero-initialized**, for non-integral fundamental type will be whatever the value 0 converted to.

## Array Size Vs sizeof
Fixed array object can use `std::size` function to get the size of the array (number of elements).
**different from** `sizeof` operator, `sizeof` will return the total size in bytes, that the object occupies.
In the case of array, it will return elementsCount \* sizeOfEachElement bytes.

# Multidimensional Fixed Array
Same as one dimensional fixed array:
To declare and initialize with given size:
```cpp
int data[10][5]{}; // 0 initialized with 10 rows and 5 cols
int array[3][5]
{
  { 1, 2, 3, 4, 5 }, // row 0
  { 6, 7, 8, 9, 10 }, // row 1
  { 11, 12, 13, 14, 15 } // row 2
};
```

```cpp
int lotsData[10][8][5][2]{}; // each additional dimension can be think of as additional feature that adds on to the previous dimension
```

## Type of fixed array
When passing fixed array as function parameter, it's type will decay to a pointer that points to the first element in the array.
This will lose some information that was available as an array, such as size.

This is the same when declaring function parameter as fixed array type, the parameter will decay to the pointer type.
```cpp
void printSize(int array[])
{
    std::cout << sizeof(array) / sizeof(array[0]) << '\n';
}

int main()
{
    int array[]{ 1, 1, 2, 3, 5, 8, 13, 21 };
    std::cout << sizeof(array) / sizeof(array[0]) << '\n';
    printSize(array);

    return 0;
}
```

Fixed array has a type `int (*)[5]*` for example, 
note it's different from `int *`, which it decays to sometimes, that's when some of their array functionality gets lost.


## Fixed Array in Class/Structs
When passing class/struct instance to functions, if that class has fixed array fields, those will not be decayed to pointer.
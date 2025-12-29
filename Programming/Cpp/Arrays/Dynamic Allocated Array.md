### new and delete for single variable
using `new` keyword to allocating memory for single variable on the heap, if the operation is successful, it will return the address of the newly allocated memory, and a `nullptr` otherwise.
```cpp
int *value {new (std::nothrow) int};
if(!value)
{
	std::cerr<<"cannot allocate memory\n";
}
```
using `delete` keyword to deallocating memory pointed by the pointer.
```cpp
delete value;
```

### new and delete for array
Use the array form of `new` and `delete` to dynamically allocate array of variables
```cpp
int length = 5;
int *array {new int[length]{}};
delete[] array;
```
One often asked question of array delete[] is, “How does array delete know how much memory to delete?” The answer is that array new[] keeps track of how much memory was allocated to a variable, so that array delete[] can delete the proper amount. Unfortunately, this size/length isn’t accessible to the programmer.
##### Initializing dynamic allocated array
```cpp
int *array{new int[5]{1,2,3,4,5}};
delete[] array;
```
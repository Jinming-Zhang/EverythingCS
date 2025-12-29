CStyle string are essentially char[], sequence of fix-sized char, with a null-terminator at the end.
## Fixed Array
A fixed array that has it's own memory location for each character, and assign the value to "wolf\0"it's local-scoped, which means the object will be destroyed when out of scope.

```cpp
char myName[]{"wolf"};
```
When checking the size of fixed array string, there will be 1 more count for the null terminator at the end.

```cpp
std::cout << std::size(myName); // 5
```
 ##### Cannot be reassigned after declared
 Since it's an array type variable, we cannot assign it to a different string after it's declared.
However, we can manipulate it just like a normal array.
```cpp
char myString[]{ "string" }; // ok
myString[0] = 'l'; // ok
myString = "rope"; // not ok!
```

##### Build-in functions for cstyle string
- strcp
- strncp
- strcat
- strncp
- strlen
Note that all of these relies on the null terminator, also can overwrite the null terminator and cause future problems.

## Symbolic constants
The string is created at the heap, and the life-time is same as the program. (static duration)
This way the compiler will place the value of the string into a read-only memory, and a pointer is created to points to that location.

```cpp
char *myName{"wolf"};
```

## cout with cstyle string
When the `cout` function sees a char* type, it will implicitly try to print a string.
This will cause unexpected behaviour when we pass it a char* but it's not intended as a string.
```cpp
#include <iostream>

int main()
{
    char c{ 'Q' };
	// keep printing until a null-terminator is reached
    std::cout << &c; //Q╠╠╠╠╜╡4;¿■A

    return 0;
}
```

## cin with cstyle string
A save method to store input into a char array:
```cpp
char name[256];
cin.getline(name, std::size(name));
```
This prevents the case where user's input is too long and may overflow the array. (overwrite the null terminator)
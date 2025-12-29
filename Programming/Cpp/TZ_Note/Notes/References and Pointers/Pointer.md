# Address-of Operator
`&` can be used as an unary operator to get the address of a variable.
`&` returns a `pointer` object
```cpp
int x{2};
std::cout<< &x ;
```
# Defeference Operator
`*` can be used as an unary operator to dereference an address and get the value of that address.
`*` returns a lvalue type.

```cpp
int x{3};
std::cout<< *(&x) ;
```

# Pointer
`Pointer` (to type x) is an **object** that stores a pointer (memory address) of an type.
```cpp
double d {3.5};
double* dPtr {&d};
```

To create a `null pointer`, use zero-initialization or `nullptr` literal.
`nullptr` is of type `nullptr_t` from `<cstddef>`
```cpp
int* nPtr{};
double* nPtr2(nullptr)
```

# Pointer and Const
- A non-const pointer to a non-const value. We can dereference it to update the value or change the pointer to point other addresses
	 ```cpp
	int x{1};
	int* iPtr{&x};
	 ```
- A non-const pointer to a const value, we can NOT dereference it to update the value, but we can change the pointer to point other addresses
	 ```cpp
	const int x{1};
	const int* iPtr{&x};
	 ```
- A const pointer to a non-const value, we can dereference it to update the value, but we can NOT change the pointer to point other addresses
	 ```cpp
	int x{1};
	int* const iPtr{&x};
	 ```
- A const pointer to a const value, we can NOT dereference it to update the value, and we can NOT change the pointer to point other addresses
	 ```cpp
	const int x{1};
	const int* const iPtr{&x};
	 ```
# Implicit Conversion to Bool
Pointers can be implicitly converted to `bool` where 
- `nullptr`  -> false
- others -> true

# Legacy Null Pointer Initialization
- 0
	```cpp
	int* ptr {0};
	```
- NULL from `<cstddef>`
	```cpp
	int* ptr{NULL};
	```

This can lead to ambiguous function overload sometimes:
```cpp
#include <iostream>
#include <cstddef> // for NULL

void print(int x) // this function accepts an integer
{
	std::cout << "print(int): " << x << '\n';
}

void print(int* ptr) // this function accepts an integer pointer
{
	std::cout << "print(int*): " << (ptr ? "non-null\n" : "null\n");
}

int main()
{
	int x{ 5 };
	int* ptr{ &x };

	print(ptr); // always calls print(int*) because ptr has type int* (good)
	print(0); // always calls print(int) because 0 is an integer literal (may or may not be what we expect)
	print(NULL); // most likely calls print(int), but could call print(int*) depending on how NULL is defined (definitely not what we want)
	print(nullptr); // always calls print(int*) because nullptr only converts to a pointer type (good)

	return 0;
}
```

inline in cpp means multiple definitions are allowed.
# Inline Function
```cpp
int max(int a, int b){
	return (a > b) ? a : b;
}
```

The `inline` keyword before a function hints the compiler that the function can be inline expanded.
However, the compiler decides if the function will be inline  expanded or not, it's not guarenteed.
>Avoid using `inline` function in general because usually compiler will have better intuition on if the function should be inline.

Not that the meaning of `inline` has been extended to multiple definition are allowed. So one use of it is to define inline function in header files.
```cpp
// some .h file
inline int foo()
{
	std::cout<<"foo";
}
```
So that when the header file is included in multiple other files, they can use the function as defined.
With out `inline` keyword, it will cause linking error because multiple definitions of the function are found.


# Inline Variable
A variable identifier has multiple definitions across different files, the linker will consolidate all inline definitions of that variable into a single variable definition in a .cpp file somewhere, and all the definitions will refer to that consolidated definition.
### Restrictions
- All definitions of the inline variable must be identical, or undefined behaviour will occur.
- The inline variable **definition** (not forward declaration) must be present in any file that uses the variable.
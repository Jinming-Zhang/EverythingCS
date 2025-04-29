# Struct

```cpp
struct Fraction
{
	int numerator {}; // data member
	int denominator {}; // data member
}; // end the definition with ;'''
```
Variables that are part of the struct are called `data members` or `member variables`.
`data members` will not be initialized if no initializer if provided.

# Member Selection Operator
Member selection operator `.` is used to access a specific `member variable`. 

# Struct Initialization
Struct with only data members are considered [[Aggregate Data Types|aggregate]],  so we can use aggregate initialization.

```cpp
struct Something
{
    int x;       // no default initialization value (bad)
    int y {};    // value-initialized by default
    int z { 2 }; // explicit default value
};

int main()
{
    Something s1;             // No initializer list: s1.x is uninitialized, s1.y and s1.z use defaults
    Something s2 { 5, 6, 7 }; // Explicit initializers: s2.x, s2.y, and s2.z use explicit values (no default values are used)
    Something s3 {};          // Missing initializers: s3.x is value initialized, s3.y and s3.z use defaults

    return 0;
}
```

### Designated Initializer (C++20)
Explicitly define which initialization values is mapped to which data member.
```cpp
struct Foo
{
    int a{ };
    int b{ };
    int c{ };
};

int main()
{
    Foo f1{ .a{ 1 }, .c{ 3 } }; // ok: f.a = 1, f.b = 0 (value initialized), f.c = 3
    Foo f2{ .b{ 2 }, .a{ 1 } }; // error: initialization order does not match order of declaration in struct

    return 0;
}
```

> Missing initialises in the list will be `zero-initialized`.

> When adding new members to a struct, try add it to the last so other initialization code will not accidentally initialize with wrong values.

> Aggregate Initialization can also be used in struct assignments.

# Passing Struct as parameters
By default, `struct` is passed by value, but usually we can pass by `const reference` to avoid unnecessary copy.
```cpp
void printEmployee(const Employee& employee)  { }
```
# Returning structs
A temporary variable will be created and it's value will be copied to the function caller, then it will be destroyed.
```cpp
Point3d getZeroPoint()
{
    return Point3d { 0.0, 0.0, 0.0 }; // return an unnamed Point3d
}
```
If the return type of the function is explicitly defined (not using `auto`), then we can return a aggregate initializer as the struct value.
```cpp
Point3d getZeroPoint()
{
    // We already specified the type at the function declaration
    // so we don't need to do so here again
    return { 0.0, 0.0, 0.0 }; // return an unnamed Point3d
	// or zero-initializer
	// return {};
}
```

# Size of structs
Size of the struct is **at least** the sum of the size of all its members.
Compiler will **padding** gaps into structures for optimization purposes. [ref](https://en.wikipedia.org/wiki/Data_structure_alignment)

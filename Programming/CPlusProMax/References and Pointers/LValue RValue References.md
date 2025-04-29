# References are NOT Objects
If possible, the compiler will optimize references away by replacing all occurrences of a reference with the referent. However, this isn’t always possible, and in such cases, references may require storage.
# LValue References Type
By appending ampersand `&` after a type, we declare a lvalue reference of that type.
> LValue references must be initialized upon declaration.
```cpp
int x {5};
int& ref {x};
```
> References can’t be reseated (changed to refer to another object)
When a reference is evaluated in an expression, it resolves to the object it’s referencing.

### Const LValue References
- `const lvalue references` can be initialized with `lvalue`, `const lvalue` and `rvalue` types.
- `const lvalue references` can only be accessed but not modified.
- `rvalue` that used to initialize `const lvalue reference` will have an extended life time to match the `const lvalue reference`

# R-value reference
A reference that is designed to be initialized with an r-value only.
An r-value reference is created using double ampersand.
```cpp
int x{ 5 };
int &lref{ x }; // l-value reference initialized with l-value x
int &&rref{ 5 }; // r-value reference initialized with r-value 5
```
> note that the variable `rref` itself is a l-value
1. r-value references extend the lifespan of the object they are initialized with to the lifespan of the r-value reference
2. non-const r-value references allow us to modify the r-value

### Taking address of rvalue reference

# Dangling references
When an object being referenced is destroyed before a reference to it, the reference is left referencing an object that no longer exists. Such a reference is called a dangling reference. Accessing a dangling reference leads to undefined behavior.



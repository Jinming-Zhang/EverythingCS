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

# R-value references
r-value reference is designed to be initialized with a r-value only.
```cpp
int&& rref{5};
```
#### Properties of r-value references
1. r-value references extends the lifespan of the object they initialized with to the lifespan of the r-value reference (same as `const l-value reference`).
2. non-const r-value reference can be modified.
# Dangling references
When an object being referenced is destroyed before a reference to it, the reference is left referencing an object that no longer exists. Such a reference is called a dangling reference. Accessing a dangling reference leads to undefined behavior.
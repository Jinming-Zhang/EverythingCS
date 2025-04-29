>Forward declarations are usually organized in header files.
# Function Forward Declaration
To access function defined in some other file.
```cpp
void foo(int x);
```

# Non-const Global Variable Forward Declaration
To access global variable defined in some other file.
```cpp
extern int g_x;
```

# Const Global Variable Forward Declaration
To access const global variable defined in some other file.
```cpp
extern const int g_x;
```

# Note
- `constexpr` variables can not have external linkage because:
	- They cannot be forward declared, because for `constexpr` we have to initialize it with a literal upon declaration.
	- Also the compiler needs to know the value of the `constexpr` variable at compile time, and compilers don't have visibility to look for definitions in other files (it's linker's job).
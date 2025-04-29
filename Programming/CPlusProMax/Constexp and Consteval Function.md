# Const member function
const member function indicates that the member function won't modify any of the member variables, and only member functions with *const* signature can be called on const objects.
```cpp
class Base
{
public:
    int getValue() const  { return m_value; }
};
```
# Constexp and Consteval Function
## Constexp Function
Recall that `constexp` is used to create compile-time constant variables.

> `constexp` functions are functions whose return value *may* be computed at compile time.
> It's guaranteed to compute at compile-time only when the return value is used as `constexp`.

Example:

```cpp
constexpr int greater(int x, int y)
{
    return (x > y ? x : y);
}

int main()
{
	// case 1: evaluated at compile-time
    constexpr int g { greater(5, 6) };            
    std::cout << g << "is greater!";

    int x{ 5 }; // not constexpr
	// case 2: evaluated at runtime
    std::cout << greater(x, 6) << " is greater!";
	
	// case 3: may be evaluated at either runtime or compile-time
    std::cout << greater(5, 6) << " is greater!"; 

    return 0;
}
```

## Consteval function
`consteval` function are functions that must be evaluated at compile-time.
Functions that marked as `consteval` but cannot be evaluated at compile-time will cause compiler error.

```cpp
#include <iostream>

consteval int greater(int x, int y) // function is now consteval
{
    return (x > y ? x : y);
}

int main()
{
	// ok: will evaluate at compile-time
    constexpr int g { greater(5, 6) };
	// ok: will evaluate at compile-time
    std::cout << greater(5, 6) << " is greater!";
	// not constexpr
    int x{ 5 };
	// error: consteval functions must evaluate at compile-time
    std::cout << greater(x, 6) << " is greater!";
    return 0;
}
```

### Note
To make `constexpr` function evaluated at compile-time whenever possible.
When **greater** is executed at compile time, we force its return value is used as constexpr, so **greater** function will return the value as constexpr, and thus it's guaranteed to be evaluated at compile-time.
```cpp
#include <iostream>

// just return the parameter as constexpr value
consteval auto compileTime(auto value)
{
    return value;
}
// function is constexpr
constexpr int greater(int x, int y)
{
    return (x > y ? x : y);
}

int main()
{
	// may or may not execute at compile-time, because the return value is not used as constexpr
    std::cout << greater(5, 6); 
	// will execute at compile-time
    std::cout << compileTime(greater(5, 6));

	// we can still call the constexpr version at runtime if we wish
    int x { 5 };
    std::cout << greater(x, 6);
    return 0;
}
```
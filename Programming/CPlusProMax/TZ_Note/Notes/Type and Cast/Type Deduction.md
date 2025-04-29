[auto]()
[auto with reference/pointer](https://www.learncpp.com/cpp-tutorial/type-deduction-with-pointers-references-and-const/)

# auto
`auto` keyword can be used in places where a type is expected, the compiler will deduce it to the most approperiate type based on the initializer
```cpp
#include <string>
const double foo()
{
    return 5.6;
}
std::string& getRef();
const std::string& getConstRef();
int main()
{
    const double cd{ 7.8 };

    auto x{ cd };    // double (const dropped)
    auto y{ foo() }; // double (const dropped)
	auto z{getRef()}; // string (ref dropped)
	
	
	const auto cx{cd};	// const double
	auto& zr{getRef()}; // string&
	
	auto& zcr{getConstRef()}; // const string&, low level const is not dropped
    return 0;
}
```
# characteristics
- drop top level `const`
- drop `reference`
- Do Not drop `pointer`

# Top Level Const
`const` is applied to the object itself.
```cpp
const int x;    // this const applies to x, so it is top-level
int* const ptr; // this const applies to ptr, so it is top-level
```
# Low Level Const
For references and pointers, low level const means the const is applied to the object that is being referenced/pointed by the reference/pointer.
```cpp
const int& ref; // this const applies to the object being referenced, so it is low-level
const int* ptr; // this const applies to the object being pointed to, so it is low-level
```
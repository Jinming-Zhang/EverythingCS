# Namespace
Anything declared in `unnamed namespace` or `inline namespace` are considered part of the parent namespace.
## Unnamed/Anonymous Namespace
```cpp
namespace {
	void foo(){}
}
```
All content in an unnamed namespace have [[Identifier Linkage#Note|static]] (file) scope ([[Identifier Linkage#Internal Linkage|internal linkage]]) , and can only be accessed within the same file, including user-defined types.

## Inline Namespace
Inline namespace is used to version content and for backward capability.
Functions in `inline namespace` will be called by default, while functions in other namespace needs to be called with an explicit scope resolution.
```cpp
#include <iostream>

inline namespace v1 // declare an inline namespace named v1
{
    void doSomething()
    {
        std::cout << "v1\n";
    }
}

namespace v2 // declare a normal namespace named v2
{
    void doSomething()
    {
        std::cout << "v2\n";
    }
}
int main()
{
	// v1 will be called by default
    doSomething(); // calls the inline version of doSomething() (which is v1)
    v1::doSomething(); // calls the v1 version of doSomething()
    v2::doSomething(); // calls the v2 version of doSomething()


    return 0;
}
```
# Scope resolution operator

[[Operators and bit manipulation#scope resolution operator | See Scope Resolution Operator]]

# Variable scope and variable shadowing
### Local Variable / automatic variable:
- Variables defined inside a block.
- They have `block scope`
- They are created at the point of definition and destryoed at the end of its block.
- Local variable does not have [[Namespaces and scope#Linkage|linkage]]
### Global variable
- Variables declared outside of a function or block
- They can be accessed from the entire file.
- They have flie scope and static duration (**destroyed when program ends**)
## Variable shadowing
Variable showdowing happens when a local scope variable has the same name as a outer scope variable.
In such cases, references of the name in the block where the local scop variable is defined will be referencing the local variable, and the outter scope variable will not be changed.
There is no way to directly access the shadowed varible in outer block.


# Using Declaration Vs Using Directive
`using declaration`  introduces new meanings of an identifier into current scope.
```cpp
using std::cout;
```
`using directive` introduces all identifiers inside the namespace into the **the lowest common ancestor of the current scope and the target namespace’s own scope** 
> Avoid `using directive` at all time!	
## Qualified and Unqualified Names
>A qualified name is a name that with associated scope.

Examples:
- std::cout
- ::foo
- classA::method1

>A unqualified name is a name that does not include scope qualifier.

Examples:
- cout
- boo()

## Using Declaration
We need a separate `using declaration` for each name.
```cpp
using std::cout;
cout<<"something";
```

## Using Directive
`using directive` imports all identifiers inside a namespace into the ["lowest common ancestor"](https://quuxplusone.github.io/blog/2020/12/21/using-directive/) of the target namespace and the scope that used the `using directive`.

```cpp
namespace NA {
    int foo(Zoo::Lion);
}
namespace NB {
    int foo(Zoo::Lion);
    namespace NC {
        namespace N1 {
            int foo(Zoo::Cat);
        }
        namespace N2 {
            int test() {
				// identifiers in N1 is introduced to NC
                using namespace N1;
				// identifiers in NA is introduced to global namespace, which got hidden by N1.
                using namespace NA;
                return foo(Zoo::Lion());
            }
        }
    }
}
```

## Summary
Prefer `using declaration` over `using directive` because `using directive` increases the chances for name collision and may alter code behaviour when the code in the namespace updated.
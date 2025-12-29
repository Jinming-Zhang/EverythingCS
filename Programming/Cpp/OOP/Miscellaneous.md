- `struct` and `class` are identical other than that member variables and functions in struct are default to public, where as in class it's default to private.
- when calling member functions of a class instance, the instance itself is implicitly passed into the function as a parameter.
- Access control works on per-class basis, which means when passing the same class type as parameter to the member function, the member function has access to private members of that parameter.
- It's good practice to return a **const reference** for getters to prevent the caller modifying the member variable.

## Constructors
The member variables of `class` type will have their default constructors called even before the container class's constructor being called.
For example, if class A has a member of type class B, then when we creating class A, class B's default constructor will be called before class A's constructor being called.

Constructors actually serve two purposes.

1.  Constructors determine who is allowed to create an object of the class type. That is, an object of a class can only be created if a matching constructor can be found.
2.  Constructors can be used to initialize objects. Whether the constructor actually does an initialization is up to the programmer. It’s syntactically valid to have a constructor that does no initialization at all (the constructor still serves the purpose of allowing the object to be created, as per the above).
#### Member initializer list
Member initializer lists allow us to initialize our members rather than assign values to them. This is the only way to initialize members that require values upon initialization, such as const or reference members, and it can be more performant than assigning values in the body of the constructor. Member initializer lists work both with fundamental types and members that are classes themselves.
```cpp
class Something
{
private:
	const int m_value;

public:
	Something(int x) : m_value{ x } // directly initialize our const member variable
	{
	}

	void print()
	{
		std::cout << "Something(" << m_value << ")\n";
	}
};
```

## Static Member Definitions
Do not put the static member definition in a header file (much like a global variable, if that header file gets included more than once, you’ll end up with multiple definitions, which will cause a linker error).
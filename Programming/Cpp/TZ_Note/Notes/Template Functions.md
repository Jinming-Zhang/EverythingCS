# Template Functions

When a same piece of logic can be used on different types, instead of using multiple `overloaded functions`, we can use a function template to replace concrete types with placeholder types, and let the compiler translates those into different overloaded functions.
> Template function here means functions with a logic template that can be applied on multiple types.
> i.e. a **max** function can be used on types such as **int**, **double**,**long**, etc..

# Declare a Template Function
To indicate to the compiler a function is a template function, we write a `template parameter declaration` first followed by the function declaration.
```cpp
template <typename T>
T max(T x, T y){
	return (x>y)?x:y;
}

template <typename T, typename U>
U Foo(T p1, double p2, U p3){
	// do something
	return p3;	
}
```

Inside `template parameter declaration`, we specify the placeholder types that will be used by the function with `typename` or `class` keyword (they are identical), then use them as type placeholder inside function wherever a type is expected.

# Function Template Instantiation

> Template Functions are not actually functions, they are used to **generate** functions by the compiler.

During a template function call, if the compiler cannot find the cooresponding function declaration, it will create on based on the template function that's being called with concrete types.

# Template Arguments Deduction
If the concrete types that we'll use for template function instantiation matches the types of template function parameters, we can omit the type specifications when calling the template function, and the compiler will infer the type by the arguments.
```cpp
// instead of
max<int>(1,2);
// we can let compiler infer the type
max(1,2); // max<int>
max<>(1.1,2.2); // max<double>
```

> If there is a non-template function that has the same name as the template function, then the `<>` matters to let compiler know if it should instantiate a template function or just call the normal function.

# Using Template Functions in Multiple Files
>Define template functions in header files and import those whenever needed.

Since the compiler needs to know the full definition of the template function to instantiate appropriate function, we need to also define it in header files so each cpp file will get a copy of the full definition. 

# Abbreviated function templates C++20
Use `auto` keyward in function parameter types is a way in C++20 to tell the compiler that the function should be treated as template function and each function parameter with `auto` type should be independent parameter type.

```cpp
auto max(auto x, auto y){
	// do stuff
}
// is same as
template <typename T, typename U>
auto max(T x, U y){
	// do stuff
}
```
# Pass by Value
By default, when a function is called, the parameters are copied into the function and destroyed when the function finishes.
This includes fundamental types as well as `class` types.
# Pass by Reference
By using `reference types` when declaring function parameters, we tell the compiler to *bind* the reference to the corresponding parameter that is passed in.
Since `reference types` act as alias to its bonded identifier, we are able to use the reference type just like using the original identifier, and potentially update it inside the function.

# Summary
Primary types are passed by value.
Structs are passed by value.
```
Arrays are passed by reference.
```
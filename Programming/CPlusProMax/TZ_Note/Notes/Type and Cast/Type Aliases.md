# Type Aliases
Type aliases are custom-defined names for a given type.
> Type Aliases do not create new type. They only give existing type a new identifier.

There are two ways of defining a type alias.
## Using
```cpp
using distance_t = double;
```
## Typedef
```cpp
typedef double price;
```

## Note
Type aliases will be substitute with the aliased type by compiler.
```cpp
distance_t dst = 100.0;
price p = 20.5;
// syntactically valid but sematically meaningless
dst = p; 
```
> If the underlying type are the same, type aliases can be used interchangablely.

> Type Aliases will not help on function overloading based on parameter types.
-   Functions
-   Arrays
-   Pointer types:
    -   Pointer to object
    -   Pointer to function
-   Pointer to member types:
    -   Pointer to data member
    -   Pointer to member function
-   Reference types:
    -   L-value references
    -   R-value references
-   Enumerated types:
    -   Unscoped enumerations
    -   Scoped enumerations
-   Class types:
    -   Structs
    -   Classes
    -   Unions
# Using Program-Defined Types in Multi-Files
The compiler needs to see the full definition of a type to decide how much memory to allocate for the variable.
So we need to put the full definition of the type in a header file and include it in other cpp files when needed.
> Type definitions are exempt from the one-definition rule, but we need to make sure **all type definitions of a givin type must be identical**.
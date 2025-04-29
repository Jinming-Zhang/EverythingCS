To be an aggregate in C++, a type must meet the following criteria:

-   Is a class type (a struct, class, or union), or an array type (a built-in array or `std::array`).
-   Has no private or protected non-static data members.
-   Has no user-declared or inherited constructors.
-   Has no base classes.
-   Has no virtual member functions.
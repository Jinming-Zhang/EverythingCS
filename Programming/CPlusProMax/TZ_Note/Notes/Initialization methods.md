# Initialization
Provide an initial value for the variable when it's defined.
There are 4 basic ways to initialize variables in c++.

> Default Initialization
>```cpp
>	 int a;
>```
>leaves the varialbe with indeterminated value (whatever in that memory)

> Copy Initialization
>```cpp
>     int b = 5;
>```
>copies the value on the rhs of '=' to the variable

> Direct Initialization
>```cpp
>	 int c (5);
>```
>for simple data type is similar to copy initialization, but for complicated types, direct initialization tends to be more efficient.

> Brace Initialization / Uniform initialization<br>
> In addition to direct initialization, brace initialization can also be used to initialize list of objects.
>```cpp
>	 // direct brace initialization
>	 int c {5}; 
>	 // copy brace initialization
>	 int c = {5};
>	 // value brace initialization
>	 // set the value to 0 or empty
>	 int c {}; 
>```
> - direct and copy brace initialization are almost the same.
> - ==Brace initialization **disalllow** narrowing conversions.==

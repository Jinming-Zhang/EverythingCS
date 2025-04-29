# Good Commenting
- at the library, program, or function level, use comments to describe what.
- inside the library, program, or function, use comments to describe how.
- at the statement level, use comments to describe why.
# variable declaration and initialization
## Initialization
- default initialization
	- only declare a variable without assign a value.
	- in most cases, this will leaves a varialbe with indeterminate value (whatever it's in the memory)

		```cpp
		int a;

- Copy Initialization
	- An initializer is provided after the equal sign.

		```cpp
		int a = 5;
		```	```
- Direct Initialization
	- An initializer is provided inside parenthesis.

		```cpp
		int a = (5);
		```	```
- Brace/Uniform/List Initialization
	- An consistent way of initializing (list) variables.
	- Brace initialization also disallows "narrowing" conversion and will generate compiler warning/error in such cases.
	- Direct brace initialization

		```cpp
		int a {5};
		```	```
	- Copy brace initialization

		```cpp
		int a = {5};
		```	```
	- Value brace initialization (Most cases will initialize the variable to 0/empty)

		```cpp
		int a {};
		```	```
	- Disallowing narrow conversion

		```cpp
		// This will cause compiler warning/error.
		// Since 4.5 is a float, if it assigned to variable a, the factional part will be lost during the conversion.
		int a {4.5};
		```	```
# Uninitialized Variable...
- Initialization = The object is given a known value at the point of definition.
- Assignment = The object is given a known value beyond the point of definition.
- Uninitialized = The object has not been given a known value yet.

# White space
Quoted text separated by nothing but whitespace (spaces, tabs, or newlines) will be concatenated
```cpp
std::cout << "hello "
     "world!"; // prints "hello world!"
```
# Literals and operators
literals are values that have been directly inserted into the source code (hard coded values).
```cpp
std::cout << "hello world!"; // "hello world!" is a literal.
int x{ 5 }; // 5 is a **literal**.
```
the value of a literal is fixed and can not be changed.
# Expressions
- An expression is a combination of literals, variables, oerators and function calls that can be executed to produce **a single value**.
- The process of executing an expression is called **evaluation**.
- Statement Vs Expression: Statements are used when we want the program to perform an action. Expressions are used when we want the program to calculate a value.
# Local Scope
- Local varialbes are destroyed in the opposite order (thing about call stack) of creation when their local scope body ends (at the end of the curly braces in which it's defined).
# Forward Declarations and Definitions
## One Definition Rule
1. Within a given file, a function, variable, type, or template can only have one definition.
2. Within a given program, a variable or normal function can only have one definition. This distinction is made because programs can have more than one file.
3. Types, templates, inline functions, and inline variables are allowed to have identical definitions in different files.
# Namespaces and Scope resolution operator (::)
To use identifiers defined in a namespace
1. __namespace__::identifier (ie: std::cout)
2. using namespace std;
# Preprocessor and Directives
Code files will go through a phase known as **translation**, which turns code file into properly encoded texts, striping out comments, process preprocessors and gets the code ready to be compiled.<br/>
## directives
Once the preprocessor has finished, all defined identifiers from the file are discarded.<br/>
Directives defined in one code file **do not have impact** on other code files in the same project.
* includes
   - #include \<iostream>
* Macro defines
   - #define identifier (substitute **identifier** with white space)
   - #define identifier substitution_text (substitute **identifier** with substitution_text)
* Conditional compilation
  - #ifdef
  - #ifndef
  - #if 0
  - #endif
# Header Files
- Header files allow us to put declarations in one location and then import then wherever we need them.
- Header files should generally not contain functions and variable definitions.
- Header files are often paired with code files, with the header file providing forward declaration for the corresponding code file. It's a good practice to name the header file same as it's corresponding code file.
## Using " or <>
### <>
Compiler will search for header only in the directory specified by **include directories**, and WILL NOT search for header files in project's directory.<br/>
**include directories** are configured as part of project/compiler setting, usually default to the directory containing the header files that come with compilerj/os.
### "
Compiler will first search in current directory, then the **include directories** if not found.
```
Use double quote for header files can be found in the current directory.

Use angled brackets for header files that come with compiler/os/third-party libraries.
```
## \<iostream> Vs <iostream.h>
Those are two DIFFERENT header files.<br/>
iostream.h came from old cpp headers when they haven't move stdlib functions into **std** namespace.<br/>
To maintain backward capability, functions that moved into **std** namespace were givin a new header which without the .h suffix.
- header files with .h have functions that are not in **std** namespace
- header files without .h have functions that are in **std** namespace
  
Libraries that inherited from C where givin a *c* prefix. (e.g. stdlib.h -> cstdlib)
```
Use the version WITHOUT the .h suffix when including header files from standard libaray
```
```
Use .h when include header files written by us
```
## Include header files from other directory
1. Use relative path in the include directive<br/>
	```
	#include "headers/someheader.h"
	```
2. Use **include directories** to tell the compiler where to find header files
   ```
   g++ -I/folder/to/headerfiles
   ```

## Header Guard
To prevent from including one header file into other files multiple times.<br/>
```cpp
#ifndef SOME_MACRO
#define SOME_MACRO
// contents
#endif
```
## Header File Best Practices
* Order of the #include directives to catch missing includes at compile time
  1. The paired header file
  2. Other headers from the project
  3. 3rd party library headers
  4. Standard library headers
* Always include header guards
* Do not define variables and functions in header files
* Give the header file the same name as the source file that's associated with.
* Make header files as independent as possible.
* Include every dependency for every header file. (Every header files should be able to compile on it's own)
* Only #include what we need
* Do not #include .cpp files

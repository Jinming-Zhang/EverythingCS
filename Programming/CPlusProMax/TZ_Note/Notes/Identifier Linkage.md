# Linkage
Linkage is used in Linking stage of compilation.

>An identifier's linkage means the use or the availability of an identifier across multiple translation unit or within a single translation unit.

## No linkage

Identifier can only be accessed in its scope.

## Internal Linkage
Identifier can be accessed in the whole same file.

## External Linkage
Identifier can be accessed by codes in other files through forward declaration.

## Summary

Local scoped variables have no linkage.
Global variable and functions identifiers can have either `Internal Linkage` or `External Linkage`.

- Local variable has no linkage, it can only be accessed inside its scope, it has [[Variable Duration#Automatic Duration|automatic duration]].
	```cpp
	{
		int x;
	}
	```
- Static local variable has no linkage, it can only be accessed inside its scope, it has [[Variable Duration#Static Duration|static duration]].
	```cpp
	{
		// can only be accessed inside its scope, but the value is keeped untile the end of the program.
		static int x{2};
		++x;
	}
	```
- Non-const global variable has external linkage, [[Variable Duration#Static Duration|static duration]]. It can be accessed by other files through [[Forward Declaration#Non-const Global Variable Forward Declaration|forward declaration]].
- const global variable has internal linkage by default, `extern` keyward can be used to give it external linkage.
	```cpp
	// internal linkage
	const int g_x{1};
	// external linkage
	extern int g_y{2};
	```
- `constexpr` global variable can only have internal linkage.
## Note
- `extern` keyword can be used for 
	- giving global variable external linkage when used on a *initialized* global variable.
		```cpp
		extern int g_x{10};
		```
	- forward declaration used to access global variables with external linkage in other files.
		```cpp
		extern int g_x;
		```
- `static` keyword can be used for
	- giving local variable static duration.
		```cpp
		{
			static int x{1};
		}
		```
	- giving function or global variable internal linkage
		```cpp
			static void foo(int x){}
		```
		```cpp
			static int g_x{1};
		```

### Share Global Constants Across Multiple Files
- Method one, define constants in a header file and import it in other files.
	- Drawback:
		- Each constant has internal scope, so when the header file is dupilicated into multiple files, each file gets it's own copy of the variable, and the compiler also needs more time to compile the additional duplicates. So change the value of a const variable will lead to recompilation of all files that include the header.
- Method Two, turning the consts into global const by defining global const variables in a cpp file, and the variable forward declarations in the corresponding header file. So that each file references to the same variable definition.
	- Drawback:
		- The consts are all runtime consts because compiler can only see the forward declarations. So these const can not be used as compile-time const, and the optimization will also be affected.
- Method Three, by defining `extern` const  [[Inline Function and Variable#Inline Variable|inline variables]] in a header file, when the header file is included by other files, they will refer to the same definition in a cpp file created by linker.
	- Drawback:
		- This way we can save runtime memory and the inline const variables can be used as compile-time const, but files include the header still needs to be recompiled if one value has changed.

## Why avoid non-const global variables
- It can be changed by **any** function.
# Identifier vs Variable
* object is a region of memory that has a value and other associated properties, object can be named or anonymous.
* named object is called **variable**, the name of the object is called **identifier**.

# Declaration vs Definition
[reference](https://www.cprogramming.com/declare_vs_define.html#:~:text=A%20declaration%20provides%20basic%20attributes,where%20that%20variable%20is%20stored.)
- Declaration provides basic attributes of a symble: type and name.
- Definition provides all of the details of a symbol:
	- for functions - function body
	- for variable - value / address
# Expression Statement
A combination of literals, variables, operators, and function calls that can be executed to produce a singular value

# Statement
A fragment of code that can be executed by the computer.

# Null Statement
A statement that doesn't do anything.
Usually used as a placeholder for places that require a statement semantically but actually don't need any logic.
```cpp
if(something){
	;
}
// or
if(something);
```

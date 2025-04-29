# Operators
## Operator precedence
All operators in c++ are assigned a level of precedence, in a compound expression (expression with multiple operators), operator with highest precedence are evaluated first.
> 1 is the highest precedence.

Adjacent operators with same precedence will be evaluated based on their associativity (left-> right or right->left).

> level 5 operators associativity of from left to right.

Value of operands can be evaluated at any order, so do not make expression depends on when the operands will be evaluated.
```cpp
int getvalue()
{
	int v{};
	std::cin<<v;
	return v;
}
// this may give unexpected result because the compiler can getvalue in any order
// the order player enters doesn't match the order in expression
std::cout<<getvalue() + (getvalue() - getvalue())<<std::endl;
```

# Member selection operator

member selection operator `.` : select member from object
member selection from pointer (arrow operator) `->`: select member from pointer to an object.

# Subscript operator []
`subscript operator` is used to subscripting/indexing the array (accessing elements in arrays).
`array subscripts` is the integral type used to indicate the position where we want to access the array.
```cpp
int array[5]{};
int i = array[3];
// [] is the subscript operator
// 3 is the subscript
```
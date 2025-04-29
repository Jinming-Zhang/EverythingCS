[reference](https://en.cppreference.com/w/cpp/language/value_category)
All Expresions in C++ have two properties: `type` and `value category`.
>As a rule of thumb to identify lvalue and rvalue expressions:
>
> lvalues expressions are those that evaluate to variables or other identifiable objects that persist beyond the end of the expression.  
>rvalues expressions are those that evaluate to literals or the returned value of functions and operators that are discarded at the end of the expression.

# Expression Type
The type of the result that the expression is evaluated to.
# Expression's Value Category
The `value category` of an expression indicates whether an expression resolves to a value, a function, or an obbject of some kind.

> Value Categories in C++:
> - lvalue
> - glvalue
> <hr/>
> - rvalue
> - prvalue
> - xvalue

>lvalue can be implicitly converted to rvalues, so lvalue can be used in placec where rvalue is expected.
# LValue
> LValue expressions are expressions that evaluates to a function or objects that has an identifier/identity (named variable or function), or an identifiable memory address.

- Non-modifiable LValue
	`const` and `constexp` lvalues
- Modifiable LValue
	LValues that are modifiable.
# RValue
RValue expressions are expressions that are not LValue.
RValues **only exists within the scope of the expression**, or the result must be used immediately, otherwise it will be discarded.

i.e.
- literals
- return value of functions
- return value of operators
### prvalues
### xvalues
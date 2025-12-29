# GoTo Statement
A `goto` statement is an *unconditional* jump that consist of 
- statement label
	```cpp
	tryAgain:
		std::cout<<"try again\n";
	```
- goto statement
	```cpp
		goto tryAgain;
	```

> A `statement label` requires at least one statement, so [[Glossary#Null Statement|null statement]] has to be used if there is no actual logic for a `statement label`.

# GoTo statement scope
- `goto statement` has function scope, it can jump forward or backward.
- A forward jump can NOT jump over initializations within the same scope.
```cpp
void printCats(bool skip)
{
    if (skip)
        goto end; // jump forward; statement label 'end' is visible here due to it having function scope
	int x{2}; // compiler ERROR!
    std::cout << "cats";
end:
    ; // statement labels must be associated with a statement
}
```
> Avoid using `goto` statement because
> - it makes code less readable
> - error prone
> - and can be replaced by if conditions in most of the cases.
# Switch Case
Two types of labels in a Switch-Case block.

- case:
- default

>`case` and `default` are labels, not *[[Glossary#Expression vs Statement|statements]]*, so they will NOT be counted into the execution steps.
>
>They are interpreted by compiler as Jumps that directly to the label.

# Fallthrough
`fallthrough` is when an execution flows from one statement underneath a label into statements underneath a subsequent label.

```cpp
int main()
{
    switch (2)
    {
    case 1:
        std::cout << 1 << '\n';
        break;
    case 2:
        std::cout << 2 << '\n'; // Execution begins here
        [[fallthrough]]; // intentional fallthrough -- note the semicolon to indicate the null statement
    case 3:
        std::cout << 3 << '\n'; // This is also executed
        break;
    }

    return 0;
}
```

One use case of `fallthrough` is to stack multiple `case` labels that shares a same final statement.
```cpp
bool isVowel(char c)
{
    switch (c)
    {
        case 'a': // if c is 'a'
        case 'e': // or if c is 'e'
        case 'i': // or if c is 'i'
        case 'o': // or if c is 'o'
        case 'u': // or if c is 'u'
        case 'A': // or if c is 'A'
        case 'E': // or if c is 'E'
        case 'I': // or if c is 'I'
        case 'O': // or if c is 'O'
        case 'U': // or if c is 'U'
            return true;
        default:
            return false;
    }
}
```
# Scope in Switch Block
By default, all identifiers inside all labels have the same scope.

>Since `case` and `default` are labels not [[Glossary#Expression vs Statement|statements]], so initialization inside `switch` and `case`/`default` label are not allowed.
>
>However, variable assignment is allowed.

 This  is because 
 - declaration at compile-time is fine
 - but initialization requires run-time execution, and codes inside a swich-case block can be jumped over based on the labels, and thus initialization may also be skipped. [ref](https://stackoverflow.com/questions/92396/why-cant-variables-be-declared-in-a-switch-statement)
 
 So we can't declare and initialize a variable at the same time inside a swich-case block.

However, we can explicitly give the identifier a scope to initialize it.
```cpp
switch (1)
{
    int a; // okay: declaration is allowed before the case labels
    int b{ 5 }; // illegal: initialization is not allowed before the case labels

    case 1:
        int y; // okay but bad practice: declaration is allowed within a case
        y = 4; // okay: assignment is allowed
        break;

    case 2:
        int z{ 4 }; // illegal: initialization is not allowed if subsequent cases exist
        y = 5; // okay: y was declared above, so we can use it here too
        break;

    case 3:
		{
		  int w{3}; // okey
		}
        break;
}
```
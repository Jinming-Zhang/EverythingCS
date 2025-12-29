#  expression with side-effect
>Avoid using variables that has side-effect applied more than once in a statement.
>```cpp
>int x = 5;
>add(x, ++x); 
>```
>indetermined behaviour, because ++x modifies value of x, result will be different depends on the order that the compiler evaluates the parameters.

>Avoid using expressions with side-effect in conjunction with **boolean logical** operations.
>if x is not 1, then ++y will not be executed due to **short circuit**, which may not be intended
>```cpp
>if(x==1 && ++y == 2){
>	//do something
>}
>```




upcasting: implicitly convert a derived pointer to base pointer.
downcasting: convert a base pointer to a derived pointer.

# C-style cast
```cpp
    double d { (double)x / y }; // convert x to a double so we get floating point division
	double d { double(x) / y }; // convert x to a double so we get floating point division
```
`c-style cast` is context dependent and  can be performed as one of `static cast`, `const cast` or `reinterpret cast`. 
It can be misused unintensionaly, avoid using `c-style cast`.

# Static Cast
`std::static_cast<int>(5.5)`

# Dynamic Cast
`dynamic_cast<Derived*>(Base*)`
`dynamic_cast<Derived&>(Base&)`

dynamic cast will do some runtime check, so it's slightly slower

When dynamic cast failed, it will return a `null_ptr`
```cpp
int main()
{
	Base* b{ getObject(true) };
	Derived* d{ dynamic_cast<Derived*>(b) }; // use dynamic cast to convert Base pointer into Derived pointer

	if (d) // make sure d is non-null
		std::cout << "The name of the Derived is: " << d->getName() << '\n';
	return 0;
}
```
dynamic cast for downcasting **won't** work in the following cases:
1. with protected or private inheritance
2. classes that do not have virtual functions
3. cases involving virtual base classes

# Const Cast
# Reinterpret Cast

## static cast vs dynamic cast
dynamic cast will do some runtime check (return null of cast failed), so it's slightly slower, whereas static cast doesn't do runtime check (and thus more dangerous).

prefer dynamic_cast when doing down casting, since it will return null_ptr upon failure, and prefer static_cast otherwise.

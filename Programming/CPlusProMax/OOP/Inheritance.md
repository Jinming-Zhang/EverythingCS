# Access Modifiers
The access specifiers only affect whether **outsiders** and **derived** classes can access those members.
When derived classes inherit members, the access modifier for inheritance changes the access modifiers for the derived classes, this only affects the outsiders and the classes that derived from the derived classes.

```cpp
class Base
{
public:
	int m_public {};
	friend std::ostream& operator<< (std::ostream& out, const Base& b)
	{
		out << "In Base\n";
		out << b.m_value << '\n';
		return out;
	}
protected:
	int m_protected {};
private:
	int m_private {};
};
```

```cpp
class D2 : private Base // note: private inheritance
{
	// Private inheritance means:
	// Public inherited members become private
	// Protected inherited members become private
	// Private inherited members stay inaccessible
public:
	int m_public2 {};
	friend std::ostream& operator<< (std::ostream& out, const D2& d)
	{
		out << "In Derived\n";
		// static_cast Derived to a Base object, so we call the right version of operator<<
		out << static_cast<const Base&>(d);
		return out;
	}
protected:
	int m_protected2 {};
private:
	int m_private2 {};
};
```

```cpp
class D3 : public D2
{
	// Public inheritance means:
	// Public inherited members stay public
	// Protected inherited members stay protected
	// Private inherited members stay inaccessible
public:
	int m_public3 {};
protected:
	int m_protected3 {};
private:
	int m_private3 {};
};
```

# Overriding Behaviour
When redefine a function in the derived class, the derived function doesn't inherit the access modifier of the function with the same name in the base class.

##### Calling friend function of base class
We'll need to cast the derived class to the type of base class in order to call the friend function of base class, since they may not be defined in side the base class.

# Virtual functions
When we use a pointer/reference of a base class variable that points to a derived class, it cannot see the members that are defined inside the derived class, so we won't be able to call any function in the derived class.
#### Virtual functions and polymorphism
**virtual function** is a special type of function that when called, resolved to the **most-derived** version of the function that exists between the base and derived class. This capability is known as **polymorphism**.

> virtual function only apply to pointer/reference type of base variables that point/reference to the base part of a derived class. If a base class variable is initialized with the copy of a derived class, then it doesn't contain the information of the derived class.

> If a function is virtual, all matching overrides in derived classes are implicitly virtual.

> Never call virtual functions from constructors or destructors.

#### override and final specifier
##### override
To ensure we override the functions we want and avoid types, we can use the *override* keyword to inform compiler to enforce that the function actually overrides some function in the base.

```cpp
class A
{
public:
	virtual std::string_view getName1(int x) { return "A"; }
	virtual std::string_view getName2(int x) { return "A"; }
	virtual std::string_view getName3(int x) { return "A"; }
};

class B : public A
{
public:
	std::string_view getName1(short int x) override { return "B"; } // compile error, function is not an override
	std::string_view getName2(int x) const override { return "B"; } // compile error, function is not an override
	std::string_view getName3(int x) override { return "B"; } // okay, function is an override of A::getName3(int)

};
```

> Use the virtual keyword on virtual functions in a base class. Use the override specifier (but not the virtual keyword) on override functions in derived classes.

##### final
the *final* specifier prevents any derived class to inherit or override the member function.
```cpp
class A
{
public:
	virtual std::string_view getName() { return "A"; }
};

class B : public A
{
public:
	// note use of final specifier on following line -- that makes this function no longer overridable
	std::string_view getName() override final { return "B"; } // okay, overrides A::getName()
};

class C : public B
{
public:
	std::string_view getName() override { return "C"; } // compile error: overrides B::getName(), which is final
};
```

#### virtual destructors
> Whenever you are dealing with inheritance, you should make any explicit destructors virtual.

This is to avoid the case that the derived class need to release memory in destructor and the wrong destructor is called when using polymorphism.

#### Virtual table
##### early binding vs late binding
- early binding: direct function calls that the compiler can link the function call to the function address at compile time
- late binding: indirect function calls such as function pointers that the compiler is not able to link the function at compile time. Late binding will take an extra step that resolves the address that the function pointer is pointing to, then jump to the address of that function.


##### virtual table
> virtual table is a lookup table of functions, that used to resolve functions calls in a late/dynamic binding manner. It's simply a static array that the compiler sets up at **compile** time, that contains one entry for each virtual function that can be called by that class. Each entry is a function pointer that points to the most-derived function accessible by that class.


1. Every class that uses virtual functions **and is derived from a class that uses virtual functions** is given its own virtual table.
2. In **base class**, the compiler adds a hidden pointer that is a member of that base class, `*__vptr`. This is set automatically when the class object is created and it points to the virtual table for that class.
3. For each **instance** of the class that has a virtual table, an extra memory of a pointer size will be allocated for the hidden member variable `*__vptr` of their **most** base class.

To do a virtual function call, it involves 3 steps:
1. use `*__vptr` to get the appropriate virtual table.
2. find the corresponding function to call in the virtual table.
3. call the function.

This is 1 step more than calling a indirect function, and 2 steps more than calling a direct function.

# Pure virtual/abstract functions and abstract base classes
Assign the function with the value 0 will declare the function as a pure virtual function.
- Any class with one or more pure virtual functions becomes an abstract base class(**abstract class**).

# Interface
A abstract base class that has no member variables and consists of all pure virtual functions.
```cpp
class IErrorLog
{
public:
    virtual bool openLog(std::string_view filename) = 0;
    virtual bool closeLog() = 0;

    virtual bool writeError(std::string_view errorMessage) = 0;

    virtual ~IErrorLog() {} // make a virtual destructor in case we delete an IErrorLog pointer, so the proper derived destructor is called
};
```

# Object slicing
When assigning a Derived object to a Base object, only the base part of the derived object is copied and the part defined in the derived part won't be visible to the base variable, thus polymorphism won't work. This is called **object slicing**.

#### Problem 1
Object slicing disables polymorphism, because it only copies the base part of the derived class to base class.
If we want to use polymorphism, we have the user reference/pointer of the base class.
For `std::vector`, we either use a pointer of the base class type, or `std::reference_wrapper` to wrap the base object as a reference.

#### Problem 2
Frankenobject: An object composed of parts of multiple objects.

```cpp
int main()
{
    Derived d1{ 5 };
    Derived d2{ 6 };
    Base& b{ d2 };

    b = d1; // this line is problematic

    return 0;
}
```

In the above code, `b` is a reference to `d2`. 
When we assign `d1` to `b`, we would expect d2 to hold same value as d1.
However, since b is a reference of type **Base**, when we use the assignment operator to assign values from `d1` to `b`, only the **Base** part of d1 is copied to d2, therefore the derive part of d2 is still unchanged.
This result `d2` to have the base part of d1, and derived part of d2.

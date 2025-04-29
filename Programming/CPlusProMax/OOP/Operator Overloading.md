In C++, Operators are  implemented as functions, we can alter the behaviours of operators by using function overloading on operator functions.
## Three ways to overload operators
1. Member function
2. Friend function
3. Normal function

#### Member Function
```cpp
class Cents
{
private:
    int m_cents {};

public:
    Cents(int cents)
        : m_cents { cents } { }

    // Overload Cents + int
    Cents operator+ (int value);

    int getCents() const { return m_cents; }
};

// note: this function is a member function!
// the cents parameter in the friend version is now the implicit *this parameter
Cents Cents::operator+ (int value)
{
    return Cents { m_cents + value };
}
```
#### Friend Function
```cpp
class Cents
{
private:
	int m_cents {};

public:
	Cents(int cents) : m_cents{ cents } { }

	// add Cents + int using a friend function
	friend Cents operator+(const Cents& c1, int value);

	// add int + Cents using a friend function
	friend Cents operator+(int value, const Cents& c1);
	int getCents() const { return m_cents; }
};
// note: this function is not a member function!
Cents operator+(const Cents& c1, const Cents& c2)
{
	// use the Cents constructor and operator+(int, int)
	// we can access m_cents directly because this is a friend function
	return Cents{c1.m_cents + c2.m_cents};
}
```
#### Normal Function
```cpp

class Cents
{
private:
  int m_cents{};

public:
  Cents(int cents)
    : m_cents{ cents }
  {}

  int getCents() const { return m_cents; }
};

// note: this function is not a member function nor a friend function!
Cents operator+(const Cents& c1, const Cents& c2)
{
  // use the Cents constructor and operator+(int, int)
  // we don't need direct access to private members here
  return Cents{ c1.getCents() + c2.getCents() };
}
```

## Overloading the assignment operator
**operator=** is used to replace the contents of the existing object with another one.
Whereas copy constructor is used to initialize new object.

## Operator overloading  suggestions
-   If you’re overloading assignment (=), subscript ([]), function call (()), or member selection (->), do so as a member function.
-   If you’re overloading a unary operator, do so as a member function.
-   If you’re overloading a binary operator that does not modify its left operand (e.g. operator+), do so as a normal function (preferred) or friend function.
-   If you’re overloading a binary operator that modifies its left operand, but you can’t add members to the class definition of the left operand (e.g. operator<<, which has a left operand of type ostream), do so as a normal function (preferred) or friend function.
-   If you’re overloading a binary operator that modifies its left operand (e.g. operator+=), and you can modify the definition of the left operand, do so as a member function.
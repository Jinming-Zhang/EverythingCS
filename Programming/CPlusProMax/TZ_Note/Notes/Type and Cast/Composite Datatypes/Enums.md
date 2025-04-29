# Enum
A `Enum` is a compound data type where **every possible value** is defined as a symbolic constant.

Enumerated types are best used when you have a smallish set of related constants, and objects only need to hold one of those values at a time.

# Terminologies
`enumeration` means the defined enum type.
`enumerator` are the options defined in each enum type.

# Unscoped Enum
Unscoped enum put their enumerators (values) into the same scope as the definition of the enum.
This increses the chance of causing name collisions.

```cpp
enum Color
{
    red,
    green,
    blue, // blue is put into the global namespace
};

enum Feeling
{
    happy,
    tired,
    blue, // error: naming collision with the above blue
};

int main()
{
    Color apple { red }; // my apple is red
    Feeling me { happy }; // I'm happy right now (even though my program doesn't compile)

    return 0;
}
```

# Scoped Enum / Enum Class
`Scoped enum` are
- Strongly typed (won't implicitly convert to integer)
- Strongly scoped (enumerators are only placed **into** the scope region of the enumeration)

```cpp

    enum class Color // "enum class" defines this as a scoped enumeration rather than an unscoped enumeration
    {
        red, // red is considered part of Color's scope region
        blue,
    };

    enum class Fruit
    {
        banana, // banana is considered part of Fruit's scope region
        apple,
    };
```

> The `class` keyword here is only used for declare scoped enum, it's not the same as `class` type (struct, class, union)

# Using Enum Statement
The `using enum` statement can import the  enumerators of the scoped enum into the current scope, which can save repeatitive prefixes when necessary.

```cpp
enum class Color
{
    black,
    red,
    blue,
};

constexpr std::string_view getColor(Color color)
{
    using enum Color; // bring all Color enumerators into current scope
    // We can now access the enumerators of Color without using a Color:: prefix

    switch (color)
    {
    case black: return "black"; // note: black instead of Color::black
    case red:   return "red";
    case blue:  return "blue";
    default:    return "???";
    }
}
```
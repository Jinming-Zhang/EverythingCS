## Define a class
```cpp
class DateClass
{
private:
    int m_year {};
    int m_month {};
    int m_day {};
	static inline int m_wow{};
public:
	// default constructor
	DateClass() = default;
	// disable this type of converting constructor call
	DateClass(char) = delete;
	DateClass(int year, int month, int day):
		m_year{year},
		m_month{month},
		m_day{day}
	{}
	void print() // defines a member function named print()
	{
	        std::cout << m_year << '/' << m_month << '/' << m_day;
	}
};
```
## Friend Functions
```cpp
class Humidity;

class Temperature
{
private:
    int m_temp {};

public:
    Temperature(int temp=0)
        : m_temp { temp }
    {
    }

    friend void printWeather(const Temperature& temperature, const Humidity& humidity);
};

class Humidity
{
private:
    int m_humidity {};

public:
    Humidity(int humidity=0)
        : m_humidity { humidity }
    {
    }

    friend void printWeather(const Temperature& temperature, const Humidity& humidity);
};

void printWeather(const Temperature& temperature, const Humidity& humidity)
{
    std::cout << "The temperature is " << temperature.m_temp <<
       " and the humidity is " << humidity.m_humidity << '\n';
}
```
## Friend Classes
```cpp
class Storage
{
private:
    int m_nValue {};
    double m_dValue {};
public:
    Storage(int nValue, double dValue)
       : m_nValue { nValue }, m_dValue { dValue }
    {
    }

    // Make the Display class a friend of Storage
    friend class Display;
};

class Display
{
private:
    bool m_displayIntFirst;

public:
    Display(bool displayIntFirst)
         : m_displayIntFirst { displayIntFirst }
    {
    }

    void displayItem(const Storage& storage)
    {
        if (m_displayIntFirst)
            std::cout << storage.m_nValue << ' ' << storage.m_dValue << '\n';
        else // display double first
            std::cout << storage.m_dValue << ' ' << storage.m_nValue << '\n';
    }
};
```

## Class Relationships
#### Composition and Aggregation

> Aggregation > Composition

##### Composition
Composition models a *part of* relationship, where the object and the part has the following relationship:
1. *part* is part of the whole object
2. *part* can only belongs to one object at a time
3. *part's* existence is managed by the container object
4. *part* doesn't know about the existence of the container object.
Example: A person has a heart.
##### Aggregation
1. *part* is part of the whole object
2. *part* can belongs to more than one object at a time
3. *part's* existence is NOT managed by the container object
4. *part* doesn't know about the existence of the container object.
Example: Few person have live at an address(*part*.

#### Association
Association models a *use a* relationship.
1.   The associated object (member) is otherwise unrelated to the object (class)
2.   The associated object (member) can belong to more than one object (class) at a time
3.   The associated object (member) does _not_ have its existence managed by the object (class)
4.   The associated object (member) may or may not know about the existence of the object (class)

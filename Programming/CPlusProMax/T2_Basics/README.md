
# Basics

## Data type categories

- Floating Point Numbers
- Integral
	- int, bool, char, enum
	- named because they are stored in memory like integers, even though their behaviours may vary
- Null Pointer
- Void

### Integral Types

## sizeof operator and 'size_t' type
- returns the number of bytes that a type or an identifier takes in memory
- 'std::size_t' in std namespace is defined as an **unsigned integral** type. It's typically used to represent *size or lengh of objects*
	``` 
	any object with a size larger than the largest value that **std::size_t** can hold will cause compiler error
	```

## unsigned int and cautions
- add 'unsigned' keyword before integer types
	```cpp
	unsigned short x{0};
	unsigned int y{0};
	unsigned long z{0};
	```
- wrapped behaviour (modulo wrapping) when overflow (only for unsigned int)
	```cpp
	// 2e16 - 1 = 65535 is the largest unsigned short value
	unsigned short x{-1}; // => -1 % 2e16 => x = 65535
	unsigned short y{65537}; // => 65537 % 2e16 => x = 2
	```
- when doing alrithmatic operation with unsigned int and signed int, signed int will be **casted** to unsigned int before the operation.
- pitfalls
  - it's **extremely** easy to make unsigned int overflow when using it doing alrithmatic operations, both with unsigned int and mixing with signed int
## fixed width int, fast/least int
Because C/C++ standard only provides minimun bytes required for **int/unsigned int** type, fixed width int type in std namespace was introduced to improve the capability of the program. The format is **std::int#_t** where # is the bits the int will take.
```cpp
std::int16_t a{0};
std::uint16_t a_1{0};
std::int32_t b{0};
std::uint32_t b_1{0};
```
However, some exotic and embedded architecture may not support fixed-width int, also may slow down the computing speed on certain architectures.  
<br/>
Fast/Least int
- fast int# provides the fastest signed/unsigned int with width of at least # bits
	```cpp
	std::int_fast16_t fastInt16{1};
	std::int_fast32_t fastInt32{1};
	```
- least int# prives the smallest signed/unsigned int with width at least # bits.
	```cpp
	std::int_least16_t leastInt16{1};
	```
### Best Practices for using int types
- using **int** for holding quantities.
- using **std::int#_t**, **std::uint#_t**  for holding quantities that needs a guaranteed range.
- using **uint** for bit manipulation or well-defined wrapping behaviour is desired

## Floating Point Numbers

### Precisions
Precision defines how many significant digits the floating point number can represent without information loss.

 | size             | significant  digit precision |
 | ---------------- | ---------------------------- |
 | 4 bytes(float)   | 6-9, usually 7               |
 | 8 bytes (double) | 15-18, usually 16            |
 | 16 bytes (long)  | 33-36                        |

### Precision Lost
When a number has a higher significant digits than the floating point number it's assigning to. (i.e. assigning a number with 10 significant digits to a float)
```cpp
float f{1234567890};
std::cout<<std::setprecision(9);
// note the digit after float's precision is inaccurate
std::cout<<f<<end; // 123456792
```
### Rounding Error
- When some of the significant digits of a floating point number is truncated due to the limited size.
- Not just happends to large numbers, but also to decimals that hards to prepresent in binary (i.e. 0.1 in decimal => 0.00011001100... in binary)
```cpp
cout<<setprecision(17);
cout<<0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1<<endl; // will show 0.99999999999999989 instead of 1
```

## Literal constants and Symbolic constants
| Literal Default Type | Value    |
| -------------------- | -------- |
| int                  | 5, 0, -3 |
| double               | 1.2      |
| char                 | 'a'      |
| bool                 | true     |

### Literal suffixes (cast default literal type)
- cast int literal
	- u/U -> uint, 5u
	- l/L -> long, 5l
	- ul/UL -> unsigned long, 5ul
	- ll/LL -> long long, 2342ll
- cast double literal
	- f/F -> float, 1.23f
	- l/L -> long duble, 1.23523l
- binar, octal, hex literals
	- 0b -> binary, int bin{0b1110}; (14)
	- 0 -> octal, int oct{012}; (10)
	- 0x -> hex, int hex(0xff); (65280)

### Bitset (printing binary)
It's defined in **bitset** header
```cpp
#include<bitset>
```

format: std::bitset\<numberOfBits>

```cpp
std::bitset<8> 8bits{0b11101010};
```

### Digit separater '
Used to make numbers more readable
```cpp
int bin{0b1111'1100};
int oct{0111'100};
int dec{541'411'100};
```
### const and constexp
- **const** for runtime unmutables
	```cpp
	int age{0};
	std::cout<<"Enter your age:"<<std::endl;
	std::cin<<age;
	const int givenAge{age};
	```
- **constexp** for compile time unmutables
	```cpp
	constexpr float gravity{9.8f};
	```
- use **const** for any variable that should not be modified after initialization and whose initializer is known at run time.
- use **constexpr** for any variable that should not be modified after initialization and whose initializer is known at compile time.

## Type conversion and static_cast
- use **static_cast\<new_type>(expression)** to cast a variable to desired type
	```cpp
	// output: 1
	std::cout<<static_cast<int>(1.234)<<endl;
	```

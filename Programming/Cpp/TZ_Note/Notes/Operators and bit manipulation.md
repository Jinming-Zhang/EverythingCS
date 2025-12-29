# Increment/Decrement Operator
<table>
<tr>
<td >Form</td>
<td>Operation</td>
</tr>
<tr>
<td>++x</td>
<td>increment x, then return x</td>
</tr>
<tr>
<td>--x</td>
<td>decrement x, then return x</td>
</tr>
<tr>
<td>x++</td>
<td>copy x, increment x, then return the copy</td>
</tr>
<tr>
<td>x--</td>
<td>copy x, decrement x, then return the copy</td>
</tr>
</table>

> Prefer prefix version, e.g ++x.
> It's more performant

# Conditional Operator ?:
It has a very low precedence (rank 16/17), it will be error prone if we use it to do anything other than assigning the result to a varialbe.
```cpp
std::cout<< x>y?1:0 <<std::endl;
```
will be equivalent to
```cpp
(std::cout<< x>y) ?1:0<<std::endl;
```
which prints x>y, and discards both 1 and 0.

> Conditional Initialization
> ```cpp
> 	// if-else can not do
> constexp bool full{false}
>constexp maxStudent {full?10:20};
>```

# scope resolution operator ::
The scope resolution operator tells the compiler that the identifier specified at the right hand operand should be looked for in the scope of the left hand operand.

If there is no namespace provided at the left hand side of the operator, then it will look into global namespace.
```cpp
::doSomething(); // look into golbal namespace
foo::doSomething(); //look into foo namespace
```

global scope resolution is useful when we want to call identifiers in global scope from within a namespace.
```cpp
void print(){
std::cout<<"real print\n";
}
namespace foo{
	void print(){};
	void f(){
		print(); //nothing show
		::print(); // calls the global version
	}
}
```

Nested namespace:
```cpp
namespace foo{
	namespace goo{
		void something();
	}
}
// or since c++17
namespace foo::goo{
	void something();
}
```

Namespace aliases provides convenient way for accessing namespaces:
```cpp
namespace active = foo::goo;
// equivelant to foo::goo::something();
active::something();
```

Packaging functions inside a nameespace also gives advantage of helping auto-complite and suggestion feature in editors.

# Bit Manipulations
<table>
<tr>
<td>Operator</td>
<td>Symbol</td>
<td>Form</td>
<td>Operation</td>
</tr>
<td>left shift</td>
<td> &lt&lt </td>
<td>  x &lt&lt y </td>
<td>all bits in x shifted left by y bits</td>
</tr>
<td>right shift</td>
<td>&gt&gt </td>
<td>x &gt&gt y</td>
<td>all bits in x shifted right by y bits</td>
</tr>
<td>bitwise NOT</td>
<td>~</td>
<td>~x</td>
<td>all bits in x flipped</td>
</tr>
<td>bitwise AND</td>
<td>&</td>
<td>x & y</td>
<td>each bit in x AND each bit in y</td>
</tr>
<td>bitwise OR</td>
<td>|</td>
<td>x | y</td>
<td>each bit in x OR each bit in y</td>
</tr>
<td>bitwise XOR</td>
<td>^</td>
<td>x ^y</td>
<td>each bit in x XOR each bit in y</td>
</tr>
</table>

New bits that shifted in will have value 0, bits that shifted out are lost forever.
>0011 << 3  result in 1000
>1100 >> 3  result in 0001

# Bit Masks

Declare bitmask variables:
```cpp
constexpr std::uint8_t mask0{1<<0}; //0000 0001
constexpr std::uint8_t mask1{1<<1}; //0000 0010
constexpr std::uint8_t mask2{1<<2}; //0000 0100
constexpr std::uint8_t mask3{1<<3}; //0000 1000
constexpr std::uint8_t mask4{1<<4}; //0001 0000
constexpr std::uint8_t mask5{1<<5}; //0010 0000
constexpr std::uint8_t mask6{1<<6}; //0100 0000
constexpr std::uint8_t mask7{1<<7}; //1000 0000
```

Assume we have a bitflags x:
```cpp
std::uint8_t x{0b0100'1010};
```
To set bits, use bitwise OR:
```cpp
// set bit at index 0, 4
std::cout<< x | (mask0 | mask4) <<std::endl;
```

To reset bits, use bitwise AND with flipped mask:
```cpp
// reset bits at index 0, 1
std::cout<< x & ~(mask0 | mask1) <<std::endl;
```

To flip bits, use bitwise XOR:
```cpp
// flip bits at index 0, 1
std::cout<< x ^ (mask0 | mask1) <<std::endl;
```

To test bits, use bitwise AND:
```cpp
// test if bits at index 0, 1 are both set
std::cout<< x & (mask0 | mask1).any()<<std::endl;
```
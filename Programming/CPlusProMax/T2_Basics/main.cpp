#include <iostream>
#include <iomanip>
#include <bitset>
using namespace std;
#define tab "\t"
#include "../Utils/utils.h"

void sizeofOperator();
void integerOverflow();
void fastLeastInt();
void floatType();
void static_cast_exp();
void literalConstants();
int main()
{
	egCall(sizeofOperator);
	egCall(integerOverflow);
	egCall(fastLeastInt);
	egCall(floatType);
	egCall(static_cast_exp);
	egCall(literalConstants);
	return 0;
}

void sizeofOperator()
{
	std::cout << "sizeof operator" << std::endl;
	std::cout << "bool:\t\t" << sizeof(bool) << " bytes\n";
	std::cout << "char:\t\t" << sizeof(char) << " bytes\n";
	std::cout << "wchar_t:\t" << sizeof(wchar_t) << " bytes\n";
	std::cout << "char16_t:\t" << sizeof(char16_t) << " bytes\n";
	std::cout << "char32_t:\t" << sizeof(char32_t) << " bytes\n";
	std::cout << "short:\t\t" << sizeof(short) << " bytes\n";
	std::cout << "int:\t\t" << sizeof(int) << " bytes\n";
	std::cout << "long:\t\t" << sizeof(long) << " bytes\n";
	std::cout << "long long:\t" << sizeof(long long) << " bytes\n";
	std::cout << "float:\t\t" << sizeof(float) << " bytes\n";
	std::cout << "double:\t\t" << sizeof(double) << " bytes\n";
	std::cout << "long double:\t" << sizeof(long double) << " bytes\n";
}
void integerOverflow()
{
	unsigned short x{65535}; // largest 16-bit unsigned value possible
	std::cout << "x was: " << x << '\n';

	x = 65536; // 65536 is out of our range, so we get wrap-around
	std::cout << "x is now: " << x << '\n';

	x = 65537; // 65537 is out of our range, so we get wrap-around
	std::cout << "x is now: " << x << '\n';
}

void fastLeastInt()
{
	cout << "Fast/Least int" << endl;
	std::cout << "least 8:  " << sizeof(std::int_least8_t) * 8 << " bits\n";
	std::cout << "least 16: " << sizeof(std::int_least16_t) * 8 << " bits\n";
	std::cout << "least 32: " << sizeof(std::int_least32_t) * 8 << " bits\n";
	std::cout << '\n';
	std::cout << "fast 8:  " << sizeof(std::int_fast8_t) * 8 << " bits\n";
	std::cout << "fast 16: " << sizeof(std::int_fast16_t) * 8 << " bits\n";
	std::cout << "fast 32: " << sizeof(std::int_fast32_t) * 8 << " bits\n";
	cout << "Why avoid std::int8_t and std::uint8_t" << endl;
	std::int8_t int8{69};
	std::uint8_t uint8{69};
	cout << "int8 value of 69: " << int8 << endl;
	cout << "uint8 value of 69: " << uint8 << endl;
	cout << "casted int8 value of 69: " << static_cast<int>(int8) << endl;
	cout << "casted uint8 value of 69: " << static_cast<int>(uint8) << endl;
}

void floatType()
{
	cout << "Float Type" << endl;
	cout << std::setprecision(16);
	std::cout << 3.33333333333333333333333333333333333333f << '\n'; // f suffix means float
	std::cout << 3.33333333333333333333333333333333333333 << '\n';	// no suffix means double
	cout << "Precision lost" << endl;
	cout << setprecision(16);
	cout << tab << "Double with precision of 16 significant digits" << endl;
	cout << tab << tab << 0.1 << endl;
	cout << setprecision(17);
	cout << tab << "Double with precision of 17 significant digits" << endl;
	cout << tab << tab << 0.1 << endl;
	// rounding errors
	cout << "Rounding Errors, double type example with precision 17" << endl;
	double d1{1.0};
	cout << tab << "double of value 1.0" << endl;
	cout << tab << tab << d1 << endl;
	cout << tab << "double of value 0.1 added 10 times" << endl;
	double d2{0};
	d2 = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1;
	cout << tab << tab << d2 << endl;
}

void static_cast_exp()
{
	cout << setprecision(16);
	cout << "static cast example" << endl;
	cout << tab << "double to int" << endl;
	cout << tab << 5.678 << endl;
	cout << tab << static_cast<int>(5.0) << endl;
}

void literalConstants()
{
	cout << "Literal and const" << endl;
	cout << "dec, oct, hex, and binary\n";
	int dec1{10};
	int oct{010};
	int hex{0x10};
	int bin{0b1110};
	cout << "10: " << dec1 << endl;
	cout << "010: " << oct << endl;
	cout << "0x10: " << hex << endl;
	cout << "0b1110: " << bin << endl;
	cout << "bitset (print binary)" << endl;
	cout << "bitset<8>(0b11101010): " << bitset<8>(0b11101010) << endl;
	cout << "bitset<32>(32): " << bitset<32>(32) << endl;
}

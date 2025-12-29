#include <iostream>
#include <bitset>
#include "../Utils/utils.h"

using namespace std;
void bitsetBitManipulation();
void bitwiseOperators();
void bitmasks();
int main()
{
	egCall(bitsetBitManipulation);
	egCall(bitwiseOperators);
	egCall(bitmasks);
	return 0;
}

void bitsetBitManipulation()
{
	cout << "Bit Manipulation\n";
	bitset<8> bit8{0b1011'0100};
	cout << "Initial bit8: " << bit8 << endl;
	cout << "Using std::bitset for bit manipulations\n";
	cout << "std::bitset.set(3) to set bit value to 1 in a given position(3)\n";
	bit8.set(3);
	cout << bit8 << endl;
	cout << "std::bitset.reset(4) to set bit value to 0 in a given position(4)\n";
	bit8.reset(4);
	cout << bit8 << endl;
	cout << "std::bitset.flip(5) to flip the bit value in a given position(5)\n";
	bit8.flip(5);
	cout << bit8 << endl;
	cout << "std::bitset.test(6) to check the bit value in a given position(6)\n";
	cout << bit8.test(6) << endl;
}

void bitwiseOperators()
{
	cout << "bitwise operators\n";
	bitset<8> bit8{0b10101010};
	cout << "initial bit8:\n"
		 << bit8 << endl;
	cout << "shift all bits to the left for 2 bits using <<2\n";
	bit8 = bit8 << 2;
	cout << bit8 << endl;
	cout << "shift all bits to the right for 2 bits using >>2\n";
	bit8 = bit8 >> 2;
	cout << bit8 << endl;
	cout << "flip all bits using ~\n";
	bit8 = ~bit8;
	cout << bit8 << endl;
	cout << "bitwise AND with 01001011\n";
	bit8 &= 0b01001011;
	cout << bit8 << endl;
	cout << "bitwise OR with 10100010\n";
	bit8 |= 0b10100010;
	cout << bit8 << endl;
	cout << "bitwise XOR with 11111111\n";
	bit8 ^= 0b11111111;
	cout << bit8 << endl;
}
void bitmasks()
{
	cout << "Bit Masks\n";
	constexpr std::uint8_t mask0{1 << 0}; // 0000 0001
	constexpr std::uint8_t mask1{1 << 1}; // 0000 0010
	constexpr std::uint8_t mask2{1 << 2}; // 0000 0100
	constexpr std::uint8_t mask3{1 << 3}; // 0000 1000
	constexpr std::uint8_t mask4{1 << 4}; // 0001 0000
	constexpr std::uint8_t mask5{1 << 5}; // 0010 0000
	constexpr std::uint8_t mask6{1 << 6}; // 0100 0000
	constexpr std::uint8_t mask7{1 << 7}; // 1000 0000

	std::uint8_t x{0b0100'1010};
	cout << "x: " << bitset<8>{x} << endl;
	cout << "set bit at index 0, 4 using bitwise OR\n";
	cout << bitset<8>{x} << "->\n" << bitset<8>{(x | (mask0 | mask4))} << endl;

	cout << "reset bit at index 1, 2 using bitwise AND with flipped mask\n";
	cout << bitset<8>{x} << "->\n" << bitset<8>{(x & ~(mask1 | mask2))} << endl;

	cout << "flip bit at index 1, 2 using bitwise XOR\n";
	cout << bitset<8>{x} << "->\n" << bitset<8>{(x ^ (mask1 | mask2))} << endl;

	cout << "test bits at index 1, 2 using bitwise AND\n";
	cout << bitset<8>{x} << "->\n" << bitset<8>{(x & (mask1 | mask2))}.any() << endl;
}

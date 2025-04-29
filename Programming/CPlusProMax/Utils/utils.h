#pragma once
#include <iostream>
// typedef void (*action)();
using action = void (*)();
void egCall(action f)
{
	std::cout << std::endl;
	f();
	std::cout << std::endl;
}

void printTitle(std::string title)
{
	std::cout << title << std::endl;
}

#include <iostream>

// global variable with external linkage by default
int g_x{3};
// const global variable with extern keyword has external linkage
extern const int ecg{5};
// function has external linkage by default
void externalLinkage()
{
	std::cout << "default external linkage function.\n";
}
// static global variable with internal linkage
static int sg_x{1};
// const global variable with internal linkage
const int cg_x{2};
// constexpr global variable with internal linkage
constexpr int cge_x{3};

// static function with internal linkage
// void internalLinkage()
static void interalLinkage()
{
	std::cout << g_x << std::endl;
}

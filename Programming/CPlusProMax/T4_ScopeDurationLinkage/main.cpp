#include <iostream>
#include "utils.h"
#include "ownNamespace.h"

using namespace std;
int doSomething(int a)
{
	return a + 10;
}

namespace foo
{
	int doSomething(int a)
	{
		return ++a;
	}
}

namespace boo
{
	int doSomething(int a)
	{
		return --a;
	}
}

void namespaceExample();
void variableShadowing();
void internalLinkageEg();
int main()
{
	egCall(namespaceExample);
	egCall(variableShadowing);
	egCall(internalLinkageEg);
	return 0;
}

void namespaceExample()
{
	cout << "user defined namespace. \n";
	int x{0};
	cout << "x: " << x << endl;
	cout << "global namespace using ::doSomething(x)" << endl;
	cout << doSomething(x) << endl;

	cout << "foo namespace using foo::doSomething(x)" << endl;
	cout << foo::doSomething(x) << endl;

	cout << "boo namespace using boo::doSomething(x)" << endl;
	cout << boo::doSomething(x) << endl;

	cout << "nested namespace using foo::fgoo::doSomething(x, 1)" << endl;
	cout << foo::fgoo::doSomething(x, 1) << endl;

	namespace active = foo::fgoo;
	cout << "nested namespace using namespace alias: active = foo::fgoo" << endl;
	cout << active::doSomething(x, 1) << endl;
}

void variableShadowing()
{
	printTitle("Variable Shadowing");
	int outter{5};
	cout << "outter: " << outter << endl;
	{
		cout << "Enter inner block" << endl;
		int outter{9};
		++outter;
		cout << "outter: " << outter << endl;
	}
	cout << "Exit inner block" << endl;
	cout << "outter: " << outter << endl;
}

extern const int ecg;
extern int g_x;
// this will give linking error because the static function defined in other file has internal linkage
void internalLinkage();
void externalLinkage();
void internalLinkageEg()
{
	printTitle("External Linkage");
	cout << "g_x defined in linkage.h: " << g_x << endl;
	cout << "ecg defined in linkage.h: " << ecg << endl;
	cout << "externalLinkage() function defined in linkage.h" << endl;
	externalLinkage();
	// this will give linking error because the static function defined in other file has internal linkage
	// internalLinkage();
}

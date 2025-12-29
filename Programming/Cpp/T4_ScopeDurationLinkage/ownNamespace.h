namespace foo
{
	int doSomething(int a, int b)
	{
		return a + b;
	}
	namespace fgoo
	{
		int doSomething(int a, int b)
		{
			return a * b;
		}
	} // namespace fgoo

} // namespace foo

namespace boo
{
	int doSomething(int a, int b)
	{
		return a - b;
	}
} // namespace boo

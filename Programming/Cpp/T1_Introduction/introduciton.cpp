#include <array>
#include <iostream>
#include <string_view>
#include <tuple>
#include <type_traits>
#include "add.h"
#include "math.h"

void StandardTesting();
void Initialization();
void iostreamTest();
void compileMultipleFiles();
namespace a::b::c
{
    inline constexpr std::string_view str{"hello"};
}

template <class... T>
std::tuple<std::size_t, std::common_type_t<T...>> sum(T... args)
{
    return {sizeof...(T), (args + ...)};
}

int main()
{
    StandardTesting();
    Initialization();
    iostreamTest();
    compileMultipleFiles();
    return 0;
}

inline void StandardTesting()
{
    std::cout << "Testing compiler capability level..." << std::endl;
    auto [iNumbers, iSum]{sum(1, 2, 3)};
    std::cout << a::b::c::str << ' ' << iNumbers << ' ' << iSum << '\n';

    std::array arr{1, 2, 3};

    std::cout << std::size(arr) << '\n';
}

inline void Initialization()
{
    std::cout << "Topic: Initialization..." << std::endl;

    int uninitialized;
    std::cout << "Value of uninitialized: " << uninitialized << std::endl;
    std::cout << "Value of operation on uninitialized: " << uninitialized + 2 << std::endl;

    int directInitialization[]{5, 25};
    for (int i = 0; i < 2; i++)
    {
        std::cout << directInitialization[i] << std::endl;
    }
    int directzBraceInitilaization{4};
}

inline void iostreamTest()
{
    std::cout << "Topic: iostreamTest..." << std::endl;
    std::cout << "Enter a number:\n";
    int x{};
    std::cin >> x;
    std::cout << "You entered " << x << std::endl;
}

inline void compileMultipleFiles()
{
    std::cout << "Compiling Multiple files..." << std::endl;
    std::cout << add(3, 5) << std::endl;
}

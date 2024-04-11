We can define an interface target with necessary requirements, and have sub libraries or top level project to satisfy the requirements defined by the interface, such as c++ version etc.

Define the interface library
`add_library(ILibName INTERFACE)`:
	- `add_library(tutorial_compiler_flags INTERFACE)`
`target_compile_features(libName INTERFACE cxx_std_11)`


Then we can use the new `ILibName` across CMakeLists to specify the required c++ version to build each library:
At top level CMakeLists:
`target_link_libraries(ProjName PUBLIC Lib1Name ILibName)`: specifies that Lib1Name should use the c++ version specified by ILibName:
	-`target_link_libraries(Tutorial PUBLIC MathFunctions tutorial_compiler_flags)`

At sub libraries' CMakeLists:
`target_link_libraries(SubLibName PUBLIC ILibName)`: specifies that this library should use the c++ version defined in ILibName:
	-`target_link_libraries(SqrtLibrary PUBLIC tutorial_compiler_flags)`

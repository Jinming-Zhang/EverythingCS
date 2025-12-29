## Commands required for every project
- `cmake_minimum_required`: cmake version is relevant for supported c++ version to compile.
	- `cmake_minimum_required(VERSION 3.10)`
- `project`: project name and version etc.
	- `project(FurryWolfEngine VERSION 1.0)`
- `set(CMAKE_CXX_STANDARD 17)` and `set(CMAKE_CXX_STANDARD_REQUIRED True)`: set c++ version and requirements
- `target_include_directories`: sets the include directories to build the final executable
	- `target_include_directories(FurryWolfEngine PUBLIC "${PROJECT_BINARY_DIR}")`
- `add_executable`: all the source files that needs to be compiled
	- `add_executable(FurryWolfEngine engine.cpp)`
	
## Config header file
config header files can be used to expose variables in CMakeLists file to source code.
`configure_file(TutorialConfig.h.in TutorialConfig.h)`
Where `TutorialConfig.h.in` is the input file that contains the variables to be replaced.

`@Tutorial_VERSION_MAJOR` and `@Tutorial_VERSION_MINOR` are automatically created by CMake when specifying the version number with `project` command.

Inside the input file, we use the macro to define the corresponding variables for CMake to replace:
```cpp
# define Tutorial_VERSION_MAJOR @Tutorial_VERSION_MAJOR@
# define Tutorial_VERSION_MINOR @Tutorial_VERSION_MINOR@
```

Then we can include the output header file template in the source code and use the variable.

```cpp
#include "TutorialConfig.h"
if (argc < 2) {
// report version
std::cout << argv[0] << " Version " << Tutorial_VERSION_MAJOR << "."
		  << Tutorial_VERSION_MINOR << std::endl;
std::cout << "Usage: " << argv[0] << " number" << std::endl;
return 1;
}
```
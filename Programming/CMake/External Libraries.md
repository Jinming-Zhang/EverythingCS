
## Extern Libraries
We can organize part of our source code files (or third party library source code files) into their own directory, with each of them has its own CMakeLists file. Then we can specify the dependencies at the top level CMakeLists file.

<hr>

#### Changes on library directory CMakeLists
- `add_library(LibName, SrcFiles...)`: specify the source files to make up a library, this is used in the CMakeLists file inside the **library directory**
	- `add_library(MathFunctions MathFunctions.cxx mysqrt.cxx)`
	
#### Changes on Top Level CMakeLists

- `add_subdirectory(LibName)`: used at **Top Level** CMakeLists file to add the subdirectory of the library to the build.
	- `add_subdirectory(MathFunctions)`
	
- `target_link_libraries(TargetName [...] LibName)`: links the library with the project
	- `target_link_libraries(Tutorial PUBLIC MathFunctions)`
	
- `target_include_directories()`: at the **Top level** of the CMakeLists, add the include directories for the libraries as well. The path can be relative to the source directory
	- `target_include_directories(Tutorial PUBLIC "${PROJECT_SOURCE_DIR}/libraryIncludeDirectires"`
<hr>
## Option (CMake Variables)
we can use the `option(MacroName "description" ON)` command at the **library level CMakeLists** to define macros that can be used in source code.

`option(MacroName "description" ON)`:
- `option(USE_MYMATH "Use tutorial provided math implementation" ON)`

next, we'll need to check in CMakelists to see if the option is selected by using the `if()` command,  and define the macro accordingly:
``` cmake
if(USE_MYMATH)
  target_compile_definitions(MathFunctions PRIVATE "USE_MYMATH")
endif()
```

## Add sublibraries in same directory for different building options

Inside the same library directory, we can use the same CMakeLists file to separate which source code should be included in the build based on the flag provided from CMake.

1. update the `add_library()` command to exclude sub-library code
2. when the option is on, add the sublibrary's source code using `add_library(libName STATIC srcFiles)` and `target_link_libraries(ThisLibName PRIVATE tarLibName)`:

updated CMakeList:
```cmake
if(USE_MYMATH)
  target_compile_definitions(MathFunctions PRIVATE "USE_MYMATH")
  add_library(sqrtLibrary STATIC mysqrt.cxx)
  target_link_libraries(MathFunctions PRIVATE sqrtLibrary)
endif()
```


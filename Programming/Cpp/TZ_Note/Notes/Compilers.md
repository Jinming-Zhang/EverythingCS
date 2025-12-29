## Include header files searching directory for linker
```
g++ -o program -I/path/to/directory *.cpp
```

Each c++ source file needs to be compiled into an object file, then object files then are linked into an executable, a shared libarary, or a static libaray(archive of object files).

Only source files(\*.cpp) are passed to the compiler. Header files are not passed to the compiler, they are included from source files using *#include* directive.

Preprocessor will take the source files and turn them into translation units. We can obtain the translation unit(preprocessed source code) with -E and -o option for g++ compiler.
>g++ -E main.cpp -o main.o

Usually compiler only needs [[Glossary#Declaration vs Definition|`declaration`]]  for compiling the file, and expecting linker can find the [[Glossary#Declaration vs Definition|`definition`]] from another file. If no source file ever defines a symbol, but it's declared, we will get errors at link time complaining about undefined symbols.
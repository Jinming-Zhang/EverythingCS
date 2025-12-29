Build with source folder and build folder
`cmake -S ./srcDir -B ./buildDir`
Build with options (note the -D prefix followed by the actual macro)
`cmake -S ./srcDir -B ./buildDir -DOptionMacro=Value`
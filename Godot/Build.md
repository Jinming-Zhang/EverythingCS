# Build Command
1. With Scons installed, the build command for `dev`, `vsproj` and `c# support` is:
	-`scons.exe platform=windows dev_build=yes vsproj=yes module_mono_enabled=yes`

2. After built the .Net-enabled Godot editor, use it to generate some of the source codes for the managed (c#) library:
-  `godot.exe --headless --generate-mono-glue modules/mono/glue`

1. Create  folder for managing local Nuget Libraries for .Net
	-`dotnet nuget add source ./MyLocalNugetSource --name MyLocalNugetSource`
2.  Generate the managed libraries:
	- `./modules/mono/build_scripts/build_assemblies.py --godot-output-dir=./bin --push-nupkgs-local MyLocalNugetSource`
	
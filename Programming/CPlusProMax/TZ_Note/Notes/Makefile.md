## Makefile
### makefile target
makefile consists of a set of targets, each target has the folowing syntax:
```
target1: prerequisites # optional list of targets
	command # must be leading tab
	command
	...
target2: prerequisites
	command
	command
	...
```

Target examples:
```
begin:
	echo "hello makefile"
```

```
clean:
	rm *.exe *.o
```

we can call make on different targets defined in makefile
```
make target1
make clean
```

when no target is provided, make will run the first target in makefile.
```
make
```
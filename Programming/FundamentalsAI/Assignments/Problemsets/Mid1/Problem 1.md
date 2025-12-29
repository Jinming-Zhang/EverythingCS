Representing the states by three-tuple (N, E, B), which means there are N northerners, E easterners and B boat on the Left side of the river bank.

### a)
- Initial state:
	- (3,3,1)
- Actions and Successor Function:
	- Moving from left to right:
		- (N-1, E, 0), moving 1 northerner to right side
		- (N-2, E, 0), moving 2 northerner to right side
		- (N, E - 1, 0), moving 1 easterner to right side
		- (N, E - 2, 0), moving 2 easterner to right side
		- (N -1, E - 1, 0), moving 1 northerner and 1 easterner to right side
	- Moving from right to left:
		- (N+1, E, 1), moving 1 northerner to left side
		- (N+2, E, 1), moving 2 northerner to left side
		- (N, E + 1, 1), moving 1 easterner to left side
		- (N, E + 2, 1), moving 2 easterner to left side
		- (N +1, E + 1, 1), moving 1 northerner and 1 easterner to left side
- Goal test:
	- (0, 0, 0)
- Path cost:
	- Each action cost 1

### b)
Possible states are the states where northerners not out numbered by easterners if northerners >=1
- boat on the left:
	- (3,3,1)
	- (3,2,1)
	- (3,1,1)
	- (3,0,1)
	- (0,3,1)
- boat on the right
	- (3,3,0)
	- (3,2,0)
	- (3,1,0)
	- (3,0,0)
	- (0,3,0)
### c)
Action sequence: 
1. (3,3,1) -> Move 1 N and 1 E to the right
1. (2,2,0) -> Move 1 E to the left 
1. (3,2,1) -> Move 2 E to the right
1. (3,0,0) -> Move 1 E to the left
1. (3,1,1) -> Move 2 N to the right
1. (1,1,0) -> Move 1 N and 1 E to the left
1. (2,2,1) -> Move 2 N to the right
1. (0,2,0) -> Move 2 E to the left
1. (0,3,1) -> Move 2 E to the right
1. (0,1,0) -> Move 1 E to the left
1. (0,2,1) -> Move 2 E to the right
1. (0,0,0) reach goal state


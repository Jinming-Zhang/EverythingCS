Dynamic programming applies when the subproblems overlap (when subproblems share subproblems).
Dynamic programming solves each subproblem just once and then saves/cache the result in a table, thereby avoiding duplicated calculations.

## Optimal Substructure
The types of problems that the optimal solution to the problem incorporate optimal solutions to related subproblems, which we may solve independently.

## Steps for developing dynamic programming algorithm
1. Characterize the structure of an optimal solution
2. Recursively define the value of an optimal solution
3. Compute the value of an optimal solution, typically in a bottom-up fashion
4. Construct an optimal solution from computed information

## Subproblem Graph
Identify the set of subproblems involved and how subproblems depend on one another.

## Approaches
##### Bottom-up Approach
Start knowing how to solve a problem for a simple case.
Then figure out how to solve the problem for two elements and so on.

> Key: Think about how to build a solution for one case off of the previous case, and be careful of overlap between the cases.

##### Top-down Approach / Memoization
Think about how we can divide the problem for case N into subproblems.
##### Half-half Approach
Think about how we can divide the data set in half.
Examples include binary search, merge sort, etc..

## Dynamic Programming
The key idea of dynamic programming:
> Taking a recursive algorithm, identifying the overlapping subproblems (*repeated calls*), and **cache the results for future recursive calls**.

### Example
##### Fibonacci
Here is a intuitive recursive function for calculating Fibonacci numbers, which has a run time complexity of $O(2^n)$
```python
def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)
```
Note how we can compute fib(n) from the previous results / subproblems.
That's where we can cache the result to avoid duplicated computation:

###### Top-down approach
```python
def fib(n:int, memo:List[int])->int:
	# base case stays the same, but we cache the result
	if n == 0 or n == 1:
		memo[n] = n
		return n
	# then we check if there is a cached result first before calculating
	if memo[n] == 0:
		memo[n] = fib(n-1, memo) + fib(n-2, memo)
	return memo[n]
```

Notice that this is a *Top-down* approach since after we cached the base case, we start from the expected value, and cascade the function calls all the way down to the base, then use the cached value to traverse back up to the tree to get the result.
###### Bottom-up approach
```python
def fib(n: int):
    if n == 0 or n == 1:
        return n
    cached: List[int] = []
    cached.append(0)
    cached.append(1)
    for i in range(2, n+1):
        cached.append(cached[i-1] + cached[i-2])
    return cached[n]
```
Similar to top-down approach ,we first calculate the results for the base case.
 This is a *Bottom-up* approach because we are calculating the result from smaller number to the target number, and utilizing the cached result along the way.
 
 Also notice that we actually only need to store two values through out the *bottom-up* process, so the algorithm can be simplified further.
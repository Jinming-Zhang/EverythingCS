# Jinming Zhang
# Problem #2
## a)
#### BFS
1->2->3->4->5->6->7->8->9->10->11->12->13->14->15->16->17->18.

#### DFS
Assume depth at lv 0 is 0, then a solution can be found using depth limit search: 1->2->4->8->16->17->9->18

## b) and c)
#### Algorithm for generating the path of number n
```
GetPath(N){
	1. calculate binary presentation of number n
	2. discard the left-most `1` in the result
	3. then from left to right:
		if the digit is `1`
			add Right to the path
		if the digit is `0`
			add Left to the path
	return path
}
```
In the case of n = 2022
1. f(2022) = 111, 1110, 0110 (2022 in binary)
2. discard the left most 1, we left, 11, 1110, 0110
	from left to right,  0 represent Left,  1 represent Right
3. Path to 2022 will be \[Right, Right, Right, Right, Right, Left, Left, Right, Right, Left\]

The time complixity of the algorithm:
$$O(log(n))$$
number **n** will have a path of length log(n).
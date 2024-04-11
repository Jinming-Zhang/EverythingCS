### Problem
Given a rod of length i, and a table that shows the prices of the rod of each length, find the optimal revenue of the rod and how to cut it.

### Analysis
For a given rod of length n, there is a total number of $2^{n-1}$ possible ways to cut the rod, for example, for each length unit i, we can decide if we should cut the rod at that position.


### Simple Solution
Given a rod of length n, let r_n be the optimal revenue can get from cutting that rod,  then we can define that $r_n = max(p_n, r_1+r_{n-1}, r_2+r_{n-2},...,r_{n-1}+r_n)$ 
which means the optimal revenue of (uncutted, cut at first unit, cut at second unit, etc...)

A simple solution to the problem would be loop through the unit, calculate the max revenue of cut the rod at the unit plus the 

### Steps to develop dynamic programming algorithm
1. Characterize the structure of an optimal solution
2. Recursively define the value of an optimal solution
3. Compute the value of an optimal solution, typically in a bottom-up fashion
4. Construct an optimal solution from computed information
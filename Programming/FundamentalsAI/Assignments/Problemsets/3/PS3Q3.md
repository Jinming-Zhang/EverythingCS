# Jinming Zhang
## Problem #3
### a)
$f(4)$ is a constraint optimization problem because it can be modelled in the following way:
1. Variables: Each cell in the board
	- $C_{i,j}$, where $i,j \subseteq [1,n]$
2. Domains: 0,1, with 1 means the cell has a knight, 0 means an empty cell
	- $D_{i,j}\subseteq[0,1]$
3. Constraints: No knight attachs each other.
	 - Suppose a knight is at cell $(i, j)$, i.e. the $C_{i,j}=1$
	- Then the value of following cell should be 0:
		1. $C_{i-2,j+1}$, $C_{i-1, j+2}$. (top-left region)
		2. $C_{i+1, j+2}$, $C_{i+2, j+1}$. (top-right region)
		3. $C_{i-1, j-2}$, $C_{i-2, j-1}$. (bottom-left region)
		4. $C_{i+1, j-2}$, $C_{i+1, j-1}$. (bottom-right region)
1. Objective function: Sum of all cells' value on the board.
	- $\sum_{i=1}^n \sum_{j=1}^n C_{i,j}$

### b)
(solution from weekly workshop)
To prove that 8 is the maximum number of knights can be placed on a $4\times 4$ board by showing that 9 knights are imposible.
Coloring the $4\times 4$ board as follows:

$$
  \left[\begin{array}{|rrrr|}
    \color{red}{口} & \color{green}{口} & \color{blue}{口}  & \color{cyan}{口} \\
    \color{blue}{口} & \color{cyan}{口}  & \color{red}{口}  & \color{green}{口}  \\
	    \color{green}{口} & \color{red}{口} & \color{green}{口}  & \color{blue}{口}  \\
	\color{cyan}{口} & \color{blue}{口} &  \color{cyan}{口} & \color{red}{口} \\
  \end{array}\right]
$$
Notice that at most 2 knights can exist among grids of the same color, otherwise two knights will attach each other.
Since the four colors filled the $4\times 4$ board, it's impossible to have more than 8 knights in the same $4\times 4$ board.
### c)
(solution from weekly workshop)
Based on the prove in b), we can conclude that in a $n\times n$ board, where n is a multiple of 4, the maximum number of knights can be placed on the board so that no knights attack each other is:
$$f(n) = (\frac{n}{4})^2 \times 8$$
This is because if we duplicate the coloring of the $4\times 4$ board 4 times to make a $8\times 8$ board, it's easy to show that the whole $8\times 8$ board can not have more than $8\times 4$ knights that do not attack each other, since any extra knight has to be one of the $4\times 4$ sub-board and since violates what we have proved in b).

In the case of n = 444444, $f(444444) = \frac{444444^2}{16}\times 8 = \frac{444444^2}{2}$
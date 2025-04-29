# Jinming Zhang
## Problem #1

### a)
Sudoku is a CSP because because we can model Sudoku into a CSP as follows:
- Variables: Each cell in the sudoku board
- Domain: Each variable has the same domain {1-9}
- Constraints: No empty cell in the board, and the digit in each row, column, and the $3\times3$ sub-board should be distinct.

### b)
- The number of conflicts for each row and column are ${9 \choose 2}=36$.
- Since the row and column conflicts are calculated in the above case, the number of conflicts for each $3\times 3$ sub-board are the ones on diagonals,3 for each diagonal.  

The total number of conflicts in a $9\times 9$ Sudoku board is
$36 \times 18 + 6\times 9 = 702$

### c)
The Sudoku problem can be seen as a graph coloring problem in a way that
1. Define the graph with nodes and edges described in b)
2. Variables will be each node in the graph
3. Domains wil be 9 different colors
4. Constraints will be the nodes connected by each edge cannot have the same color.
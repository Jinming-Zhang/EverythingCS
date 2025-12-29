# Jinming Zhang

## Problem #1

### a). Determining the shortest path from your favourite restaurant in Vancouver to the Northeastern Vancouver campus. 

- Initial State
	- Location of Northeastern Vancouver Campus
- Actions
	- All the roads available
- Transition Model
	- The roads can take at each location and the location that each road leads to.
- Goal Test
	- If the location is favourite restaurant
- Path Cost
	- Time takes, calorie consumption (uphill/downhill), transit fair (if applicable)
	
### b). Solving a jumbled 3 × 3 × 3 Rubik’s Cube in the minimum possible number of moves.

- Initial State
	- The Rubik's cube
- Actions
	- Rotate each side of the cube plus the 3 sides in the middle
- Transition Model
	- The available rotations and the new cube each rotation leads to
- Goal Test
	- If each side of the cube has the same color
- Path Cost
	- Number of actions taken to get to restore the cube
	
### c). Completing a (partially-filled) Sudoku puzzle and obtaining the (unique) solution.

- Initial State
	- A partially filled sudoku board
- Actions
	- Fill one empty grid onr change one already filled grid with an integer from 1-9
- Transition Model
	- The new sudoku board after each action
- Goal Test
	- If the board is filled with number 1-9 and all the columns, rows diagonals and each sub 3x3 grid doesn't contain duplicated digit.
- Path Cost
	- The number of action/try taken to reach the final goal
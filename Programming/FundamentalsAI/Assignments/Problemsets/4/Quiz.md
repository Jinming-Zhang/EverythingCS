# Jinming Zhang
## Question #1
15,7
## Question #2
7.2
## Question #3
Unless we know the upper and lower bound value of the terminal nodes, non of the branch can be pruned
## Question #4
Let player X be the player we try to maximize.

On terminal states:
- if the board has 3 consecutive X in rows/columns/diagonoals (X is the winner), return 100
- if the board has 3 consecutive O in rows/columns/diagonoals (X is the loser), return -100

On non-terminal states:
- return (the number of consecutive X) - (the number of consecutive O)
## Question #5
> Stretegy: Only play one turn

Some note:
Probability of having 1 in at least one dice = $\frac{11}{36}$
Probability of winning in a single toss = $\frac{25}{36}$
Let a random variable X be the number of tosses until first lose occurs, then X is a discrete geometric random variable, with winning probability:
0.7 at toss 1
0.2 at toss 2
below 0.1 at toss 3
Also  the expected gain if not lose at each tose = ((4+5+6+7+8)+(5+6+7+8+9)+(6+7+8+9+10)+(7+8+9+10+11)+(8+9+10+11+12)) \* (1/36) =  5.55555
The most rational decision will be only play one turn.
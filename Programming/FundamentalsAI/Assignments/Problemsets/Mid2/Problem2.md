### a)
Payoff function for Rose:
Payoff $= 0\cdot p_1\cdot p_2+x\cdot p_1\cdot r_2+(-z)\cdot p_1\cdot s_2$
$+ (-x)\cdot r_1\cdot p_2+x0\cdot r_1\cdot r_2+(-z)\cdot r_1\cdot s_2$
$+ z\cdot s_1\cdot p_2+(-y)\cdot s_1\cdot r_2+0\cdot s_1\cdot s_2$

=$x\cdot p_1\cdot r_2-z\cdot p_1\cdot s_2$
$-x\cdot r_1\cdot p_2+y\cdot r_1\cdot s_2$
$+z\cdot s_1\cdot p_2-y\cdot s_1\cdot r_2$

With Colin's strategy, the payoff function for Rose will become:
Payoff $=-0.01\cdot r_1+0.01\cdot s_1$
So Rose's stradegy will be choose Scissors every time.

### b)
When x=y=z=1,  payoff for Rose is:
$p_1\cdot r_2-p_1\cdot s_2$
$-r_1\cdot p_2+r_1\cdot s_2$
$+s_1\cdot p_2-s_1\cdot r_2$
- When Colin pick paper everytime, $p_2=1$, Rose's payoff is $-r_1+s_1$
- When Colin pick rock everytime, $r_2=1$, Rose's payoff is $p_1-s_1$
- When Colin pick scissors everytime, $s_2=1$, Rose's payoff is $-p_1+r_1$
- Also $p_1+r_1+s_1=1$

We'll get 3 equations:
	a). $2\cdot s_1-r_1-p_1=0$
	b). $2\cdot p_1-s_1-r_1=0$
	c). $p_1+r_1+s_1=1$
And by solving the equations, we'll get
	- $p_1=\frac{1}{3}$
	- $r_1=\frac{1}{3}$
	- $s_1=\frac{1}{3}$

Since this is a zero-sum game, same goes for Colin.
Therefore, at Nash Equilibrium, both players will play rock, paper scissors randomly with equal probability.
This makes sense because the reward for winning with paper, rock, scissors are the same, so there is no preference for both players to win the game with a specific choice, and they'll play randomly.

### c)
When x=1, y=2, z=3,
#### Nash Equilibrium for Rose
Payoff for Rose is:
$p_1\cdot r_2-3\cdot p_1\cdot s_2$
$-r_1\cdot p_2+2\cdot r_1\cdot s_2$
$+3\cdot s_1\cdot p_2-2\cdot s_1\cdot r_2$
- When Colin pick paper everytime, $p_2=1$, Rose's payoff is $-r_1+3\cdot s_1$
- When Colin pick rock everytime, $r_2=1$, Rose's payoff is $p_1-2\cdot s_1$
- When Colin pick scissors everytime, $s_2=1$, Rose's payoff is $-3\cdot p_1+2\cdot r_1$
- Also $p_1+r_1+s_1=1$

We'll get 3 equations:
	a). $5\cdot s_1-r_1-p_1=0$
	b). $2\cdot p_1-s_1-r_1=0$
	c). $p_1+r_1+s_1=1$
And by solving the equations, we'll get
	- $p_1=\frac{1}{3}$
	- $r_1=\frac{1}{2}$
	- $s_1=\frac{1}{6}$
	
#### Nash Equilibrium for Colin
Since the game is zero sum and Colin's situation is same as Rose, therefore at Nash Equilibrium, Colin's strategy will be same as Rose:
	- $p_2=\frac{1}{3}$
	- $r_2=\frac{1}{2}$
	- $s_2=\frac{1}{6}$
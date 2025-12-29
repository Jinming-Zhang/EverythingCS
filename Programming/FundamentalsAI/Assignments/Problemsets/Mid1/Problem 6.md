### a)
When both players play optimally, player with a multiple of 3 coins left is guarenteed to lose and the other player is guarenteed to win. So the optimal value of v(n) = -1 when n is a multiple 3, and 1 other wise.

### b)
When Max moving first:
$v(1)= 1$
$v(2)= 1$
$v(3)=\frac{1}{2}$
$v(4)=1$
$v(5)=1$
$v(6)=(\frac{1}{2})^2$

### c)
##### Case 1:
When the number of coins left for Max is not a multiple of 3,  Max is guarenteed to win when play optimally.

##### Case 2:
When the number of coins left for Max is a multiple of 3,  the win rate is purely based on how Minnie plays the game.

Suppose at Max's turn, the number of coins left is $3n$:
- If Max took 1 coin, the number of coins left to Minnie is $3n-1$
	- If Minnie took 1 coin, then Max is guarenteed to win the game. (P=0.5)
	- If Minnie took 2 coin, then Max is back to the same state as before. (P=0.5)
- If Max took 2 coins, the number of coins left to Minnie is $3n-2$:
	- If Minnie took 1 coin, then Max is back to the same state as before. (P=0.5)
	- If Minnie took 2 coin, then Max is guarenteed to win the game. (P=0.5)

> Regardless of Max's action, Minnie has a $\frac{1}{2}$ chance to make a mistake and lose the game at each action.

For Max:
- $v(n)=1$, when n is not a multiple of 3, 
- $v(n)=1\times P(\text{Max win}) + -1\times P(\text{Minnie win}) =1-2\times(\frac{1}{2})^\frac{n}{3}$, when n is a multiple of 3.
	- $\frac{1}{2}^\frac{n}{3}$ is the probability that Minnie wins the game (i.e. choose correct number of coins at every turn.).
	- $1-\frac{1}{2}^\frac{n}{3}$ is the probability that Max wins the game.

Therefore, **when n=33**, the probability for Minnie to win the game is $\frac{1}{2}^\frac{33}{3} = \frac{1}{2048}$.
$v(33) = 1 - 2\times P(\text{Minnie win}) = 1-\frac{1}{1024}\approx 0.999023$, which is greater than 0.999 and less than 1.
# Problem #3
### a)
$V^*_{k+1}=\sum T(s,a,s')\cdot [R(s,a)\cdot \gamma V_{k}^*(s)]$
Based on the rule, there are 3 possible outcomes of the game
1. Before the game ends, the payoff is always 0
2. The point is exactly the target score, the payoff is the score
3. The point is more than the target score, the payoff is 0

And two possible actions:
1. Play until win or lose
2. Stop and lose immediately

So the optimal value at state s at iteration k+1 will be the best possible outcomes among the 3 options:
1. Stop at iteration k, and based on the value, get 0 or n points.
2. Play and get a head with $\frac{1}{2}$ chance, and ends up in a state with a value 2 more than current state
3. Play and get a tail with $\frac{1}{2}$ chance, and ends up in a state with value of 1 more than current state

Therefore, at any iteration, the optimal solution for a state will be the best among these 3 options.

### b) and c)
Since there are only two states of the game: we either get 0 point or win the game with n points, and winning the game is the only way to get a positive payoff.

So the value of $V^*(0)$ is same as $P(\text{winning the game})\cdot n$

#### To find the probability of winning the game with n points
Let P(n) be the probability of winning a game with n points.
Since to lose the game, we need to first get to n-1 points and toss a head, so we can say that the probability of losing a game with n points is:
$$P(n)=1-\frac{1}{2}\cdot P(n-1)$$
We can expand this and get the following:
$P(1)=\frac{1}{2}$
$P(2)=1-\frac{1}{2}\cdot (\frac{1}{2})=1-\frac{1}{4}$
$P(3)=1-\frac{1}{2}\cdot (1-\frac{1}{4})=1-\frac{1}{2}+\frac{1}{8}$
$P(4)=1-\frac{1}{2}\cdot (1-\frac{1}{2}+\frac{1}{8})=1-\frac{1}{2}+\frac{1}{4}-\frac{1}{16}$
...
$P(n)=1+\frac{(-1)}{2}+\frac{(-1)^2}{2^2}+\frac{(-1)^3}{2^3}+...+\frac{(-1)^{n-2}}{2^{n-2}}+\frac{(-1)^{n+1}}{2^n}$

Which is $1+\frac{(-1)^{n+1}}{2^n}-\sum_{i=1}^{n-2} (-\frac{1}{2})^i$, for n>2

#### When n = 5
$V^*(0)=P(5)\cdot 5 = 0.65625\cdot 5=3.28125$

#### When n = 1000000000
Also as n approach to $+\infty$:
1. the term $\sum_{i=1}^{n-2} (-\frac{1}{2})^i$ converges to $\frac{1}{3}$, (sum of geogetric series)
2. the term $\frac{(-1)^{n+1}}{2^n}$ approaches to 0

So $P(1000000000)=1+0-\frac{1}{3} = \frac{2}{3}$ and $V^*(0)=\frac{2000000000}{3}$
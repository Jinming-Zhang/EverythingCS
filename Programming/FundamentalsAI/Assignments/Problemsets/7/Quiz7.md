## Question #1
#### Value Iteration
Initialize each state with value zero and some final value at terminal states, compute each states' optimal expected value by propagating the value from the terminal states.

#### Policy Iteration
Starting from current state, compute the optimal policy for each sub-states by recursively computing the expected outcome of each action and possible result states, then make the action that results in highest expected value be the optimal policy for each state.

## Question #2
N= 4
When the score is 4 or more, stop playing

## Question #3
$$V_{k+1}(s)=max(s, \frac{V_{k}(S+1)+V_k(S+3)}{2})$$

$V^*(0) = 2\times \frac{1}{2} + \frac{15}{4} \times \frac{1}{2} =2.875$

## Question #4
A is true.
## Question #5
Favour to the Chris, the person roll the dice second.
- If Bob chose Dice X, Chris has a win rate higher than 1/2 based on the result of Bob
- Same as if Bob chose Dice Y.
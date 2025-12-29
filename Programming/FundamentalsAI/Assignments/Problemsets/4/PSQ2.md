# Problem #2

### a)
Since the sum of a geometric seris $\sum{ar^k}$, and when $|r|<1$, the sum is a finite number $\frac{a}{1-r}$.

In Bellman equation, $V^*_{k+1}=\sum T(s,a,s')\cdot [R(s,a)\cdot \gamma V_{k}^*(s)]$, since each reward is constant, then there exist some constant c, that it's greater than the sum of all rewards.

Therefore, it can be expressed as the sum of some  constant $c$, and $\gamma \cdot V_{k}^*(s)$
then we'll have $c + \gamma \cdot \gamma^2 \cdot \gamma ^3 \cdot ...\cdot \gamma ^k\cdot V^*(0)$

Since $0 \lt \gamma \lt 1$, so $\gamma \cdot \gamma^2 \cdot \gamma ^3 \cdot ...\cdot \gamma ^k$ is a geometric series with constant a =1, and a common ratio $\gamma$, and the final value of $V_k^*(s)$ will converge to a constant $\frac{1}{1-\gamma}$
  
### b)
Since in policy iteration, the best policy is based on the value of $V^*(s)$, 
$\pi_{k+1}(s) = argmax_a\sum_{a}T(s,a,s')\cdot V^*(s)$
so if the value iteration converged, policy iteration must also converged.

However, policy iteration is coverged doesn't imply that value iteration is converted.
Taking Nick's solution as an example:
![[Pasted image 20221102142555.png]]
The policy converged at iteration 4,  whereas values converged at iteration 6

### c)
Based on the proof of a), as long as the discount factor is between (0,1), the result of the value iteration will converge to a constant.
Since the only difference between to MDPs are the discount factor, this means the final value of the two MDPs will be converged into two slightly different values, with a factor of $\frac{1}{1-\gamma_1}$ and $\frac{1}{1-\gamma_2}$ respectively.
Since the value of two MDPs only differ linearly, the best policy  extracted from the two MDPs should be the same, which means $\pi_1(s) =\pi_2(s)$
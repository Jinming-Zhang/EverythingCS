### a)
$V^*_{k+1}=\sum T(s,a,s')\cdot [R(s,a)\cdot \gamma V_{k}^*(s)]$
Since at each state we have two options: Play and Stop, we'll end up into two different states:
- When stop, we get whatever we have at the current state.
- When play, we'll get the expected value from the two possible outcomes, with $\frac{1}{6}$ chance of getting 3 more points and $\frac{5}{6}$ chance of getting 1 more points.

Therefore the optimal value at each step will be the optimal value among current state, and the expected value of keep playing.

### b)
$V^*(0)=5\cdot \frac{5}{6}\cdot \frac{5}{6} + 5\cdot \frac{5}{6}\cdot \frac{5}{6} +5\cdot \frac{5}{6}\cdot \frac{5}{6} + 5\cdot (\frac{5}{6})^5\approx 3.745$
The optimal policy would be keep playing until get 4 dollors.

### c)
| State | Stop | Play  |
|-------|------|-------|
| 0     | 0    | 3.745 |
| 1     | 1    | 3.8   |
| 2     | 2    | 3.727 |
| 3     | 3    | 3.472 |
| 4     | 4    | 4.166 |
| 5     | 5    | 0     |


# Problem #5
## a) 
#### Solution Path using h1:
![](https://lh4.googleusercontent.com/t5atWlV4cZv5GNGh5MPYranswVUKnfyTzl-HXcLFaN6QniS9O5Tb6SZnOGFASUg_NzVKruXE5qUlry9ayDcvNsOVKo6C77LydBYJ4mUz6ry9CAeRy8Ia9AEB3aUge82CVBPkXT6lufpKBujdrY2Sy5-4p9gFbX0fuqfATkjrHvUvEObQwGGUHRihyw)

#### Solution Path for h2: 
Very similar to h1 but expands less node
![](https://lh5.googleusercontent.com/wGl4hv6DOeuplUatr7aLHT9eX9vNgb0h9FyIHd2UMXy2PYdVDdCN6a9W_D45RpGeuhgb7OqeoGgpjZZz4Njeae_7LpozEvTkyzNFV_4yVSFJruVWsd4kRDg89je9Mi91lUNGiC7bKHCiKbEmMSKYaqcWo8PvpWa185lEqY6CvWnKKghdaV6Mta3SyQ)
## b)

#### Admissibility:
For each step, we can only move 1 block, for h1, we need to move at least $h_{1}$  moves in each state, so $h_1$ is guaranteed not more than the actual steps.
For h2,  as we need to at least move back all the paces back, so this value is guaranteed not more than the actual steps as well.
Therefore h1 and h2 are all admissible.

#### Consistency:
Since each step cost 1, for h1 and h2 to be consistent, it means at each state n and the successors of n, n' need to satisfy:
$$h(n)\le 1+h(n') $$

Because we can only move one tile at a time, the result of each action at each state is either 1 step closer to the goal or 1 step further to the goal. In both cases, the heuristic of the resulting state is still no lesser than the heuristic of current state plus 1.

#### Better heuristics
In general, if two heuristics are both consistent, then the one that returns a larger value is a better heuristic.

*From text book page 104:*
Nodes with f (n) < C ∗ will surely be expanded.
Since in A\*, f(n) = g(n) + h(n), so nodes with heuristic that satisfies:
$$h(n) \lt C*- g(n)$$
are surelly expanded by A\*.
Heuristic return lower value means more node code satisfy the equition and be expanded. So heuristic that returns a larger value will never expands nodes more than using heuristic that return a smaller value.

In this case, `h2 is better than h1`.

## c)
By proving  `each movement of the blank tile can only change the score either +2, -2, or 0`, we can solve both questions.

1. Since the goal state as a score of 0, we can say that
	- 41372586 is solvable because its score is even number
	- 41372568 is unsolvable because its score is an odd number.

2. Since for any state, its score is either odd or even, therefore half of the initial states out of 40320 are solvable (20160), and the other half are unsolvable (20160).


#### To prove each movement of the blank tile can only change the score either +2, -2, or 0
In any state of the game, we have 2 choices on how to move the blank tile:
1. Horizontally
2. Vertically

![](https://lh5.googleusercontent.com/wGiSqBhKB9ZHAjlFQ1QGtm5IDfmxU4fyxXVxUkms0lGTF_Zax0MmW11QjaG2MNO8CesCz4MTVO-Z_uIiYCIZyj6gBLvmapvtj0UVhs5VsLooBvIqUv7yDIv3M0iZWbemmmCbtsBQ2gu2LRteN971DG6SaI4phCQL7Q2RBWSamuLJSKCEXJSrC98E1Q)

#### Case 1:
It's easy to show that moving the tile horizontally doesn't change the score, it has no effect on the number sequence that obtained from the game state.

#### Case 2:
When the blank tile is moved vertically, it always swaps the blank tile with the number that is either 2 numbers before or after it.

Let A, B represent the two numbers in between, and $\alpha$ be the number that swapped with the blank tile, we have 3 possible scenarios before we move the blank tile vertically:
- Case 2.1:  $\alpha$ is less than both A and B
	- In this case, after the movement, the score will increase by 2, since both ($\alpha$, A) and ($\alpha$, B) will be in wrong order.
- Case 2.2:  $\alpha$ is greater than both A and B
	- In this case, after the movement, the score will decrease by 2 (oppsite situation as case 2.1).
- Case 2.3:  $\alpha$ is in between A and B
	- In this case, after the movement, the score will stay the same. Because before the movement, one of ($\alpha$, A) and ($\alpha$, B) is in wrong order, say ($\alpha$, A), and after the movement, ($\alpha$, A) will be in the right order, but ($\alpha$, B) will changed from right order to wrong order. So the total score stays the same.

#### The Brute Force way
Luyi has done a python program to calculate the number as the total permutation is limited.
![](https://lh6.googleusercontent.com/JNq-B3w_-dN3mx_JSqPRb3oYDjKY44GbfC_9q-JKIkH1iDUM2J7PKPI9il_204DilBgqiPKRQs_I3O-SA488QkcYCVwLWRHiQEmv2uA2J10X9xrAvFwZZ7MLwuXQRvv5kIsPsG98FoOJY9rLnM_RjEHpGLewI0chKobTaR5uE_omWSJa2wk-FDLH2Q)
With the result: 
![](https://lh6.googleusercontent.com/ZO_FpfWiOFhMcW8ZQuevISYWhSQ4gCl6im0cHgCoqLoeeQG2ckEhQKXBu4N5PHK4Oiis6jRgfjRzqii-kD0aDfDsjusbjfWdoLUoyrUQaXnZgVc9jY_wxVUML8Yu07rc0efm-0Wc_vS8J1veXxh3l9uwdIo5AMp4IFkPS4InH_gPM3vUBKrRV0qXUg)
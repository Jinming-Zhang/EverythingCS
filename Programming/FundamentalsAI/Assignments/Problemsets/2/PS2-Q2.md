# Jinming Zhang
## Problem #2
### a)
There are 2 solutions for 4 queens problem:
$$
  \left[\begin{array}{|rrrr|}
    口 & 👑 & 口 & 口 \\
    口 & 口 & 口 & 👑 \\
    👑 & 口 & 口 & 口 \\
    口 & 口 & 👑 & 口 \\
  \end{array}\right]
$$
And
$$
  \left[\begin{array}{|rrrr|}
    口 & 口 & 👑 & 口 \\
    👑 & 口 & 口 & 口 \\
    口 & 口 & 口 & 👑 \\
    口 & 👑 & 口 & 口 \\
  \end{array}\right]
$$
### b)
Optimal solution found by hill-climbing  algorithm:
>[1, 3, 5, 2, 4]

At each iteration, define the reachable next states as altering the number in each index with a different number that's in range $[1,5]$ inclusive.

For example, in first iteration, the reachable states are:
- alter **1** at index 0 with a number from \[2,3,4,5\]
- alter **3** at index 1 with a number from \[1,2,4,5\]
- alter **5** at index 2 with a number from \[1,2,3,4\]
- alter **2** at index 3 with a number from \[1,3,4,5\]
- alter **4** at index 4 with a number from \[1, 2,3,5\]

The chose the state that has lowest number of attacking pairs as the state for next iteration, until no better solution can be found.

##### Outputs from python script:
iteration: 1
- next possible state :  [2, 2, 1, 2, 4], score: 4
- next possible state :  [3, 2, 1, 2, 4], score: 4
- next possible state :  [4, 2, 1, 2, 4], score: 4
- next possible state :  [5, 2, 1, 2, 4], score: 3
- next possible state :  [1, 1, 1, 2, 4], score: 3
- next possible state :  [1, 3, 1, 2, 4], score: 2
- next possible state :  [1, 4, 1, 2, 4], score: 3
- next possible state :  [1, 5, 1, 2, 4], score: 2
- next possible state :  [1, 2, 2, 2, 4], score: 3
- next possible state :  [1, 2, 3, 2, 4], score: 4
- next possible state :  [1, 2, 4, 2, 4], score: 3
- next possible state :  [1, 2, 5, 2, 4], score: 2
- next possible state :  [1, 2, 1, 1, 4], score: 4
- next possible state :  [1, 2, 1, 3, 4], score: 4
- next possible state :  [1, 2, 1, 4, 4], score: 4
- next possible state :  [1, 2, 1, 5, 4], score: 4
- next possible state :  [1, 2, 1, 2, 1], score: 7
- next possible state :  [1, 2, 1, 2, 2], score: 6
- next possible state :  [1, 2, 1, 2, 3], score: 6
- next possible state :  [1, 2, 1, 2, 5], score: 5
- find a better solution: [1, 3, 1, 2, 4], score: 2

iteration: 2
- next possible state :  [2, 3, 1, 2, 4], score: 3
- next possible state :  [3, 3, 1, 2, 4], score: 2
- next possible state :  [4, 3, 1, 2, 4], score: 3
- next possible state :  [5, 3, 1, 2, 4], score: 1
- next possible state :  [1, 1, 1, 2, 4], score: 3
- next possible state :  [1, 2, 1, 2, 4], score: 5
- next possible state :  [1, 4, 1, 2, 4], score: 3
- next possible state :  [1, 5, 1, 2, 4], score: 2
- next possible state :  [1, 3, 2, 2, 4], score: 2
- next possible state :  [1, 3, 3, 2, 4], score: 2
- next possible state :  [1, 3, 4, 2, 4], score: 2
- next possible state :  [1, 3, 5, 2, 4], score: 0
- next possible state :  [1, 3, 1, 1, 4], score: 2
- next possible state :  [1, 3, 1, 3, 4], score: 3
- next possible state :  [1, 3, 1, 4, 4], score: 2
- next possible state :  [1, 3, 1, 5, 4], score: 2
- next possible state :  [1, 3, 1, 2, 1], score: 4
- next possible state :  [1, 3, 1, 2, 2], score: 3
- next possible state :  [1, 3, 1, 2, 3], score: 4
- next possible state :  [1, 3, 1, 2, 5], score: 2
- find a better solution: [1, 3, 5, 2, 4], score: 0

iteration: 3
- next possible state :  [2, 3, 5, 2, 4], score: 2
- next possible state :  [3, 3, 5, 2, 4], score: 1
- next possible state :  [4, 3, 5, 2, 4], score: 2
- next possible state :  [5, 3, 5, 2, 4], score: 1
- next possible state :  [1, 1, 5, 2, 4], score: 1
- next possible state :  [1, 2, 5, 2, 4], score: 2
- next possible state :  [1, 4, 5, 2, 4], score: 2
- next possible state :  [1, 5, 5, 2, 4], score: 1
- next possible state :  [1, 3, 1, 2, 4], score: 2
- next possible state :  [1, 3, 2, 2, 4], score: 2
- next possible state :  [1, 3, 3, 2, 4], score: 2
- next possible state :  [1, 3, 4, 2, 4], score: 2
- next possible state :  [1, 3, 5, 1, 4], score: 1
- next possible state :  [1, 3, 5, 3, 4], score: 2
- next possible state :  [1, 3, 5, 4, 4], score: 2
- next possible state :  [1, 3, 5, 5, 4], score: 2
- next possible state :  [1, 3, 5, 2, 1], score: 2
- next possible state :  [1, 3, 5, 2, 2], score: 1
- next possible state :  [1, 3, 5, 2, 3], score: 2
- next possible state :  [1, 3, 5, 2, 5], score: 1
- no better solution found, returning current solution

which is [1, 3, 5, 2, 4]
##### Python script snippet
```py
def deep_clone(lst):
    return [x for x in lst]


def evaluate_state(state: List[int]):
    '''
    state: [1,2,1,2,4]
    len(state) = n, for n queens problem
    range(state) = [1,n], inclusive
    '''
    attacking_pairs = 0
    cp = deep_clone(state)
    # attacking row pairs
    unique = list(dict.fromkeys(cp))
    attacking_pairs += (len(state)-len(unique))

    # attacking diagonal pairs
    for i in range(0, len(state)-1):
        curr = state[i]
        next = state[i+1]
        if abs(curr-next) == 1:
            attacking_pairs += 1
    return attacking_pairs


def climb(initial_state: List[int]):
    n = len(initial_state)
    possible_values = range(1, n+1)
    current_state = deep_clone(initial_state)
    current_score = evaluate_state(current_state)
    iter_count = 1
    while(True):
        print("iteration: "+str(iter_count))
        next_candidate = deep_clone(current_state)
        next_candidate_score = current_score

        for i in range(0, n):
            value = current_state[i]
            actions = deep_clone(possible_values)
            actions.remove(value)
            for action in actions:
                next = deep_clone(current_state)
                next[i] = action
                next_score = evaluate_state(next)
                print("\t next possible state : ",
                      str(next)+", score: "+str(next_score))
                if(next_score < next_candidate_score):
                    next_candidate = deep_clone(next)
                    next_candidate_score = next_score
        if next_candidate_score < current_score:
            current_state = deep_clone(next_candidate)
            current_score = next_candidate_score
            print("find a better solution: " + str(current_state) +
                  ", score: "+str(current_score))
        else:
            print("no better solution found, returning current solution")
            break
        iter_count += 1
    return current_state


print(evaluate_state([1, 2, 1, 2, 4]))
print(climb([1, 2, 1, 2, 4]))
```
### c)
#### Winning Strategy of a $5\times 5$ Board
Starting with Maximus, by placing a queen in the middle of the board, Maximus divides the board into 2 symmetrical sub-sections:

- top-left  and bottom-right sections are symmetrical in relation to A.
- top-right and bottom-left sections are symmetrical in relation to A.

$$
  \left[\begin{array}{|rrrrr|}
    💀 & \color{blue}{口} & 💀  & \color{cyan}{口}  & 💀  \\
    \color{red}{口} & 💀 & 💀  & 💀  & \color{green}{口}  \\
    💀 & 💀 & Q  & 💀  & 💀  \\
    \color{green}{口} & 💀 & 💀  & 💀  & \color{red}{口}  \\
    💀 & \color{cyan}{口} & 💀  & \color{blue}{口}  & 💀  \\
  \end{array}\right]
$$
As shown in the above figure, grid with same color are symmetric to each other related to Q.


Now Minnie has to make the next move.

However, it doesn't matter where Minnie place the Queen, it can not attack the cell that is symmetrical to it's position, so in Maximus' turn, he can always place the Queen at the symmetrical position of where Minnie placed his Queen.

After Maximus' respond to Minnie's move, the available positions on the board in each sub-section is symmetrical again, which meas either
- There are a pair of available grids on the board that do not attach each other
- There is no available grids on the board anymore.

In the first case, after Minnie's move, Maximus always has the available move that is symmetrical to where Minnie placed the Queen.
In the second case, Minnie loses the game since there is no available grids on the board for his turn.

> So the winning stategy for Maximus is to always place the queen in the center of the board, and place the queen at the symmetrical position based on where Minnie placed the queen, until there is no more space available for Minnie.

#### Winning Strategy for a $n\times n$ Board where n is odd number
The winning strategy of a $n\times n$ board of odd number of n is the same as the winning strategy of a $5 \times 5$. 
Since n is an odd number, which means Maximus can always place the queen in the center of the board and divide the board into two symetrical sub-sections.
Then Maximus can place the queen accordingly and wait until no more space available for Minnie to move.
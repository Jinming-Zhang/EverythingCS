# Report Jinming Zhang
## Q1
I did the project alone.

## Q2
##### Hardest Question
Question 1 Value Iteration:
The tricky part is to update the values in a batch so that the updated value doesn't effect the update of other values at the same iteration.
This problem is hard to notice and took me sometime to fix.
##### Easiest Question
Question 2 Bridge Crossing Analysis:
This part is easiest because just set the noise to 0 and everything become predicitble

## Q3
I tried debug the program step and step and noticed that at certain step it was referencing the value that was just updated at the previous step, and realized that what 'update in batch' means.

## Q4
In the three pacman projects I learned and practice different aspect of AI and all of them are beneficial.
I learned the strategy of searching algorithms and how to generalize it so we can use the same algorithm to solve different types of problems by structuring the problem in a specific way.

The adverserial search is a great strategy in games where two player compete with each other. By using exhusive search, we are able to find the best strategy and guarenteed a win. Or if there is no way to win just don't play the game.

In reinforcement learning, we learned a generailized strategy that can be suited into different problems in a stochastic environment, where we don't need to know the rules of the problem. By create an angent and let it experience the environment in a large number of iterations, it can leanr the best strategy by itself.

## Q5
I think the classical search is particularly helpful after I realized I can form different problems into a search problem, then I can feed it into A\* search and find a solution.
I think it has great potential, if I can find a way to form the problem into a search problem, then the solution can be yield right away. 

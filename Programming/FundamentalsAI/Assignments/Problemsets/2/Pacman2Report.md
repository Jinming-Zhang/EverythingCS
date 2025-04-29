# Jinming Zhang
## Q1
I worked alone
## Q2
The evaluation part is the most difficult and Reflex agent is the easiest.
## Q3
distance to closest food is the only feature, the lower the better so it's substracted from a constant.
## Q4
#### Relevant features: 
   - pacman position
    - distance to closest food
    - number of food left
    - distance to closest ghost
    - distance to closest capsule
    - distance to closest food
    - number of food left
    - total scare time

#### Ideal strategy:
when pacman is 3 units away from the ghost, ignore ghost and focus on getting food, with preference of getting capsule first
when pacman is 3 units within the ghost, if the ghost is scared, hunt the ghost, otherwise dodge the ghost
## Q5
AlphaBetaAgent will always lose because because the game score is decreasing overtime and when the agent assumes the ghosts always move optimally it concludes that it can never win, so to keep the score as high as possible the best action is suicide.

ExpectimaxAgent can win sometimes because the ghosts are not always moving optimally and when they don't, there will be a winning chance that AlphaBeta agent cannot foresee, so ExpectimaxAgent can catch such chances and win the game occasionally.
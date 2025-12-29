### a)
Szeka always win when n = 4
### b)
Szeka always win when n = 5
### c)
Jinming always win when n = 6
### d)
Jinming always win when n = 2022

#### Stretegy for every case:
The goal is to construct a bipartite with even number of nodes on each side.

Suppose X, Y  are two set of nodes for the bipartite graph, then:
- Whenever a player connect to nodes with an edge, those two nodes will be put into two different set, X and Y respectively
- Based on the privous move, the next player can always balance the size of X, Y by connecting another two nodes that hasn't been connected and doesn't form an odd cycle.

This way, the maximum number of edges of such bipartite graph is sizeof(X) $\times$ sizeof(Y). 

- In case of  n=5, sizeof(X) == 2, sizeof(Y) == 3, so the total number of edges before forming a odd cycle is $2\times 3=6$
- In case of  n=5, sizeof(X) == sizeof(Y) == 3, so the total number of edges before forming a odd cycle is $3\times 3=9$

> Since if a player want's to balance the size of X, Y, he can always achieve it. So even if the other player knows that he/she is losing and wants to break the balance, and therefore changing the edges available before forming a odd cycle, he won't be able to do it.

If the resulting edge is odd number, then the player moves first will always win.
If the resulting edge is even number, then the player moves second will always win.


#### Example for n=6
Starting size of X and Y are 0, after the first player connecting two nodes, sizeof(X) == sizeof(Y) == 1

![[Pasted image 20221026160420.png]]

Now doesn't matter what second player choose to connect, first player can always find a way to balance the number of nodes in set X and Y:

If second player choose BC, then first player choose CD
![[Pasted image 20221026160606.png]]

This way, there will be $3\times 3 = 9$ edges in total before a odd cycle has to be formed, and since first player starts first, second player is guarenteed to lose when it's their turn.


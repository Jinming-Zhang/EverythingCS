# Problem #1
Reward table for Rose:
| Colin\Rose | Red | Black |
|------------|-----|-------|
| Red        | p   | -r    |
| Black      | -q  | s     |

Reward table for Colin:
| Colin\Rose | Red | Black |
|------------|----|-------|
| Red        | -p |  r    |
| Black      | q  | -s    |

$P(\text{rose pick red}=x)$, $P(\text{rose pick black}=1-x)$
$P(\text{colin pick red}=y)$, $P(\text{colin pick black}=1-y)$

### a)
##### Rose's expected payoff:
$p\cdot P(\text{rose=red \& colin=red}) +-r\cdot P(\text{rose=black \& colin=red}) +-q\cdot P(\text{rose=red \& colin=black})+s\cdot P(\text{rose=black \& colin=red})$
$\implies$
$p \cdot xy + (-r)\cdot (1-x)y + (-q) \cdot x(1-y) + s\cdot(1-x)(1-y)$
$\implies$
$pxy-ry+rxy-qx+qxy+s-sy-sx+sxy$
$\implies$
$(p+r+s+q)xy-(q+s)x-(s+r)y+s$

substitute $p=2,q=1,r=5,s=2$
$\implies$
$(2+5+2+1)xy-(1+2)x-(2+5)y+(s)$
$\implies$
$$10xy-3x-7y+2$$
##### Colin's expected payoff:
$-(p+r+s+q)xy+(q+s)x+(s+r)y-s$
$\implies$
$$3x+7y-10xy-2$$

### b)
##### Nash Equilibrium for Rose:
In the case of colin always pick red, $y=1$, the expected payoff for rose is:
$7x-5$
To maximize this, rose will pick red every time($x=1$), so that 2 is the rose's payoff.

In the case of colin always pick black, $y=0$, the expected payoff for rose is:
$-3x+2$
To maximize this, rose will pick black every time($x=0$), so that 2 is the rose's payoff.

At equilibruim:
$7x-5=-3x+2$
$\implies$
$x=0.7$
Which means when $x=0.7$, Rose pick red 70% of the time and black 30% of the time, it doesn't matter what Colin picks, Rose will always have a pay off of -0.1.

##### Nash Equilibrium for Colin:
$(p+r+s+q)xy-(q+s)x-(s+r)y+s$
In the case of Rose always pick red, $x=1$, the expected payoff for Colin is:
$-3y+1$
To maximize this, Colin will pick black every time($y=0$), so that 1 is the Colin's payoff.

In the case of Rose always pick black, $x=0$, the expected payoff for Colin is:
$7y-2$
To maximize this, Colin will pick red every time($y=1$), so that 5 is the Colin's payoff.

At equilibruim:
$-3y+1=7y-2$
$\implies$
$y=0.3$
Which means when $y=0.7$, Colin pick red 30% of the time and black 70% of the time, it doesn't matter what Rose picks, Colin will always have a pay off of 0.1

### c)
Recall the payoff function of Rose in with terms p,q,r,s:
$$(p+r+s+q)xy-(q+s)x-(s+r)y+s$$

By assuming whether Colin choose red or black, we have two different result of the payoff equation:
$(p+r+s+q)x-(q+s)x+r$
$-(q+s)x+s$
$\implies$
$(p+r)x+r$
$-(q+s)x+s$
We set both equal to 0, so that the payoff for Rose will be 0, and get
$(p+r)x+r=0$
$-(q+s)x+s=0$
We can eliminating $x$ by multiply $-(q+s)$ for first equation and $(p+r)$ for second equation, and get
$sp+sr=0$
$-rq-rs=0$
$\implies$
$p=-r$
$q=-s$
So when  $p=-r$ and  $q=-s$, the payoff for Rose is 0.
which is the same as $ps=qr$. 
by substitute p with -r and q with -s, we get
$-rs=-rs$
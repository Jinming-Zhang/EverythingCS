### a)
##### P(+B)
$P(B) = P(B|A)\cdot P(A) + P(B|\lnot A)\cdot P(\lnot A)$
$=0.3\cdot 0.1 + 0.5 \cdot 0.9$
= 0.48

##### P(+C)
$P(C)=P(C|A,B)\cdot P(B|A)\cdot P(A)$
$+ P(C|A,\lnot B)\cdot P(\lnot B|A)\cdot P(A)$
$+ P(C|\lnot A, B)\cdot P(B|\lnot A)\cdot P(\lnot A)$
$+ P(C|\lnot A, \lnot B)\cdot P(\lnot B|\lnot A) \cdot P(\lnot A)$
$= 0.2\cdot 0.3\cdot 0.1$
$+ 0.4\cdot 0.7\cdot 0.1$
$+ 0.6\cdot 0.5 \cdot 0.9$
$+ 0.8 \cdot 0.5\cdot 0.9$
$=0.664$

##### P(+D)
$P(D) = P(D|C)\cdot P(C) + P(D|\lnot C)\cdot P(\lnot C)$
$=0.7\cdot 0.664 +0.9\cdot 0.336$
$=0.7672$

### b)
##### P(D|A)
$P(C|A)=P(C|A,B)\cdot P(B|A)+P(C|A,\lnot B)\cdot P(\lnot B|A)$
$=0.2\cdot 0.3 +0.4\cdot 0.7$
$=0.3394$

$P(D|A) = P(D|C)\cdot P(C|A) + P(D|\lnot C)\cdot P(\lnot C|A)$
$=0.7\cdot 0.3394 +0.9\cdot 0.6606$
$=0.8321$

##### P(A|D)
$P(A|D)=\frac{P(D|A)\cdot P(A)}{P(D)}$
$=\frac{0.8321\cdot 0.1}{0.7672}$
$=0.1085$

### c)
##### Scenario
Blue, Cyan and Doggo are three students at NEU, Blue wants to ask Cyan out for dinner at Doggo's restaurant on weekend, but it also depends on if the new Assignment will be posted before the weekend.

##### Scenario
Let the bayes network describes the following:

$P(A)=0.1$: A new Assignment is out before the weekend
$P(B|A)=0.3$: Blue will ask Cyan out for dinner if a new Assignment is out.
$P(B|\lnot A)=0.7$: ... if there is no new Assignment.
$P(C|A, B)=0.6$: Cyan wants to go for dinner if Blue asked him out and there is a new Assignment.
$P(C|\lnot A, B)=0.9$: Cyan wants to go for dinner if Blue asked him out and there is no new Assignment.
$P(C|A, \lnot B)=0.1$: Cyan wants to go for dinner if Blue didn't ask him out and there is a new Assignment.
$P(C|\lnot A, \lnot B)=0.3$: Cyan wants to go for dinner if Blue didn't ask him out and there is no new Assignment.
$P(D|C)=0.8$: Doggo sees Cyan at restaurant if Cyan wants to go for dinner
$P(D|\lnot C)=0.1$: Doggo sees Cyan at restaurant if Cyan doesn't want to go for dinner

##### Goal
P(A|D) =0.048 : A new assignment is out if Doggo sees Cyan at restaurant.

##### Simulation
See file simulationQ4.py


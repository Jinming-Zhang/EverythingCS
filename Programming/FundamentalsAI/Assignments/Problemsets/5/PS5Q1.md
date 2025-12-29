### a)
Since the probability of a tie can also be written as t = 1-(b+a), so the probability of B wins can be interpreted as n ties follwed by B wins:
$P(W_B)=(1-(b+c))^n\cdot b$
Same for the probability of C wins:
$P(W_C)=(1-(b+c))^n\cdot c$

Based on the formular of sum of geometric series, they both have a common ratio of $1-(b+c) = 1-b-c$, and can be simplified to following:
- $P(W_b)= \frac{1}{1-(1-b-c)}\cdot b=\frac{b}{b+c}$
- $P(W_c)= \frac{1}{1-(1-b-c)}\cdot c=\frac{c}{b+c}$

### b)
When Bob rolls 7:
- Probability of Chris if he choose Dice X:
	- $P(tie) = \frac{1}{6}$
	- $P(lose) = \frac{5}{6}$

- Probability of Chris if he choose Dice Y:
	- $P(tie) = \frac{1}{2}$
	- $P(lose) = \frac{1}{2}$

Chris will always choose Y since it has lowest losing probability.

When Bob rolls 0:
- Probability of Chris if he choose Dice X:
	- $P(tie) = \frac{1}{6}$
	- $P(win) = \frac{5}{6}$

- Probability of Chris if he choose Dice Y:
	- $P(tie) = \frac{1}{2}$
	- $P(win) = \frac{1}{2}$

Chris will always choose X since it has highest winning probability.

##### If Bob always choose Y
$c=P(\text{Bob rolls 0 and Chris rolls 7 or 3})$
$= \frac{1}{2}\cdot \frac{5}{6}=\frac{5}{12}$
$t=P(\text{Bob rolls 7 and Chris rolls 7})+P(\text{Bob rolls 0 and Chris rolls 0})$
$=\frac{1}{2}\cdot \frac{1}{6} +\frac{1}{2}\cdot \frac{1}{2}=\frac{1}{3}$
$b=1-c-t=\frac{1}{4}$

$P(W_b|Bob choose Y)=\frac{b}{b+c}=\frac{\frac{1}{4}}{\frac{8}{12}}=0.375$
$P(W_c|Bob choose Y)=\frac{c}{b+c}=\frac{\frac{5}{12}}{\frac{8}{12}}=0.625$

### c)
##### If Bob always choose X
- If Bob rolls 7, Chris will always choose Y because it has highest tie rate
- If Bob rolls 3, Chris will always choose X because it has lowest lose rate
- If Bob rolls 0, Chris will always choose X because it has highest win rate

Based on the above optimal strategy for Chris, we can find $b,c,t$ when Bob always choose X:
$c=P(\text{Bob rolls 3 and Chris rolls 7})+P(\text{Bob rolls 0 and Chris rolls 7 or 3})$
$= \frac{4}{6}\cdot \frac{1}{6}+\frac{1}{6}\cdot \frac{5}{6}=\frac{9}{36}$
$t=P(\text{Bob rolls 7 and Chris rolls 7})+P(\text{Bob rolls 3 and Chris rolls 3})+P(\text{Bob rolls 0 and Chris rolls 0})$
$=\frac{1}{6}\cdot \frac{1}{2} +\frac{4}{6}\cdot \frac{4}{6}+\frac{1}{6}\cdot \frac{1}{6}=\frac{20}{36}$
$b=1-c-t=\frac{7}{36}$

$P(W_b|Bob choose X)=\frac{b}{b+c}=\frac{\frac{7}{36}}{\frac{16}{36}}=0.4375$
$P(W_c|Bob choose Y)=\frac{c}{b+c}=\frac{\frac{9}{36}}{\frac{16}{36}}=0.5625$

##### Optimal Strategy
Since Bob always play first, and when he plays X he has a higher probability, so the optimal strategy for Bob is to always choose X.
Then the optimal strategy for Chris is as described in c).
There for when both player play optimally:

$P(W_b|Bob choose X)=\frac{b}{b+c}=\frac{\frac{7}{36}}{\frac{16}{36}}=0.4375$
$P(W_c|Bob choose Y)=\frac{c}{b+c}=\frac{\frac{9}{36}}{\frac{16}{36}}=0.5625$
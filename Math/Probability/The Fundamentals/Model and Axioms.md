## Sample Space
- To define a sample space, we need to 
	- Describe the possible outcomes
	- Describe beliefs about the likelihood of outcomes
	
- Then we define a sample space be a set of all possible outcomes
- A sample space has properties of
	- Elements are mutually exclusive (only one outcome at a time)
	- Elements are collectively exhaustive (contains all possibilities)
	- At *right* granularity (try not include irrelevant elements)


#### Example: Toss a coin and note the weather
Sample space:
<center>
{Head, Raining}, {Head, Not Raining}, {Tail, Raining}, {Tail, Not Raining}
</center>

It has all the possible outcomes, and only one outcome can happen at a given time.
But the weather may be an irrelevant element, so it can be removed from the sample space.

## Probability Axioms
<center>
 A and B represents different sample spaces.
</center>

A probability model needs to satisfy the following 3 axioms to be legitimate:
- Non-negativity:
	- $P(A)\ge 0$
- Normalization:	
	- $P(\Omega) = 1$, where $\Omega$ is the whole set of the sample space.
- (for finite sample space) Additivity:
	- If $A\cap B = \varnothing$, then $P(A\cup B) = P(A)+P(B)$

## Probability Event:
A probability event, A, is a subset of the sample space, probability is assigned to events:
e.g. $$P(A) = 0.5$$


## Properties of Probabilities
$$A^c \text{ donates the complement of set A}$$

- $A^c \cup A = \Omega$
- $A^c \cap A = \varnothing$
- $P(A^c \cup A) = P(\Omega) = 1 = P(A)+P(A^c)$
- For disjoint probability event sets, $A, ..., A_n$
	- $P(A_1 \cup A_2~\cup ~ ...~\cup~A_k) = P(A_1) + P(A_2) + ... + P(A_k)$
	- $\Leftrightarrow P(\{A_1 , A_2, ...,A_k\}) = P(A_1) + P(A_2) + ... + P(A_k)$
- If $A\subset B$, then $P(A)\leq P(B)$
- $P(A\cup B)=P(A) + P(B) - P(A\cap B)$
- $\Leftrightarrow P(A\cup B) \geq P(A) + P(B)$, since $P(A\cap B) \geq 0$
- $P(A\cup B \cup C) = P(A) + P(B\cap A^c) + P(C\cap A^c \cap B^c)$ ![[Pasted image 20251230190643.png]]

## Countable Additivity
An example of discrete and infinite sample spaces:
- Outcomes: number of tosses until first head occurs
- Sample Space: {1,2,3,...}
- Probability law (define probability of every outcome/event):
	- $P(n) = \frac{1}{2^n},~n=1,2,3$, n be the outcome


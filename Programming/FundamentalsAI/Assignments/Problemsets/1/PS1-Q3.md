# Jinming Zhang
# Problem #3
## a)
ABCD are all right color
AB is not in the correct position
CD in in the correct position
Final sequence = BACD

## b)
 n = 4
Let A,B,C,D,E,F representing 6 different colors
- `Step 1`:  Choose A,B,C,D, based on the rule, there must be atleast two colors that is correct, so there will be 3 possibilities:
	- **Case 1**: The number of correct color is 2
	- **Case 2**: The number of correct color is 3
	- **Case 3**: The number of correct color is 4

#### Case 1:
In the case of A, B, C, D have two correct colors:
- `Step 2`: Choose C,D,E,F.
	- In this step we swap A,B with E,F, there are 3 possible cases:
		1. A, B are both wrong colors:
			- Then C,D,E,F will be the 4 correct colors. `colors found`
		2. A, B are both correct colors:
			- Then C,D,E,F will have 2 correct colors, and the correct colors will be A,B,E,F. `colors found`
		3. One of A,B is correct,
			- C,D,E,F will have 3 correct colors, needs further test.

In the case of C,D,E,F has 3 correct colors:
	Based on our knowledge, untile now, we know that
		- One of A, B is correct.
		- Since A,B,C,D have 2 correct colors, A, B have one correct colors, so C,D only have one correct color.
		- C,D,E,F have 3 correct colors
	Since only one of C, D is correct color, we can say that both E, F are correct colors
	**Now we can swap E or F with a color that we are unsure about to see if it's a correct color.**
	- `Step 3`: Check the correct color in A,B, by choosing C,D,E,A
		- In this step, we swap F with A, since we know for sure F is a correct color, there are two cases in this step:
			1. C,D,E,A have 3 correct color (same as C,D,E,F), which means A is a correct color
			2. C,D,E,A have 2 correct color, which means A is wrong, and B is the correct color
	- `Step 4`: Base on the result from step 3, we'll have 3 colors for sure that are correct, then we can use same way to decide the correct color from C,D. For example, if in step 3 we found A is a correct color, then the correct colors are either A,E,F,C or A,E,F,D. `colors found`

#### Case 2:
In the case of A,B,C,D have three correct colors:
- `Step 2`: Choose C,D,E,F
	- In this step we swap A,B with E,F, there are 2 possible cases(since A,B can not be wrong at the same time):
		1. Both A and B are correct colors,
			- Then C,D,E,F will have 2 correct colors, and we know that one of C,D is correct, so one of E,F is correct
		2. One of A, B is correct:
			- Then C,D,E,F will have 3 correct colors, and we know that both C, D is correct, and one of E,F is correct.

Since in both cases, we will know for sure that either **both A,B are correct**, or **both C, D are correct**, combined with **A,B,C,D have three correct colors**, we are in the situition that is same as `Case 1, Step 2`, where we can swap out a known-correct color to test if an unknown color is a correct color.
Therefore, we can follow the same precedure as case one, use `Step 3` to decide the correct color from E,F, and `Step 4` to find all four correct colors

#### Case 3:
`A,B,C,D, YES!`


## c)
m=10
In b) we showed that we can use at most 4 steps to determine the 4 correct colors out of 6. Here, we'll show that we can use at most 6 steps to determine the correct order of the 4 colors, so we can solve the whole problem in 10 steps in total.

Let 1,2,3,4 be the four colors that we want to put into order, the correct order is unknown at first.

`Step 5`:
- We try 1,2,3,4, there are 3 possible cases, 1 impossible cases:
	- **Case 1**: 1 of the colors is in order
	- **Case 2**: 2 of the colors is in order
	- **Case 3**: 0 or the colors is in order
	- **Case 4**: 4 of the colors is in order
	- **Case 5**: 3 of the colors is in order (impossible)

#### Case 1
In the case of 1,2,3,4 has 1 color in correct order, there are total 8 possible cases for the correct order:
 (1,3,4,2),  (1,4,2,3),  (3,2,4,1),  (4,2,1,3),  (2,4,3,1),  (4,1,3,2),  (2,3,1,4),  (3,1,2,4)
We can choose anyone of them and separate the results again in cases.

 `Step 6`: Chose 1,3,4,2
 In this step, we chose 1,3,4,2, we can also divide the outcome into cases that, 1,3,4,2 has 1/2/0/4 correct colors in order respectively. But given that 1,2,3,4 has only 1 color in correct order, the possible outcomes are reduced as follows:
- Subcase 1: 1,3,4,2 has 1 color in correct order, then the possible cases are:
	- (1,4,2,3), (1,2,3,4), (4,3,2,1), (2,3,1,4), (3,2,4,1), (2,1,4,3), (3,4,1,2), (4,1,3,2)
	- but given that (1,2,3,4) has one color in correct order, only **(1,4,2,3), (2,3,1,4), (3,2,4,1), (4,1,3,2)** are the possible outcomes.
- Subcase 2: 1,3,4,2 has 2 color in correct order, then the possible cases are: 
	- (1,3,2,4), (1,2,4,3), (1,4,3,2), (2,3,4,1), (4,3,1,2), (3,1,4,2)
	- again, we can see that none of them satisfy that (1,2,3,4) has one color in correct order, so we can **discard this subcase completely**.
- Subcase 3: 1,3,4,2 has 0 color in correct order, then the possible cases are:
	- **(3,1,2,4), (4,2,1,3), (2,4,3,1)**
	- since all of them satisfy (1,2,3,4) has 1 color in correct order and (1,3,4,2) has 0 color in correct order, we have 3 possible cases for this subcase.
- Subcase 1: 1,3,4,2 has 4 color in correct order, then `problem solved`.

Therefore, after step 6:
- If we ended up in subcase 1,  we can solve the problem in 4 steps.
- If we ended up in subcase 2,  we can solve the problem in 3 steps.

`In either case, we can solve the whole problem in 10 steps`.
 
#### Case 2:
In the case of 1,2,3,4 has 2 colors in correct order, there are total 6 possibilities for the correct order. 
(1,2,4,3), (1,4,3,2),(1,3,2,4),(4,2,3,1),(3,2,1,4),(2,1,3,4)
Similar as Case 1, we chose anyone of the possible cases and examine the possible subcases

`Step 6`: Chose (1,2,4,3)
In this step we chose (1,2,4,3), we'll do the same as we did in Case 1, divide the result into subcases and examine each subcase:
- Subcase 1: (1,2,4,3) has 0 color in correct order, then the possible cases are
	- (2,1,3,4), (4,3,1,2), (3,4,2,1)
	- Since (1,2,3,4) has 2 color in correct order, **(2,1,3,4)** is the only possible outcome, and it has to be the correct color order. `problem solved`
- Subcase 2: (1,2,4,3) has 1 color in correct order, then the possible cases are:
	- (1,4,3,2), (1,3,2,4), (4,2,3,1), (3,2,1,4), (2,3,4,1), (3,1,4,2), (2,4,1,3), (4,1,2,3)
	- Since we know that (1,2,3,4) has two colors in correct order, so only **(1,4,3,2), (1,3,2,4), (4,2,3,1), (3,2,1,4)** are the possible cases.
- Subcase 2: (1,2,4,3) has 2 color in correct order, then the possible cases are:
	- (1,2,3,4), (1,3,4,2), (1,4,2,3), (3,2,4,1), (4,2,1,3), (2,1,4,3)
	- Since none of them also satisfy (1,2,3,4) has 2 correct colors in order, we can **discard this subcase completely**.
- Subcase 4: (1,2,4,3) has 4 color in correct order, `problem solved`.

After step 6, the worst case scenario is that we left 4  possible subcases. Therefore, `we we can still solve the whole problem in 10 steps in total`.

#### Case 3:
In the case of 1,2,3,4 has 0 color in correct order, there are 3 possible cases for the correct order:
**(2,1,4,3), (3,4,1,2), (4,3,2,1)**

`We can simply try each one and solve the whole problem in 10 steps`.
#### Case 4:
`1,2,3,4 YES!`

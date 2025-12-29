Prior: The initial probability that we calculated.
Event: What gives us information to calculate a better probabilities.
Posterior: The final probability that we calculated based on prior and event.

#### Example: Probability that a patient is sick
1. Prior: 
	1. Based on the statistics, we know that 1 out of 10000 people is sick
	2. So our initial belief that a person is sick is 0.0001
2. Event:
	1. Then we know that a person is diagnosed sick, and the test as 99% correctness rate.
3. Posterior:
	1. Based on the test result, we recalculate the probability that the person is sick, and the updated probability is 0.0098

## Bayes Theorem
Given
1. The probability that the email is a spam 1/5
2. The probability that the spam email has 'lottery' is 3/4
3. The probability that the ham email has 'lotter' is 1/20
Find:
The probability that the email is spam given it has the word 'lottery'

First, we find the intersection probability, so to say:
1. The probability that an email is both spam and has the word 'lottery'

Since the email has the word 'lottery' is observed, i.e. the condition is already happened, Based on multiplication rule
P(spam|lottery)=$\frac{P(spam \cap lottery)}{P(lottery)}$
P(lottery) = P(lottery and spam ) + P(lottery and ham)

> The probability of the given condition, is the sum of the probability of the given condition happened AND the probability of all the possible values of other random variables.

##### Formally
P(A|B) = P(B and A)/(P(B and A) + P(B and not A))
Then apply rule of conditional probability:
P(A|B) = P(B|A)P(A)/(P(B|A)P(A) + P(B|not A)P(not A))

# The Naive Bayes Algorithm
$P(sick|positive) = \frac{0.99\cdot 0.0001}{0.99\cdot 0.0001+0.01\cdot 0.9999}\approx 0.00980$
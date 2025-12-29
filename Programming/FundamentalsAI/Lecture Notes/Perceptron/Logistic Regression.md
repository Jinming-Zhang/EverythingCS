Also called Continuous Perceptron, will return the likelihood of a given data entry, instead of 0/1.

## Sigmoid Function
Instead of a function return either 0 or 1, make it return a number between 0 and 1.
$$\sigma(x)=\frac{1}{1+e^{-x}}$$
- For positive x, the sigmoid function will return a number close to 1
- For negative x, the sigmoid function will return a number close to 0
- When x=0, it returns 0.6

The new score of the classifier will be the result of feeding our original score to the sigmoid function.

## Error Functions for Continuous Perceptron
1. Absolute Error
2. Square Error
3. **Log Loss (Most used one)**

First, get the probability of the prediction being the same as it's original label.
Then for the error function, we want it to generate a large number of the probability is close to 0, and a smaller number if that probability os closer to 1.
$$-ln(x)$$

So if the label is 0:
- The error will be -ln(1 - prediction)
If the label is 1:
- The error will be -ln( prediction)
Since the label is either 0 or 1, we can simplify this into one equation:
$$LogLoss=-label\cdot ln(prediction)-(1-label)ln(1-prediction)$$

To calculate the log loss of the classifier on the whole data set:
1. For each data point, we calculate the probability that the classifier predicts for the label (apply -ln(x) on the resulting score).
2. We multiply the result for all the data point, to get the total probability that the classifier gives for all the labels.
3. We use the ln(x) on the probability to avoid the multiplication of series of very tiny numbers, $ln(x_1\cdot x_2\cdot x_3\cdot x_4)=ln(x_1)+ln(x_2)+ln(x_3)+ln(x_4)$
4. Since ln(x) gives negative number when x<1, we invert the sign by multiplying each term with -1
5. The sum will be the classifier's log loss over the entire dataset.

## Logistic Regression Trick
- If a data point is correctly classified, move the line slightly away from that data point.
- If a data point is incorrectly classified, move the line slightly closer to that data point.
### Process:
- Input:
	- A classifier with weights for each feature and a bias term
	- List of labelled training data points 
	- A learning rate
	- A number of epochs/training iterations.
- Procedure:
	- Loop until error doesn't change much:
		1. pick a random data point
		2. Apply the logistic regression trick:
			1. Find the probability and get the error score.
			2. Update each weight based on the error score and learning rate.


## Perceptron
A classification model which consists of a set of weights for every feature, and a threshold, can be in the form of bias. The perceptron get the weighted total score and compare with the threshold, then returns a 1 or 0.

## Error Function
An error function is used to evaluate how good the current classifier is.
A simple error function will be the score that the current weight returns, since when the score is 0, it means that the classifier correctly classified the data entry. And when score is not 0, it either means the classifier returns a false positive or false negative.

### Perceptron Algorithm
Start with randomly assigned weights and improve the weight over time during iterations over the training dataset.
1. Calculate the score of a (randomly selected) data point.
2. If the data point is correctly classified, do nothing
3. If the data point is incorrectly classified, substract/add learning rate for each weight and the bias term based on if the label is 0 or 1.
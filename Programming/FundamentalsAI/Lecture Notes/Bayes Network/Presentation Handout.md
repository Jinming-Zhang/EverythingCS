# Bayes Theorem Review
## 1
Hello everyone, welcome to today's presentation.
Today we'll be talking about Naive Bayes algorithm, which is based on bayes theorem. And it's application in  spam filtering with some examples.

## 2
First, let's do a very quick review of bayes theorem

## 3
I believe most of us are very familiar with bayes formula by now, which is (very quickly read the formula once)
But why is this formula so important

## 4
well, It is important because it gives us the ability to update our belief of something based on the observation of certain events.

Here are 3 terminologies about bayes theorem and naive bayes algorithm that we'll be talking about later on in this presentation.

- Prior: our initial belief of something, in this formula, it's P(A)
- Event: Some event that we can observe, in this formula, the event is B
- Posterior: our updated belief based on our observation of the event, which is P(A|B) in the formula, updated belief of A, given B has happened.

## 5
This is the screenshot from MIT's open probability course, that I think can help understanding the concept better.
In the diagram, we have 3 disjoint events A1, A2 and A3, and we know the probability of each event
B is another event that we can observe, and we also know the probability of event B happens given A1, A2 or A3 has happened.

So the bayes theorem in this diagram will be, once we have observed that event B has happened, how can we update of our belief of the probability of A1, A2, and A3 that will happen.

For example, out initial belief of A1, A2, A3 are 3 big yellow chucks.
Now we niticed that B has happened.
Then say for A3, our belief for A3 is not the old yellow chunk anymore.
Since we know that B has happened, our belief is shifted to the orange chunk, and our updated belief for A3 will be 
this orange chunk and A3, probability of A3 and B
out of the whole orange chunk, which is probability of B

Also notice, what is the probability of B? is the sum of A1 and B, A2 and B, A3 and B.
How do we get probability of, say, A2 and B
Based on multiplication rule, we know that P(A2 and B) = P(A2) * P(B|A2)
Noticed how that we know both A2,(our initial belief), and P(B|A2)

And this is how we calculate the updated belief using bayes theorem.

## 6
To consolidate our understanding further more, let's revisit our classical old quiz problem: sick or healthy

We'll use the same setup
1. there is a rare disease, that 1 out of ten thousands people will have the disease
2. there is a test that has a 99% correctness rate, which means if a person has that disease, the test will report positive 99% of the time, and negative 1% of the time. If the person doesn't have that disease, then the test will report negative 99% of the time, and positive 1% of the time

## 7
Now say that my friend Reed tested positive, what's the probability that Reed has the disease, well we all know where it's going, but... Reed you can start panicing now

anyway, to use the terminologies we just learned to describe this problem:
Our initial belief, the probability that reed is sick, is 0.0001
Our event, will be that, reed tested positive
Our updated belief after we observed the event, will be that, what's the probability that reed does have the disease, (recall at initial belief), given that he tested positive, (recall at event)

## 8
Now let's apply bayes theorem to find our updated belief
We want to find the probability that reed is sick given he tested positive.
which based on bayes theorem, is 
- the probability of test positive given it's sick, (the correctness rate of our test)
- times the initial probability of reed is sick (our initial belief)
- divided by the probability of test positive, (our event)

## 9
And what's the probability of positive? 
look at the diagram we see that among all the 4 possible out comes, two  of them are test positive, so calculate them respectively and sum them up
(pointing at branches)

## 10
And we'll get our updated belief that Reed is sick, 0.0098, less than 1%!
You can relax now Reed.

## 11
Notice that our updated belief did increased a bit, from 0.0001 to 0.0098, and that is because our friend did test positive after all
but it didn't increase that much, why?
The error rate of the test, 1% is still a lot larger than the actual probability of having the disease, therefore, the amount of people that will get misdiagnosed is more than the people that have the disease!

## 12, 13
and some summary of what we just did incase people  wants to review this later

## 14
Now let's get into the real topic, Naive Bayes classifier

## 15
what is a classifier, well, a classifier is a program that identifies which set of a categories that an observation belongs to.
For example, a student classifier's job will be classifying a given stuent into the pre-defined categories that it was trained.
Sees me, I'm a good student.
Sees Reed, Reed is an excellent stuent
Sees Richard, omg Richard is a genius

## 16 
and the Naive Bayes classifier we'll be talking about, it belongs to a familar of simple probabilistic classifiers that 
- it's based on applying bayes theorem (Bayes)
- With a strong independent assumption between features (Naive)

We'll know what does it mean by independent assumption and features very shortly.

## 17
and the use case we'll be using to demonstrate Naive Bayes classifier is spam classification!

## 18
Which means, we'll train a model using Naive Bayes Algorithm from an email database (what we have)
Then give me an email, we'll use the trained model to classify, what's the probability of that email is a spam? (what we want)

## 19
And here is something we can compute right away from an email database, that will be used by the naive bayes algorithm:
1. A database of emails that has already been classified as spam or ham (ham means good email btw), this gives us the **initial belief**, P(email is spam) and/or P(email is ham)
2. for each word appeared in the database, the probability of that word appear in spam and ham.
So each word we see/observe in the an email is an event, and this means we know that for each word (event B) the probability that it appears in spam or ham P(B|A)

Now I'll hand over to luyi, who will be talking about how do we find the probability of a single word is a spam, the probability of 2 or more words together is a spam, and therefore, the probability of a given email is a spam







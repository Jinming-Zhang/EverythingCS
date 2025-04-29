b)
Problem:
Reed just bought a new born puppy, it is extremely cute. Reed is very satisfied with it but with only one issue: it pees all over the place!

Unable to keep an eye on the puppy all the time, Reed, as an outstanding computer scientist, developed a monitoring system, that can recognize where and when the puppy has just peed.

Based on the system, Reed has designed a reinforcement learning program for the lovely puppy to help it learn how to pee in the house:

Inside the monitored room, Reed allocates an area that is dedicated for the puppy to pee, and it takes 10% of the total room area.
Whenever the puppy peed, the monitoring system will identify whether the puppy peed at the correct place, and take actions correspondingly: 
if the puppy didn't pee at the correct location, the system will play an angry barking to give a puppy a small warning
if the puppy did pee at the correct location, the system will throw a nice treat to the puppy as a reward.

Suppose the puppy needs to pee 10 times a day, a warning barking sound gives the puppy -5 emotion score, and a nice treat gives the puppy 20 emotion score. 
Whenever the puppy wants to pee, it can decide to pee, not pee, or move to a different location.
The puppy has a learning rate of 0.1
The puppy has a discount factor of 0.5
The puppy has a 10% chance to pee at the correct place every time he peed.

How many days it will take for the puppy to learn to always pee at the correct place?


Based on the output, after 68 tries, the puppy's knowledge has converged!
Therefore, after 7 days, the puppy will learn how to pee at the correct location!
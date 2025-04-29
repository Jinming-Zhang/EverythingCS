#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Recall our Markov Decision Process (MDP) from last week:
# +3 points for Heads, +1 point for Tails
# Stop at any time and collect that many points as your payoff.
# But if you get 6 or more points, your payoff is nothing.


# List our States (S), Actions (A), and Discount Factor (Gamma)
S = [0, 1, 2, 3, 4, 5, 'DONE']
A = ['STOP', 'PLAY']
Gamma = 1


# Define the Transition function with three parameters:
# current state (s), action (a), new state (n)
def T(s,a,n):
    if a=='STOP' and n=='DONE':
        return 1
    if a=='PLAY':
        if s=='DONE':
            if n=='DONE': return 1
        else:
            if n=='DONE':
                if s==5: return 1
                if s==4: return 0.5
                if s==3: return 0.5
            else:
                if n-s == 1: return 0.5
                if n-s == 3: return 0.5
    return 0


# Define the Reward function with three parameters:
# current state (s), action (a), new state (n)
def R(s,a,n):
    if a=='STOP' and n=='DONE':
        if s in [0,1,2,3,4,5]: return s
    return 0


# Define the Value Iteration table V[k][s] and the
# Policy Iteration table P[k][s], with 101 rows
V = [ [0 for s in S] for k in range(101)]
P = [ ['' for s in S] for k in range(101)]


# Use the Bellman Equation to determine Row k+1 of
# tables V and P, using the information in Row k.

for k in range(100):
    for s in S:
        
        # Initialize bestValue and bestPolicy
        bestValue=-1
        bestPolicy='UNKNOWN'

        # For each State-Action pair (s,a), determine Q(s,a) using the
        # Bellman Equation by considering all new states n from state s.
        
        for a in A:
            qValue = 0
            for n in S:
                qValue += T(s,a,n)*(R(s,a,n) + Gamma*V[k][S.index(n)])
            if qValue > bestValue:
                bestValue = qValue
                bestPolicy = a
                
        V[k+1][S.index(s)]=bestValue
        P[k+1][S.index(s)]=bestPolicy
        
        
# Print the results of our Value and Policy Iteration

print("Results of Value Iteration")
x=1
while V[x] != V[x-1]:
    print(V[x])
    x+=1
    
print("")    
print("Results of Policy Iteration")
x=1
while P[x] != P[x-1]:
    print(P[x])
    x+=1

    
# Output the results of our 100th iteration.
print("")
for s in S:
    i = S.index(s)
    print("In state", s, "the optimal action is", P[100][i], "with value", V[100][i])


# In[2]:


# Temporal Difference Learning
import random

# Let P be a policy.
S = [0, 1, 2, 3, 4, 5, 'DONE']
P = ['PLAY', 'PLAY', 'PLAY', 'PLAY', 'STOP', 'STOP', 'STOP']


# Initialize the Values Array V and set the Learning Rate
V = [ [0 for s in S] for k in range(10000)]
Alpha = 0.01

# Run TD Learning for t iterations.

t = 999
k = 0
for k in range(t):
    
    print("")
    print("Before iteration", k, "our state values are", V[k])
    
    # For each state (s), determine the action (a) based on the optimal policy
    # Run an experiement: find the new state (n), calculate the reward, and
    # generate the Sample Value.  Use this sample to update V(s)
    
    for s in S:
        
        i = S.index(s)
        a = P[i]
        coin = 'NONE'
        
        if a == 'STOP':
            n = 'DONE'
            j = 6
        else:
            if random.random() <0.5: 
                coin = 'TAILS'
                n = s+1
                if not n in S: n = 'DONE'
            else: 
                coin = 'HEADS'
                n = s+3
                if not n in S: n = 'DONE'
            
        # Get the correct indices for n from set S
        j = S.index(n)
        
        sample = R(s,a,n) + V[k][j]

        # The new estimate for V(i) is equal to (1-Alpha) times the old estimate 
        # for V(i) plus (Alpha) times the result of our sample.  If Alpha = 0.5,
        # then these two results have the same weight of 50%.
        
        V[k+1][i]=(1-Alpha)*V[k][i] + Alpha*sample
        
        print("State", s, "Action", a, "Flip", coin, "Updated Value", V[k+1][i])


# In[3]:


# Q Learning

S = [0, 1, 2, 3, 4, 5, 'DONE']
A = ['STOP', 'PLAY']

Q = [ [[0 for a in A] for s in S] for k in range(1000)]


# Set learning rate
Alpha = 0.01

# run Q Learning for t iterations
t = 999

for k in range(t):
    print("")
    print("Iteration", k, ": our q-values are", Q[k])
    
    
    for s in S:
        for a in A:     
            coin = 'NONE'
            
            if a == 'STOP' or s == 'DONE':
                n = 'DONE'
            else:
                if random.random() <0.5: 
                    coin = 'TAILS'
                    n = s+1
                    if not n in S: n = 'DONE'
                else: 
                    coin = 'HEADS'
                    n = s+3
                    if not n in S: n = 'DONE'
            
            # Get the correct indices for s and n from set S, and the correct
            # index for a from A - i.e., A.index('STOP')=0, A.index('PLAY')=1
            i = S.index(s)
            j = S.index(n)
            b = A.index(a)
            
            # Calculate the sample and update the (k+1)th row of the Q table
            
            sample = R(s,a,n) + max(Q[k][j][0], Q[k][j][1])
            
            Q[k+1][i][b] = (1-Alpha)*Q[k][i][b] + Alpha*sample
            
            print("State", s, "Action", a, "Flip", coin, "Updated Value", Q[k+1][i][b])


# In[ ]:

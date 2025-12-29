#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Code for the Viterbi Algorithm
# Credit: https://en.wikipedia.org/wiki/Viterbi_algorithm

# Our states are Rain (R) and No Rain (N)
# Define the start probability, the transition probabilities, and
# the emission (or sensor) probabilities.

states = ("R", "N")
start_p = {"R": 0.6, "N": 0.4}
trans_p = {
    "R": {"R": 0.7, "N": 0.3},
    "N": {"R": 0.3, "N": 0.7},
}
emit_p = {
    "R": {"umbrella": 0.5, "no umbrella": 0.5},
    "N": {"umbrella": 0.5, "no umbrella": 0.5},
}


# In[2]:


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    for st in states:
        V[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}
    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for st in states:
            max_tr_prob = V[t - 1][states[0]]["prob"] * trans_p[states[0]][st]
            prev_st_selected = states[0]
            for prev_st in states[1:]:
                tr_prob = V[t - 1][prev_st]["prob"] * trans_p[prev_st][st]
                if tr_prob > max_tr_prob:
                    max_tr_prob = tr_prob
                    prev_st_selected = prev_st

            max_prob = max_tr_prob * emit_p[st][obs[t]]
            V[t][st] = {"prob": max_prob, "prev": prev_st_selected}

    for line in dptable(V):
        print(line)

    opt = []
    max_prob = 0.0
    previous = None
    # Get most probable state and its backtrack
    for st, data in V[-1].items():
        if data["prob"] > max_prob:
            max_prob = data["prob"]
            best_st = st
    opt.append(best_st)
    previous = best_st

    # Follow the backtrack till the first observation
    for t in range(len(V) - 2, -1, -1):
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]

    print('The steps of states are ' + ' '.join(opt) +
          ' with highest probability of %s' % max_prob)


def dptable(V):
    # Print a table of steps from dictionary
    # yield " ".join(("%12d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)


# In[3]:


# Add your Observations, i.e., what you saw each day.
observations = ("umbrella", "umbrella", "umbrella",
                "no umbrella", "no umbrella", )

# Now run the Viterbi Algorithm
viterbi(observations, states, start_p, trans_p, emit_p)

# In[4]:


# Where do these numbers come from?

# If it's rain, there's a 70% chance it's rain the next day
# If it's not rain, there's a 70% chance it's not rain the next day

# We saw an umbrella on Day 1, 2, 3
# If it's rain, 90% chance of umbrella
# If it's not rain, 20% chance of umbrella

print("Day 1", [0.6 * 0.9, 0.4 * 0.2])
print("Day 2", [0.54 * 0.7 * 0.9, 0.54 * 0.3 * 0.2])
print("Day 3", [0.3402 * 0.7 * 0.9, 0.3402 * 0.3 * 0.2])

# We saw no umbrella on Day 4, 5
# If it's rain, 10% chance of no umbrella
# If it's not rain, 80% chance of no umbrella

print("Day 4", [0.21432 * 0.7 * 0.1, 0.21432 * 0.3 * 0.8])
print("Day 5", [0.05143 * 0.3 * 0.1, 0.05143 * 0.7 * 0.8])

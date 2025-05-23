# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp
import util

from learningAgents import ValueEstimationAgent
import collections


class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """

    def __init__(self, mdp: mdp.MarkovDecisionProcess, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        mdpStates = self.mdp.getStates()
        # self.values: Counter(), which stores value for each action
        # for state in mdpStates:
        #     self.values[state] = util.Counter()
        for i in range(self.iterations):
            valuesCp = self.values.copy()
            for s in mdpStates:
                # compute qa for all actions in the state
                actions = self.mdp.getPossibleActions(s)
                optimalvalue = -99999999
                for a in actions:
                    suma = 0
                    for (sprime, prob) in self.mdp.getTransitionStatesAndProbs(s, a):
                        reward = self.mdp.getReward(s, a, sprime)
                        vk = self.discount * self.getValue(sprime)
                        suma += (prob*(reward+vk))
                    if (suma > optimalvalue):
                        optimalvalue = suma
                        valuesCp[s] = suma
            self.values = valuesCp.copy()

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        qsa = 0
        for (sprime, prob) in self.mdp.getTransitionStatesAndProbs(state, action):
            reward = self.mdp.getReward(state, action, sprime)
            vk = self.discount*self.getValue(sprime)
            qsa += prob*(reward+vk)
        return qsa

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        vopt = -999999999
        actions = self.mdp.getPossibleActions(state)
        if (len(actions) == 0):
            return None
        besta = actions[0]
        for a in actions:
            v = self.computeQValueFromValues(state, a)
            if (v > vopt):
                besta = a
                vopt = v
        return besta

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)


class AsynchronousValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        An AsynchronousValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs cyclic value iteration
        for a given number of iterations using the supplied
        discount factor.
    """

    def __init__(self, mdp: mdp.MarkovDecisionProcess, discount=0.9, iterations=1000):
        """
          Your cyclic value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy. Each iteration
          updates the value of only one state, which cycles through
          the states list. If the chosen state is terminal, nothing
          happens in that iteration.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state)
              mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        mdpStates = self.mdp.getStates()
        index = 0
        for i in range(self.iterations):
            cp = self.values.copy()
            s = mdpStates[index]
            if index+1 >= len(mdpStates):
                index = 0
            else:
                index += 1
            # compute qa for all actions in the state
            actions = self.mdp.getPossibleActions(s)
            optimalvalue = -99999999
            for a in actions:
                suma = 0
                for (sprime, prob) in self.mdp.getTransitionStatesAndProbs(s, a):
                    reward = self.mdp.getReward(s, a, sprime)
                    vk = self.discount * self.getValue(sprime)
                    suma += (prob*(reward+vk))
                if (suma > optimalvalue):
                    optimalvalue = suma
                    cp[s] = suma
            self.values = cp.copy()

        "*** YOUR CODE HERE ***"


class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """

    def __init__(self, mdp: mdp.MarkovDecisionProcess, discount=0.9, iterations=100, theta=1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def getThatDiff(self, state):
        currentV = self.getValue(state)
        actions = self.mdp.getPossibleActions(state)
        highest = -99999999
        for action in actions:
            highest = max(self.getQValue(state, action), highest)
        diff = abs(highest - currentV)
        return diff

    def runValueIteration(self):
        predecessors = {}
        allStates = self.mdp.getStates()
        # compute predecessors for all states
        for state in allStates:
            if state == 'TERMINAL_STATE':
                continue
            predecessors[state] = set()
            for otherState in allStates:
                actions = self.mdp.getPossibleActions(otherState)
                for a in actions:
                    for (sprime, pro) in self.mdp.getTransitionStatesAndProbs(otherState, a):
                        if sprime == state:
                            predecessors[state].add(otherState)
        # initialize an empty pq
        pq = util.PriorityQueue()
        # for each non-terminal state
        for state in allStates:
            if state == 'TERMINAL_STATE':
                continue
            diff = self.getThatDiff(state)
            pq.push(state, -diff)
        # for iteration
        for i in range(self.iterations):
            # if q empty, terminate
            if pq.isEmpty():
                return
            # pop a state s off the q
            state = pq.pop()
            # update the value of s in self.values
            cp = self.values.copy()
            actions = self.mdp.getPossibleActions(state)
            optimalvalue = -99999999
            for a in actions:
                suma = 0
                for (sprime, prob) in self.mdp.getTransitionStatesAndProbs(state, a):
                    reward = self.mdp.getReward(state, a, sprime)
                    vk = self.discount * self.getValue(sprime)
                    suma += (prob*(reward+vk))
                if (suma > optimalvalue):
                    optimalvalue = suma
                    cp[state] = suma
            self.values = cp.copy()
            # for each predecessor p of s
            for predecessor in predecessors[state]:
                diff = self.getThatDiff(predecessor)
                if diff > self.theta:
                    pq.update(predecessor, -diff)

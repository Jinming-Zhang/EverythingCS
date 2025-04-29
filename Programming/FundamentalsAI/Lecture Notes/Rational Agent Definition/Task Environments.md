# Agent and Environment
Agent can be viewed as perceiving **Environments** through **Sensors** and acting through **Actuators**.

> An agent's behaviour is described by the agent function that maps any given percept sequence to an action (Function that perform decision making based on perception history).


# Task Environment
<p class="stickies">
Task environments, which are essentially the “problems” to which rational agents are the “solutions.”We group all these under the heading of the task environment.
</p>

Task environment fully descripes and defines the agent's objective, including what the agent's working environment is like, what's the definition of a good environment state, and how the agent will percept and interact with the environment.

>When designing an agent, the first step must always to be specify the task environment **as fully as possible**.

## PEAS (define task environment)
- Performance Measure
	- The environment states that resulted from the sequence of actions that the agent took.
	- There is no fixed performance measure, we need to define it ourselves and include as much as relevant factors as possible.
	- *It's better to define it according to the desired environment state other than the desired agent behaviour.*
- Environment
	- The environment the agent will be working with.
- Actuators
	- The components that the agent uses to interact with the environment.
- Sensors
	- The components that the agent uses to percept the environment

# Properties of Task Environments
#### 1. Fully observable vs. Partially observable
Depends on the **performance measure**, if the agent's sensors give all the relevant states of the environment at any given time.
> Unobservable environment:
> The agent has no sensors or can not percept the environment at all.

#### 2. Single agent vs. Multi-agent
Number of agents involved in the task environment.
> Multi-agent relationships
> - Competitive: One agent's rational action will deduce other agents' performance measure.
> - Cooperative: One agent's rational action improve other agents' performance measure.

#### 3. Deterministic vs. Stochastic vs. Uncertain vs. Nondeterministic
If the next state of the **environment** is completely determined by the **agent's state** and **the agent's action**, then the task environment is *deterministic*, otherwise, it's *stochastic*.

The task environment is *uncertain* if it's not fully observable or not deterministic. In *stochastic* task environment, the uncertainty follows probability rules.

A *nondeterministic* task environment means the actions are characterized by their possible outcomes without knowing the probability. So usually needs agent to succeed for **all possible** outcomes of its actions.

#### 4. Episodic vs. Sequential
If each action the agent takes is independent, then the task environment is *episodic*.
If the agent's acion can affect all future decisions, then the task environment is *sequential*.
#### 5. Static vs. Dynamic vs. Semidynamic
If the environment can change when the agent is deliberating (thinking), then it's a *dynamic* task environment, otherwise, it's *static*.
*Semi-dynamic* task environment means the environment will not change while the agent is thinking, but the time spent by the agent will affect the performance measure.

#### 6. Discrete vs. Continuous
If the task environment has a finite number of distinct states, then it's *discrete*, otherwise, its *continuous*.

#### 7. Known vs. Unknown
If the **agent** knows the rules of the environment, ie. knows the outcome of every action, then the task environment is *known*, otherwise, the task environment is *unknown*.

<p class="stickies">
Known vs. Unknow is different from Observable vs. Partially-Observable
</p>

>Solitaire card games are *Known* and *Partially Observable*.
The rules are known but the agent can not sense the cards that haven't been dealt yet.

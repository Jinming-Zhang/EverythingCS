##### Initial Distribution
$$\begin{pmatrix} \frac{1}{3}\\\ \frac{1}{3} \\\ \frac{1}{3} \end{pmatrix}$$
##### Transition Model (T):
$$\begin{pmatrix}0.8 & 0.2 & 0.3\\\ 0.1 & 0.6 & 0.3\\\ 0.1 & 0.2 & 0.4\end{pmatrix}$$
##### Sensor Model (S_True):
$$\begin{pmatrix}0.8 & 0 & 0\\\ 0 & 0.7 & 0\\\ 0 & 0 & 0.6\end{pmatrix}$$
##### Sensor Model (S_False):
$$\begin{pmatrix}0.2 & 0 & 0\\\ 0 & 0.3 & 0\\\ 0 & 0 & 0.4\end{pmatrix}$$


### a)
##### Explain the formula
Based on the transition matrix defined above, at each iteration, we get an updated belief by multiplying the probability from different scenarios with the previous belief.

For example, the first row of the transition matrix consist of the probability of transition from Sunny to Sunny, from Cloudy to Sunny and from Rainy to Sunny, when multiplying the first row of the transition matrix with our previous belief,  we'll get the belief for next iteration (before any event occurs).

After we multiply the transition matrix with previous belief, we'll get the belief for each scenario for next iteration, then we can update the belief by the event, which is multiplying the sensor model matrix (true/false based on the evidence) with the result.

The last step is to normalize the result so it can be interpreted as a probability.

Combine all the steps, we'll have the equation for each iteration, which is
$$F_{t+1}= \alpha_{t+1}\cdot O_{t+1}\cdot F_t $$
where $\alpha_{t+1}$ is the normalization matrix at t+1, $O_{t+1}$ is the corresponding sensor model matrix based on the event at t+1.

##### Find the filtering probability
To find $P(X_3|E_1=angry, E_2=happy, E_3=angry)$,  first find 
- $P(X_2|E_1=angry, E_2=happy)$ and 
- $P(X_1|E_1=angry)$

1. $F_1=P(X_1|E_1=angry) = S_{False} \cdot T \cdot initialDistribution$
$= \begin{pmatrix}0.2 & 0 & 0\\\ 0 & 0.3 & 0\\\ 0 & 0 & 0.4\end{pmatrix} \cdot\begin{pmatrix}0.8 & 0.2 & 0.3\\\ 0.1 & 0.6 & 0.3\\\ 0.1 & 0.2 & 0.4\end{pmatrix} \cdot \begin{pmatrix} \frac{1}{3}\\\ \frac{1}{3} \\\ \frac{1}{3} \end{pmatrix}$
$=[0.08667, 0.1, 0.0933], \text{normalize to}$
$=[0.3095, 0.3571, 0.3333]$

2. $F_2 = P(X_2|E_1=angry, E_2=happy) = S_{True}\cdot T\cdot F_1$
$= \begin{pmatrix}0.8 & 0 & 0\\\ 0 & 0.7 & 0\\\ 0 & 0 & 0.6\end{pmatrix} \cdot\begin{pmatrix}0.8 & 0.2 & 0.3\\\ 0.1 & 0.6 & 0.3\\\ 0.1 & 0.2 & 0.4\end{pmatrix} \cdot \begin{pmatrix} 0.3095 \\\ 0.3571 \\\ 0.3333 \end{pmatrix}$
$=[0.3352, 0.2417, 0.1414], \text{normalize to}$
$=[0.4667, 0.3364, 0.1969]$

3.  $F3=P(X_3|E_1=angry, E_2=happy, E_3=angry)= S_{False}\cdot T\cdot F_2$
$= \begin{pmatrix}0.2 & 0 & 0\\\ 0 & 0.3 & 0\\\ 0 & 0 & 0.4\end{pmatrix} \cdot\begin{pmatrix}0.8 & 0.2 & 0.3\\\ 0.1 & 0.6 & 0.3\\\ 0.1 & 0.2 & 0.4\end{pmatrix} \cdot \begin{pmatrix} 0.4667 \\\ 0.3364 \\\ 0.1969 \end{pmatrix}$
$=[0.09994, 0.092277, 0.077], \text{normalize to}$
$=[0.3711, 0.3427, 0.2862]$

Therefore, $P(X_3|E_1=angry, E_2=happy, E_3=angry)=[0.3711, 0.3427, 0.2862]$, with 
- P(X=sun)=0.3711
- P(X=cloudy)=0.3427
- P(X=rainy)=0.2862

### b)
##### n=6
$$F_6 =\alpha \cdot T^3\cdot F_3=\begin{pmatrix}0.8 & 0.2 & 0.3\\\ 0.1 & 0.6 & 0.3\\\ 0.1 & 0.2 & 0.4\end{pmatrix}^3\cdot \begin{pmatrix} 0.3711 \\\ 0.3427 \\\ 0.2862 \end{pmatrix}$$

$$\implies \begin{pmatrix} 0.5156 \\\ 0.2939 \\\ 0.1905 \end{pmatrix}$$
##### n=10000
As $n->\infty$ , the result will approach to the steady state, which is the normalized eigen vector of transition matrix: \[0.5454, 0.2728, 0.1818\]

By calculating $F_10000$
$$F_6 =\alpha \cdot T^{9997}\cdot F_3=\begin{pmatrix}0.8 & 0.2 & 0.3\\\ 0.1 & 0.6 & 0.3\\\ 0.1 & 0.2 & 0.4\end{pmatrix}^{9997}\cdot \begin{pmatrix} 0.3711 \\\ 0.3427 \\\ 0.2862 \end{pmatrix}$$

$$\implies \begin{pmatrix} 0.5454 \\\ 0.2728 \\\ 0.1818 \end{pmatrix}$$
### c)
Smoothing probability
$P(X_1|E_1=angry, E_2=happy, E_3=angry)$
$=P(X_1|E_1=angry)\times P(E_2=happy, E_3=angry|X_1)$
$=F_1\times P(E_2=happy, E_3=angry|X_1)$


Let $B_2=P(E_3=angry|X_2)$, then 
$$B_2 = T\cdot S_{False}\cdot [1,1,1]=\begin{pmatrix}0.8 & 0.2 & 0.3\\\ 0.1 & 0.6 & 0.3\\\ 0.1 & 0.2 & 0.4\end{pmatrix} \cdot \begin{pmatrix}0.2 & 0 & 0\\\ 0 & 0.3 & 0\\\ 0 & 0 & 0.4\end{pmatrix} \cdot \begin{pmatrix} 1 \\\ 1 \\\ 1 \end{pmatrix}$$
$$B_2=\begin{pmatrix} 0.3778 \\\ 0.3556 \\\ 0.2667 \end{pmatrix}$$

 We can get $B_1=P(E_2=happy, E_3=angry|X_1)$
 $$B_1 = T\cdot S_{True}\cdot B_3=\begin{pmatrix}0.8 & 0.2 & 0.3\\\ 0.1 & 0.6 & 0.3\\\ 0.1 & 0.2 & 0.4\end{pmatrix}\cdot \begin{pmatrix}0.8 & 0 & 0\\\ 0 & 0.7 & 0\\\ 0 & 0 & 0.6\end{pmatrix}\cdot \begin{pmatrix} 0.3778 \\\ 0.3556 \\\ 0.2667 \end{pmatrix}$$
$$B_1=\begin{pmatrix} 0.4775 \\\ 0.32 \\\ 0.2025 \end{pmatrix}$$
Finally, we can get the smoothing probability of $P(X_1|E_1=angry, E_2=happy, E_3=angry)$
$=F_1 \times P(E_2=happy, E_3=angry|X_1)$
$=F_1 \times B_1$
$=\begin{pmatrix} 0.3095\cdot 0.4775 \\\ 0.3571\cdot 0.32 \\\ 0.3333\cdot 0.2025 \end{pmatrix}$
normalized to $\begin{pmatrix} 0.4484 \\\ 0.3468 \\\ 0.2048 \end{pmatrix}$


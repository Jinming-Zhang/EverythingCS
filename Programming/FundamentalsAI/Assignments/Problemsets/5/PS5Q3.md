##### Initial Distribution
$$\begin{pmatrix} \frac{1}{3}\\\ \frac{1}{3} \\\ \frac{1}{3} \end{pmatrix}$$
##### Transition Model (T):
$$\begin{pmatrix}0.6 & 0.2 & 0.4\\\ 0.3 & 0.3 & 0.1\\\ 0.1 & 0.5 & 0.5\end{pmatrix}$$
##### Sensor Model (S_True):
$$\begin{pmatrix}0.9 & 0 & 0\\\ 0 & 0.8 & 0\\\ 0 & 0 & 0.7\end{pmatrix}$$
##### Sensor Model (S_False):
$$\begin{pmatrix}0.1 & 0 & 0\\\ 0 & 0.2 & 0\\\ 0 & 0 & 0.3\end{pmatrix}$$


### a)
To find the steady state of P(X), calculate the eigenvector of the transition model:
$$\begin{pmatrix}0.6 & 0.2 & 0.4\\\ 0.3 & 0.3 & 0.1\\\ 0.1 & 0.5 & 0.5\end{pmatrix}\cdot \begin{pmatrix} x\\\ y \\\ z \end{pmatrix}= \begin{pmatrix} x\\\ y \\\ z \end{pmatrix}$$
and solve for x, y, z, we get:
$$\begin{pmatrix} x\\\ y \\\ z \end{pmatrix}= \begin{pmatrix} 0.7408 \\\ 0.3951 \\\ 0.5433 \end{pmatrix}$$
Then we normalize the vector, and get:
$$\begin{pmatrix} x\\\ y \\\ z \end{pmatrix}= \begin{pmatrix} 0.4412 \\\ 0.2353 \\\ 0.3235 \end{pmatrix}$$
So at steady state, $P(X) = [0.4412, 0.2353, 0.3235]$

### b)
To find $P(X_3|E_1=happy, E_2=happy, E_3=angry)$,  first find 
- $P(X_2|E_1=happy, E_2=happy)$ and 
- $P(X_1|E_1=happy)$

1. $F_1=P(X_1|E_1=happy) = S_{True} \cdot T \cdot initialDistribution$
$= \begin{pmatrix}0.9 & 0 & 0\\\ 0 & 0.8 & 0\\\ 0 & 0 & 0.7\end{pmatrix} \cdot\begin{pmatrix}0.6 & 0.2 & 0.4\\\ 0.3 & 0.3 & 0.1\\\ 0.1 & 0.5 & 0.5\end{pmatrix} \cdot \begin{pmatrix} \frac{1}{3}\\\ \frac{1}{3} \\\ \frac{1}{3} \end{pmatrix}$
$=[0.36, 0.1867, 0.2567], \text{normalize to}$
$=[0.4481, 0.2324, 0.3195]$

2. $F_2 = P(X_2|E_1=happy, E_2=happy) = S_{True}\cdot T\cdot F_1$
$= \begin{pmatrix}0.9 & 0 & 0\\\ 0 & 0.8 & 0\\\ 0 & 0 & 0.7\end{pmatrix} \cdot\begin{pmatrix}0.6 & 0.2 & 0.4\\\ 0.3 & 0.3 & 0.1\\\ 0.1 & 0.5 & 0.5\end{pmatrix} \cdot \begin{pmatrix} 0.4481 \\\ 0.2324 \\\ 0.3195 \end{pmatrix}$
$=[0.3988, 0.1889, 0.2245], \text{normalize to}$
$=[0.4910, 0.2325, 0.2764]$

3.  $F3=P(X_3|E_1=happy, E_2=happy, E_3=angry)= S_{False}\cdot T\cdot F_2$
$= \begin{pmatrix}0.1 & 0 & 0\\\ 0 & 0.2 & 0\\\ 0 & 0 & 0.3\end{pmatrix} \cdot\begin{pmatrix}0.6 & 0.2 & 0.4\\\ 0.3 & 0.3 & 0.1\\\ 0.1 & 0.5 & 0.5\end{pmatrix} \cdot \begin{pmatrix} 0.4910 \\\ 0.2325 \\\ 0.2764 \end{pmatrix}$
$=[0.045170, 0.048943, 0.091076], \text{normalize to}$
$=[0.2439, 0.2643, 0.4918]$

Therefore, $P(X_3|E_1=happy, E_2=happy, E_3=angry)=[0.2439, 0.2643, 0.4918]$, with 
- P(X=sun)=0.2439
- P(X=cloudy)=0.2643
- P(X=rainy)=0.4918

### c)
To find $P(X_5|E_1=happy, E_2=happy, E_3=angry)$, given $P(X_3|E_1=happy, E_2=happy, E_3=angry)$:
$P(X_5|E_1=happy, E_2=happy, E_3=angry)=T^2\cdot F_3$
$= \begin{pmatrix}0.6 & 0.2 & 0.4\\\ 0.3 & 0.3 & 0.1\\\ 0.1 & 0.5 & 0.5\end{pmatrix} \cdot\begin{pmatrix}0.6 & 0.2 & 0.4\\\ 0.3 & 0.3 & 0.1\\\ 0.1 & 0.5 & 0.5\end{pmatrix} \cdot \begin{pmatrix} 0.2439 \\\ 0.2643 \\\ 0.4918 \end{pmatrix}$
$=[0.4389, 0.2195, 0.3416]$

Therefore, $P(X_5|E_1=happy, E_2=happy, E_3=angry)=[0.4389, 0.2195, 0.3416]$, with 
- P(X=sun)=0.4389
- P(X=cloudy)=0.2195
- P(X=rainy)=0.3416
# Question #1
A -> Filtering
B -> Smoothing
C -> Prediction
# Question #2
$P(X_1|e_1) = [\frac{27}{31}, \frac{4}{31}]$
# Question #3
$B'(X_2)=[\frac{27}{31}\cdot 0.7 + \frac{4}{31}\cdot 0.3, \frac{27}{31}\cdot 0.3 + \frac{4}{31}\cdot 0.7]$
$=[0.64838709677, 0.35161290322]$
$B(X_2)=[0.64838709677\cdot 0.9, 0.35161290322\cdot 0.2]$
$B(X_2)=[0.58354838709, 0.07032258064]$
$B(X_2)=[0.58354838709, 0.07032258064]$
$B(X_2)=[\frac{0.58354838709}{0.65387096773}, \frac{0.07032258064}{0.65387096773}]$
$B(X_2)=[0.89245189936, 0.10754810063]$
# Question #4
B
# Question #5
State variables $W_t$ be if the student studied at week t.
Evidence variables $E_i$ be if the student passed the weekly quiz at week t.

By using viterbi algorithm, we can approximate probability of whether the student studied at week t+1 based  on if that student passed the weekly quiz at week t+1.
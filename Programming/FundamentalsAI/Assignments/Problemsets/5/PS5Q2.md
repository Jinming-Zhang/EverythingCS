### a)
##### P(C)
$P(C)=P(C|H,T)\cdot P(H,T)+P(C|H,\lnot T)\cdot P(H,\lnot T)+P(C|\lnot H,T)\cdot P(\lnot H,T)+P(C|\lnot H,\lnot T)\cdot P(\lnot H,\lnot T)$

$=0.85\cdot 0.3\cdot 0.8+0.9\cdot 0.3\cdot 0.2+0.7+0.7\cdot 0.2+0.3\cdot 0.7\cdot 0.8$
$=0.524$


##### P(D)
$P(D)=P(D|C)\cdot P(C) + P(D|\lnot C) \cdot P(\lnot C)$
$=0.8\cdot 0.524+0.1\cdot 0.476$
$=0.4668$


##### P(W)
$P(C)=0.524, P(\lnot C)=0.476$
$P(D)=0.4668, P(\lnot D)=0.5332$

$P(W)=P(W|D,C)\cdot P(D,C) +P(W|D,\lnot C)\cdot P(D,\lnot C) +P(W|\lnot D,C)\cdot P(\lnot D,C) +P(W|\lnot D,\lnot C)\cdot P(\lnot D,\lnot C)$
$=0.8\cdot 0.4668\cdot 0.476+0.9\cdot 0.4668\cdot 0.524+0.8\cdot 0.5332\cdot 0.524+0.1\cdot 0.476\cdot 0.5332$
$=0.64679808$

### b)
##### P(C|H)
$P(C|H)=P(C|H,T)\cdot P(T) + P(C|H,\lnot T)\cdot P(\lnot T)$
$=0.9\cdot 0.2+0.85\cdot 0.8$
$=0.86$
$P(\lnot C|H)=P(\lnot C|H,T)\cdot P(T) + P(\lnot C|H,\lnot T)\cdot P(\lnot T)$
$=0.1\cdot 0.2+0.15\cdot 0.8$
$=0.14$

##### P(D|H)
$P(D|H)=P(D|C,H)\cdot P(C|H) + P(D|\lnot C,H) \cdot P(\lnot C|H)$
$=0.8\cdot 0.86+0.1\cdot 0.14$
$=0.702$

$P(\lnot D|H)=0.298$

##### P(W|H)
$P(W|H)=P(W|D,C,H)\cdot P(D,C|H)$
$+P(W|D,\lnot C,H)\cdot P(D,\lnot C|H)$
$+P(W|\lnot D,C,H)\cdot P(\lnot D,C|H)$
$+P(W|\lnot D,\lnot C,H)\cdot P(\lnot D,\lnot C|H)$
$=0.8\cdot 0.702\cdot 0.14+0.9\cdot 0.702\cdot 0.86+0.8\cdot 0.298\cdot 0.86+0.1\cdot 0.14\cdot 0.298$
$=0.831168$

### c)
$P(H|W)=\frac{P(W|H)\cdot P(H)}{P(W)}=\frac{0.831168\cdot 0.3}{0.64679808}=0.38551505904$
# Q1
$P(cold|winter)=\frac{P(cold \cap winter)}{P(winter)}=\frac{0.1+0.14}{0.06+0.1+0.1+0.14}=0.6$
# Q2
$P(winter|cold)=\frac{P(cold \cap winter)}{P(cold)}=\frac{0.1+0.14}{0.02+0.1+0.04+0.14}=0.8$
# Q3
B

# Q4
0.84891
# Q5
| H | T | C | Probability |
|---|---|---|-------------|
| T | T | T | 0.9         |
| T | T | F | 0.1         |
| T | F | T | 0.85        |
| T | F | F | 0.15        |
| F | T | T | 0.7         |
| F | T | F | 0.3         |
| F | F | T | 0.3         |
| F | F | F | 0.7         |
$P(C)=0.6875$

| C | W | Probability |
|---|---|-------------|
| T | T | 0.9         |
| T | F | 0.1         |
| F | T | 0.2         |
| F | F | 0.8         |

$P(W)=0.55$

$P(H|W)=\frac{P(W|H)\cdot P(H)}{P(W)}=\frac{P(C|H)\cdot P(W|C) \cdot P(H)}{0.55}=\frac{\frac{1.6}{2.75}\cdot 0.9 \cdot 0.3}{0.55}\approx 0.28561983471$
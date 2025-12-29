A point p = (x,y), and a vector's direction v
the projected point $p'$ is $p'=(p'\cdot u)u$

The projection can be seen as two parts:
- direction, which is the vector u
- signed scalar, which means the length of the projection onto u

## Why dot product gives the signed scalar

Definition of dot product:
$$\vec{a}\cdot\vec{b}=|a|*|b|*cos(\theta)$$
This can also be written as:
$$\vec{a}\cdot\vec{b}=|a|*cos(\theta)*|b|$$
By trigonometry:
1. $cos(\theta)$ is the ratio between *the length of projected part of a onto b* over *length of a*. $\frac{\text{a project onto b}}{\text{length of a}}$ 
2. when we multiply it by magnitude of a, we get the length of a projected onto b

## Project onto vector of angle theta
when we represent the vector by angle, as $(cos(\theta), sin(\theta))$.
$$v = (cos(\theta), sin(\theta))$$
for a point (x,y), it's projection onto the vector is
$$\text{scalar} = (x,y)\cdot(cos(\theta), sin(\theta))=x* cos(\theta) + y* sin(\theta)$$
Then multiply the scalar onto the direction $v=(cos(\theta), sin(\theta))$:
$$p = [(x*cos(\theta)+y*sin(\theta))*cos(\theta), (x* cos(\theta) + y* sin(\theta))*sin(\theta)]$$

If we expand this, we can factor out a coefficient matrix:
$$M_\theta = \begin{bmatrix}
cos^2(\theta)           &  sin(\theta)*cos(\theta)\\
sin(\theta)*cos(\theta) &  sin^2(\theta)
\end{bmatrix}$$

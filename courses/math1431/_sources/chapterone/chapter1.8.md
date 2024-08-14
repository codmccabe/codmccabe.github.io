# Section 1.8 - Absolute Value Function

The absolute value of a number $a$, denoted $|a|$, gives the undirected distance from $a$ to $0$ on a number line. The absolute value function is defined as $$|x|=\begin{cases}
x & \text{if }x\ge0\\
-x & \text{if }x<0
\end{cases}.$$

:::{table}
|Eq or Ineq|Equivalent Form|Solution Set|
|---|---|---|
|Case 1: $\|x\|=k$|$x=k$ or $x=-k$|$\{-k,k\}$|
|Case 2: $0\le\|x\|<k$|$-k<x<k$|$(-k,k)$|
|Case 3: $\|x\|>k\ge0$|$x<-k$ or $x>k$|$(-\infty,-k)\cup(k,\infty)$|
:::
:::{prf:theorem}
:label: solutionabsequation
The equation $|x|=a$ if and only if $x=a$ or $x=-a$. Furthermore, $|x|=|a|$ if and only if $x=a$ or $x=-a$.
:::
::::{prf:example}
:label: 18absequation1
Solve $$|9-4x|=7$$
:::{dropdown} Solution:
Since $|x|=a$ if and only if $x=a$ or $x=-a$ we have $$\begin{aligned}
9-4x & =7 & 9-4x & =-7\\
-4x & =-2 & -4x & =-16\\
x & =\frac{-2}{-4} & x & =\frac{-16}{-4}\\
 & =\frac{1}{2} &  & =4\end{aligned}$$ Therefore, the solution set is $$x=\{\frac{1}{2},4\}$$
:::
::::
::::{prf:example}
:label: 18absequation2
Solve $$|3x+2|=|x-5|$$
:::{dropdown}
Since $\|x\|=\|a\|$ if and only if $x=a$ or $x=-a$ we have 
$$\begin{aligned}
3x+2 & =x-5 & 3x+2 & =-(x-5)\\
3x-x & =-5-2 & 3x+2 & =-x+5\\
2x & =-7 & 3x+x & =5-2\\
x & =\frac{-7}{2} & 4x & =3\\
 &  & x & =\frac{3}{4}\end{aligned}$$ 
Therefore, the solution set is $$x=\{-\frac{7}{2},\frac{3}{4}\}.$$
:::
::::
# Section 2.3 - Functions

:::{prf:definition} Relation
:label: relation
A relation is a set of ordered pairs. Alternatively, a relation is a correspondence from one set of numbers to another set of numbers. Each correspondence can be represented as an element and each element can be represented as an ordered pair. The first value of the ordered pair will be the independent variable and the second value of the ordered pair will be called the dependent variable.
:::

:::{prf:definition} Function
:label: function
A function is a relation in which, for each distinct value of the first component of the ordered pairs, there is exactly one value of the second component.
:::

:::{prf:theorem}
:label: functionSet
Let $f$ be a function where $x$ is the independent variable and is an element of the set $A$. Let $y$ be the dependent variable and is an element of the set $B$. Let $f$ be a correspondence $$f:A\to B$$ such that $$f=\left\{ (x,y)\,|\,x\in A\land y\in B\right\}$$ and for every $x\in A$ there is exactly one value $y\in B$ such that $(x,y)\in f$. Then $f$ is called a function.
:::

:::{prf:definition} Independent and Dependent Variable
:label: independentDependentVariable
For every relation consisting of a set of ordered pairs $(x,y)$, there are two important sets of elements.

-   The set of all values of the independent variables $x$ is the domain.

-   The set of all values of the dependent variable $y$ is the range.

:::

:::{prf:example}
:label: relationsandfunctions
Let $$\begin{aligned}
f & =\left\{ (1,2),(1,3),(2,2),(3,2)\right\} \\
g & =\left\{ (1,2),(2,5),(5,3),(4,8)\right\} \end{aligned}$$ where $f$ and $g$ are relations.

The relation $f$:

-   $f$ is not a function since $1\to2$ and $1\to3$. This means the first number does not relate to exactly one element in the second number.

-   The domain of the the relation $f$ is $\{1,2,3\}$.

-   The range of the relation $f$ is $\{2,5,3,8\}$.

-   The correspondence is $1\to2$, $1\to3$, $2\to2$, and $3\to2$ or the table of values is:

      | $x$ |  $y$|
      |:-----:| :-----:|
      |  1  |   2|
      |  1  |   3|
      |  2  |   2|
      |  3  |   2|

The relation $g$:

-   $g$ is a function.

-   The domain of the function is $\{1,2,5,4\}$.

-   The range of the function is $\{2,5,3,8\}$.

-   The correspondence is $1\to2$, $2\to5$, $5\to3$, and $4\to8$ or the table of values is:

     |  $x$ |  $y$|
     | :-----:| :-----:|
     |   1  |   2|
     |   2  |   5|
     |   5  |   3|
     |   3  |   8|

:::

:::{prf:definition} Variations of the Definition of Function
:label: functionVariation

1.  A function is a relation in which, for each distinct value of the first component of the ordered pairs, there is exactly one value of the second component.

2.  A function is a set of ordered pairs in which no first component is repeated.

3.  A function is a rule or correspondence that assigns exactly one range value to each distinct domain value.

4.  A function $f$ with the correspondence $x\to y$, where $y$ is a function of $x$ is denoted $$y=f(x)$$ and is called function notation.

    a.  If $y=f(x)$ and (for example) $(1,2)$ is an element of the function set then $$2=f(1).$$

:::

::::{prf:example}
:label: evalFunction1
Let $$f(x)=x^{2}+x-6.$$ Find $f(0)$ and solve $f(x)=0$.
:::{dropdown} Solution:
To find $f(0)$ we have $$\begin{aligned}
f(0) & =(0)^{2}+(0)-6\\
 & =-6\end{aligned}$$

To solve $f(x)=0$ we have $$\begin{aligned}
x^{2}+x-6 & =0\\
(x+3)(x-2) & =0\\
x & =\{-3,2\}\end{aligned}$$
:::
::::

::::{prf:example}
:label: functionxplush1
Let $$f(x)=x^{2}+x+1$$ Find $f(x+h)$.
:::{dropdown} Solution:
  $$\begin{aligned}
f(x+h) & =(x+h)^{2}+(x+h)+1\\
 & =(x^{2}+2xh+h^{2})+x+h+1\\
 & =x^{2}+2xh+h^{2}+x+h+1\end{aligned}$$
:::
::::

:::{prf:definition} Increasing, Decreasing, and Constant Functions
:label: incDecFunction
Suppose that a function $f$ is defined over an open interval $I$ and $x_{1}$ and $x_{2}$ are in $I$ (denoted $x_{1},x_{2}\in I$).

1.  The function $f$ is increasing over $I$ if and only if $f(x_{1})<f(x_{2})$ for all $x_{1}<x_{2}$.

2.  The function $f$ is decreasing over $I$ if and only if $f(x_{1})>f(x_{2})$ for all $x_{1}<x_{2}$.

3.  The function $f$ is constant over $I$ if and only if $f(x_{1})=f(x_{2})$ for all $x_{1}<x_{2}$.

:::
:::{prf:corollary} Relative Extremes (or Local Extremes)
:label: relativeExtreme
Suppose that a function $f$ is defined over an open interval $I$ and $c\in I$.

-   If near $x=c$, $f(c)$ is the largest or smallest value of $f$, then we say that $x=c$ is a relative extreme.

-   If for all $x\in I$, $f(c)$ is the largest or smallest value of $f$, then we say that $x=c$ is an absolute extreme.

:::
::::{prf:example}
:label: piecewisePlot
Define $$f(x)=\begin{cases}
2(x-1)^{2}+1 & 0\le x<1\\
2(x-2)^{2}+3 & 1\le x<2\\
3 & 2\le x<4
\end{cases}$$ and the plot is:
:::{tikz}
    \draw[dashed,gray!40](-1,-1)grid(5,5);
	\draw[->](-1,0)--(5,0)node[below right]{$x$};
	\draw[->](0,-1)--(0,5)node[above right]{$y$};
	\foreach \x in {1,2,3,4}
		\draw
			(\x,2pt)--(\x,-2pt)node[below,font=\tiny]{$\x$}
			(2pt,\x)--(-2pt,\x)node[left,font=\tiny]{$\x$}
		;
	\draw[thick,blue]
		(0,4) parabola bend (1,1) (1,1)
		parabola bend (2,3) (2,3)
		-- (4,3)
	;
:::
1. The function is increasing on $[0,1)$
2. The function is decreasing on $[1,2)$
3. The function is constant on $(2,4]$
::::

:::{prf:corollary} Domain of Important Functions (part one)
:label: domainList1

-   The domain of the function $f(x)=x$ is the set of all value $x$ such that $x$ is a real number. $$\text{dom}(x)=\{x\,|\,x\in\mathbb{R}\}$$

-   The domain of the function $f(x)=x^{n}$ where $n$ is any integer is the set of all value $x$ such that $x$ is a real number. $$\text{dom}(x^{n})=\{x\,|\,x\in\mathbb{R}\}$$

-   The domain of the function $f(x)=\sqrt{x}$ is the set of all $x$ such that $x\ge0$. $$\text{dom}(\sqrt{x})=\{x\,|\,x\ge0\}$$

-   The domain of the function $f(x)=\frac{1}{x}$ is the set of all $x$ such that $x\ne0$. $$\text{dom}(\frac{1}{x})=\{x\,|\,x\ne0\}$$

:::
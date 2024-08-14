# Section 2.4 - Linear Functions

:::{prf:definition}
:label: linearFunction
A function $f$ is a linear function if, for real numbers $m$ and $b$, $$f(x)=mx+b.$$

-   If $a\ne0$, then the domain and the range of $f$ are both $(-\infty,\infty)$.

-   If $a=0,$then we say $f$ is the constant function and the domain is $(-\infty,\infty)$. The plot of the constant function is described as a horizontal line.

-   The standard form linear equation is $$Ax+By=C$$ where $A,B,C\in\mathbb{Z}$ such that $A\ge0$ and $\text{gcf}(A,B,C)=1$.

-   Two or more integers with a greatest common factor of one is called relatively prime. For example, 6 and 25 are not prime individually; however, 6 and 25 are relatively prime when considered together.

-   The slope $m$ of the line through the point $(x_{1},y_{1})$ and $(x_{2},y_{2})$ is defined as follows $$m=\dfrac{\Delta y}{\Delta x}=\dfrac{y_{2}-y_{1}}{x_{2}-x_{1}}$$ where $\Delta x\ne0$. The slope of the line constructed from $y=mx+b$ is the change in $y$ over the change in $x$.

-   Whenever $\Delta x=0$ we say the line is vertical. This means the slope is undefined.

-   Whenever $\Delta y=0$ while $\Delta x\ne0$ we say the line is horizontal. The means the slope is zero.

:::
:::::{prf:example}
:label: linearRelationshipExample1
In 2009, the federal government spent \$141.1 billion on research and development. In 2017, \$118.3 billion was spent. Assuming a linear relationship, and find the average rate of change in the amount of money spend on R&D per year. Graph as a line segment, and interpret the result.
::::{dropdown} Solution:
If coordinates given is not obvious consider constructing a table of values. The two coordinates we have are $(x_{1},y_{1})=(2009,141.1)$ and $(x_{2},y_{2})=(2017,118.3)$. A linear relationship follows the model $$f(x)=mx+b$$ where $f(2009)=141.1$, $f(2017)=118.3$, $$\begin{aligned}
m & =\dfrac{y_{2}-y_{1}}{x_{2}-x_{1}}\\
 & =\dfrac{118.3-141.1}{2017-2009}\\
 & =-2.85\end{aligned}$$ This means the average rate of change in the amount of money spent on R&D per year is -2.85 billion dollars per year. The plot would look like:
:::{tikz}
    \draw[->](0,0)--(5,0)node[below right]{x (years)};
	\draw[->](0,0)--(0,5)node[above left]{y (billion dollars)};
	\draw
		(2pt,4)--(-2pt,4)node[left]{$141.1$}
		(2pt,3)--(-2pt,3)node[left]{$118.3$}
		(1,2pt)--(1,-2pt)node[below]{$2009$}
		(4,2pt)--(4,-2pt)node[below]{$2017$}
	;
	\draw[thick,blue,fill=blue]
		(0,4)circle(2pt)node[above right]{$(2009,141.1)$}
		(4,3)circle(2pt)node[above right]{$(2017,118.3)$}
		(0,4)--(4,3)
	;
:::
::::
:::::
It can be claimed that the change in R&D funding is not linear. A secant line can be used to approximate the rate of change of the curve over a change in $x$ (or change in the horizontal axis).

:::{prf:definition} Secant Line
:label: secantLine
Let $f$ be a function defined over an interval $I$ and $x_{1},x_{2}\in I$. The average rate of change of a function from $x_{1}$ to $x_{2}$ is defined as $$m_{ave}:=\dfrac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}.$$ The line through these two points is a secant line where the slope of the line is $m_{ave}$.
:::
:::{prf:definition} Business Models
:label: businessModels
Let $p$ be the price variable and $x$ be the number of units variable. We denote the cost function $C(x)$. We define the revenue function as $$R(x)=xp$$ where sometime $p$ is a demand function with respect to $x$. We define the profit function as $$P(x)=R(x)-C(x).$$
:::

::::{prf:example}
:label: businessModelExample1
Assume that the cost to produce an item is a linear function and that all items produced are sold. The fixed cost is \$1500, the variable cost per item is \$100, and the item sells for \$125.

1.  Find the cost function.

2.  Find the revenue function.

3.  Find the profit function.

4.  According to the profit function, what happens if zero units are sold, and will the company make a profit?
:::{dropdown} Solution:
Since it costs \$100 to produce each unit and there is a fixed cost of \$1500 we can define the cost function as $$C(x)=100x+1500.$$ Since each unit is sold for \$125 we have the revenue function $$R(x)=125x.$$ All together we have $$\begin{aligned}
P(x) & =R(x)-C(x)\\
 & =125x-(100x+1500)\\
 & =25x-1500\end{aligned}$$

Note, that $P(0)=-1500$ which means that if zero units are sold then the profit would be $-\$1500$ (a loss of 1500 dollars).

Note, that $P(x)>0$ is when the company will make a profit. $$\begin{aligned}
P(x) & >0\\
25x-1500 & >0\\
25x & >1500\\
x & >\frac{1500}{25}\\
x & >60\end{aligned}$$ This means that after 60 units are sold the company will make a profit\... Why will the company continue to make a profit?
:::
::::
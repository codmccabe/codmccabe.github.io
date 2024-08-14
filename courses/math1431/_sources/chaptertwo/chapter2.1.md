
# Section 2.1 - Rectangular Coordinates and Graphs

:::{prf:definition} Major Definitions:

-   An ordered pair consists of two components, written inside parentheses.

-   Given two real number lines intersecting perpendicularly at $(0,0)$ makes up the rectangular coordinate system.

-   The intersection of the two number lines at $(0,0)$ is called the origin.

-   The number lines are called axis, the horizontal axis is the $x$-axis and the vertical axis is the $y$-axis.

-   The plane into which the coordinate system is introduced is the coordinate plane, or $xy$-plane.

-   The $x$-axis and $y$-axis divide the plane into four regions, or quadrants. Points on the $x$-axis or $y$-axis belong to no quadrant.

-   Let $(x_{1},y_{1})$ and $(x_{2},y_{2})$ be two points on the $xy$-plane $$\begin{aligned}
    \Delta x & =x_{2}-x_{1}\\
    \Delta y & =y_{2}-y_{1}\\
    d & =\sqrt{\left(\Delta x\right)^{2}+\left(\Delta y\right)^{2}}\\
     & =\sqrt{(x_{2}-x_{1})^{2}+(y_{2}-y_{1})^{2}}\\
    M & =\left(\frac{x_{1}+x_{2}}{2},\frac{y_{1}+y_{2}}{2}\right)\end{aligned}$$ where $\Delta x$ is the change in $x$, $\Delta y$ is the change in $y$, $d$ is the distance between $(x_{1},y_{1})$ and $(x_{2},y_{2})$, and $M$ is the midpoint between $(x_{1},y_{1})$ and $(x_{2},y_{2})$.

-   The solution to a one variable equation can be represented as $x=a$ on the $x$-axis.

-   The solution to a two variable equation can be represented as an ordered on the $xy$-plane.

-   The graph of an equation is found by plotting ordered pairs that are solutions to the equation, sometimes called constructing a table of values. The intercepts of the graph are good points to plot first. An $x$-intercept is a point where the graph intersects the $x$-axis. A $y$-intercept is a point where the graph intersects the $y$-axis.
:::
::::{prf:example}
:label: collinear1
Determine whether the three points are collinear.

- $(0,-7)$, $(-3,5)$, and $(2,-15)$
:::{dropdown} Solution:
The distance between $(0,-7)$ and $(-3,5)$ is
\begin{align*}
d & =\sqrt{(0-(-3))^{2}+(-7-5)^{2}}\\
 & =\sqrt{9+144}\\
 & =\sqrt{153}\text{ or }3\,\sqrt{17}
\end{align*}

The distance between $(0,-7)$ and $(2,-15)$ is
\begin{align*}
d & =\sqrt{(0-2)^{2}+(-7-(-15))^{2}}\\
 & =\sqrt{4+64}\\
 & =\sqrt{68}\text{ or }2\,\sqrt{17}
\end{align*}
The distance between $(-3,5)$ and $(2,-15)$ is
\begin{align*}
d & =\sqrt{(-3-2)^{2}+(5-(-15))^{2}}\\
 & =\sqrt{25+400}\\
 & =\sqrt{425}\text{ or }5\,\sqrt{17}
\end{align*}
As we can see $3\sqrt{17}+2\sqrt{17}=5\sqrt{17}$ which implies the
three points are collinear.
:::

- $(-1,-3)$, $(-5,12)$, and $(1,-11)$
:::{dropdown} Solution:
The distance from $(-1,-3)$ to $(-5,12)$ is $\sqrt{241}\approx15.5$.

The distance from $(-1,-3)$ to $(1,-11)$ is $2\sqrt{17}\approx8.2$.

The distance from $(-5,12)$ to $(1,-11)$ is $\sqrt{565}\approx23.8$. 

Since 
$$
\sqrt{241}+2\sqrt{17}\ne\sqrt{565}
$$
we say the three points are not collinear.
::::

:::::{prf:example}
:label: plotpoints
Plot the following from a table of values:

|$x$|-7|-5|4|6|
|-|--|--|-|-|
|$y$|-5|4|-2|5|

::::{dropdown} Solution:
:::{tikz}
    [scale=0.2]
	\draw[dashed,gray!50](-8,-8)grid(8,8);
	\draw[<->](-8,0)--(8,0)node[below right]{$x$};
	\draw[<->](0,-8)--(0,8)node[above right]{$y$};
	\foreach \x in {-7,...,-2,-1,1,2,...,7}
	\draw[font=\tiny]
		(\x,2pt)--(\x,-2pt)
		(2pt,\x)--(-2pt,\x)
	;
	\draw[blue,fill=blue]
		(-7,-5)circle(4pt)
		(-5,4)circle(4pt)
		(4,-2)circle(4pt)
		(6,5)circle(4pt)
	;
:::
::::

|$x$|-3|-2|-1|0|
|---|--|--|--|-|
|$y$|9|4|1|0|

::::{dropdown} Solution:
:::{tikz}
    [scale=0.2]
	\draw[dashed,gray!50](-10,-10)grid(10,10);
	\draw[<->](-10,0)--(10,0)node[below right]{$x$};
	\draw[<->](0,-10)--(0,10)node[above right]{$y$};
	\foreach \x in {-9,-8,-7,...,-2,-1,1,2,...,7,8,9}
	\draw[font=\tiny]
		(\x,2pt)--(\x,-2pt)
		(2pt,\x)--(-2pt,\x)
	;
	\draw[blue,fill=blue]
		(-3,9)circle(4pt)
		(-2,4)circle(4pt)
		(-1,1)circle(4pt)
		(0,0)circle(4pt)
	;
:::
::::

:::::


Given the two variable equation construct a table of values and plot the ordered pairs on the $xy$-plane.

1.  $2y-x=-2$

2.  $y-\sqrt{x}=-3$

3.  $y=x^{2}$
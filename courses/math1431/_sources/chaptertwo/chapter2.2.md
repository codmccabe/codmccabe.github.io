# Section 2.2 - Circles

:::{prf:definition}
:label: circle
A circle is the set of all points in a plane that lie a given distance from a given point. The given distance is called the circle's radius, denoted $r$, and the given point is called the center, denoted $(h,k)$. The equation that satisfies this definition is $$(x-h)^{2}+(y-k)^{2}=r^{2}.$$

The equation $x^{2}+y^{2}=1$ defines the unit circle (since the radius of the circle is $1$ and is centered at $(0,0)$).
:::

Consider: 

$$\begin{aligned}
(x-h)^{2}+(y-k)^{2} & =c\iff\\
(x-h)^{2}+(y-k)^{2}-c & =0\iff\\
y^{2}-2\,k\,y+x^{2}-2\,h\,x+k^{2}+h^{2}-c & =0\iff\\
x^{2}+y^{2}+(-2h)x+(-2k)y+\left(k^{2}+h^{2}-c\right) & =0\iff\\
x^{2}+y^{2}+Dx+Ey+F & =0\end{aligned}$$

:::{prf:definition} General Form of the Equation of a Circle
:label: generalCircleEQ

From some real number $D,$$E$, and $F$, the equation $$x^{2}+y^{2}+Dx+Ey+F=0$$ can have a graph that is a circle or a point or is nonexistent.
:::

:::{prf:corollary}
:label: circleEQConditions
Given $$(x-h)^{2}+(y-k)^{2}=c$$ for any number $c$.

1.  If $c>0$, then $r^{2}=c$, and the graph of the equation is a circle with radius $\sqrt{c}$.

2.  If $c=0$, then the graph of the equation is the single point $(h,k)$.

3.  If $c<0$, then no points satisfy the equation, and the graph is nonexistent.

:::

::::{prf:example}
:label: solveCompletingSquare1
Solve by completing the square $$6x^{2}+13x+5=0$$
:::{dropdown} Solution:
First, divide by $6$ to get the leading coefficient equal to one. $$x^{2}+\frac{13}{6}x+\frac{5}{6}=0.$$ Second, subtract $\frac{5}{6}$ from both sides and leave space to "complete the square". $$x^{2}+\frac{13}{6}x+\underline{\,\,\,\,}=-\frac{5}{6}+\underline{\,\,\,\,}.$$ Third, complete the square by adding $\left(\dfrac{\frac{13}{6}}{2}\right)^{2}=\left(\dfrac{13}{12}\right)^{2}=\dfrac{169}{144}$ to both sides $$\begin{aligned}
x^{2}+\frac{13}{6}x+\frac{169}{144} & =-\frac{5}{6}+\frac{169}{144}\\
\left(x+\frac{13}{12}\right)^{2} & =\frac{49}{144}\\
x+\frac{13}{12} & =\pm\sqrt{\frac{49}{144}}\\
x & =-\frac{13}{12}\pm\frac{7}{12}=\begin{cases}
-\frac{13}{12}+\frac{7}{12} & =-\frac{6}{12}=-\frac{1}{2}\\
-\frac{13}{12}-\frac{7}{12} & =-\frac{20}{12}=-\frac{5}{3}
\end{cases}\end{aligned}$$

The solution $x=\{-\frac{1}{2},-\frac{5}{3}\}$.
:::
::::

::::{prf:example}
:label: centerradiusCircleprom1
Give the center center and radius of the circle with equation $$2x^{2}+2y^{2}+2x-6y=45$$

:::{dropdown} Solution:
First, we will divide both sides by $2$ to get $x^{2}$ and $y^{2}$ to have coefficients of one (in preparation of completing the square). $$\begin{aligned}
2x^{2}+2y^{2}+2x-6y & =45\\
x^{2}+y^{2}+x-3y & =\frac{45}{2}\end{aligned}$$ Second, we group up the $x$ and $y$ variable terms. Third, find the completing the square term by computing $\left(\frac{b}{2}\right)^{2}$. For $x$, $b=1$. For $y$, $b=-3$. $$\begin{aligned}
\left(x^{2}+x+\underline{\,\,\,}_{1}\right)+\left(y^{2}-3x+\underline{\,\,\,}_{2}\right) & =\frac{45}{2}+\underline{\,\,\,}_{1}+\underline{\,\,\,}_{2}\\
\underline{\,\,\,}_{1} & =\left(\frac{1}{2}\right)^{2}=\frac{1}{4}\\
\underline{\,\,\,}_{2} & =\left(\frac{-3}{2}\right)^{2}=\frac{9}{4}\\
\left(x^{2}+x+\frac{1}{4}\right)+\left(y^{2}-3x+\frac{9}{4}\right) & =\frac{45}{2}+\frac{1}{4}+\frac{9}{4}\\
\left(x+\frac{1}{2}\right)^{2}+\left(y-\frac{3}{2}\right)^{2} & =25\\
\left(x-\left(-\frac{1}{2}\right)\right)^{2}+\left(y-\frac{3}{2}\right)^{2} & =5^{2}\end{aligned}$$

This means, the implicit equation $2x^{2}+2y^{2}+2x-6y=45$ can be rewritten as $\left(x+\frac{1}{2}\right)^{2}+\left(y-\frac{3}{2}\right)^{2}=25$. From the second equation we notice $$\begin{aligned}
(h,k) & =(-\frac{1}{2},\frac{3}{2})\\
r^{2} & =25\implies r=\sqrt{25}=5.\end{aligned}$$ Therefore, the center for the circle is $(-\frac{1}{2},\frac{3}{2})$ and $r=5$.
:::
::::

::::{prf:example}
:label: centeradiusCircleProm2
Give the center and radius of the circle represented by the equation $$x^{2}+y^{2}+6x+8y+9=0.$$
:::{dropdown}
  $$\begin{aligned}
x^{2}+y^{2}+6x+8y & =-9\\
\left(x^{2}+6x+c_{1}\right)+\left(y^{2}+8y+c_{2}\right) & =-9+c_{1}+c_{2}\\
c_{1} & =\left(\frac{6}{2}\right)^{2}=\left(3\right)^{2}=9\\
c_{2} & =\left(\frac{8}{2}\right)^{2}=\left(4\right)^{2}=16\\
\left(x^{2}+6x+9\right)+\left(y^{2}+8y+16\right) & =-9+9+16\\
(x+3)^{2}+(y+4)^{2} & =16\\
(x-(-3))^{2}+(y-(-4))^{2} & =4^{2}\\
(h,k) & =(-3,-4)\\
r & =4\end{aligned}$$
:::
::::
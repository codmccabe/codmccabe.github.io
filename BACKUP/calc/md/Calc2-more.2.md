# More Stuff for Calc 2
* [Home](https://codmccabe.github.io/)
* [Calc Home](https://codmccabe.github.io/calc/)
* [Polar Coordinates and stuff](#PolarCord)
* [Area and Length of polar coordinates](#areaLengthPolar)
* [Conic](#conic)

<a id='PolarCord'></a>
## Polar Coordinates
---
### Equations Relating Polar and Cartesian Coordinates
$$x=r\cos(\theta)\, y=r\sin(\theta)\, r^2=x^2+y^2\, \tan(\theta)=\frac{y}{x}$$

#### Example of Catesian to Polar
Find a polar question for the circle $x^2+(y-3)^2=9$.

First, we want to expand the left hand side of the equation and hope that we can use the identities listed above. For example, we can anticipate $x^2+y^2$ as being present on the left hand side of the equation after we expand (use the distributive property) for the expression $(y-3)^2$. After we have grouped terms by there known polar to cartesian identities, we must also setup the equation to have all variables on one side of the equation and the constants on the other side of the equation. We hope that the left hand side of the equation can be completely replaced by $r$'s and trig functions and we have that the right hand side is zero. We then solve for $r$ (why we hope the right hand side is zero).

1. We expand the left hand side of the equation:
$$x^2+(y-3)^2 = x^2 + y^2 - 6y + 9$$
2. We organize:
$$\left(x^2+y^2\right) - 6\cdot y +9$$
3. We go back to the equation $x^2+(y-3)^2=9$ and subtract $9$ from both sides:
$$\left(x^2+y^2\right) - 6\cdot y +9 = 9 \iff \left(x^2+y^2\right) - 6\cdot y = 0$$
4. We use the identities,$y=r\sin(\theta)$ and $r^2=x^2+y^2$, and we factor the $r$:
$$\left(x^2+y^2\right) - 6\cdot y = 0 \iff r^2-6r\sin(\theta)=0\iff r\cdot \left(r-6\sin(\theta)\right)=0$$
5. Since $\sin(0)=0$ and solve the equation we have $r=0$ and $r=6\sin(\theta)$ we have the following that satisfies both equations
$$r=6\sin(\theta).$$

#### Example of Polar to Cartesian
Replace the polar equation, $r=\dfrac{4}{2\cos(\theta)-\sin(\theta)}$ by equivalent Cartesian equations.

Like the previous example we want all the trig functions and $r$'s to one side of the equation. Then the constants on the other side. We then rewrite the terms in such a way that we can compare them with the identities above.

1. Multiply $2\cos(\theta)-\sin(\theta)$ to both sides:
$$r\left(2\cos(\theta)-\sin(\theta)\right)=4$$
2. Use the distributative property:
$$2r\cos(\theta)-r\sin(\theta)  = 4$$
3. Use the identity $x=r\cos(\theta)$ and $y=r\sin(\theta)$:
$$2x-y=4$$
4. Then solve for $y$:
$$y=2x-4$$

---
### Symmetry Tests for Polar Graphs in the Cartesian $xy$-Plane
<a id='polarSym'>![image.png](attachment:image.png)</a>
1. Symmetry about the $x$-axis: If the point $(r,\theta)$ lies on the graph, then the point $(r,-\theta)$ or $(-r,\pi-\theta)$ lies on the graph.
2. Symmetry about the $y$-axis: If the point $(r,\theta)$ lies on the graph, then the point $(r,\pi-\theta)$ or $(-r,-\theta)$ lies on the graph.
3. Symmetry about the origin: If the point $(r,\theta)$ lies on the graph, then the point $(r,\theta)$ or $(r,\theta+\pi)$ lies on the graph.

---
### Slope of the Curve $r=f(\theta)$ in the Cartesian $xy$-Plane
<a id='polarSlope'>$$\left.\frac{dy}{dx}\right|_{(r,\theta)}=\dfrac{f'(\theta)\sin(\theta)+f(\theta)\cos(\theta)}{f'(\theta)\cos(\theta)-f(\theta)\sin(\theta)}$$</a> provided $\frac{dx}{d\theta}\ne 0$ at $(r,\theta)$.


* [Home](https://codmccabe.github.io/)
* [Calc Home](https://codmccabe.github.io/calc/)
* [Polar Coordinates and stuff](#PolarCord)
* [Area and Length of polar coordinates](#areaLengthPolar)
* [Conic](#conic)

<a id='areaLengthPolar'></a>
# Area and Length of Polar Coordinates


```maxima

```

* [Home](https://codmccabe.github.io/)
* [Calc Home](https://codmccabe.github.io/calc/)
* [Polar Coordinates and stuff](#PolarCord)
* [Area and Length of polar coordinates](#areaLengthPolar)
* [Conic](#conic)


```maxima

```

<a id='conic'></a>
# Conic


```maxima

```

* [Home](https://codmccabe.github.io/)
* [Calc Home](https://codmccabe.github.io/calc/)
* [Polar Coordinates and stuff](#PolarCord)
* [Area and Length of polar coordinates](#areaLengthPolar)
* [Conic](#conic)

## References:
[1](#polarSym) Screenshot from Thomas' 14th Edition Calculus Textbook page 686. 
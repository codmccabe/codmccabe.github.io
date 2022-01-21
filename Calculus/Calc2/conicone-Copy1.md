# Conic Section
* [Home](https://codmccabe.github.io)

### Theorem (Focus, Directrix, and Eccentricity)

Let $F$ be a fixed point (called the focus) and $l$ be a fixed line (called the directrix) in a plane. Let $e$ be a fixed positive number (called the eccentricity). The set of all points $P$ in the plane such that 

$$ \dfrac{|PF|}{|Pl|} = e $$

(that is, the ration of the distance from $F$ to the distance from $l$ is the constant $e$) is a connect section.

The conic is:
* a circle if $e=$,
* an ellipse if $e<1$,
* a parabola if $e=1$,
* or a hyperbola if $e>1$.

---
### Theorem (Polar Equation and Conic Section)

Assume $F$ (focus) is at the origin/pole.

A polar equation of the form:

$$r=\dfrac{ed}{1\pm e\cos(\theta)}\, \text{or}\, r=\dfrac{ed}{1\pm e\sin(\theta)}$$

represents a conic section with eccentricity $e$.

---

#### Example (Algebra Skills Check)

Write the equation $\dfrac{a}{b+cx}$ as $\dfrac{m}{1+nx}$ where $a,b,c,m,n$ are real numbers.

$$
\begin{array}{rl}
    \dfrac{a}{b+cx} & = \frac{a}{b+\frac{b}{b}\cdot cx}\\
    & = \dfrac{a}{b+b\cdot \frac{c}{b}x}\\
    & = \dfrac{a}{b\left(1+\frac{c}{b}x\right)}\\
    & = \dfrac{\frac{a}{b}}{1+\frac{c}{b}x}\\
    & = \dfrac{m}{1+nx}
\end{array}
$$

where $m=\frac{a}{b}$ and $n=\frac{c}{b}$.

---

### Definition (Conic Section General Form Equations)

A conic section has the general form

$$Ax^2+Bxy+Cy^2+Dx+Ey+F=0$$

where $A,B,C$ are non-zero real numbers.

### Theorem (Characteristics of the General Form Equations)

If $A$ and $C$ are non zero real numbers and $B=0$, then we have the following general equation:

$$Ax^2+Cy^2+Dx+Ey+F=0$$

and the conic has not been rotated.
* If $A\ne C$ and $AC>0$, then the equation represents an ellipse.
* If $A = C$, then the equation represents a circle.
* If $A<0$ or $C<0$, then the equation represents a hyperbola.
* IF $A$ or $C$ is allowed to be zero, then the equation represents a parabola.

<iframe src="https://www.geogebra.org/classic/tm2wpace?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

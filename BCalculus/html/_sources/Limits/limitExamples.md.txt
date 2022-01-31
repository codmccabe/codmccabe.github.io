# Limit Examples

Here we will look at specific examples using the limit.

### Recall:
Suppose

$$
\lim_{x\to a}f(x)=L\,\,\text{ and }\,\,\lim_{x\to a}g(x)=M
$$

Then
1. ${\displaystyle \lim_{x\to a}\left[f(x)\right]}^{r}{\displaystyle =\left[\lim_{x\to a}f(x)\right]^{r}=L^{r}}$
where $r$ is a positive number.
2. ${\displaystyle \lim_{x\to a}cf(x)=c\lim_{x\to a}f(x)=cL}$ where
$c$ is a real number.
3. ${\displaystyle \lim_{x\to a}\left[f(x)\pm g(x)\right]=\lim_{x\to a}f(x)\pm\lim_{x\to a}g(x)=L\pm M}$.
4. ${\displaystyle \lim_{x\to a}\left[f(x)g(x)\right]=\left[\lim_{x\to a}f(x)\right]\left[\lim_{x\to a}g(x)\right]=L\cdot M}$.
5. ${\displaystyle \lim_{x\to a}\frac{f(x)}{g(x)}=\frac{\lim_{x\to a}f(x)}{\lim_{x\to a}g(x)}=\frac{L}{M}}$
where $M\ne0$.
6. ${\displaystyle \lim_{x\to a}x}=a$
7. ${\displaystyle \lim_{x\to a}b}=b$
8. ${\displaystyle \lim_{x\to \infty}\frac{1}{x}}=0$ (thm. 5)
9. If $f(x)=g(x)$ for all $x\ne a$, then ${\displaystyle \lim_{x\to a}f(x)=\lim_{x\to a}g(x)}$. (cor. 1)
10. If $\lim_{x\to a^{+}}f(x)\ne\lim_{x\to a^{-}}f(x)$, then we say $\lim_{x\to a}f(x)$ does not exists. (cor. 2)


---

#### Example 1

Evaluate the limit:

$$
\lim_{x\to3}\dfrac{x^{2}+3x+4}{x^{2}+7}
$$

SOLUTION:

$$
\begin{align*}
\lim_{x\to3}\dfrac{x^{2}+3x+4}{x^{2}+7} & =\dfrac{\lim_{x\to3}x^{2}+\lim_{x\to3}3x+\lim_{x\to3}4}{\lim_{x\to3}x^{2}+\lim_{x\to3}7}\\
 & =\dfrac{\left(\lim_{x\to3}x\right)^{2}+3\lim_{x\to3}x+4}{\left(\lim_{x\to3}x\right)^{2}+7}\\
 & =\dfrac{\left(3\right)^{2}+3\cdot3+4}{\left(3\right)^{2}+7}\\
 & =\frac{11}{8}
\end{align*}
$$

---

#### Example 2
Evaluate the limit:

$$
\lim_{x\to64}\dfrac{\sqrt{x}-8}{x-64}
$$

SOLUTION:

$$
\begin{align*}
\lim_{x\to64}\dfrac{\sqrt{x}-8}{x-64} & =\lim_{x\to64}\dfrac{\sqrt{x}-8}{x-64}\cdot\left(\dfrac{\sqrt{x}+8}{\sqrt{x}+8}\right)\\
 & =\lim_{x\to64}\dfrac{x-64}{(x-64)\cdot(\sqrt{x}+8)}\\
 & =\lim_{x\to64}\dfrac{1}{\sqrt{x}+8}\\
 & =\dfrac{\lim_{x\to64}1}{\lim_{x\to64}\sqrt{x}+\lim_{x\to64}8}\\
 & =\dfrac{1}{\sqrt{\lim_{x\to64}x}+8}\\
 & =\dfrac{1}{\sqrt{64}+8}\\
 & =\dfrac{1}{8+8}\\
 & =\dfrac{1}{16}
\end{align*}
$$

---

#### Example 3

Let

$$
f(x)=\begin{cases}
x^{2}+1 & x\le1\\
3x-2 & x>1
\end{cases}
$$

Evaluate:

1. $f(1)$

2. ${\displaystyle \lim_{x\to1}f(x)}$

SOLUTION:

1. Evaluate $f(1)$ means to evaluate $f$ exactly when $x=1$. According
to the definition of the piecewise function we have

$$
f(1)=1^{2}+1=2.
$$
2. In order to evaluate this piecewise function we must first evaluate
$\lim_{x\to1^{-}}f(x)$ and $\lim_{x\to1^{+}}f(x)$. If the two are
equal $L$ then we say $\lim_{x\to1}f(x)=L$; however, if the two
are not equal we say $\lim_{x\to1}f(x)$ does not exist.

$$
\begin{aligned}\lim_{x\to1^{-}}f(x) & =\lim_{x\to1^{-}}\left(x^{2}+1\right)=1^{2}+1=2\\
\lim_{x\to1^{+}}f(x) & =\lim_{x\to1^{+}}\left(3x-2\right)=3(1)-2=1
\end{aligned}
$$

Since $\lim_{x\to1^{-}}f(x)\ne\lim_{x\to1^{+}}f(x)$ we say $\lim_{x\to1}f(x)$
does not exist.

---
#### Example 4
Evaluate the limit:

$$
\lim_{h\to0}\dfrac{\frac{1}{x+h}-\frac{1}{x}}{h}
$$

SOLUTION:

First, we will simplify $\dfrac{\frac{1}{x+h}-\frac{1}{x}}{h}$

$$
\begin{align*}
\dfrac{\frac{1}{x+h}-\frac{1}{x}}{h} & =\dfrac{\left(\frac{x}{x}\right)\cdot\frac{1}{x+h}-\frac{1}{x}\cdot\left(\frac{x+h}{x+h}\right)}{h}\\
 & =\dfrac{\frac{x-(x+h)}{x(x+h)}}{h}\\
 & =\dfrac{\frac{-h}{x(x+h)}}{h}\\
 & =\dfrac{1}{h}\cdot\left(\dfrac{-h}{x(x+h)}\right)\\
 & =-\dfrac{1}{x(x+h)}
\end{align*}
$$

Next, we notice that $\dfrac{\frac{1}{x+h}-\frac{1}{x}}{h}=-\dfrac{1}{x(x+h)}$
for all $h\ne0$. Thus, by Corollary 1 we have

$$
\lim_{h\to0}\dfrac{\frac{1}{x+h}-\frac{1}{x}}{h}=\lim_{h\to0}\dfrac{-1}{x(x+h)}=-\dfrac{1}{x(x+0)}=-\dfrac{1}{x^{2}}.
$$

---
#### Example 5
Evaluate the limit:

$$
\lim_{h\to0}\dfrac{\sqrt{x+h}-\sqrt{x}}{h}
$$

SOLUTION:

First, we simplify $\dfrac{\sqrt{x+h}-\sqrt{x}}{h}$:

$$
\begin{align*}
\dfrac{\sqrt{x+h}-\sqrt{x}}{h} & =\dfrac{\sqrt{x+h}-\sqrt{x}}{h}\cdot\left(\dfrac{\sqrt{x+h}+\sqrt{x}}{\sqrt{x+h}+\sqrt{x}}\right)\\
 & =\dfrac{(x+h)-(x)}{h\left(\sqrt{x+h}+\sqrt{x}\right)}\\
 & =\dfrac{h}{h\left(\sqrt{x+h}+\sqrt{x}\right)}\\
 & =\dfrac{1}{\sqrt{x+h}+\sqrt{x}}
\end{align*}
$$

Next, notice $\dfrac{\sqrt{x+h}-\sqrt{x}}{h}=\dfrac{1}{\sqrt{x+h}+\sqrt{x}}$
for all $h\ne0$. Thus, by Corollary 1 we have

$$
\lim_{h\to0}\dfrac{\sqrt{x+h}-\sqrt{x}}{h}=\lim_{h\to0}\dfrac{1}{\sqrt{x+h}+\sqrt{x}}=\dfrac{1}{\sqrt{x+0}+\sqrt{x}}=\dfrac{1}{2\sqrt{x}}
$$

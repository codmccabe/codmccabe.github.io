# Limits and Continuity

---
### Recall (Function):

#### Definition:
A function $f$ is a rule of correspondence that associates with each element $x$ in one set $D$, called the domain, a single value of $f(x)$ from a second set, $R$. The set of all values obtained is called the range of the function.

#### Domain/Range of Functions

Let $y=f(x)$.

|Name |$f(x)$|$n\in \mathbb{Z}$|$a\in \mathbb{R}$|Domain|Range|Example|
|:---|:---:|:---:|:---:|:---:|:---:|---|
|Polynomials|$f(x)=a_{n}x^{n}+\cdots+a_{1}x+a_{0}$|n/a|n/a| $\{ x \| x \in (-\infty,\infty) \}$ |$\{ y \| y \in (-\infty,\infty) \}$ |$f(x)=m x+b$ or $f(x)=ax^2+bx+c$|
|Radical|$f(x)=x^{1/n}=\sqrt[n]{x}$|$n$ is even|n/a|$\{ x\|x\in[0,\infty) \}$|$\{ y\|y\in(-\infty,\infty) \}$|$f(x)=\sqrt{x}$|
|Radical|$f(x)=x^{1/n}=\sqrt[n]{x}$|$n$ is odd|n/a|$\{ x\|x\in(-\infty,\infty) \}$|$\{ y\|y\in(-\infty,\infty) \}$|$f(x)=\sqrt[3]{x}$|
|Reciprocal|$f(x)=x^n$|$n<0$|n/a|$\{ x\|x\in(-\infty,0)\cup(0,\infty) \}$|$\{ y\|y\in(-\infty,0)\cup(0,\infty) \}$|$f(x)=\frac{1}{x}$|
|Exponential|$f(x)=a^x$|n/a|$a>0$ and $a\ne 1$|$\{ x\|x\in(-\infty,\infty) \}$|$\{ y\|y\in (0,\infty)\}$|$f(x)=e^x$|
|Logarithmic|$f(x)=\log_a(x)$|n/a|$a>0$ and $a\ne 1$|$\{ x\|x\in (0,\infty)\}$|$\{ y\|y\in(-\infty,\infty) \}$|$f(x)=\log_e(x)=\ln(x)$|

#### Combination of Functions:
Let $f$ and $g$ be two functions.
* $\left( f\pm g \right)(x)=f(x)\pm g(x)$
* $\left( f\cdot g \right)(x)=f(x)\cdot g(x)$
* $\left( \frac{f}{g} \right)(x)=\left(f\div g\right)(x)=f(x)\div g(x)=\dfrac{f(x)}{g(x)}$ where $g(x)\ne 0$ everywhere.
* $\left( f\circ g \right)(x)=f(g(x))$ the $\circ$ is the composition of functions operator.

Notice that $f\circ g \ne g\circ f$.

#### Monotonicity of Functions:
Let $f$ be a function of $x$ and for every $x_1$ and $x_2$, $a\le x_1<x_2 \le b$:
* If $f(x_1)<f(x_2)$, then $f$ is called an increasing function on the interval $[a,b]$.
* If $f(x_1)>f(x_2)$, then $f$ is called a decreasing function on the interval $[a,b]$.

### Recall (Limits):
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

## Continuity of Functions

#### Definition (Three steps to continuity):
A function $f$ is continuous at a number $x=a$ if the following
conditions are satisfied.
1. $f(x)$ is defined
2. ${\displaystyle \lim_{x\to a}f(x)}$ exists
3. ${\displaystyle \lim_{x\to a}f(x)=f(a)}$

If $f$ is not continuous at $x=a$, then $f$ is said to be discontinuous at $x=a$.

#### Properties of Continuous Functions:
1. The constant function $f(x)=c$ is continuous everywhere.
2. The identity function $f(x)=x$ is continuous everywhere.

If $f$ and $g$ are continuous at $x=a$, then
1. $f\pm g$ is continuous at $x=a$.
2. $fg$ is continuous at $x=a$.
3. $\frac{f}{g}$ is continuous at $x=a$ provided that $g(a)\ne0$.

Let $P$ be a polynomial function and $R$ be a rational function
($R(x)=\frac{p(x)}{q(x)}$ where $p$ and $q$ are polynomials), then
1. $P$ is continuous everywhere.
2. $R$ is continuous everywhere except when $q(x)=0.$

#### Limits and Continuous Functions:
Let $p(x)$ and $q(x)$ be polynomial functions. Let $a$ be a real
number. Then:
1.

$$
\lim_{x\to a}p(x)=p(a)
$$

2.  

$$
\lim_{x\to a}\frac{p(x)}{q(x)}=\frac{p(a)}{q(a)}\text{ when } q(a)\ne0
$$

3.  

$$
\lim_{x\to a}e^{p(x)}=e^{p(a)}
$$

4.  

$$
\lim_{x\to a}\ln(p(x))=p(a)\text{ when } p(a)>0
$$

#### Intermediate Value Theorem (IVT)
If $f$ is a continuous function on a closed interval $[a,b]$, and
if $y_{0}$ is any value between $f(a)$ and $f(b)$, then $y_{0}=f(c)$
for some $c$ in $[a,b]$.

![ivtGraph1.svg](attachment:ivtGraph1.svg)

#### Definition
We say the solution of th equation $f(x)=0$ is a root of the equation or the zero of the function $f$.

#### Theorem
Let $f$ be continuous on the interval $[a,b]$. Then the following are true:
1. If $f(x)>0$ for all $x\in[a,b]$ then $f$ has no roots for all $x\in[a,b]$.
2. If $f(x)<0$ for all $x\in[a,b]$ then $f$ has no roots for all $x\in[a,b]$.

#### Corollary
Let $f$ be continuous on the interval $[a,b]$. Then the following are true:
1. If there exists a $c\in(a,b)$ such that $f(c)=0$ and $f(a)<0$, then $f(b)>0$.
2. If there exists a $c\in(a,b)$ such that $f(c)=0$ and $f(a)>0$, then $f(b)<0$.

#### Corollary
Let $f$ be continuous on the interval $(a,b)$. Let $a<x_1<c<x_2<b$ and $f(c)=0$. Then the following are true:
1. If $f(x_1)<0$, then $f(x)\le 0$ for all $x\in(a,c]$.
2. If $f(x_1)>0$, then $f(x)\ge 0$ for all $x\in(a,c]$.

If $f$ is continuous on the interval $(a,b)$, there exists a $c\in(a,b)$ such that $a<x_1<c<x_2<b$ and $f(c)=0$, and $f(x_2)>0$, then what can be said about all $x\in[c,b)$?

---
#### Example
Let $f(x)=x^2-1$. Where is $f(x)$ positive and where is $f(x)$ negative.

SOLUTION:

Notice that $f(1)=0$, $f(-1)=0$, and $f$ is continuous on $(-\infty,\infty)$.
1. Choose $x_1=-2<-1$. Since $f(-2)=3$ we have by Corollary that $f(x)>0$ for all $x\in(-\infty,-1)$.
2. Choose $x_1=0<1$. Since $f(0)=-1$ we have by Corollary that $f(x)<0$ for all $x\in(-1,1)$.
3. Choose $x_1=2>1$. Since $f(2)=3$ we have by Corollary that $f(x)>0$ for all $x\in(1,\infty)$.

Finally, we conclude that
1. $f(x)>0$ for all $x\in(-\infty,-1)\cup(1,\infty)$ and
2. $f(x)<0$ for all $x\in(-1,1)$.

Consider the graph:


```maxima
plot2d(x^2-1,[x,-3,3]);
```

![svg](./md/limitCont_files/./md/limitCont_6_0.svg)



#### Exercise:
Let $f(x)=\frac{x^3}{3}-4 x$. Find where $f$ is positive or negative using the same reasoning above. The solution should follow the image below:

\[HINT
1. Solve $f(x)=0$.
2. Create 4 subintervals.
3. Choose $x_1$ in each of the subintervals.
4. Make observations based on the Corollary.\]


```maxima
plot2d(x^3/3-4*x,[x,-5,5]);
```


![svg](./md/limitCont_files/./md/limitCont_8_0.svg)


---
#### Example
Let

$$
f(x)=\begin{cases}
x^2+1 & x\ne 1\\
k & x = 1
\end{cases}
$$

Find $k$ such that $f$ is continuous at $x=1$.

SOLUTION:

Need to find $k$ such that:
1. $\lim_{x\to 1}f(x)$ exists.
2. $f(1)$ exists.
3. $\lim_{x\to1}f(x)=f(1)$.

First notice:

$$
f(x)=\begin{cases}
x^{2}+1 & x\ne1\\
k & x=1
\end{cases}=\begin{cases}
x^{2}+1 & x<1\\
k & x=1\\
x^{2}+1 & x>1
\end{cases}
$$

(1) Evaluate

$$
\lim_{x\to1}f(x)=\begin{aligned}\lim_{x\to1^{-}}f(x)=\lim_{x\to1^{-}}\left(x^{2}+1\right)=(1)^{2}+1=2\\
\lim_{x\to1^{+}}f(x)=\lim_{x\to1^{+}}\left(x^{2}+1\right)=(1)^{2}+1=2
\end{aligned}
=2=\lim_{x\to1}f(x)
$$

which means $\lim_{x\to1}f(x)$ exists.

(2) Evaluate

$$
f(1)=k
$$

which means $f(1)$ exists.

(3) In order for $\lim_{x\to1}f(x)=f(1)$ we must set $k=2$. If $k=2$,
then

$$
\lim_{x\to1}f(x)=2=k=f(1).
$$

That is, in order for $f$ to be continuous at $x=1$, $k$ must be
$2$.


---
#### Example
Let

$$
f(x)=\begin{cases}
\frac{x^2-a^2}{x-a} & x\ne a\\
k & x=a
\end{cases}
$$

Find $k$ such that $f$ is continuous at $x=a$.

SOLUTION:

Need to find $k$ such that:
1. $\lim_{x\to a}f(x)$ exists.
2. $f(a)$ exists.
3. $\lim_{x\to a}f(x)=f(a)$.

First notice:

$$
f(x)=\begin{cases}
\frac{x^{2}-a^{2}}{x-a} & x\ne1\\
k & x=1
\end{cases}=\begin{cases}
\frac{x^{2}-a^{2}}{x-a} & x<a\\
k & x=a\\
\frac{x^{2}-a^{2}}{x-a} & x>a
\end{cases}
$$

(1) First, simplify

$$
\begin{align*}
\frac{x^{2}-a^{2}}{x-a} & =\dfrac{(x-a)(x+a)}{x-a)}\\
 & =x+a
\end{align*}
$$

Evaluate

$$
\lim_{x\to a}f(x)=\begin{aligned}\lim_{x\to a^{-}}f(x)=\lim_{x\to1^{-}}\frac{x^{2}-a^{2}}{x-a}=x+a=a+a=2a\\
\lim_{x\to a^{+}}f(x)=\lim_{x\to1^{+}}\frac{x^{2}-a^{2}}{x-a}=x+a=a+a=2a
\end{aligned}
=2a=\lim_{x\to a}f(x)
$$

which means $\lim_{x\to a}f(x)$ exists.

(2) Evaluate

$$
f(a)=k
$$
which means $f(a)$ exists.

(3) In order for $\lim_{x\to a}f(x)=f(a)$ we must set $k=2a$. If
$k=2a$, then

$$
\lim_{x\to1}f(x)=2a=k=f(1).
$$

That is, in order for $f$ to be continuous at $x=a$, $k$ must be
$2a$.

#### Exercise
Recall that the average rate of change of a function $f$ is

$$
\dfrac{f(x_2)-f(x_1)}{x_2-x_1}
$$

Let $f(x)=x^2$.
1. Find the average rate of change of the function $f$ as $x$ goes from $1$ to $2$.
2. Find the average rate of change of the function $f$ as $x$ goes from $0$ to $1$.
3. Find the average rate of change of the function $f$ as $x$ goes from $0.5$ to $1$.
4. Find the average rate of change of the function $f$ as $x$ goes from $1$ to $1.5$.
5. Attempt to find the instantaneous rate of change of the function $f$ at $x=1$.

(For (5.) use the method worked out from the previous example; here is the solutions to each part.)


```maxima
f(x):=x^2$
m(x1,x2):=(f(x2)-f(x1))/(x2-x1)$
m(2,1);
m(0,1);
m(0.5,1); m(1,1.5);
limit(m(x,1),x,1);
```
$$\tag{${\it \%o}_{48}$}3$$

$$\tag{${\it \%o}_{49}$}1$$

$$\tag{${\it \%o}_{50}$}1.5$$

$$\tag{${\it \%o}_{51}$}2.5$$

$$\tag{${\it \%o}_{52}$}2$$

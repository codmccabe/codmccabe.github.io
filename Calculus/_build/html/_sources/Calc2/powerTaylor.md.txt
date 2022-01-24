```maxima
set_plot_option([svg_file, "maxplot.svg"])$
```

# Power Series and Taylor Series
* [Home](https://codmccabe.github.io/index.html)
* [Calc Home](https://codmccabe.github.io/calc/index.html)
* [Power Series](#power)
* [Properties of Power Series](#propPower)
* [Taylor Series](#taylor)
* [Using Taylor Series](#usingTaylor)


<a id='power'></a>
## Power Series
* [Home](https://codmccabe.github.io/index.html)
* [Calc Home](https://codmccabe.github.io/calc/index.html)
* [Power Series](#power)
* [Properties of Power Series](#propPower)
* [Taylor Series](#taylor)
* [Using Taylor Series](#usingTaylor)

### Definition (Power Series)
A series of the form
$$ \sum_{n=0}^{\infty}c_nx^n = c_0 +c_1x+c_2x^2+\cdots$$
is a power series centered at $x=0$. A series of the form
$$\sum_{n=0}^{\infty}c_n\left(x-a\right)^n = c_0+c_1(x-a)+c_2(x-a)^2+\cdots$$
is a power series centered at $x=a$.

---
### Definition (Factorial)
Let $n$ be a natural number. Then $$n! = 1\cdot 2\cdot \dots \cdot (n-1)\cdot n$$

---
### Theorem (Convergence of a Power Series)
Consider the power series $\sum_{n=0}^{\infty}c_n(x-a)^n$. The series satisfies exactly one of the following properties:
1. The sereis converges at $x=a$ and diverges for all $x\ne a$.
2. The series converges for all real numbers $x$.
3. There exists a real number $R>0$ such that the series converges if $|x-a|<R$ and diverges if $|x-a|>R$. At the values $x$ where $|x-a|=R$, the series may converge or diverge.

---
### Definition (Radius of Converence)
Consider the power series $\sum_{n=0}^{\infty}c_n(x-a)^n$. The set of real numbers $x$ where the series converges is the interval of convergence. If there exists a real number $R>0$ such that the series converges for $|x-a|<R$ and diverges for $|x-a|>R$, then $R$ is the radius of convergence. If the series converges only at $x=a$, we say the radius of convergence is $R=0$. If the series converges for all real numbers $x$, we say the radius of convergence is $R=\infty$.

---
### Representing functions as Power Series

$$1+x+x^2+x^3+\cdots = \sum_{n=0}^{\infty}x^n$$
and
$$a+ar+ar^2+ar^3+\cdots = \frac{a}{1-r}$$
by geometric series.
Therefore, if $|x|<1$, the series $sum_{n=0}^{\infty}x^n$ converges to $\frac{1}{1-x}$ and
$$1+x+x^2+\cdots = \sum_{n=0}^{\infty}x^n = \frac{1}{1-x}$$ for $|x|<1$.

#### Example (Power Series for $\frac{1}{1+x^3}$)
Remember that the following $\sum_{n=0}^{\infty}x^n=\frac{1}{1-x}$ convergs when $|x|<1$. 

Consider, $\sum_{n=0}^{\infty}(-x^3) = \frac{1}{1-(-x^3)} = \frac{1}{1+x^3}$ converges if and only if $|-x^3|<1$.

#### Example (Power Series for $\frac{x^2}{4-x^2}$)
Remember from the Geometric Series:

$$\sum_{n=0}^{\infty}ar^n = a+ar+ar^2+\cdots = \frac{a}{1-r},$$

$$\sum_{n=0}^{\infty}\left(x^2\right)^n = \sum_{n=0}^{\infty}x^{2n} = \frac{1}{1-x^2},$$

$$
\begin{array}{rl}
    \frac{x^2}{4-x^2} & = \frac{x^2}{4(1-\frac{x^2}{4})}\\
    & = \frac{\frac{x^2}{4}}{1-\frac{x^2}{4}}\\
    & = \frac{\frac{x^2}{4}}{1-\left( \frac{x}{2}\right)^2}\\
    & = \frac{x^2}{4}\cdot \frac{1}{1-\left(\frac{x}{2}\right)^2},
\end{array}
$$

and
$$\frac{x^2}{4}\cdot \frac{1}{1-\left(\frac{x}{2}\right)^2} = \frac{x^2}{4}\cdot \sum_{n=0}^{\infty} \left(\frac{x}{2}\right)^{2n} = \sum_{n=0}^{\infty}\frac{x^2}{4}\cdot \left(\frac{x}{2}\right)^{2n}$$ where the series converges only if $\left|\left(\frac{x}{2}\right)^2\right|<1$.

---

<a id='propPower'></a>
## Properties of Power Series
* [Home](https://codmccabe.github.io/index.html)
* [Calc Home](https://codmccabe.github.io/calc/index.html)
* [Power Series](#power)
* [Properties of Power Series](#propPower)
* [Taylor Series](#taylor)
* [Using Taylor Series](#usingTaylor)

### Definition (Combining Power Series)
Suppose that the two power series $\sum_{n=0}^{\infty}c_nx^n$ and $\sum_{n=0}^{\infty}d_nx^n$ converges to the function $f$ and $g$, respectively, on a common interval $I$.
1. The power series $\sum_{n=0}^{\infty}\left(c_nx^n\pm d_nx^n\right)$ converges to $f\pm g$ on $I$.
2. For any integer $m\ge 0$ and any real number $b$, the power series $sum_{n=0}^{\infty}b x^m c_n x^n$ converges to $bx^mf(x)$ on $I$.
3. For ny integer $m\ge 0$ and any real number $b$, the series $\sum_{n=0}^{\infty}c_n\left(bx^m\right)^n$ converges to $f(bx^m)$ for all $x$ such that $bx^m$ is in $I$.

---
### Definition (Multiplying Power Series)
Suppose that the power series $\sum_{n=0}^{\infty}c_nx^n$ and $\sum_{n=0}^{\infty}d_nx^n$ converge to $f$ and $g$, respectively, on a common interval $I$.

Let $$e_n=c_0d_n+c_1d_{n-1}+c_2d_{n-2}+\cdots + c_{n-1}d_1+c_nd_0 = \sum_{k=0}^{n}c_kd_{n-k}.$$

Then
$$\left( \sum_{n=0}^{\infty}c_nx^n \right)\left( \sum_{n=0}^{\infty}d_nx^n \right) = \sum_{n=0}^{\infty}e_nx^n$$

and

$$\sum_{n=0}^{\infty}e_nx^n$$ converges to $f(x)\cdot g(x)$on $I$.

The series $\sum_{n=0}^{\infty}e_nx^n$ is known as the Cauchy product of the series $\sum_{n=0}^{\infty}c_nx^n$ and $\sum_{n=0}^{\infty}d_nx^n$.

---
### Theorem (Term-by-Term Differentiation and Integration for Power Series
Supose that the power series $\sum_{n=0}^{\infty}c_n(x-a)^n$ converges on the interval $(a-R,a+R)$ for some $R>0$. Let $f$ be the function defined by the series
$$f(x)=\sum_{n=0}^{\infty}c_n(x-a)^n = c_0+c_1(x-a)+\cdots$$ for $|x-a|<R$. Then $f$ is differentiable on the interval $(a-R,a+R)$ and we can find $f'$ by differentiating the series term-by-term:
$$f'(x)=\sum_{n=0}^{\infty}nc_n(x-a)^{n-1}$$
for $|x-a|<R$.

Also, to find $\intf(x)\,dx$, we can integrate the series term=by-term. The resulting series converges on $(a-R,a+R)$, and we have
$$\intf(x)\,dx = C+\sum_{n=0}^{\infty}c_n\frac{(x-a)^{n+1}}{n+1}$$ for $|x-a|<R$.

#### NOTE
Why is $f$ differentiable on the interval $(a-R,a+R)$?

---
### Theorem (Uniqueness of Power Series)
let $\sum_{n=0}^{\infty}c_n(x-a)^n$ and $\sum_{n=0}^{\infty}d_n(x-a)^n$ be two convergent ower series such that 
$$\sum_{n=0}^{\infty}c_n(x-a)^n = \sum_{n=0}^{\infty}d_n(x-a)^n$$
for all $x$ in an open interval containing $a$. Then $c_n=d_n$ for all $n\ge 0$.

---

<a id='taylor'></a>
## Taylor Series
* [Home](https://codmccabe.github.io/index.html)
* [Calc Home](https://codmccabe.github.io/calc/index.html)
* [Power Series](#power)
* [Properties of Power Series](#propPower)
* [Taylor Series](#taylor)
* [Using Taylor Series](#usingTaylor)

### Definition (Taylor and Maclurin Series)
If $f$ ha derivatives of all orders at $x=a$, then the Taylor series for the function $f$ at $a$ is
$$\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n$$ where 
$$n!=1\cdot 2\cdot 3\cdot \cdots \cdot (n-1)\cdot n.$$

When $a=0$ the Taylor series for $f$ at zero is known as the Maclaurin Series for $f$.

---
### Theorem (Uniquencess of Taylor Series)
If a function $f$ has a power series at $a$ that converges to $f$ on some open interval containing $a$, then that power series is the taylor series for $f$ at $a$.

---
### Defintion Taylor Polynomial of Finite Degree)
If $f$ has $n$ derivatives at $x=a$, then the $n^{\text{th}}$ Taylor polynomial for $f$ at $a$ is
$$p_n(x)=f(a)+f'(a)(x-a)+\frac{f''(a)}{2!}(x-a)^2+\cdots +\frac{f^{(n)}(a)}{n!}(x-a)^n$$

Whatn $a=0$ the Taylor polynomial for $f$ at zero is known as the Maclaurin polynomial for $f$.

#### NOTE
For the topic of linear approximations, the linerization function is $p_1$.

---
### Theorem (Taylor's Theorem with Remainder)
Let $f$ be a function that can be differentiated $n+1$ times on an interval $I$ containing the real number $a$. Let $p_n$ be the $n^{\text{th}}$ Taylor polynomial of $f$ at $a$ and let 
$$R_n(x)=f(x)-p_n(x)$$ be the $n^{\text{th}}$ remainder.

Then for each $x$ in the interval $I$, there exists a real number $c$ between $a$ and $x$ such that 
$$R_n(x)=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$

If there exists a real number $M$ such that $\left| f^{(n+1)}(x) \right|\le M$ for all $x\in I$, then
$$|R_n(x)|\le \frac{M}{(n+1)!}|x-a|^{n+1}$$
for all $x\in I$.

---
### Theorem (Convergence of Taylor Series)
Suppose that $f$ has derivatives of all orders on an interval $I$ containing $a$. Then the Taylor series
$$\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n$$
converges to $f(x)$ for all $x\in I$ if and only if
$$\lim_{n\to \infty}R_n(x) = 0$$ for all $x\in I$.

---

<a id='usingTaylor'></a>
## Using Taylor Series
* [Home](https://codmccabe.github.io/index.html)
* [Calc Home](https://codmccabe.github.io/calc/index.html)
* [Power Series](#power)
* [Properties of Power Series](#propPower)
* [Taylor Series](#taylor)
* [Using Taylor Series](#usingTaylor)

### Definition (Maclaurin Series and Binomial Series)
For any real number $r$, the Maclaurin series for $f(x)=1+x)^r is the binomial series. It converges to $f$ for $|x|<1$, and we write
$$(1+x)^r = \sum_{n=0}^{\infty}\binom{r}{n}x^n = 1+rx+\frac{r(r-1)}{2!}x^2+\cdots +\frac{r(r-1)\cdot \cdots \cdot (r-n+1)}{n!}x^n+\cdots $$
for $|x|<1$.

---

|Function | Maclaurin Series | Interval of Convergence|
| --- | --- | --- |
|$$f(x)=\frac{1}{1-x}$$ | $$\sum_{n=0}^{\infty}x^n$$ | $$-1<x<1$$ |
|$$f(x)=e^x$$ | $$\sum_{n=0}^{\infty}\frac{x^n}{n!}$$ | $$-\infty <x<\infty $$|
|$$f(x)=\sin(x)$$ | $$\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n+1}}{(2n+1)!}$$ | $$-\infty <x<\infty $$|
|$$f(x)=\cos(x)$$ | $$\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n}}{(2n)!}$$ | $$-\infty <x<\infty $$|
|$$f(x)=\ln(1+x)$$ |$$\sum_{n=0}^{\infty}(-1)^{n+1}\frac{x^n}{n}$$ | $$-1<x\le 1$$|
|$$f(x)=\tan^{-1}(x)$$ | $$\sum_{n=0}^{\infty}(-1)^n\frac{2^{2n+1}}{2n+1}$$ | $$-1<x\le 1$$|
|$$f(x)=(1+x)^r$$ | $$\sum_{n=0}^{\infty}\binom{r}{n}x^n$$ | $$-1<x<1$$|

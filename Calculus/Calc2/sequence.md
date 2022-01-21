# Sequences and Series
* [Home](https://codmccabe.github.io/index.html)
* [Calc Home](https://codmccabe.github.io/calc/index.html)
* [Sequences](#sequences)
* [Properties of Sequences](#propSeq)
* [Bounded and Monotonic](#boundMono)

<a id='sequences'></a>
## Sequence
### Definition (Converges and Diverges)

The sequence $\{a_n\}$ converges to the number $L$ if for every positive number $\epsilon$ there corresponds an integer $N$ such that

$$ |a_n-L|<\epsilon \text{ whenever } n>N$$

If no such number $L$ exists, we say that $\{a_n\}$ diverges.

If $\{a_n\}$ converges to $L$, we write

$$\lim_{n\to \infty}a_n=L \text{ or } a_n\to L$$

and call $L$ the limit of the sequence.

### Definition (Diverges to $\pm \infty$)
If for every number $M$ there exists an $N$ such that for all $n>N$ we have $a_n>M$, then the sequence $\{a_n\}$ diverges to infinity. This is denoted by:

$$\lim_{n\to\infty}a_n=\infty \text{ or } a_n\to \infty $$

Similarly, If for every $m$ there exists an $N$ such that for all $n>N$ we have $a_n<m$, then the sequence $\{a_n\}$ diverges to negative infinity. This is denoted by:

$$\lim_{n\to \infty}a_n = -\infty \text{ or } a_n\to -\infty. $$

---

* [Home](https://codmccabe.github.io/index.html)
* [Calc Home](https://codmccabe.github.io/calc/index.html)
* [Sequences](#sequences)
* [Properties of Sequences](#propSeq)
* [Bounded and Monotonic](#boundMono)

<a id='propSeq'></a>
## Properties of Sequences
### Theorem (Law of Sequences)
Let $\{a_n\}$ and $\{b_n\}$ be sequences of real numbers, and let $A$ and $B$ be real numbers. The following rules hold if
$$ \lim_{n\to \infty}a_n=A \text{ and } \lim_{n\to \infty}b_n=B$$
1. $\lim_{n\to \infty}\left(a_n \pm b_n\right)= \lim_{n\to \infty}a_n\pm \lim_{n\to \infty}b_n$
2. $\lim_{n\to \infty}k\cdot a_n = k\cdot A$ where $k$ is some real number.
3. $\lim_{n\to \infty}\left(a_n\cdot b_n\right)= A\cdot B$
4. $\lim_{n\to \infty}\dfrac{a_n}{b_n} = \dfrac{A}{B}$ provided $B\ne 0$

---

### Theorem (Squeeze Theorem)
Let $\{a_n\}$, $\{b_n\}$, and $\{c_n\}$ be sequences of real numbers. If $a_n\le b_n\le c_n$ hold for for all $n>N$ where $N$ is some natural number and 
$$\lim_{n\to \infty}a_n=\lim_{n\to \infty}c_n=L$$
then 
$$\lim_{n\to \infty}b_n=L.$$

---
### Theorem (Continuous Function)
Let $\{a_n\}$ be a seqeunce of real numbers. If $a_n\to L$ and if $f$ is a function that is continuous at $L$ and defined at all $a_n$, then $$f(a_n)\to f(L)$$

---

### Theorem
Suppose that $f(x)$ is a function defined for all $x\ge n_0$ and that $\{a_n\}$ is a  sequence of real numbers such that $a_n=f(n)$ for $n\ge n_0$. Then 
$$\lim_{n\to \infty}a_n=L \text{ whenever } \lim_{n\to \infty}f(x)=L $$

---

### Theorem (Popular Functions)
The following six sequences converges to the limit listed below:
1. $\lim_{n\to \infty}\frac{\ln(n)}{n}=0$
2. $\lim_{n\to \infty}\sqrt[n]{n}=1$
3. $\lim_{n\to \infty}x^{\frac{1}{n}}=1$ provided $x>0$ and fixed
4. $\lim_{n\to \infty}x^n=0$ provided $-1<x<1$ and fixed
5. $\lim_{n\to \infty}\left( 1+\frac{x}{n} \right)^n = e^x$ for any fixed $x$ 
6. $\lim_{n\to \infty}\dfrac{x^n}{n!}=0$ for any fixed $x$

---
### Definition (Factorial)
Let $n$ be a natural number
$$n! = 1\cdot 2\cdot 3\cdot \cdots \cdot n$$
A useful properties is $$(n+1)! = (n+1)\cdot n!$$

* [Home](https://codmccabe.github.io/index.html)
* [Calc Home](https://codmccabe.github.io/calc/index.html)
* [Sequences](#sequences)
* [Properties of Sequences](#propSeq)
* [Bounded and Monotonic](#boundMono)

<a id='bondMono'></a>
## Bounded and Monotonic
### Definition
A sequence $\{a_n\}$ is bounded from above if there exists a number $M$ such that $a_n\le M$ for all $n$. The number $M$ is an upper bound for $\{a_n\}$. If $M$ is an upper bound for $\{a_n\}$ but no number less than $M$ is an upper bound for $\{a_n\}$, then $M$ is the least upper bound for $\{a_n\}$.

A seqeunce $\{a_n\}$ is bounded from below if there exists a number $m$ such that $a_n\ge m$ or all $n$. The number $m$ is a ower bound of $\{a_n\}$. If $m$ is a lower bound for $\{a_n\}$ but no number greater that $m$ is a lower bound for $\{a_n\}$, then $m$ is the greatest lower bound for $\{a_n\}$.

If $\{a_n\}$ is bounded from above and below, then $\{a_n\}$ is bounded. If $\{a_n\}$ is not bounded, then we say that $\{a_n\}$ is an unbounded sequence.

### Definition
A sequence $\{a_n\}$ is increasing (nondecreasing) if $a_n\le a_{n+1}$ for all $n$. That is,

$$a_1\le a_2\le a_3\le \cdots $$

The sequence is decreasing (nonincreasing) if $a_n\ge a_{n+1}$ for all $n$. That is,

$$a_1 \ge a_2 \ge a_3 \ge \cdots $$

---

### Theorem (Monotonic Sequence Theorem)
If a sequence $\{a_n\}$ is both bounded and monotonic, then the sequence converges.


* [Home](https://codmccabe.github.io/index.html)
* [Calc Home](https://codmccabe.github.io/calc/index.html)
* [Sequences](#sequences)
* [Properties of Sequences](#propSeq)
* [Bounded and Monotonic](#boundMono)


```maxima

```

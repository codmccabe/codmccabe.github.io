$\newcommand{\ddx}[1]{\frac{d}{dx}\left[#1\right]}$
# Hyperbolic Functions
* [Home](https://codmccabe.github.io/)
* [Calc Home](https://codmccabe.github.io/calc/index.html)
* [Definitions, Thoerems, and Lemmas](#DefThmLem)
* [Examples](#example)

<a id='DefThmLem'></a>
## Definitions, Theorems, and Lemmas

### Complex Numbers and Trigonometry
Relationship to trigonometry
$$\begin{aligned}\cos(x) & =\Re(e^{ix})=\dfrac{e^{ix}+e^{-ix}}{2} & \sin(x) & =\Im(e^{ix})=\dfrac{e^{ix}-e^{-ix}}{2i}\\
\cos(iy) & =\dfrac{e^{y}+e^{-y}}{2}=\cosh(y) & \sin(iy) & =\dfrac{e^{y}-e^{-y}}{2i}=i\sinh(y)
\end{aligned}$$

---
### The Sum of Two Angles
The Sum of Two Angles 
$$\cos(\alpha+\beta)=\cos(\alpha)\cos(\beta)-\sin(\alpha)\sin(\beta)$$
$$\sin(\alpha+\beta)=\cos(\alpha)\sin(\beta)+\cos(\beta)\sin(\alpha)$$


Proof. Sum of Angles
$$\begin{aligned}
 \cos(\alpha+\beta) & =\Re\left(e^{i(\alpha+\beta)}\right) & i & =\sqrt{-1}\\
 & =\Re\left(e^{i\alpha}e^{i\beta}\right)\\
 & =\Re\left((\cos(\alpha)+i\sin(\alpha)(\cos(\beta)+i\sin(\beta)\right) & i^{2} & =-1\\
 & =\Re\left(\cos(\alpha)\cos(\beta)+i\left(\cos(\alpha)\sin(\beta)+\sin(\alpha)\cos(\beta)\right)+i^{2}\sin(\alpha)\sin(\beta)\right)\\
 & =\cos(\alpha)\cos(\beta)-\sin(\alpha)\sin(\beta)
\end{aligned}
$$

Proof. 
$$\begin{aligned}
 \sin(\alpha+\beta) & =\Im\left(e^{i(\alpha+\beta)}\right) & i & =\sqrt{-1}\\
 & =\Im\left(e^{i\alpha}e^{i\beta}\right)\\
 & =\Im\left((\cos(\alpha)+i\sin(\alpha)(\cos(\beta)+i\sin(\beta)\right) & i^{2} & =-1\\
 & =\Im\left(\cos(\alpha)\cos(\beta)+i\left(\cos(\alpha)\sin(\beta)+\sin(\alpha)\cos(\beta)\right)+i^{2}\sin(\alpha)\sin(\beta)\right)\\
 & =\cos(\alpha)\sin(\beta)+\sin(\alpha)\cos(\beta)
\end{aligned}
$$

---
### Hyperbolic Functions in Exponential Form
$$
\begin{aligned}
 \cosh(x) & :=\dfrac{e^{x}+e^{-x}}{2} & \text{sech}(x) & =\dfrac{1}{\cosh(x)}\\
 \sinh(x) & :=\dfrac{e^{x}-e^{-x}}{2} & \text{csch}(x) & =\dfrac{1}{\sinh(x)}\\
 \tanh(x) & :=\dfrac{\sinh(x)}{\cosh(x)} & \coth(x) & =\dfrac{1}{\tanh(x)}
\end{aligned}
$$

---
### More Necessary Identities
$$
\begin{aligned}
 \cosh^{2}(x)-\sinh^{2}(x) & =1 & \cosh^{2}(x) & =\dfrac{\cosh(2x)+1}{2}\\
 \sinh(2x) & =2\sinh(x)\cosh(x) & \sinh^{2}(x) & =\dfrac{\cosh(2x)-1}{2}\\
 \cosh(2x) & =\cosh^{2}(x)+\sinh^{2}(x) & \tanh^{2}(x) & =1-\text{sech}^{2}(x)
\end{aligned}
$$

---
### Derivative of the Hyperbolic Functions
$$
\begin{aligned}
 \frac{d}{dx}\left[\sinh(x)\right] & =\cosh(x) & \frac{d}{dx}\left[\cosh(x)\right] & =\sinh(x)\\
 \frac{d}{dx}\left[\tan(x)\right] & =\text{sech}^{2}(x) & \frac{d}{dx}\left[\coth(x)\right] & =-\text{csch}^{2}(x)\\
 \frac{d}{dx}\left[\text{sech}(x)\right] & =-\text{sech}(x)\tanh(x) & \frac{d}{dx}\left[\text{csch}(x)\right] & =-\text{csch}(x)\coth(x)
\end{aligned}
$$

---
### Integration Table for Hyperbolic Functions
$$
\begin{aligned}
 \int\sinh(x)\,dx & =\cosh(x)+C & \int\cosh(x)\,dx & =\sinh(x)+C\\
 \int\text{sech}^{2}(x)\,dx & =\tan(x)+C & \int-\text{csch}^{2}(x)\,dx & =\coth(x)+C\\
 \int-\text{sech}(x)\tanh(x)\,dx & =\text{sech}(x)+C & \int-\text{csch}(x)\coth(x)\,dx & =\text{csch}(x)+C
\end{aligned}
$$

---
### Inverse Hyperbolic Functions
1. Let $x\in(-\infty,\infty)$ and $f(x)=\sinh(x)\in(-\infty,\infty)$,
then $f^{-1}(x)=\sinh^{-1}(x)\in(-\infty,\infty)$ where $x\in(-\infty,\infty)$. 
2. Let $x\in[0,\infty)$ and $f(x)=\cosh(x)\in[1,\infty)$, then $f^{-1}(x)=\cosh^{-1}(x)\in[0,\infty)$
where $x\in[1,\infty)$. 
3. Let $x\in(0,1]$ and $f(x)=\text{sech}(x)\in[0,\infty)$, then $f^{-1}(x)=\text{sech}^{-1}(x)\in(0,1]$
where $x\in[0,\infty)$.
4. Let $x\in(-\infty,\infty)$ and $f(x)=\tanh(x)\in(-1,1)$, then $f^{-1}(x)=\tanh^{-1}(x)\in(-\infty,\infty)$
where $x\in(-1,1)$.
5. Let $x\in(-\infty,0)\cup(0,\infty)$ and $f(x)=\coth(x)\in(-\infty,-1)\cup(1,\infty)$,
then $f^{-1}(x)=\coth^{-1}(x)$ where $x\in(-\infty,-1)\cup(1,\infty)$.
6. Let $x\in(-\infty,0)\cup(0,\infty)$ and $f(x)=\text{csch}^{-1}(x)\in(-\infty,0)\cup(0,\infty)$,
then $f^{-1}(x)=\text{csch}^{-1}(x)$ where $x\in(-\infty,0)\cup(0,\infty)$. 
$$
\begin{aligned}
 \text{sech}^{-1}(x) & =\cosh^{-1}(\frac{1}{x})\\
 \text{csch}^{-1}(x) & =\sinh^{-1}(\frac{1}{x})\\
 \coth^{-1}(x) & =\tanh^{-1}(\frac{1}{x})
\end{aligned}
$$

---
### Derivative of the Inverse Hyperbolic Functions
$$
\begin{aligned}
 \frac{d}{dx}\left[\sinh^{-1}(x)\right] & =\dfrac{1}{\sqrt{1+x^{2}}}\\
 \ddx{\cosh^{-1}(x)} & =\dfrac{1}{\sqrt{x^{2}-1}} & x & >1\\
 \ddx{\text{sech}^{-1}(x)} & =-\dfrac{1}{x\sqrt{1-x^{2}}} & |x| & <1\\
 \ddx{\tanh^{-1}(x)} & =\dfrac{1}{1-x^{2}} & |x| & >1\\
 \ddx{\coth^{-1}(x)} & =\dfrac{1}{1-x^{2}} & 0<x & <1\\
 \ddx{\text{csch}^{-1}(x)} & =-\dfrac{1}{|x|\sqrt{1+x^{2}}} & x & \ne0
\end{aligned}
$$

---
### Integral Table of Invese Hyperbolic Functions
$$
\begin{aligned}
 \int\dfrac{1}{\sqrt{1+x^{2}}}\,dx & =\sinh^{-1}(x)+C\\
 \int\dfrac{1}{\sqrt{x^{2}-1}}\,dx & =\cosh^{-1}(x)+C & x & >0\\
 \int-\dfrac{1}{x\sqrt{1-x^{2}}}\,dx & =\text{sech}^{-1}(x)+C\\
 \int\dfrac{1}{1-x^{2}}\,dx & =\tanh^{-1}(x)+C\\
 \int\dfrac{1}{1-x^{2}}\,dx & =\coth^{-1}(x)+C & x & >0\\
 \int-\dfrac{1}{|x|\sqrt{1+x^{2}}}\,dx & =\text{csch}^{-1}(x)+C & x & \ne0
\end{aligned}
$$

* [Home](https://codmccabe.github.io/)
* [Calc Home](https://codmccabe.github.io/calc/index.html)
* [Definitions, Thoerems, and Lemmas](#DefThmLem)
* [Examples](#example)

## Examples

#### Evaluate an integral
$$\int\dfrac{2\,dx}{\sqrt{3+4x^{2}}}$$
$$
\begin{aligned}
 \int\dfrac{2\,dx}{\sqrt{3+4x^{2}}} & =\int\dfrac{2\,dx}{\sqrt{(\sqrt{3})^{2}+(2x)^{2}}}\\
 & =\int\dfrac{2\,dx}{\sqrt{(\sqrt{3})^{2}+\left(\dfrac{\sqrt{3}}{\sqrt{3}}\right)^{2}(2x)^{2}}}\\
 & =\int\dfrac{2\,dx}{\sqrt{(\sqrt{3})^{2}\left(1+\left(\dfrac{2x}{\sqrt{3}}\right)^{2}\right)}}\\
 & =\dfrac{2}{\sqrt{3}}\int\dfrac{dx}{\sqrt{1+\left(\dfrac{2x}{\sqrt{3}}\right)^{2}}}\\
u & =\dfrac{2}{\sqrt{3}}x\\
du & =\frac{2}{\sqrt{3}}\,dx\\
\frac{\sqrt{3}}{2}du & =dx\\
 & =\frac{2}{\sqrt{3}}\cdot\frac{\sqrt{3}}{2}\int\dfrac{du}{\sqrt{1+u^{2}}}\\
 & =\sinh^{-1}(u)+C\\
 & =\sinh^{-1}(\frac{2x}{\sqrt{3}})+C
\end{aligned}
$$


```maxima
integrate(2/sqrt(3+4*x^2),x);
```




$$\tag{${\it \%o}_{3}$}{\rm asinh}\; \left({{ 2\, x}\over{\sqrt{3}}}\right)$$



* [Home](https://codmccabe.github.io/)
* [Calc Home](https://codmccabe.github.io/calc/index.html)
* [Definitions, Thoerems, and Lemmas](#DefThmLem)
* [Examples](#example)


```maxima

```

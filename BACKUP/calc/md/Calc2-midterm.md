# Calc 2 Mid-Term Summer 2021
Here is a collection of problems pulled from Jim's PowerPoint presentations. 
* [Home](https://codmccabe.github.io)
* [Calc Page](https://codmccabe.github.io/calc/)


1. Evaluate the following:

$$\int \cos^4(2t)\,dt$$
$$\int \cos(3t)\sin(8t)\,dt$$
$$\int_1^3 \sin(8x)\sin(x)\,dx$$
$$\int \cot(10x)\csc^4(10x)\,dx$$


```maxima
integrate((cos(2*t))^4,t);
```




\[\tag{${\it \%o}_{3}$}\frac{\frac{\frac{\sin \left(8\,t\right)}{2}+4\,t}{8}+\frac{\sin \left(4\,t\right)}{2}+t}{4}\]




```maxima
integrate(cos(3*t)*sin(8*t),t);
```




\[\tag{${\it \%o}_{2}$}-\frac{\cos \left(11\,t\right)}{22}-\frac{\cos \left(5\,t\right)}{10}\]




```maxima
integrate(sin(8*x)*sin(x),x,1,3);
```




\[\tag{${\it \%o}_{5}$}\frac{7\,\sin 9-9\,\sin 7}{126}-\frac{7\,\sin 27-9\,\sin 21}{126}\]




```maxima
float(integrate(sin(8*x)*sin(x),x,1,3));
```




\[\tag{${\it \%o}_{6}$}-0.01740302177606207\]




```maxima
integrate(cot(10*x)*(csc(10*x))^4,x);
```




\[\tag{${\it \%o}_{8}$}-\frac{1}{40\,\sin ^4\left(10\,x\right)}\]



## Some useful identities
* $\sin^2(x)+\cos^2(x)=1$
* $\tan^2(x)+1=\sec^2(x)$
* $\cos^2(x)=\frac12\left(1+\cos(2x)\right)$
* $\sin^2(x)=\frac12\left(1-\cos(2x)\right)$
* $\sin(x)\cos(x)=\frac12\sin(2x)$

## Trig Substitution:
|Form |Looks Like|Substitution|Limit Assumptions|
| :----------------: | :----------------: | :----------------: | :----------------: |
|$$\sqrt{b^2x^2-a^2}$$|$$\sec^2(\theta)-1=\tan^2(\theta)$$|$$x=\frac{a}{b}\sec(\theta)$$|$$0\le\theta<\frac{\pi}{2},\,\frac{\pi}{2}<\theta\le \pi$$|
|$$\sqrt{a^2-b^2x^2}$$|$$1-\sin^2(\theta)=\cos^2(\theta)$$|$$x=\frac{a}{b}\sin(\theta)$$|$$-\frac{\pi}{2}\le\theta\le\frac{\pi}{2}$$|
|$$\sqrt{a^2+b^2x^2}$$|$$\tan^2(\theta)+1=\sec^2(\theta)$$|$$x=\frac{a}{b}\tan(\theta)$$|$$-\frac{\pi}{2}<\theta<\frac{\pi}{2}$$|

Use a trig substitution to eliminate the root.
1. $\sqrt{4-9x^2}$
2. $\sqrt{3+25x^2}$
3. $\left(7x^2-3\right)^{\frac{5}{2}}$
4. $\sqrt{(w+3)^2-100}$
5. $\sqrt{4(9x-5)^2+1}$
6. $\sqrt{1-4x-2x^2}$
7. $\left( x^2-8x+21 \right)^{\frac{3}{2}}$
8. $\sqrt{e^{8x}-9}$


```maxima
f1(x):=sqrt(4-9*x^2)$
    f1((2/3)*sec(theta));
    factor(f1((2/3)*sec(theta)));
```




\[\tag{${\it \%o}_{12}$}\sqrt{4-4\,\sec ^2\vartheta}\]






\[\tag{${\it \%o}_{13}$}2\,\sqrt{1-\sec ^2\vartheta}\]



Notice that $2\sqrt{1-\sec^2(\theta)}=2\sqrt{\tan^2(\theta)}=2\tan(\theta)$. Thus, by letting $x=\frac{2}{3}\sec(\theta)$ we have $$\sqrt{4-9x^2}=2\tan(\theta)$$


```maxima
f2(x):=sqrt(3+25*x^2)$
    f2((sqrt(3)/5)*tan(theta));
    factor(f2((sqrt(3)/5)*tan(theta)));
```




\[\tag{${\it \%o}_{15}$}\sqrt{3\,\tan ^2\vartheta+3}\]






\[\tag{${\it \%o}_{16}$}\sqrt{3}\,\sqrt{\tan ^2\vartheta+1}\]



Notice that $\sqrt3\sqrt{\tan^2(\theta)+1}=\sqrt3\sqrt{\sec^2(\theta)}=\sqrt3\sec(\theta)$. thus, by letting $x=\frac{\sqrt3}{5}\tan(\theta)$ we have $$\sqrt{3+25x^2}=\sqrt3\sec(\theta)$$


```maxima
f3(x):=(7*x^2-3)^(5/2)$
    f3((sqrt(3)/sqrt(7)*sec(theta)));
    factor(f3((sqrt(3)/sqrt(7)*sec(theta))));
    3^(5/2)*((tan(theta))^2)^(5/2);
```




\[\tag{${\it \%o}_{12}$}\left(3\,\sec ^2\vartheta-3\right)^{\frac{5}{2}}\]






\[\tag{${\it \%o}_{13}$}3^{\frac{5}{2}}\,\left(\sec ^2\vartheta-1\right)^{\frac{5}{2}}\]






\[\tag{${\it \%o}_{14}$}3^{\frac{5}{2}}\,\tan ^4\vartheta\,\left| \tan \vartheta\right| \]



Notice that $3^{5/2}\cdot (\sec^2(\theta)-1)^{5/2} = 3^{5/2}\cdot tan^5(\theta)$. Thus, by letting $x=\frac{\sqrt3}{\sqrt7}\sec(\theta)$ we have $$\left(7x^2-3\right)^{5/2}=3^{5/2}\tan^5(\theta)$$


```maxima
f4(x):=sqrt((x+3)^2-100)$
    f4(10*sec(theta)-3);
    factor(f4(10*sec(theta)-3));
```




\[\tag{${\it \%o}_{33}$}\sqrt{100\,\sec ^2\vartheta-100}\]






\[\tag{${\it \%o}_{34}$}10\,\sqrt{\sec ^2\vartheta-1}\]



Notice that $10\sqrt{\sec^2(\theta)-1}=10\tan(\theta)$. Thus, by letting $x=10\sec(\theta)-3$ we have $$\sqrt{(x+3)^2-100}=10\tan(\theta)$$


```maxima
f5(x):=sqrt(4*(9*x-5)^2+1)$
    solve((1/2)*tan(theta)=9*x-5,x);
    f5((tan(theta)+10)/18);
    factor(f5((tan(theta)+10)/18));
```




\[\tag{${\it \%o}_{60}$}\left[ x=\frac{\tan \vartheta+10}{18} \right] \]






\[\tag{${\it \%o}_{61}$}\sqrt{4\,\left(\frac{\tan \vartheta+10}{2}-5\right)^2+1}\]






\[\tag{${\it \%o}_{62}$}\sqrt{\tan ^2\vartheta+1}\]



First, solve the equation: $$\frac12\tan(\theta)=9x-5$$ to get $x=\frac{\tan(\theta)+10}{18}$. Then we notice that $\sqrt{\tan^2(\theta)+1}=\sec(\theta)$. Thus, with $x=\frac{\tan(\theta)+10}{18}$, we have, $$\sqrt{4(9x-5)^2+1}=\sec(\theta)$$

Use a trig substitution to evaluat ethe given integral. $$\int \frac{\sqrt{x^2+16}}{x^4}\, dx$$


```maxima
integrate(sqrt(x^2+16)/x^4,x);
```




\[\tag{${\it \%o}_{129}$}-\frac{\left(x^2+16\right)^{\frac{3}{2}}}{48\,x^3}\]




```maxima
Top(x):=sqrt(x^2+16)$
    Top(4*tan(theta));
    factor(Top(4*tan(theta)));
```




\[\tag{${\it \%o}_{96}$}\sqrt{16\,\tan ^2\vartheta+16}\]






\[\tag{${\it \%o}_{97}$}4\,\sqrt{\tan ^2\vartheta+1}\]



Notice that when $x=4\tan(\theta)$, we have $$\sqrt{x^2+16}=4\sec(\theta)$$


```maxima
(4*sec(theta))/((4*tan(theta))^4);
trigreduce((4*sec(theta))/((4*tan(theta))^4));
```




\[\tag{${\it \%o}_{121}$}\frac{\sec \vartheta}{64\,\tan ^4\vartheta}\]






\[\tag{${\it \%o}_{122}$}\frac{\cot ^3\vartheta\,\csc \vartheta}{64}\]




```maxima
trigreduce((cot(x))^2+1);
```




\[\tag{${\it \%o}_{124}$}\csc ^2x\]



So we have:

$$\int \frac{\sqrt{x^2+16}}{x^4}\, dx= \int\frac{\sec(\theta)}{64\tan^4(\theta)}\,dx$$

Recall that $\csc^2(\xi)=\cot^2(\xi)+1$. That is,

$$\cot^3(\theta)\cdot \csc(\theta)=\left(\cot(\theta)\csc(\theta)\right)\cdot \cot^2(\theta)$$

$$\left(\cot(\theta)\csc(\theta)\right)\cdot \cot^2(\theta) = \left(\cot(\theta)\csc(\theta)\right)\cdot \left(\csc^2(\theta)-1\right)$$

$$\int\frac{\sec(\theta)}{64\tan^4(\theta)}\,dx = \frac{1}{64} \int \left(\cot(\theta)\csc(\theta)\right)\cdot \left(\csc^2(\theta)-1\right)\,d\theta$$

Let $u=\csc(\theta)$ and $du=\cot(\theta)\csc(\theta)$, then

$$\frac{1}{64} \int \left(\cot(\theta)\csc(\theta)\right)\cdot \left(\csc^2(\theta)-1\right)\,d\theta= \frac{1}{64}\int\left(u^2-1\right)\,du$$


```maxima
IF9(u):=(u*(u^2-3)/192);
IF9(csc(theta));
```




\[\tag{${\it \%o}_{142}$}{\it IF}_{9}\left(u\right):=\frac{u\,\left(u^2-3\right)}{192}\]






\[\tag{${\it \%o}_{143}$}\frac{\csc \vartheta\,\left(\csc ^2\vartheta-3\right)}{192}\]



## Partial Fractions
|Factor in Denominator|Term in Partial Fraction Decomposition|
|:------:|:-----------------------:|
|$$ax+b$$|$$\dfrac{A}{ax+b}$$|
|$$(ax+b)^k$$|$$\dfrac{A_1}{ax+b}+\dfrac{A_2}{(ax+b)^2}+\cdots+\dfrac{A_k}{(ax+b)^k},\,k=1,2,3,...$$|
|$$(ax^2+bx+c)^k$$|$$\dfrac{A_1x+B_1}{ax^2+bx+c}+\dfrac{A_2x+B_2}{(ax^2+bx+c)^2}+\cdots+\dfrac{A_kx+B_k}{(ax^2+bx+c)^k},\,k=1,2,3,...$$

## Improper Integrals
1. If $\int_a ^tf(x)\,dx$ exists for every $t>a$, then $$\int_a^{\infty}f(x)\,dx=\lim_{t\to\infty}\int_a^tf(x)\,dx$$ Provided the limit exists and is finite.
2. If $\int_t ^bf(x)\,dx$ exists for every $b>t$, then $$\int_{-\infty}^bf(x)\,dx=\lim_{t\to\infty}\int_t^bf(x)\,dx$$ Provided the limit exists and is finite.
3. If $\int_{-\infty}^{c}f(x)\,dx$ and $\int_{c}^{\infty}f(x)\,dx$ are both convergent, then $$\int_{-\infty}^{\infty}f(x)\,dx=$\int_{-\infty}^{c}f(x)\,dx+\int_{c}^{\infty}f(x)\,dx$$ where $c$ is any number.
4. If $f(x)$ is continuous on the interval $[a,b)$ and not continuous at $x=b$, then $$\int_a^bf(x)\,dx=\lim_{x\to b^-}\int_a^tf(x)\,dx$$ provied the limit exists and is finite.
5. If $f(x)$ is continuous on the interval $(a,b]$ and not continuous at $x=a$, then $$\int_a^bf(x)\,dx=\lim_{t\to a^+}\int_t^bf(x)\,dx$$ provided the limit exists and is finite.
6. If $f(x)$ is not continuous at $x=c$ where $a<c<b$ and $\int_a^cf(x)\,dx$ and $\int_c^bf(x)\,dx$ are both convergent, then $$\int_a^bf(x)\,dx=\int_a^cf(x)\,dx+\int_c^bf(x)\,dx$$
7. If f(x) is not continuous at $x=a$ and $x=b$ and if $\int_a^cf(x)\,dx$ and $\int_c^bf(x)\,dx$ are both convergent, then $$\int_a^bf(x)\,dx=\int_a^cf(x)\,dx+\int_c^bf(x)\,dx$$ where $c$ is any number.

Note for number 3: the integral $\int_{-\infty}^{\infty}f(x)\,dx$ is convergent if and only if $\int_{-\infty}^cf(x)\,dx$ and $\int_c^{\infty}f(x)\,dx$ are both convergent.

### Comparison Test

---
If $a>0$ then $$\int_a^{\infty}\dfrac{1}{x^p}\,dx$$ is convergent if $p>1$ and divergent if $p\le1$.

---
If $f(x)\ge g(x)\ge 0$ on the interval $[a,\infty)$, then
1. If $\int_a^{\infty}f(x)\,dx$ converges then so does $\int_a^{\infty}g(x)\,dx$.
2. If $\int_a^{\infty}g(x)\,dx$ diverges then so does $\int_a^{\infty}f(x)\,dx$.

### L'Hospital's Rule
Suppose ${\displaystyle \lim_{x\to a}|f(x)|=\lim_{x\to a}|g(x)|=\infty}$ or $\displaystyle \lim_{x\to a}f(x)=\lim_{x\to a}g(x)=0$.
If ${\displaystyle \lim_{x\to a}\dfrac{f'(x)}{g'(x)}}$ exists in
either the finite or infinite sense, then
$$
\lim_{x\to a}\dfrac{f(x)}{g(x)}=\lim_{x\to a}\dfrac{f'(x)}{g'(x)}.
$$

### Average Function Value
The average value of a function $f(x)$ over the interval $[a,b]$ is given by $$f_{ave}=dfrac{1}{b-a}\int_a^bf(x)\,dx$$

### The Mean Value Theorem for Integrals
If $f(x)$ is continuous function on $[a,b]$ then there is a number $c\in[a,b]$ such that $$\int_a^bf(x)\,dx=f(c)(b-a)$$

### Arc Length
If $f'$ is continuous on $[a,b]$, then the length (arc length) of the curve $y=f(x)$ from the point $A=(a,f(a))$ to the point $B=(b,f(b))$ is the value of the integral $$L=\int_a^b\sqrt{1+\left[f'(x)\right]^2}\,dx=\int_a^b\sqrt{1+\left[ \frac{dy}{dx} \right]^2}$$


### Volume by Disks for Rotation About the x-Axis
Let $A(x)=\pi(R(x))^2$ where $R(x)$ is a function of the radius of the circle over the domain $x$. The Volume of the object is then $$V=\int_a^bA(x)\,dx$$

### EXAMPLE (Volume by Disks for Rotation)
The region between the curve $y=\cos(x)$,$\frac{\pi}{4}\le x\le \frac{3\pi}{4}$, and the x-axis is revolved about the x-axis to generate a solid. Find its volume.

---
First, look at the graph:


```maxima
%%html
<iframe src="https://www.geogebra.org/3d/hapxqvpr?embed" width="400" height="400" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>
```


<iframe src="https://www.geogebra.org/3d/hapxqvpr?embed" width="400" height="400" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>




```maxima

```

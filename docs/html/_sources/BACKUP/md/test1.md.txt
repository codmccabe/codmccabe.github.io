Let $y=\ln\left(\dfrac{6x^{1/5}}{20+4x^{1/5}}\right)$. Find the
derivative of $y$ with respect to $x$.

First, we will rewrite $y$ in a more pleasant way:
$$\begin{aligned}\ln\left(\dfrac{6x^{1/5}}{20+4x^{1/5}}\right) & =\ln(6x^{1/5})-\ln(20+4x^{1/5})\\
 & =\ln(6)+\dfrac{1}{5}\ln(x)-\ln(4(5+x^{1/5}))\\
 & =\ln(6)+\dfrac{1}{5}\ln(x)-\ln(4)-\ln(5+x^{1/5})
\end{aligned}$$

Now, differentiate
$$\begin{aligned}\frac{d}{dx}\left[\ln\left(\dfrac{6x^{1/5}}{20+4x^{1/5}}\right)\right] & =\frac{d}{dx}\left[\ln(6)+\dfrac{1}{5}\ln(x)-\ln(4)-\ln(5+x^{1/5})\right]\\
 & =0+\dfrac{1}{5x}-0-\dfrac{\frac{1}{5}x^{-4/5}}{5+x^{1/5}}\\
 & =\dfrac{1}{5x}-\dfrac{1}{5x^{4/5}\left(5+x^{1/5}\right)}
\end{aligned}$$ where ever $y$ is defined.

Let $y=\sqrt{\dfrac{1}{x(x+1)}}$. Then $$\begin{aligned}
    y&=\left( \dfrac{1}{x(x+1)} \right)^{1/2}\\
    &= \dfrac{1^{1/2}}{\left( x(x+1) \right)^{1/2}}\\
    &= \dfrac{1}{x^{1/2}(x+1)^{1/2}}
\end{aligned}$$

That is, $y=\sqrt{\dfrac{1}{x(x+1)}}=\dfrac{1}{x^{1/2}(x+1)^{1/2}}$.
Natural Log both sides: $$\begin{aligned}
    \ln(y)&=\ln\left( \dfrac{1}{x^{1/2}(x+1)^{1/2}} \right)\\
    &=\ln(1)-\ln\left( x^{1/2}(x+1)^{1/2} \right)\\
    &=0-\ln(x^{1/2})-\ln((x+1)^{1/2})\\
    &=-\frac12 \ln(x)-\frac12 \ln(x+1)\\
    &=-\frac12\left(\ln(x)+\ln(x+1)\right)
\end{aligned}$$

Multiply both sides by $-2$ and then implicate differentiate:

$$\begin{aligned}
    \frac{d}{dx}\left[-2\ln(y)\right]&=\frac{d}{dx}\left[\ln(x)+\ln(x+1)\right]\\
    -2\frac{1}{y}\frac{dy}{dx}&=\frac{1}{x}+\frac{1}{x+1}\\
    \frac{dy}{dx}&=-\frac{y}{2}\left( \frac{1}{x}+\frac{1}{x+1} \right)
\end{aligned}$$

Where $y=\sqrt{\dfrac{1}{x(x+1)}}$

Let $y=\ln\left( \dfrac{(x^2+8)^5}{\sqrt{4-x}} \right)$. Then
$$y=\ln\left( \dfrac{(x^2+8)^5}{\sqrt{4-x}} \right)=...=5\ln(x^2+8)-\frac12\ln(4-x)$$

If we set $f(x)=\ln(x^2+8)$ and $g(x)=\ln(4-x)$. Then
$$y=\ln\left( \dfrac{(x^2+8)^5}{\sqrt{4-x}} \right)=5f(x)-\frac12g(x)$$
and
$$y'=\frac{d}{dx}\left[\ln\left( \dfrac{(x^2+8)^5}{\sqrt{4-x}} \right)\right]=5f'(x)-\frac12g'(x)$$

Now, find $f'(x)$ and $g'(x)$.
$$f'(x)=\left(\ln(x^2+8)\right)'=\dfrac{\left( x^2+8 \right)'}{x^2+8}=\dfrac{2x}{x^2+8}$$
and
$$g'(x)=\left( \ln(4-x) \right)'=\dfrac{(4-x)'}{4-x}=\dfrac{-1}{4-x}$$

Therefore, putting everything together we have:
$$y'=\frac{d}{dx}\left[\ln\left( \dfrac{(x^2+8)^5}{\sqrt{4-x}} \right)\right]=5f'(x)-\frac12g'(x)=5\left(\dfrac{2x}{x^2+8}\right)-\frac12\left(\dfrac{-1}{4-x}\right)$$

Let $y=\cot^{-1}\left( \sqrt{4x^2-1} \right)+\sec^{-1}(2x)$,
$f(x)=\sqrt{4x^2-1}$, and $g(x)=2x$. Then

$$\label{eq:f1}
    f'(x)=\frac{d}{dx}\left[(4x^2-1)^{1/2}\right]=\dfrac{(4x^2-1)'}{2\sqrt{4x^2-1}}=\dfrac{8x}{2\sqrt{4x^2-1}}$$

and

$$\label{eq:g1}
    g'(x)=\frac{d}{dx}\left[2x\right]=2$$

Since $\frac{d}{dx}\left[\cot^{-1}(x)\right]=-\dfrac{1}{x^2+1}$ and
chain rule we have

$$\label{eq:cotchain}
    \frac{d}{dx}\left[\cot^{-1}(f(x))\right]=-\dfrac{1}{\left(f(x)\right)^2+1}\cdot f'(x)$$

Since $\frac{d}{dx}\left[\sec^{-1}(x)\right]=\dfrac{1}{|x|\sqrt{x^2-1}}$
and chain rule we have

$$\label{eq:secchain}
    \frac{d}{dx}\left[\sec^{-1}(g(x))\right]=\dfrac{1}{|g(x)|\sqrt{\left(g(x)\right)^2-1}}\cdot g'(x)$$

By Equations [\[eq:f1\]](#eq:f1){reference-type="eqref"
reference="eq:f1"} and
[\[eq:cotchain\]](#eq:cotchain){reference-type="eqref"
reference="eq:cotchain"} we have

$$\label{eq:dcf1}
    \frac{d}{dx}\left[\cot^{-1}\left(\sqrt{4x^2-1}\right)\right]=-\dfrac{1}{\left(\sqrt{4x^2-1}\right)^2+1}\cdot \dfrac{8x}{2\sqrt{4x^2-1}}=...=-\dfrac{1}{x\sqrt{x^2-1}}$$

By Equations [\[eq:g1\]](#eq:g1){reference-type="eqref"
reference="eq:g1"} and
[\[eq:secchain\]](#eq:secchain){reference-type="eqref"
reference="eq:secchain"} we have

$$\label{eq:dsg1}
    \frac{d}{dx}\left[\sec^{-1}(2x)\right]=\dfrac{1}{|2x|\sqrt{\left(2x\right)^2-1}}\cdot (2)$$

Therefore, by Equations [\[eq:dcf1\]](#eq:dcf1){reference-type="eqref"
reference="eq:dcf1"} and [\[eq:dsg1\]](#eq:dsg1){reference-type="eqref"
reference="eq:dsg1"} we have

$$\frac{d}{dx}\left[\cot^{-1}\left( \sqrt{4x^2-1} \right)+\sec^{-1}(2x)\right]=-\dfrac{1}{\left(\sqrt{4x^2-1}\right)^2+1}\cdot \dfrac{8x}{2\sqrt{4x^2-1}}+\dfrac{2}{|2x|\sqrt{\left(2x\right)^2-1}}$$

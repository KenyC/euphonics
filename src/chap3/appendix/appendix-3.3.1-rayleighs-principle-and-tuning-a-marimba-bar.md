## 3.3.1 : Rayleigh's principle and tuning a marimba bar {#rayleighs-principle-and-tuning-a-marimba-bar .entry-title}

Rayleigh's principle gives a powerful tool for understanding the effect
on the natural frequencies of any system, when a small change is made.
The argument is very general. Recall what Rayleigh's principle says: if
you can guess a reasonable approximation to a mode shape, then by
substituting it into the expression for the Rayleigh quotient you obtain
an estimate of the associated squared natural frequency that is *more
accurate* than your mode guess. Now suppose you have a structure that
you have already analysed to find its mode shapes and frequencies. You
decide to modify the structure a bit. Can you make a reasonable guess at
a new mode shape? Of course you can: if the change is small, you simply
use the mode shape of the original system. So the method is to take the
modified expression for the Rayleigh quotient, incorporating the
structural change, but evaluate it with the original mode shape. That
will give an estimate of the new squared frequency that is correct to
leading order in your small perturbation.

A good illustration of this is the problem of making a small adjustment
to the thickness distribution along the length of a bending beam. The
first step is to see how we can apply Rayleigh's principle at all to a
continuous system like a beam. Recall from section 3.2.5 that the
starting point requires expressions for the potential and kinetic
energies of the vibrating system. Previously we looked at discrete
systems, so that the energies were expressed as summations. But for a
continuous system like a bending beam, these sums turn into integrals.

If the displacement of the beam is $w(x,t)$, the kinetic energy is
very easy to write down. Each small element of the beam contributes an
amount "$\frac{1}{2}m v^2$", involving the mass and velocity of that
element. Thus the total kinetic energy is simply

$$T=\frac{1}{2}\int_0^L{\rho b h \left(\frac{\partial
w}{\partial t}\right)^2} dx \tag{1}$$

for a beam with rectangular cross-section $b \times h$ so that the
mass per unit length is $\rho b h$. The potential energy requires a
little more thought. The energy in a bending beam is stored in curvature
resisted by the bending moment. The assumption (see section 3.2.1) was
that the bending moment was proportional to the curvature, with constant
of proportionality $EI$. The result is that each small element of the
beam has stored energy per unit length "$\frac{1}{2}EI \times
\mathrm{(curvature)}^2$". This is directly analogous to the more
familiar result for a spring of stiffness $k$ stretched by a distance
$z$: the stored energy is $\frac{1}{2}k z^2$. So the total
potential energy of our rectangular-section beam is

$$V=\frac{1}{2}\int_0^L{\frac{E b h^3}{12}
\left(\frac{\partial^2 w}{\partial x^2}\right)^2} dx
.\tag{2}$$

We are interested in the case where the width $b$ stays constant, but
the thickness $h$ can vary with $x$. So we can write the Rayleigh
quotient in the form

$$R=\frac{E}{12 \rho} \frac{\int_0^L{ h^3
(w^{\prime\prime})^2} dx}{\int_0^L{h w^2} dx} .\tag{3}$$

where $w^{\prime\prime}$ denotes the second derivative of $w$
with respect to $x$. We can start from the case with constant
$h=h_0$, which we have already analysed to give the mode shapes
plotted in Fig. 1 of section 3.2. Now suppose that we remove a bit of
material from our beam, so that the thickness becomes
$h=h_0\lbrack{}1-\delta(x)\rbrack{}$. Consider one of the mode shapes $u_n(x)$,
with natural frequency $\omega_n$. We know that

$$\omega_n^2=\frac{E h_0^2}{12 \rho}
\frac{\int_0^L{(u_n^{\prime\prime})^2} dx}{\int_0^L{u_n^2} dx}
.\tag{4}$$

Now the new value is given, courtesy of Rayleigh, by

$$\omega^2 \approx \frac{E h_0^2}{12 \rho} \frac{\int_0^L{
(1-\delta)^3 (u_n^{\prime\prime})^2} dx}{\int_0^L{(1-\delta)
u_n^2} dx}\tag{5}$$

$$\approx \frac{E h_0^2}{12 \rho} \frac{\int_0^L{ (1-3\delta)
(u_n^{\prime\prime})^2} dx}{\int_0^L{(1-\delta) u_n^2} dx}$$

$$\approx \frac{E h_0^2}{12 \rho} \frac{\int_0^L{ (1-3\delta)
(u_n^{\prime\prime})^2} dx}{\int_0^L{u_n^2} dx} \times
\left\lbrack{}1 + \frac{\int_0^L{\delta u_n^2 dx}}{\int_0^L{u_n^2} dx}
\right\rbrack{}$$

ignoring terms of order $\delta^2$ or higher, and making use of the
binomial theorem for the last line. Now using eq. (4), we obtain

$$\omega^2 \approx \omega_n^2 - \frac{E h_0^2}{4 \rho}
\frac{\int_0^L{\delta (u_n^{\prime\prime})^2
dx}}{\int_0^L{u_n^2} dx} + \omega_n^2 \frac{\int_0^L{\delta
u_n^2 dx}}{\int_0^L{u_n^2} dx} \tag{6}$$

$$= \omega_n^2\left\lbrack{}1 - 3\frac{\int_0^L{\delta
(u_n^{\prime\prime})^2 dx}}{\int_0^L{(u_n^{\prime\prime})^2}
dx} + \frac{\int_0^L{\delta u_n^2 dx}}{\int_0^L{u_n^2} dx}
\right\rbrack{}$$

$$=\omega_n^2\left\lbrack{}1+ \int_0^L{G_n(x) \delta(x) dx}\right\rbrack{}
\tag{7}$$

where

$$G_n(x)=-\frac{3
(u_n^{\prime\prime})^2}{\int_0^L{(u_n^{\prime\prime})^2 dx}} +
\frac{u_n^2}{\int_0^L{u_n^2 dx}} . \tag{8}$$

So despite the complication of this derivation, eq. (7) tells a simple
story. The function $G_n$ tells you everything you need to know about
the sensitivity of this particular natural frequency to modifications in
thickness. If you scrape away some material in a region where $G_n$ is
positive, the natural frequency will rise. Where $G_n$ is negative, it
will fall.

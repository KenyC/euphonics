## 4.1.3 Energy, intensity and impedance {#energy-intensity-and-impedance .entry-title}

We start by rewriting eqs. (15) and (16) from section 4.1.1 in terms of
the particle velocity $\underline{v^{\prime}}=\frac{\partial
\underline{\xi}}{\partial t}$, to obtain

$$-\rho_0 \nabla \cdot \underline{v^{\prime}} = \frac{1}{c^2}
\frac{\partial p^{\prime}}{\partial t} \tag{1}$$

and

$$\rho_0 \frac{\partial \underline{v^{\prime}}}{\partial t} = - \nabla
p^{\prime} . \tag{2}$$

We can combine these to give an important energy equation. Multiply eq.
(1) by $p^{\prime}/\rho_0$, take the scalar product of eq. (2) with
$\underline{v^{\prime}}$ and add the two together:

$$\dfrac{1}{\rho_0 c^2} p^{\prime} \dfrac{\partial p^{\prime}}{\partial t} + p^{\prime}
\nabla \cdot \underline{v^{\prime}} + \rho_0 \underline{v^{\prime}} \cdot
\dfrac{\partial \underline{v^{\prime}}}{\partial t} + \underline{v^{\prime}} \cdot
\nabla p^{\prime} = 0 \tag{3}$$

which can be rewritten

$$\dfrac{\partial}{\partial t} \left( \dfrac{1}{2} \rho_0
v^{\prime}^2 + \dfrac{1}{2 \rho_0 c^2} p^{\prime}^2 \right) + \nabla \cdot (p^{\prime}
\underline{v^{\prime}}) = 0 . \tag{4}$$

The two terms in the brackets describe the kinetic energy density
$E_k=\rho_0 v^{\prime}^2/2$ and the potential energy density stored in
compression of the air, $E_p=p^{\prime}^2/2 \rho_0 c^2$. The final term
relates to energy flux. The vector $\underline{I}=p^{\prime} \underline{v^{\prime}}$
is called the intensity: it gives the rate and direction at which
acoustic energy crosses a unit area of space. If eq. (4) is integrated
over a volume $V$ bounded by a surface $S$, we obtain

$$\int_V{\dfrac{\partial}{\partial t} (E_k+E_p) dV} +
\int_V{\nabla \cdot \underline{I} dV}=0 \tag{5}$$

so, using the divergence theorem,

$$\int_V{\dfrac{\partial}{\partial t} (E_k+E_p) dV} +
\int_S{\underline{I} \cdot \underline{n} dS}=0 \tag{6}$$

which implies that the rate of change of total energy inside $V$ is
balanced by energy transport across its surface $S$ which is governed
by the intensity.

For a plane wave in the $x$ direction, we can write $p^{\prime}=\hat{p}
e^{i \omega (t-x/c)}$. The only non-zero component of velocity will
be in the $x$ direction; we can denote it $u'$. From the $x$
component of eq. (2), we then have

$$-\rho_0 \dfrac{\partial u^{\prime}}{\partial t} = \dfrac{\partial
p^{\prime}}{\partial x} = -\dfrac{i \omega \hat{p}}{c} e^{i \omega
(t-x/c)} \tag{7}$$

so that

$$u^{\prime} = \dfrac{\hat{p}}{\rho_0 c} e^{i \omega (t-x/c)} .
\tag{8}$$

Pressure and velocity are in phase, and their ratio, called *impedance*,
is

$$\frac{p^{\prime}}{u^{\prime}} = \rho_o c =Z \tag{9}$$

where $Z$ is a real value that is independent of frequency. It is a
material property of the air, called the *characteristic impedance*, or
sometimes *wave impedance*.

The concept of impedance is used in several fields of science, and the
general context is always the same. There are two variables, one
force-like and the other motion-like, whose product gives *power.* In an
electrical system we would have voltage and current, in a mechanical
system we would have force and velocity. For our sound wave we have
force per unit area, i.e. pressure, and velocity, so that their product
gives power per unit area. In all these cases the impedance is the ratio
of the force-like variable to the motion-like variable. The inverse
ratio is called *admittance*. We will look extensively at mechanical
admittance of stringed instrument bodies in Chapter 5.

Returning to our plane wave in the $x$ direction, the intensity vector
is also in the $x$ direction, with magnitude

$$I=p^{\prime} u^{\prime} = \dfrac{\hat{p}^2}{Z} \cos^2{\omega (t-x/c)} .
\tag{10}$$

Note that we can't use the complex exponential representation directly
here, because intensity is a nonlinear quantity. At a position $x$,
the intensity varies with time with a $\cos^2$ dependence. The most
interesting quantity is the average intensity over one cycle, and since
we know that the average value of $\cos^2$ is 1/2, the result is

$$\left\langle I \right\rangle =\frac{1}{2} \frac{\hat{p}^2}{Z} .
\tag{11}$$

For the spherical wave from section 4.1.2 we have

$$p^{\prime}=\frac{\hat{p}}{r} e^{i \omega t - i k r} \tag{12}$$

from eq. (7), and

$$u^{\prime} = \frac{\hat{p}}{i\omega \rho_0 r} \left( \frac{1}{r}
+\frac{i \omega}{c} \right) e^{i\omega t - ikr} =
\frac{\hat{p}}{\rho_0 r} \left(\frac{1}{c} + \frac{1}{i \omega
r}\right) e^{i\omega t - ikr}\tag{13}$$

for the radial component of velocity. We want to multiply this by $p^{\prime}$
from eq. (12) and average over a cycle, as we did in the plane-wave
case. But this time we need to be a bit careful. The first term in the
brackets in eq. (13) describes a component of $u'$ that is in phase
with $p^{\prime}$, so that we can average the product as before, gaining a
factor 1/2 in the process. But the second term has an extra factor of
$i$ in the complex representation: this component of velocity is in
*quadrature* with the pressure (i.e. $90^\circ$ out of phase), which
means that the product of the two will average to zero over one cycle.
So we only need to keep the first term, with the result

$$\left\langle I \right\rangle =\frac{1}{2} \frac{\hat{p}^2}{Z}
\tag{14}$$

exactly as in the case of the plane wave.

This calculation gives a clue for how we should interpret the near field
and far field in this example. The term in eq. (13) which contributed to
energy transport was the far field term, decaying like $1/r$. The near
field term, decaying like $1/r^2$, was the one in quadrature,
involving no net energy flow. This near field term has a simple physical
interpretation: it describes *incompressible* motion of the air around
the pulsating sphere. You can picture it by thinking of pumping up a
spherical balloon under water: the water flow will be essentially
incompressible, and it gets pushed symmetrically outwards by the growing
sphere. For incompressible motion like this, the condition on a
spherical surface of radius $r$ is that the total *volume flow* across
the surface must be independent of $r$. The area of the surface is
proportional to $r^2$, so we see why the velocity needs to vary like
$1/r^2$. This interpretation applies to many problems involving sound
sources with small Helmholtz number. Within the near field, there is a
component of incompressible motion, which can dominate over the
sound-radiating component of motion at small distances.

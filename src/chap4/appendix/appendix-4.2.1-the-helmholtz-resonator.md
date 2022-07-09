## 4.2.1 The Helmholtz resonator {#the-helmholtz-resonator .entry-title}

Figure 1 shows the geometry of an idealised Helmholtz resonator. A
vessel with rigid walls encloses a volume $V$, and is connected to the
outside world via a neck of length $L$ and cross-sectional area $S$.
As usual, we assume that the pressure and density take the forms
$p(t)=p_0+p^{\prime}(t)$ and $\rho(t)=\rho_0+\rho^{\prime}(t)$, where
subscripts 0 denote the steady atmospheric pressure and density, and
primes denote the acoustic perturbations, assumed to be small in
comparison. We consider the case where the acoustic pressure is
$p'_1(t)$ just outside the neck of the vessel, and we aim to
calculate the corresponding pressure $p'_2(t)$ inside the volume. We
define the mass flow rate inwards through the neck to be $q(t)$.

![Figure 1. An idealised Helmholtz resonator: a rigid bottle of volume V
with a neck of length L and cross-sectional area
S](uploads/2021/01/Bottle-1024x481.jpg){width="100%"}

Conservation of mass requires that

$$q=V\dfrac{\partial \rho^{\prime}}{\partial t} \tag{1}$$

so for a harmonic disturbance at angular frequency $\omega$,

$$q=V i \omega \rho^{\prime} . \tag{2}$$

This density change produces a proportional change in pressure, and we
already know from section 4.1.1 that the constant of proportionality is
the square of the speed of sound $c$:

$$p^{\prime}_2=c^2 \rho^{\prime}_2 = \dfrac{c^2 q}{i \omega V} . \tag{3}$$

Now if the "plug" of air in the neck moves as a rigid body, Newton's law
requires

$$\left( p^{\prime}_1 - p^{\prime}_2 \right) S = \rho_0 L S \dfrac{\partial
u}{\partial t} \tag{4}$$

where $u$ is the velocity of the plug into the neck. But $q=\rho_o S
u$, so

$$p^{\prime}_1 = \dfrac{c^2 q}{i \omega V} + \dfrac{L}{S} i \omega q .
\tag{5}$$

Thus

$$q= -\dfrac{i \omega S}{L} \dfrac{p^{\prime}_1}{\left\lbrack{}\omega^2
-\frac{c^2 S}{VL}\right\rbrack{}} \tag{6}$$

and so finally

$$p^{\prime}_2= -\dfrac{c^2 S}{VL} \dfrac{p^{\prime}_1}{\left\lbrack{}\omega^2
-\frac{c^2 S}{VL}\right\rbrack{}} . \tag{7}$$

Resonance obviously occurs when

$$\omega = c \sqrt{\frac{S}{VL}} .\tag{8}$$

In this very simple theoretical model the response is infinite at
resonance. As usual, the amplitude is limited in practice by damping,
which in this case arises from viscous losses and from sound radiation.

To calculate a Helmholtz resonance frequency more accurately we would
need to include an *end correction*: the effective mass of air moving in
and around the neck is a little larger than the geometric dimensions of
the neck itself, because of the kinetic energy involved in the air flow
near the ends of the neck. This is usually allowed for by adding a small
extra length to the real length. The magnitude of the required
correction depends on the geometry around the opening, and requires
numerical calculation. Two simple idealised cases give an idea of the
magnitude: they involve a circular opening of radius $a$, and a neck
which is either "flanged" or "unflanged", as sketched in Fig. 2.

![Figure 2. End corrections for a neck without (left) and with (right) a
flange](uploads/2021/01/end_corrections-1024x443.jpg){width="100%"}

One consequence is that even a thin-walled vessel with an opening can
show a Helmholtz resonance: an example is sketched in Fig. 3. For this
case there is a "flange" on both sides of the opening, so the effective
neck length for a circular opening of radius $a$ will be $L \approx
2 \times 0.85 a=1.7 a$.

![Figure 3. A thin-walled Helmholtz resonator, where the effective neck
length consists entirely of the end
corrections.](uploads/2021/01/no_neck.jpg){width="100%"}

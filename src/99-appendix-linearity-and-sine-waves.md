# Appendix to 2.1 : Linearity and sine waves {#linearity-and-sine-waves}

The technical definition of a linear system is as follows. Suppose we
know that an input $f_1(t)$ produces an output $g_1(t)$, while an
input $f_2(t)$ produces an output $g_2(t)$. Then it will always be
the case that any linear combination of the two inputs will produce the
same linear combination of the outputs. So for example input
$2f_1-f_2$ will give the output $2g_1-g_2$. Provided we also assume
that the properties of the system itself do not vary with time (although
of course the input will vary with time), then this is enough
information to be able to prove the "sine wave in, sine wave out" result
described in the main text.

The underlying mathematical reason for the importance of sine waves is
that they are *eigenfunctions* of the process of differentiation:
differentiating a sine wave gives another sine wave, changed only in
amplitude and phase. This is related to the "sine wave in, sine wave
out" property: if you imagine that your system in the "black box" is
described by a differential equation of some kind, then if the equation
is linear in the usual mathematical sense, it consists of a linear
combination of the function and its derivatives. It follows that if the
function is a sine wave, then the total output will still be a sine wave
since each separate term in the equation gives a sine wave, and adding
sine waves together (all at the same frequency) still leaves another
sine wave.

For many algebraic manipulations involving sine waves, it is easier to
use the complex-number representation, taking advantage of the famous
result

$$e^{i \omega t}=\cos \omega t+i\sin \omega t . \tag{1}$$

This allows us to package the amplitude and phase of a sine wave into a
single complex number. From equation (1), $\cos\omega
t=\mathrm{Re}(e^{i \omega t})$. Now suppose we have a sine wave with
amplitude $a$ and phase $\phi$:

$$f(t)=a\cos(\omega t + \phi)=\mathrm{Re}(ae^{i \omega
t+i\phi})=\mathrm{Re}(Ae^{i \omega t}) \tag{2}$$

where

$$A=ae^{i\phi}. \tag{3}$$

As a shorthand, we usually do not bother to write the
$\mathrm{Re}(...)$. We just talk about a sine wave $Ae^{i \omega
t}$ with frequency $\omega$ and (complex) amplitude $A$. Just keep
in the back of the mind that if the answer to a calculation involves
complex numbers, then what we really mean is that the physical solution
is the Real part of the complex answer.

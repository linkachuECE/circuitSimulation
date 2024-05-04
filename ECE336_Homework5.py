import cmath
import math

from circuitFunctions import *

### PROBLEM 3 ###

def power_IZ(current, impedance):
    return (1/2) * (current * phasorConjugate(current)) * impedance

def power_VI(voltage, current):
    return (1/2) * voltage * phasorConjugate(current)

omega = 20
R1 = 10
R2 = 3
R3 = 2
L1 = 8
L2 = 8
Lm = 2

Zr1 = R1
Zr2 = R2
Zr3 = R3
Zl1 = impedanceInductor(L1, omega)
Zl2 = impedanceInductor(L2, omega)
Zlm = impedanceInductor(Lm, omega)

Vs = 20

I1 = phasor_rect(1.79987, 0.21475)
I2 = phasor_rect(1.13278, 0.93058)
I3 = phasor_rect(0.28024, 0.23615)

Ir1 = I1
Ir2 = (I1 - I2)
Ir3 = I3

Vr1 = Ir1 * Zr1
Vr2 = Ir2 * Zr2
Vr3 = Ir3 * Zr3

Sr1 = power_IZ(Ir1, Zr1)
Sr2 = power_IZ(Ir2, Zr2)
Sr3 = power_IZ(Ir3, Zr3)

Svs = power_VI(Vs, I1)

# PROBLEM 5
omega = 10
Vs = 3
R = 30
L1 = 10
L2 = 10
Lm = 3
C = 2 * 10**(-3)

Zc = impedanceCapacitor(C, omega)
Zl1 = impedanceInductor(L1, omega)
Zl2 = impedanceInductor(L2, omega)
Zlm = impedanceInductor(Lm, omega)
Zr = R

I1 = phasor_rect(-0.00621, -0.04552)
I2 = phasor_rect(0.01552, -0.03621)

Il1 = I1
Il2 = I2
Ic = I1 - I2
Ir = I2

Sl1 = power_IZ(Il1, Zl1)
Sl2 = power_IZ(Il2, Zl2)
Sc = power_IZ(Ic, Zc)
Sr = power_IZ(Ir, Zr)

Svs = power_VI(Vs, I1)

# PROBLEM 6

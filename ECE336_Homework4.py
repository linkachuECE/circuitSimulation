import cmath
import math

from circuitFunctions import *

### PROBLEM 1 ###

omega = 8

C = (1/320)
R = 100
L = 10

Vs = phasor_polar(10, 30)
Is = phasor_polar(0.1, 0)
Zl = impedanceInductor(L, omega)
Zc = impedanceCapacitor(C, omega)
Zr = R

Vx = ((Vs/Zl) + Is) * parallelImpedance(Zl, Zc)
Vy = Vx + (Is * Zr)

Vl = Vs - Vx
Vc = Vx
Vr = Vy - Vx

Il = Vl/Zl
Ic = Vc/Zc
Ir = Vr/Zr

Ivs = Il
Vis = Vy

Sl = (1/2) * Vl * phasorConjugate(Il)
Sc = (1/2) * Vc * phasorConjugate(Ic)
Sr = (1/2) * Vr * phasorConjugate(Ir)

Sis = (1/2) * Vis * phasorConjugate(Is)
Svs = (1/2) * Vs * phasorConjugate(Ivs)

Sabsorbed = Sl + Sc + Sr
Sgiven = Svs + Sis

### PROBLEM 5 ###

omega = 10

Vs = phasor_polar(240, 0)
Is = phasor_polar(4, 0)

R1 = 50
R2 = 40
C = 5 * (10**(-3))
L = 3

Zr1 = R1
Zr2 = R2
Zc = impedanceCapacitor(C, omega)
Zl = impedanceInductor(L, omega)

Vx = ((Vs/Zr1) + Is) * parallelImpedance(Zr1, Zc, (Zl + Zr2))

Vr1 = (Vs - Vx)
Vc = Vx
Vr2 = Vx * (Zr2/(Zr2 + Zl))
Vl = Vx * (Zl/(Zr2 + Zl))

Ir1 = Vr1/Zr1
Ir2 = Vr2/Zr2
Il = Vl/Zl
Ic = Vc/Zc

Sr1 = (1/2) * Vr1 * phasorConjugate(Ir1)
Sr2 = (1/2) * Vr2 * phasorConjugate(Ir2)
Sl = (1/2) * Vl * phasorConjugate(Il)
Sc = (1/2) * Vc * phasorConjugate(Ic)

Ivs = Ir1
Vis = Vx

Sis = (1/2) * Vis * phasorConjugate(Is)
Svs = (1/2) * Vs * phasorConjugate(Ivs)

Sabsorbed = Sr1 + Sr2 + Sc + Sl
Sgiven = Sis + Svs

### PROBLEM 6 ###

Vs = phasor_polar(2, 0)

omega = 3
R = 4
L = 1
C = (1/9)

Zr = R
Zl = impedanceInductor(L, omega)
Zc = impedanceCapacitor(C, omega)

Vx = (Vs/Zc) * parallelImpedance((Zl + Zr), Zc, 0.1)
Vy = Vs - Vx

Is = 0.1 * Vx
Ivs = Vx/(Zr + Zl)

Vr = Ivs * Zr
Vl = Ivs * Zl
Vc = Vy

Ir = Vr/Zr
Il = Vl/Zl
Ic = Vc/Zc

Sr = (1/2) * Vr * phasorConjugate(Ir)
Sc = (1/2) * Vc * phasorConjugate(Ic)
Sl = (1/2) * Vl * phasorConjugate(Il)

Vis = Vy

Svs = (1/2) * Vs * phasorConjugate(Ivs)
Sis = (1/2) * Vis * phasorConjugate(Is)

Sabsorbed = Sr + Sc + Sl
Sgiven = Svs + Sis

prettyPrintPhasor(Sgiven - Sabsorbed)
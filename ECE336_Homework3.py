import cmath
import math

from circuitFunctions import *

###### HOMEWORK 3 #######

## QUESTION 4 ##
omega = 20
Vs = 3
Is = 0.1
Zr = 80
Zc = phasor_rect(0, -50)
Zl = phasor_rect(0, 20)

Va = parallelImpedance(Zc, Zl) * ((Vs/Zc) + (Is))

Vx = Va + (Is * Zr)

I1 = (Vs - Va)/Zc

I2 = Va/Zl

## QUESTION 5 ##
Zc = phasor_rect(0, -1/(20 * 0.001))
Zl = phasor_rect(0, 20 * 10)
R1 = 80
R2 = 30
Is = 3

Zthev = Zc + R1 + Zl
Vthev = Is * (R1 + Zl)
Inort = Vthev / Zthev

## QUESTION 6 ##

Vs = 2
Zl = phasor_rect(0, 60)
Zc = phasor_rect(0, -25)
Zr = 30

Vout = (-((Zc + Zr)/Zl)) * Vs
Iout = (Vout/1000)

## QUESTION 7 ##

# Current source 1
R = 80
Zl1 = phasor_rect(0, 20)
Zc1 = phasor_rect(0, -100)
Is1 = 8

Zt1 = parallelImpedance(R, Zl1, Zc1)
V1 = Is1 * Zt1

# Current source 2
R = 80
Zl2 = phasor_rect(0, 200)
Zc2 = phasor_rect(0, -10)
Is2 = 3

Zt2 = parallelImpedance(R, Zl2, Zc2)
V2 = Is2 * Zt2

prettyPrintPhasor(V2)
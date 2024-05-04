import cmath
import math
from circuitFunctions import *

# FUCKING AROUND
Vt = phasor_polar(6, 30)
Zl1 = phasor_rect(0, 120)
Zl2 = phasor_rect(0, 60)
Zc1 = phasor_rect(0, -0.25)
Zr1 = 2

Zt = parallelImpedance(Zc1 + Zr1, Zl2) + Zl1

It = Vt / Zt

# I1 = It * (Zl2/(Zl2 + Zr1 + Zc1))

Va = Vt - (It * Zl1)
I1 = Va / (Zr1 + Zc1)
I2 = Va / Zl2

prettyPrintPhasor(Va)
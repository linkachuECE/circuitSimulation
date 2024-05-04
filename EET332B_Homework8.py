import cmath
import math

from circuitFunctions import *

### HOMEWORK 8 ###

Z = phasor_polar(27.7, -40)
Vp = 277.1
Van = Vp * phasor_polar(1, 0)
Vbn = Vp * phasor_polar(1, -120)
Vcn = Vp * phasor_polar(1, 120)

Vab = math.sqrt(3) * Van * phasor_polar(1, 30)
Vbc = math.sqrt(3) * Vbn * phasor_polar(1, 30)
Vca = math.sqrt(3) * Vcn * phasor_polar(1, 30)

V1 = Vab
V2 = Vbc
V3 = Vca

I1 = V1/Z
I2 = V2/Z
I3 = V3/Z

Il1 = math.sqrt(3) * I1 * phasor_polar(1, -30)
Il2 = math.sqrt(3) * I2 * phasor_polar(1, -30)
Il3 = math.sqrt(3) * I3 * phasor_polar(1, -30)

prettyPrintPhasor(Il3)
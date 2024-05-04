import cmath
import math

from circuitFunctions import *

###### HOMEWORK 2 #######

# PROBLEM 1 #

# Declarations
Vs = phasor_polar(3, -90)
Is = phasor_polar(2, 0)
Zr = 10                       # 10 ohms
Zc = phasor_rect(0, -12.5)    # -j12.5 ohms
Zl = phasor_rect(0, 24)       # j24 ohms

# Calculations
Va = parallelImpedance(Zr, Zl) * (Is + (Vs/Zr))

Vb = Va + (Zc + Is)

# prettyPrintPhasor(Vb)
# prettyPrintPhasor(Vb)

# PROBLEM 2 #

# Declarations
Vs = phasor_polar(6, 0)
Zr1 = 20                    # 20 ohms
Zr2 = 20                    # 20 ohms
Zc1 = phasor_rect(0, -20)   # -j20
Zl1 = phasor_rect(0, 10)    # j10
Zr3 = 30                    # 30 ohms

# Calculations
Vb = phasor_polar(3, 83.4)
Va = 1 - (phasor_polar(0.11, -18.43) * Vb)

I3 = Vb / (Zl1 + Zr3)

Vo = I3 * Zr3

# prettyPrintPhasor(Vo)

# PROBLEM 3 #

# Declarations

Vs1 = phasor_polar(10, 0)
Vs2 = phasor_polar(6, -90)
Zr = 4
Zl = phasor_rect(0, 4)
Zc = phasor_rect(0, -2)

Va = (1/((1/Zr) + (1/Zl) + (1/Zc))) * ((Vs1/Zr) + (Vs2/Zl))

I1 = (Vs1 - Va)/Zr
I2 = (Vs2 - Va)/Zl

# prettyPrintPhasor(I2)


# PROBLEM 4 #

# Declarations
Is = phasor_polar(4, 30)
Zl = phasor_rect(0, 2000)
Zc = phasor_rect(0, -1000)
Zr = 2000

# Calculations

Vthevenin = Is * (1/((1/Zl) + (1/Zr)))
Rthevenin = Zc + parallelImpedance(Zl, Zr)


# prettyPrintPhasor(Rthevenin)

# PROBLEM 5 #

# Declarations
Vs = 100
It = phasor_polar(3, -60)   

# Calculations
Zt = Vs/It

Zr = Zt.real
Zl = phasor_rect(0, 50)

Zc = Zt.imag

# PROBLEM 6
Vs = phasor_polar(3, 30)
Zc = phasor_rect(0, -1000000)
Zr1 = phasor_rect(2000, 0)
Zr2 = phasor_rect(10000, 0)

Z1 = parallelImpedance(Zc, Zr2)
Z2 = Zr1

Vo = Vs * (1 + (Z1/Z2))

prettyPrintPhasor(Vo)
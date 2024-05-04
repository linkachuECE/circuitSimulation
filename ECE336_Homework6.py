import cmath
import math

from circuitFunctions import *

def power_IZ(current, impedance):
    return (1/2) * (current * phasorConjugate(current)) * impedance

def power_VI(voltage, current):
    return (1/2) * voltage * phasorConjugate(current)

def power_VZ(voltage, impedance):
    return (1/2) * ((voltage * phasorConjugate(voltage)) / phasorConjugate(impedance))

### PROBLEM 3 ###

omega = 8

Va = phasor_polar(20, -90)
Vb = phasor_polar(20, 150)
Vc = phasor_polar(20, 30)

Ra = 3
Rb = 7
Rc = 6
Zra = Ra
Zrb = Rb
Zrc = Rc

La = 5
Lb = 3
Lc = 2
Zla = impedanceInductor(La, omega)
Zlb = impedanceInductor(Lb, omega)
Zlc = impedanceInductor(Lc, omega)

Za = Zra + Zla
Zb = Zrb + Zlb
Zc = Zrc + Zlc

Vn = ((Va/Za) + (Vb/Zb) + (Vc/Zc)) * parallelImpedance((Za), (Zb), (Zc))

Vza = Va - Vn
Vzb = Vb - Vn
Vzc = Vc - Vn

Sa = power_VZ(Vza, Za)
Sb = power_VZ(Vzb, Zb)
Sc = power_VZ(Vzc, Zc)

St = Sa + Sb + Sc

Ia = Vza/Za
Ib = Vzb/Zb
Ic = Vzc/Zc

Sva = power_VI(Va, Ia)
Svb = power_VI(Vb, Ib)
Svc = power_VI(Vc, Ic)

### PROBLEM 4 ###

omega = 10

Va = phasor_polar(30, 0)
Vb = phasor_polar(30, -120)
Vc = phasor_polar(30, 120)

Ra = 2
Rb = 4
Rc = 6
Zra = Ra
Zrb = Rb
Zrc = Rc

La = 3
Lb = 8
Lc = 9
Zla = impedanceInductor(La, omega)
Zlb = impedanceInductor(Lb, omega)
Zlc = impedanceInductor(Lc, omega)

Za = Zra + Zla
Zb = Zrb + Zlb
Zc = Zrc + Zlc

# prettyPrintPhasor(Za, "Za", "ohms")
# prettyPrintPhasor(Zb, "Zb", "ohms")
# prettyPrintPhasor(Zc, "Zc", "ohms")

Ia = Va/Za
Ib = Vb/Zb
Ic = Vc/Zc

# prettyPrintPhasor(Ia, "Ia", "A")
# prettyPrintPhasor(Ib, "Ib", "A")
# prettyPrintPhasor(Ic, "Ic", "A")

Sa = power_VI(Va, Ia)
Sb = power_VI(Vb, Ib)
Sc = power_VI(Vc, Ic)

# prettyPrintPhasor(Sa, "Sa", "VA")
# prettyPrintPhasor(Sb, "Sb", "VA")
# prettyPrintPhasor(Sc, "Sc", "VA")

# prettyPrintPhasor(Vb * Ib)




# PROBLEM 5
Vlrms = 220
Vl = Vlrms * math.sqrt(2)

Vab = Vl * phasor_polar(1, 0)
Vbc = Vl * phasor_polar(1, 120)
Vca = Vl * phasor_polar(1, 240)

# prettyPrintPhasor(Vl, "Vl", "V")

Z1 = 33
Z2 = 47

Ip1 = Vl/Z1
Ip2 = Vl/Z2
# prettyPrintPhasor(Ip1, "Ip1", "A")
# prettyPrintPhasor(Ip2, "Ip2", "A")

Il1 = math.sqrt(3) * Ip1
Il2 = math.sqrt(3) * Ip2
Ilt = (Il1 + Il2)
# prettyPrintPhasor(Il1, "Il1", "A")
# prettyPrintPhasor(Il2, "Il2", "A")
# prettyPrintPhasor(Ilt, "Ilt", "A")


# PROBLEM 6
Vsrms = 480 / math.sqrt(3)
Vs = Vsrms * math.sqrt(2)

Va = Vs * phasor_polar(1, -30)
Vb = Vs * phasor_polar(1, -150)
Vc = Vs * phasor_polar(1, 90)
# prettyPrintPhasor(Va, "Va", "V")
# prettyPrintPhasor(Vb, "Vb", "V")
# prettyPrintPhasor(Vc, "Vc", "V")

Vl = phasorMagnitude(math.sqrt(3) * Va)
# prettyPrintPhasor(Vl, "Vl", "V")

Zdelta = phasor_polar(16, -75)
Zline = 12
# prettyPrintPhasor(Zdelta, "Zdelta", "ohms")
# prettyPrintPhasor(Zline, "Zline", "ohms")

# prettyPrintPhasor(1/Zdelta, "1/Zdelta")
# prettyPrintPhasor((-1/Zline) - (2/Zdelta), "(-1/Zline) - (2/Zdelta)")

# prettyPrintPhasor((-1/Zdelta) * Va, "-1/Zdelta * Va")
# prettyPrintPhasor((-1/Zdelta) * Vb, "-1/Zdelta * Vb")
# prettyPrintPhasor((-1/Zdelta) * Vc, "-1/Zdelta * Vc")

Vx = phasor_polar(109.33874,-8.89874)
Vy = phasor_polar(109.34510,-128.89686)
Vz = phasor_polar(109.34060, 111.10360)

Ia = Va - Vx/Zline

Vxy = Vx - Vy
Ixy = (Vx - Vy)/Zdelta

# prettyPrintPhasor(Vxy, "Vxy", "V")
# prettyPrintPhasor(Ia, "Ia", "A")
# prettyPrintPhasor(Ixy, "Ixy", "A")

# PROBLEM 7

omega = 377

Vs = 170

Va = Vs * phasor_polar(1, 0)
Vb = Vs * phasor_polar(1, -120)
Vc = Vs * phasor_polar(1, 120)

R = 1000
C = 2 * 10**(-6)
L = 3

Zr = R
Zc = impedanceCapacitor(C, omega)
Zl = impedanceInductor(L, omega)
# prettyPrintPhasor(Zc, "Zc", "ohms")
# prettyPrintPhasor(Zl, "Zl", "ohms")

Iab = (Va - Vb)/(Zr)
Ibc = (Vb - Vc)/(Zl)
Ica = (Vc - Va)/(Zc)
# prettyPrintPhasor(Iab, "Iab", "A")
# prettyPrintPhasor(Ibc, "Ibc", "A")
# prettyPrintPhasor(Ica, "Ica", "A")

Ia = Iab - Ica
Ib = Ibc - Iab
Ic = Ica - Ibc
# prettyPrintPhasor(Ia, "Ia", "A")
# prettyPrintPhasor(Ib, "Ib", "A")
# prettyPrintPhasor(Ic, "Ic", "A")

Sa = power_VI(Va, Ia)
Sb = power_VI(Vb, Ib)
Sc = power_VI(Vc, Ic)
# prettyPrintPhasor(Sa, "Sa", "VA")
# prettyPrintPhasor(Sb, "Sb", "VA")
# prettyPrintPhasor(Sc, "Sc", "VA")

St = Sa + Sb + Sc
# prettyPrintPhasor(St, "St", "VA")

prettyPrintPhasor(Va - Vb, "Vab", "V")
prettyPrintPhasor(Vs * math.sqrt(3), "Vl", "V")
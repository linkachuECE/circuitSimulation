import math
import cmath

def phasor_rect(x, y):
    return complex(x, y)

def phasor_polar(r, theta):
    return cmath.rect(r, math.radians(theta))

def polar_InDegrees(phasor):
    return (cmath.polar(phasor)[0], math.degrees(cmath.polar(phasor)[1]))

def phasorMagnitude(phasor):
    return abs(phasor)

def phasorConjugate(phasor):
    magnitude = cmath.polar(phasor)[0]
    angle = math.degrees(cmath.polar(phasor)[1])
    
    newAngle = -angle

    newPhasor = phasor_polar(magnitude, newAngle)

    return newPhasor

def prettyPrintPhasor(phasor, title="", units=""):
    rect = phasor
    pol = polar_InDegrees(phasor)
    
    sym = '-' if rect.imag < 0 else '+'

    title = ("phasor" if title == "" else title)

    print(title + ":")
    print("- Rectangular: {:.8f} {} j{:.8f} {}".format(rect.real, sym, abs(rect.imag), units))
    print("- Polar: {:.8f}r, {:.8f}θ {}\n".format(pol[0], pol[1], units))

def impedanceCapacitor(capacitance, omega):
    return phasor_rect(0, -(1/(omega * capacitance)))

def impedanceInductor(inductance, omega):
    return phasor_rect(0, (omega * inductance))

def parallelImpedance(*args):
    denominator = 0
    for val in args:
        denominator += (1/val)

    return (1 / denominator)
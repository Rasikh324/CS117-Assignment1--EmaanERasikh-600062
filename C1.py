
# Defines functions for current (I = V / R) and power (P = I^2 * R)

def ohms_current(v, r):
    I = v/r
    return I

def power_dissipated(i, r):
    P = i**2*r
    return P

voltage = 12
resistance = 6
current = ohms_current(voltage, resistance)
power = power_dissipated(current, resistance)
print(f"Current = {current} A")
print(f"Power = {power} W")

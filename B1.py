
# Prints the current through a 10 ohm resistor for supply voltages 1 V to 10 V

resistance = 10
for voltage in range(1,11,1):
    print(f"V = {voltage} V, I = {voltage/resistance} A")


# Calculates current from voltage and resistance and checks if the fuse will blow

V = float(input("Enter voltage (V): "))
R = float(input("Enter resistance (ohm): "))
if R <= 0:
    print("Invalid resistance")
else:
    I =V/R
    print(f"Current = {I} A")
    if I > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")

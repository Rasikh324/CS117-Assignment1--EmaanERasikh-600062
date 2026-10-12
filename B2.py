
# Reads the number of series resistors and each value, then prints the total series resistance

total = 0
resistance_count = int(input("How many resistors? "))
for i in range(resistance_count):
    resistance = int(input(f"Enter R{i+1}: "))
    total+= resistance

print(f"Total resistance = {total} ohm")
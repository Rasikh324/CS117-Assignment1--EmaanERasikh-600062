# Finds the count above 3.2 V, highest, lowest and average of sensor readings using one loop
readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
count = 0
highest = readings[0]
total = 0
smallest = readings[0]
for i in range(len(readings)):
    total = total + readings[i]
    if readings[i] > 3.2:
        count += 1
    if readings[i] > highest:
        highest = readings[i]
    if readings[i] < smallest:
        smallest = readings[i]

print(f"Readings above 3.2 V: {count}")
print(f"Highest: {highest} V")
print(f"Lowest: {smallest} V")
print(f"Average: {total/len(readings):.2f} V")
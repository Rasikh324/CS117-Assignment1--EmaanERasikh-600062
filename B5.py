# Bins measured 100-ohm resistors by tolerance until the user enters 0

measured = float(input("Please enter your measurement: "))
one_percent = 0
five_percent = 0
rejected = 0
while measured != 0:
    if 99.0 <= measured <= 101.0:
        one_percent += 1
    elif 95.0 <= measured <= 105.0:
        five_percent += 1
    else:
        rejected += 1
    measured = float(input("Please enter your measurement: "))

print(f"1% tolerance: {one_percent}")
print(f"5% tolerance: {five_percent}")
print(f"Reject: {rejected}")

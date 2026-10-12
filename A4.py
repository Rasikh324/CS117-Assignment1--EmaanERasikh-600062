
# Takes two bits and prints the output of the AND, OR and XOR gates

A = int(input("Enter A: "))
B = int(input("Enter B: "))
if A in (0, 1) and B in (0, 1):
    print("AND =", int(A== 1 and B ==1))
    print("OR =", int(A== 1 or B ==1))
    print("XOR =", int(A != B))
else:
    print("Bits must be 0 or 1")

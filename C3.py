# Converts a positive decimal number to a binary string using repeated division by 2

def decimal_to_binary(n):
    binary = ""

    while n > 0:
        if n % 2 == 0:
            binary = str(0) + binary
        else:
            binary = str(1) + binary
        n = n // 2
    return(binary)

print("decimal_to_binary(10) ->", decimal_to_binary(10))
print("decimal_to_binary(25) ->", decimal_to_binary(25))
# Returns the equivalent resistance of resistors connected in parallel

def parallel_resistance(resistors):
    reciprocal = 0
    total = 0
    for i in range(len(resistors)):
        reciprocal += 1/resistors[i]
    total += 1/reciprocal
    return total

print("parallel_resistance([10, 10]) ->", round(parallel_resistance([10, 10]), 2))
print("parallel_resistance([100, 200, 300]) ->", round(parallel_resistance([100, 200, 300]), 2))

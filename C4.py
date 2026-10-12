
# Calculates the unloaded and loaded output voltage of a voltage divider

def loaded_divider(vs,r1,r2,rl):
    unloaded_voltage = vs* r2/(r1 + r2)
    r_eq = (rl * r2)/(rl + r2)
    loaded_voltage = vs * r_eq/(r1 + r_eq)

    return unloaded_voltage, loaded_voltage
print("loaded_divider(12, 1000, 1000, 500) ->", loaded_divider(12, 1000, 1000, 500))

# Converts a star (Y) network of three resistors to the equivalent delta network

def star_to_delta(ra, rb, rc):
    r_numerator = ra * rb + rb * rc + ra* rc
    r_ab = r_numerator / rc
    r_ca = r_numerator / rb
    r_bc = r_numerator / ra

    return round(r_ab, 2), round(r_bc, 2), round(r_ca, 2)

print("star_to_delta(10, 20, 30) ->", star_to_delta(10, 20, 30))
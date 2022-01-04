G = 6.67408*10**-11

def gravitational_force(M: float,
                        m: float,
                        r: float) -> float:
    F = G * (M*m) / r**2 
    return F

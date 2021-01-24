#Calculates transformed velocity components.
from gamma import gamma

#Define ux', uy', uz' functions.
def u_prime(ux, uy, uz, v):
    c = 299792458   #Define speed of light in m/s.
    ux *= c; uy *= c; uz *= c; v *= c
    ux_prime = (ux - v) / (1 - ux * v / c**2)
    uy_prime = uy / (gamma(v) * (1 - ux * v / c**2))
    uz_prime = uz / (gamma(v) * (1 - ux * v / c**2))
    return ux_prime/c, uy_prime/c, uz_prime/c

#__Main__
if __name__ == "__main__":
    #Ask for input of S frame velocities.
    ux = float(input("Enter ux as a decimal of c:"))
    uy = float(input("Enter uy as a decimal of c:"))
    uz = float(input("Enter uz as a decimal of c:"))
    
    #Get relative velocity of frames.
    v = float(input("Enter the relative frames velocity as a decimal of c:"))
    print("")
    
    #Calculate S' velocities.
    ux_prime, uy_prime, uz_prime = u_prime(ux, uy, uz, v)
    print("The value of ux_prime =", ux_prime, "c")
    print("The value of uy_prime =", uy_prime, "c")
    print("The value of uz_prime =", uz_prime, "c")
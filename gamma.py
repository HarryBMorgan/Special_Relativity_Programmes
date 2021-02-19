#Calculation of gamma factor in soecial relativity.
from math import sqrt

#Define a global variable.
c = 299792458.0   #Define speed of light in m/s.

#Define a function to calculate gamma.
def gamma(v):
    if v < 0.1 * c: #If v is not in order of c, assume it's a decimal and * c.
        v *= c
    return 1 / sqrt(1 - (v**2.0 / c**2.0))

def gamma_inverse(gamma):   #Returns beta = v/c.
    return sqrt(1 - (1 / gamma**2))


#__Main__
if __name__ == "__main__":
    #Import useful libraries.
    from fractions import Fraction

    #ask for input of velocity.
    v = float(input("Input the velocity as a decimal of c:"))
    
    #Call gamma fuction.
    gamma = gamma(v)
    
    #Print value to user.
    print("The gamma value =", Fraction(gamma), "=", '%.5f' %gamma)